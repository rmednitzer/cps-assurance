# Contributing

## Review process

All changes to this repository follow the change management policy (POL-CPS-03 for product-affecting changes; platform-assurance POL-10 for general changes).

| Path | Review required | Approver |
|------|----------------|----------|
| `policies/` | Legal review + safety manager + CISO | Safety manager signs tag |
| `registers/hazard-register.md` | Safety engineer + safety manager | Merge request review |
| `registers/safety-constraint-register.md` | Safety engineer + safety manager | Merge request review |
| `registers/threat-register.md` | OT security lead + CISO | Merge request review |
| `registers/zone-conduit-register.md` | OT security lead + CISO | Merge request review |
| `registers/ssi-register.md` | Safety engineer + OT security lead (joint) | Merge request review |
| `registers/traceability-manifest.md` | Safety manager + compliance lead | Merge request review |
| `registers/product-register.md` | Product owner + compliance lead | Merge request review |
| `docs/` | Peer review (1 reviewer minimum) | Any team member |
| `templates/`, `checklists/` | Safety manager or CISO | Merge request review |

## Safety-critical change rule

Any change that modifies a hazard (H-n), safety function (SF-n), safety constraint (SC-n), threat (T-n), SIL/PL allocation, zone boundary (Z-n), or conduit definition (CO-n) is a **safety-critical change**. These require:

1. Joint review by safety engineer AND OT security lead
2. Impact analysis on the SSI register (does this change create or modify a safety-security interaction?)
3. Documented blast radius assessment
4. Signed tag after approval: `safety/H-nn-vN.N` or `zone/Z-nn-vN.N`

## Commit conventions

- Sign all commits (GPG or SSH): `git commit -S`
- Use conventional commits: `feat:`, `fix:`, `docs:`, `policy:`, `register:`, `safety:`, `security:`
- Policy approvals: create a signed tag `policy/POL-CPS-XX-vN.N` after management sign-off
- Safety-critical changes: signed tag `safety/{change-id}` after joint review

## Branch model

- `main` — approved, current state of CPS governance
- `draft/*` — work in progress (hazard analysis updates, zone model changes, policy revisions)
- No direct pushes to `main` — merge requests only

## Evidence

Every approved register update and policy version is stored in the evidence pipeline (link to platform-assurance evidence store: `evidence/governance/cps/{year}/`). Do not manually upload — use the merge-to-main CI trigger or the governance upload CLI.


## Local validation

Run local validation before opening a merge request:

```bash
make validate
```

The validator checks canonical Markdown references, duplicate IDs, unresolved placeholders in governance metadata, and JSON schema integrity under `schemas/`. CI runs the same check on pull requests.
