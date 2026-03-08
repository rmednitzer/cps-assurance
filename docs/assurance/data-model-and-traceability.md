# CPS Data Model and Traceability

**Purpose:** turn the repository from a Markdown-only doctrine set into a typed assurance repository with canonical IDs, machine-readable entries, and generated traceability.

## 1 — Canonical object types

The repository uses the following first-class objects:

- `PROD-n` — product or economic-operator scoped item
- `L-n` — loss
- `H-n` — hazard
- `SF-n` — safety function
- `UCA-n` — unsafe control action
- `SC-n` — safety constraint
- `T-n` — threat
- `Z-n` — zone
- `CO-n` — conduit
- `SSI-n` — safety-security interaction
- `JSSR-n` — joint safety-security requirement
- `E-n` — evidence artifact or evidence package
- `G-n` / `C-n` / `S-n` — assurance-case goal, context, strategy

## 2 — Canonical machine-readable shape

Registers may remain human-readable, but each entry should also exist as one file per object with YAML front matter or JSON/YAML sidecar. The minimum metadata for every object is:

```yaml
id: H-1
object_type: hazard
status: draft
owner: Safety Manager
review_cycle: quarterly
review_trigger:
  - change: SF-n
  - incident: yes
links:
  mitigated_by: [SF-1]
  constrained_by: [SC-1]
  interacts_with: [SSI-1]
provenance:
  basis: [F,90]
  verified_on: 2026-03-08
```

Use the JSON schemas under `schemas/` as the source of truth for required fields and enums.

## 3 — Mandatory numeric runtime-contract fields

For any object affecting physical behaviour, the following numeric fields are mandatory where applicable:

- `process_safety_time_ms`
- `sample_period_ms`
- `latency_budget_ms`
- `jitter_budget_ms`
- `stale_data_timeout_ms`
- `watchdog_threshold_cycles`
- `actuator_authority_limit`
- `degraded_mode_trigger`
- `safe_state`

A safety or security review is incomplete if a control path can change physical state and these fields are absent or explicitly unknown.

## 4 — Traceability closure rule

Every release candidate must close this chain for all in-scope products:

```text
regulatory clause / hazard / threat
  -> control artifact (SF / SC / Z / CO / JSSR)
  -> verification artifact
  -> evidence location
  -> acceptance / sign-off
```

The canonical release artifact for that closure is `registers/traceability-manifest.md`.

## 5 — Generation and validation rules

- Canonical file references must use actual repo paths, not symbolic names.
- IDs must be unique within their namespace.
- Every `SSI-n` must reference at least one `SC-n` and one `T-n`.
- Every `JSSR-n` must point back to at least one `SSI-n`.
- Every product conformity assessment must link back to hazards, threats, constraints, and interactions that justify its controls.
- Provenance tags must use only `[F]`, `[I]`, or `[S]` with confidence levels `{50,70,80,90}`.

## 6 — Cross-repo integration

Zone and safety-constraint entries may reference platform-assurance controls via `platform_controls: [CTL-nnnn]`. These are not validated locally (different repo), but they make the dependency explicit for audit and traceability. The platform-assurance control catalog (`controls/catalog.yaml`) is the canonical source for CTL-nnnn definitions.

Evidence artifacts produced by the CPS layer flow into the platform-assurance evidence pipeline. The interface is defined in `docs/evidence/cps-evidence-types.md`.

## 7 — Minimal migration path

1. Keep existing Markdown registers as executive views.
2. Add one-file-per-entry machine-readable records under a future `records/` tree.
3. Validate those records against `schemas/` in CI.
4. Generate the traceability manifest and assurance-case skeleton from the typed records.
5. Treat generated artifacts as release evidence, not as hand-edited source.
