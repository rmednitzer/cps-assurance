# CI/CD Governance Pipeline

**Purpose:** Document the continuous integration and delivery pipeline for CPS assurance artifacts, from local validation through evidence storage.

## 1 — Current CI pipeline

### GitHub Actions workflow

**Trigger:** Push to `main` or pull request targeting `main`.

**Jobs:**

| Job | Tool | What it checks |
|-----|------|---------------|
| `validate` | `make validate` (Python script) | Broken references, duplicate IDs, JSON schema syntax, required artifacts, artifact-index consistency, cross-register referential integrity, orphaned files, traceability closure |
| `check-yaml` | `make check-yaml` | YAML syntax for all `.yaml` / `.yml` files |
| `check-json` | `make check-json` | JSON syntax for all schema files in `schemas/` |
| `lint-markdown` | markdownlint-cli2 | Markdown formatting and style consistency |

### Local validation

Run before pushing:

```bash
make all          # validate + check-yaml + check-json
make validate     # full repository validation
make lint-md      # markdown linting (requires markdownlint)
```

## 2 — Validation stages

### Stage 1: Syntax validation

- JSON schemas are valid JSON and contain required keys (`$schema`, `$id`, `type` or `allOf`)
- YAML files parse without errors
- Markdown files have consistent formatting

### Stage 2: Reference integrity

- Backtick path references resolve to existing files
- Markdown link targets resolve to existing files
- All files referenced in `artifact-index.yaml` exist on disk

### Stage 3: Semantic validation

- No duplicate canonical IDs (H-n, SF-n, etc.) across registers
- Cross-register references resolve (e.g., SSI register references to H-n that exist in hazard register)
- Placeholder metadata flagged in registers and policies (informational)
- Orphaned files not listed in artifact-index.yaml flagged

### Stage 4: Traceability validation

- Each hazard (H-n) linked to at least one safety function (SF-n)
- Each safety function linked back to a hazard
- Traceability closure gaps reported as notes

## 3 — Evidence collection

### When artifacts become evidence

| Trigger | Action | Evidence type |
|---------|--------|---------------|
| Hazard analysis approved | Store signed analysis document | `hazard_analysis` |
| Safety function test completed | Store test report with timing data | `safety_function_test` |
| Proof test executed | Store proof test record | `proof_test_record` |
| Zone/conduit model verified | Store verification report | `zone_conduit_verification` |
| SSI analysis reviewed | Store review record | `ssi_review` |
| Conformity assessment complete | Store conformity package | `conformity_package` |
| Product build | Generate and store SBOM | `sbom_cps` |
| Annual review completed | Store signed checklist | `annual_review` |

### Evidence metadata

Each evidence artifact includes:

```json
{
  "artifact_type": "safety_function_test",
  "source": "cps-assurance",
  "cps_ids": ["SF-1", "H-1"],
  "framework_tags": ["IEC-61508", "Machinery-Reg-EHSR-1.1.2"],
  "retention_tier": "governance_10y",
  "sha256_hash": "<computed at upload>"
}
```

### Storage path convention

```
evidence/governance/cps/{year}/{artifact_type}/{artifact_id_or_filename}
```

Example: `evidence/governance/cps/2026/safety_function_test/SF-1-proof-test-2026-03.pdf`

## 4 — Integration with platform-assurance

CPS evidence flows into the platform-assurance evidence pipeline:

```
cps-assurance (this repo)
    ↓ produces evidence artifacts
platform-assurance evidence pipeline
    ↓ transport (signed upload)
MinIO WORM storage
    ↓ indexing
OpenSearch (searchable evidence catalog)
    ↓ integrity
Daily hash chain (cosign keyless signing via Sigstore)
```

### Cross-repo references

- CPS safety constraints (SC-n) may reference platform-assurance controls (CTL-nnnn)
- CPS evidence artifacts tag platform-assurance control IDs for traceability
- Platform-assurance POL-10 (change management) applies to all CPS changes; CPS policies add safety/security gates

## 5 — Release workflow

### Pre-release validation

1. All CI checks pass (syntax, references, semantic, traceability)
2. No unresolved errors in `make validate`
3. All placeholder metadata resolved for release-scope registers

### Approval gates

| Gate | Approver | Scope |
|------|----------|-------|
| Safety gate | Safety manager | Hazard register, safety constraints, proof test records |
| Security gate | OT security lead | Threat register, zone/conduit model, SSI register |
| Compliance gate | Compliance lead | Product register, conformity packages, DoC |

All three gates must pass before release.

### Release process

1. Create release branch from `main`
2. Run full validation: `make all`
3. Collect approval signatures (safety + security + compliance)
4. Tag release: `release/v{N.N}` (signed tag)
5. Generate traceability manifest snapshot
6. Upload evidence artifacts to platform-assurance pipeline
7. Merge to `main`

### Safety-critical releases

For changes affecting H-n, SF-n, SC-n, SIL/PL, Z-n, or CO-n:

1. Joint safety-security change review (per `checklists/change-review.md`)
2. Additional tag: `safety/{change-id}-v{N.N}` or `zone/{change-id}-v{N.N}`
3. Evidence of joint review stored in evidence pipeline

## 6 — Future enhancements

| Enhancement | Description | Priority |
|-------------|-------------|----------|
| Automated traceability reports | Generate regulation → artifact → evidence chain as JSON/CSV | High |
| Evidence hash chain integration | Automated upload to platform-assurance pipeline on release | High |
| Schema validation of register entries | Parse markdown tables and validate against JSON schemas | Medium |
| Dependency graph visualization | Generate DOT/Mermaid diagrams of entity relationships | Medium |
| Artifact publishing | Publish rendered documentation to internal documentation site | Low |
| Automated SBOM generation | Generate SBOMs in CI for CPS firmware/software products | High |

*Reference: `docs/evidence/cps-evidence-types.md`, `docs/assurance/data-model-and-traceability.md`, CONTRIBUTING.md.*
