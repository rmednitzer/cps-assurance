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
  8. Cross-register referential integrity
  9. Orphaned file detection
 10. Traceability closure validation
 11. pyyaml dependency handling (within Check 6)
 12. JSON schema field validation
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# --- CLI flags ---
VERBOSE = '--verbose' in sys.argv

# --- Color support ---
_USE_COLOR = sys.stdout.isatty()

def _red(s: str) -> str:
    return f'\033[91m{s}\033[0m' if _USE_COLOR else s

def _yellow(s: str) -> str:
    return f'\033[93m{s}\033[0m' if _USE_COLOR else s

def _green(s: str) -> str:
    return f'\033[92m{s}\033[0m' if _USE_COLOR else s


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

# Regex for references to canonical IDs anywhere in markdown text.
# Matches patterns like H-1, SF-12, SC-3 etc. but NOT template patterns like H-n.
CANONICAL_ID_REF_RE = re.compile(
    r'\b((?:L|H|SF|UCA|SC|T|Z|CO|SSI|JSSR|PROD)-\d+)\b'
)

# Template patterns to skip (literal "n" instead of a number)
TEMPLATE_ID_RE = re.compile(
    r'^(?:L|H|SF|UCA|SC|T|Z|CO|SSI|JSSR|PROD)-n$'
)

# Code block markers
CODE_BLOCK_RE = re.compile(r'^```')


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def resolve_md_reference(source: Path, ref: str) -> Path:
    if ref.startswith('./') or ref.startswith('../'):
        return (source.parent / ref).resolve()
    return (ROOT / ref).resolve()


def strip_code_blocks(text: str) -> str:
    """Remove fenced code blocks from text."""
    lines = text.split('\n')
    result = []
    in_code = False
    for line in lines:
        if CODE_BLOCK_RE.match(line.strip()):
            in_code = not in_code
            continue
        if not in_code:
            result.append(line)
    return '\n'.join(result)


errors: list[str] = []
notes: list[str] = []
seen_ids: dict[str, str] = {}
checked_files: set[str] = set()

# --- Check 1 + 2: Broken references ---
for md in MD_FILES:
    checked_files.add(rel(md))
    text = md.read_text(encoding='utf-8')

    if VERBOSE:
        print(f'  checking {rel(md)}')

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

