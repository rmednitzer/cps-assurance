# CPS Assurance Repository

Governance-as-code for cyber-physical systems under EU product regulation.

Covers the three domains that are inseparable in CPS: functional safety, OT/ICS security, and EU product conformity — plus their interaction.

## Status

| Area | Status |
|------|--------|
| Safety architecture (IEC 61508 / ISO 13849) | Template ready — populate per system |
| OT security architecture (IEC 62443) | Template ready — populate per plant/facility |
| Regulatory mapping (Machinery Reg / CRA / RED) | Complete — verify against hEN publications |
| Safety-security interaction analysis | Framework ready — populate per system |
| Policies (3 CPS-specific) | Template ready — legal review + management approval required |
| Registers (hazard, zone-conduit, SSI, product) | Stub — initial population required |
| Checklists (pre-commissioning, change review) | Template ready |

## Repository structure

```
.
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── .github/
│   └── CODEOWNERS
│
├── docs/
│   ├── architecture/
│   │   ├── cps-reference-architecture.md    # System boundary, Purdue levels, PIAL boundaries
│   │   └── standards-applicability.md       # Which IEC/ISO/EU instruments apply and why
│   ├── safety/
│   │   ├── functional-safety-approach.md    # SIL/PL methodology, STPA integration
│   │   └── safety-security-interaction.md   # Joint STPA-STRIDE, SS-1..SS-7 taxonomy
│   ├── security/
│   │   └── ot-security-architecture.md      # IEC 62443 zone/conduit, SL-T, Purdue enforcement
│   └── compliance/
│       ├── regulatory-mapping.md            # Machinery Reg + CRA + RED → controls crosswalk
│       └── conformity-assessment-guide.md   # CE marking pathway for CPS products
│
├── policies/
│   ├── POL-CPS-01-safety-management.md      # Functional safety management per IEC 61508-1
│   ├── POL-CPS-02-ot-security.md            # OT security per IEC 62443-2-1
│   └── POL-CPS-03-product-conformity.md     # EU product conformity and post-market obligations
│
├── registers/
│   ├── hazard-register.md                   # Losses, hazards, UCAs, SIL/PL, safety functions
│   ├── zone-conduit-register.md             # IEC 62443-3-2 zones, conduits, SL-T allocation
│   ├── ssi-register.md                      # Safety-security interactions + joint requirements
│   └── product-register.md                  # Products, applicable directives, conformity status
│
├── templates/
│   ├── hazard-analysis/
│   │   └── TEMPLATE-hazard-entry.md
│   ├── zone-conduit/
│   │   └── TEMPLATE-zone-conduit-entry.md
│   ├── product-certification/
│   │   └── TEMPLATE-product-gap-assessment.md
│   ├── safety-security-interaction/
│   │   └── TEMPLATE-ssi-entry.md
│   └── change-review/
│       └── TEMPLATE-safety-security-change-review.md
│
└── checklists/
    ├── pre-commissioning-safety.md          # Before a CPS goes live
    ├── pre-commissioning-security.md        # Before OT network changes go live
    └── annual-review.md                     # Yearly re-assessment checklist
```

## Conventions

- All documents use [F]/[I]/[S] epistemic tags with {50,70,80,90} confidence
- Dates: YYYY-MM-DD; Times: 24h; Units: SI; Currency: EUR
- Policies require signed Git tags on approval
- Registers are append-mostly; changes via merge request with review
- IDs for traceability: H-n (hazard), SF-n (safety function), Z-n (zone), CO-n (conduit), SSI-n (interaction), JSSR-n (joint requirement), PROD-n (product)

## Regulatory scope

- **Machinery Regulation 2023/1230** (application 2027-01-20 [S,85])
- **CRA** (EU 2024/2847) — phased application [S,75]
- **RED** 2014/53/EU + cybersecurity delegated act [S,70]
- **LVD** 2014/35/EU
- **EMC** 2014/30/EU
- **IEC 61508** / **ISO 13849-1** / **IEC 61511** (functional safety)
- **IEC 62443** (OT/ICS security)
- **IEC 63069** / **IEC TR 63074** (safety-security interface)
- **AI Act** (if CPS contains AI — link to platform-assurance for IT-layer governance)

## Relationship to platform-assurance

This repo governs the **CPS-specific** layer: physical safety, OT networks, product certification. The [platform-assurance](../platform-assurance/) repo governs the **IT platform layer**: ISMS, NIS2 entity obligations, GDPR, evidence pipeline, observability, IAM.

Where they connect:
- Platform-assurance evidence pipeline stores CPS evidence artifacts
- Platform-assurance ISMS policies (POL-01..10) apply to the IT layer; CPS policies (POL-CPS-01..03) extend them for the physical layer
- Platform-assurance risk register (RSK-nnn) and CPS hazard register (H-n) share a common risk assessment methodology
- NIS2 obligations flow from platform-assurance; CPS-specific controls feed back as NIS2 Art 21 technical measures

## Getting started

1. Read `docs/architecture/standards-applicability.md` — determine which standards and directives apply
2. Populate `registers/product-register.md` — list CPS products with applicable directives
3. Conduct hazard analysis — use `templates/hazard-analysis/` to populate `registers/hazard-register.md`
4. Build zone/conduit model — use `templates/zone-conduit/` to populate `registers/zone-conduit-register.md`
5. Run safety-security interaction analysis — use `templates/safety-security-interaction/`
6. Get legal review on `policies/` — adapt to org context; management approval
7. Execute checklists before commissioning
