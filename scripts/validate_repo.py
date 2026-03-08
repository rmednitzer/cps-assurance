#!/usr/bin/env python3
"""CPS-assurance repository validator.

Checks:
  1. Broken backtick-enclosed .md path references
  2. Broken markdown link targets [text](path.md)
  3. Duplicate canonical IDs across registers
  4. JSON schema syntax validity
  5. Required graph-completion artifacts exist
  6. Artifact index file existence (if artifact-index.yaml present)
  7. Placeholder metadata in registers and policies (informational)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_FILES = sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts)
SCHEMA_FILES = sorted((ROOT / 'schemas').glob('*.json')) if (ROOT / 'schemas').exists() else []

BACKTICK_PATH_RE = re.compile(r'`([^`]+\.md)`')
MD_LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
ID_DEF_RE = re.compile(r'(?m)^\|\s*((?:L|H|SF|UCA|SC|T|Z|CO|SSI|JSSR|PROD)-\d+)\s*\|')
PLACEHOLDER_RE = re.compile(
    r'\bYYYY-MM-DD\b|\[Populate|\[Name\]|\[Role\]|\[Brief description\]|\[System name\]'
)
CANONICAL_ID_SOURCES = ('registers/',)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def resolve_md_reference(source: Path, ref: str) -> Path:
    if ref.startswith('./') or ref.startswith('../'):
        return (source.parent / ref).resolve()
    return (ROOT / ref).resolve()


errors: list[str] = []
notes: list[str] = []
seen_ids: dict[str, str] = {}

# --- Check 1 + 2: Broken references ---
for md in MD_FILES:
    text = md.read_text(encoding='utf-8')

    # Backtick path references
    for match in BACKTICK_PATH_RE.finditer(text):
        ref = match.group(1)
        target = resolve_md_reference(md, ref)
        if not target.exists():
            errors.append(f'{rel(md)}: broken backtick path reference `{ref}`')

    # Markdown link references
    for match in MD_LINK_RE.finditer(text):
        target_str = match.group(1)
        if target_str.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        # Strip fragment
        target_str = target_str.split('#')[0]
        if not target_str:
            continue
        target = resolve_md_reference(md, target_str)
        if not target.exists():
            errors.append(f'{rel(md)}: broken markdown link target `{target_str}`')

    # --- Check 3: Duplicate IDs ---
    if rel(md).startswith(CANONICAL_ID_SOURCES):
        for obj_id in ID_DEF_RE.findall(text):
            prior = seen_ids.get(obj_id)
            if prior and prior != rel(md):
                errors.append(f'duplicate ID {obj_id}: {prior} and {rel(md)}')
            else:
                seen_ids[obj_id] = rel(md)

    # --- Check 7: Placeholder metadata ---
    if (rel(md).startswith('registers/') or rel(md).startswith('policies/')) and PLACEHOLDER_RE.search(text):
        notes.append(f'{rel(md)}: contains unresolved placeholder metadata')

# --- Check 4: JSON schema syntax ---
for schema_file in SCHEMA_FILES:
    try:
        json.loads(schema_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        errors.append(f'{rel(schema_file)}: invalid JSON schema: {exc}')

# --- Check 5: Required graph-completion artifacts ---
required_files = [
    'registers/threat-register.md',
    'registers/safety-constraint-register.md',
    'registers/traceability-manifest.md',
    'docs/assurance/data-model-and-traceability.md',
    'docs/evidence/cps-evidence-types.md',
    'templates/threat-model/TEMPLATE-threat-entry.md',
    'templates/safety-constraints/TEMPLATE-safety-constraint-entry.md',
    'templates/assurance-case/TEMPLATE-assurance-case.md',
    'templates/traceability/TEMPLATE-traceability-manifest.md',
]
for req in required_files:
    if not (ROOT / req).exists():
        errors.append(f'missing required artifact: {req}')

# --- Check 6: Artifact index ---
artifact_index_path = ROOT / 'artifact-index.yaml'
if artifact_index_path.exists():
    try:
        import yaml
        idx = yaml.safe_load(artifact_index_path.read_text(encoding='utf-8'))
        seen_paths: set[str] = set()
        for artifact in idx.get('artifacts', []):
            path = artifact.get('path', '')
            if path in seen_paths:
                errors.append(f'artifact-index.yaml: duplicate path {path}')
            seen_paths.add(path)
            if not (ROOT / path).exists():
                errors.append(f'artifact-index.yaml: missing file {path}')
    except ImportError:
        notes.append('artifact-index.yaml: pyyaml not installed, skipping YAML validation')
    except Exception as exc:
        errors.append(f'artifact-index.yaml: parse error: {exc}')

# --- Output ---
if notes:
    print('NOTES:')
    for note in notes:
        print(f'  - {note}')

if errors:
    print('ERRORS:')
    for error in errors:
        print(f'  - {error}')
    sys.exit(1)

print('Repository validation passed.')