# --- Check 4 + 12: JSON schema syntax and field validation ---
for schema_file in SCHEMA_FILES:
    checked_files.add(rel(schema_file))
    if VERBOSE:
        print(f'  checking {rel(schema_file)}')
    try:
        data = json.loads(schema_file.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        errors.append(f'{rel(schema_file)}: invalid JSON schema: {exc}')
        continue

    # Check 12: required schema fields
    if '$schema' not in data:
        errors.append(f'{rel(schema_file)}: missing "$schema" key')
    if '$id' not in data:
        errors.append(f'{rel(schema_file)}: missing "$id" key')
    if 'type' not in data and 'allOf' not in data:
        errors.append(f'{rel(schema_file)}: missing "type" or "allOf" key')

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

# --- Check 6 + 11: Artifact index (with pyyaml dependency handling) ---
artifact_index_path = ROOT / 'artifact-index.yaml'
indexed_paths: set[str] | None = None
if artifact_index_path.exists():
    try:
        import yaml
        idx = yaml.safe_load(artifact_index_path.read_text(encoding='utf-8'))
        seen_paths: set[str] = set()
        indexed_paths = set()
        for artifact in idx.get('artifacts', []):
            path = artifact.get('path', '')
            if path in seen_paths:
                errors.append(f'artifact-index.yaml: duplicate path {path}')
            seen_paths.add(path)
            indexed_paths.add(path)
            if not (ROOT / path).exists():
                errors.append(f'artifact-index.yaml: missing file {path}')
        checked_files.add('artifact-index.yaml')
    except ImportError:
        print(_yellow(
            'WARNING: pyyaml not installed. Install with: pip install -r scripts/requirements.txt'
        ))
        notes.append('artifact-index.yaml: pyyaml not installed, skipping YAML validation')
    except Exception as exc:
        errors.append(f'artifact-index.yaml: parse error: {exc}')

# --- Check 8: Cross-register referential integrity ---
if VERBOSE:
    print('  checking cross-register referential integrity')
for md in MD_FILES:
    md_rel = rel(md)
    text = md.read_text(encoding='utf-8')
    text_no_code = strip_code_blocks(text)

    # Only enforce cross-ref integrity in registers (not docs/templates/examples/checklists)
    if not md_rel.startswith('registers/'):
        continue

    for match in CANONICAL_ID_REF_RE.finditer(text_no_code):
        ref_id = match.group(1)
        # Skip template patterns
        if TEMPLATE_ID_RE.match(ref_id):
            continue
        # Skip references inside the register that defines this ID
        defining_file = seen_ids.get(ref_id)
        if defining_file == md_rel:
            continue
        # Only report if the ID is referenced but never defined anywhere
        if ref_id not in seen_ids:
            errors.append(f'{md_rel}: reference to undefined ID {ref_id}')

# Deduplicate cross-ref errors (same ID may be referenced many times)
_seen_xref_errors: set[str] = set()
deduped_errors: list[str] = []
for e in errors:
    if 'reference to undefined ID' in e:
        if e in _seen_xref_errors:
            continue
        _seen_xref_errors.add(e)
    deduped_errors.append(e)
errors = deduped_errors

# --- Check 9: Orphaned file detection ---
EXCLUDE_DIRS = {'.git', '__pycache__'}
EXCLUDE_FILES = {'.pre-commit-config.yaml', '.gitignore', 'scripts/requirements.txt'}
if VERBOSE:
    print('  checking for orphaned files')
if indexed_paths is not None:
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():
            continue
        rp = rel(p)
        # Skip excluded dirs
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        # Skip excluded files
        if rp in EXCLUDE_FILES:
            continue
        checked_files.add(rp)
        if rp not in indexed_paths:
            notes.append(f'{rp}: not listed in artifact-index.yaml')

# --- Check 10: Traceability closure validation ---
if VERBOSE:
    print('  checking traceability closure')

# Collect all hazard IDs and safety-function IDs
hazard_ids = {k for k in seen_ids if k.startswith('H-')}
sf_ids = {k for k in seen_ids if k.startswith('SF-')}

# For each hazard, check that at least one SF references it somewhere in the registers
for h_id in sorted(hazard_ids):
    # Search all register files for SF rows that mention this hazard
    found_sf_link = False
    for md in MD_FILES:
        if not rel(md).startswith('registers/'):
            continue
        text = md.read_text(encoding='utf-8')
        # Look for this hazard ID referenced in any line that also contains an SF
        for line in text.split('\n'):
            if h_id in line and any(sf in line for sf in sf_ids):
                found_sf_link = True
                break
            # Also check if any SF register row references this hazard
            if h_id in line and 'SF-' in line:
                found_sf_link = True
                break
        if found_sf_link:
            break
    if not found_sf_link:
        notes.append(f'traceability: {h_id} has no linked safety function (SF-n)')

# For each SF, check it links back to a hazard
for sf_id in sorted(sf_ids):
    found_h_link = False
    for md in MD_FILES:
        if not rel(md).startswith('registers/'):
            continue
        text = md.read_text(encoding='utf-8')
        for line in text.split('\n'):
            if sf_id in line and any(h in line for h in hazard_ids):
                found_h_link = True
                break
            if sf_id in line and 'H-' in line:
                found_h_link = True
                break
        if found_h_link:
            break
    if not found_h_link:
        notes.append(f'traceability: {sf_id} has no linked hazard (H-n)')

# --- Output ---
total_files = len(checked_files)
num_errors = len(errors)
num_notes = len(notes)

if notes:
    print(_yellow('NOTES:'))
    for note in notes:
        print(_yellow(f'  - {note}'))

if errors:
    print(_red('ERRORS:'))
    for error in errors:
        print(_red(f'  - {error}'))

# Summary line
summary = f'Checked {total_files} files, found {num_errors} errors, {num_notes} notes'
if errors:
    print(_red(summary))
    sys.exit(1)
else:
    print(_green(summary))
    if not notes:
        print(_green('Repository validation passed.'))
