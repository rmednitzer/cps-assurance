# CPS Regulatory Mapping

## Machinery Regulation × CRA × IEC 62443 × IEC 61508 → Controls

**Date:** 2026-03-05
**Frameworks:** Machinery Regulation 2023/1230, CRA (EU 2024/2847), IEC 62443, IEC 61508, RED 2014/53/EU
**Status:** DRAFT — requirement IDs are [S,80]; verify against current official texts before audit.

---

## Assumptions

- **Product profile:** Organisation manufactures or integrates CPS products with digital elements placed on the EU market. [I,80]
- **Safety relevance:** Products contain safety functions requiring SIL/PL allocation. [I,80]
- **OT deployment:** Products are deployed in industrial environments with existing OT networks. [I,80]
- **Dual obligation:** Organisation has both product obligations (Machinery Reg, CRA) AND may have operator obligations (NIS2) for its own OT infrastructure. [I,70]

---

## 1 — Control domain crosswalk

The highest-leverage shared control is **a unified risk assessment covering both safety hazards and cybersecurity threats** — it satisfies Machinery Regulation EHSR 1.1.2, CRA Annex I security risk assessment, IEC 61508 hazard analysis, and IEC 62443-3-2 zone risk assessment simultaneously. [I,80]

| Control domain | Machinery Reg EHSR | CRA Annex I | IEC 62443 | IEC 61508/13849 | RED |
|---------------|-------------------|-------------|-----------|-----------------|-----|
| Risk assessment | 1.1.2 (safety integration) | Part I (security risk assessment) | 3-2 (zone risk) | Part 1 (HARA) | — |
| Cybersecurity of controls | **1.1.9** (protection against corruption) | Part I (all properties) | 3-3, 4-2 (SL) | — (see IEC 63069) | 3.3(d) |
| Access control | — | Part I (AuthN/AuthZ) | 3-3 FR1, FR2 | — | — |
| Secure update | 1.2.1 (no safety regression) | Part I (secure update mechanism) | 4-1, 4-2 | Modification mgmt | — |
| Data protection | — | Part I (encryption at rest/transit) | 3-3 FR4 | — | 3.3(e) |
| Event logging | — | Part I (security event logging) | 3-3 FR6 | — | — |
| SBOM | — | **Part II (mandatory)** | — | — | — |
| Vulnerability handling | — | Part II (address without delay) | 4-1 (SDL) | — | — |
| ENISA/CSIRT reporting | — | Part II (24h/72h/14d) | — | — | — |
| Safety function integrity | 1.2.1 (SIL/PL) | — | Safety zone SL-T | Core scope | — |
| E-stop | 1.2.4 (stopping functions) | — | — | Core scope | — |
| Failure of power supply | 1.2.6 | — | 3-3 FR7 | Core scope | — |
| Physical hazard protection | 1.3–1.5 | — | — | Core scope | — |
| DoS resilience | — | Part I (DoS resilience) | 3-3 FR7 | — | — |
| CE marking | **Required** | **Required** | — | — | **Required** |
| Technical documentation | **Annex VII** | **Annex VII** (CRA) | — | IEC 61508 reporting | Required |

---

## 2 — Shared evidence catalogue

Evidence items that satisfy multiple frameworks simultaneously:

| Evidence item | Mach. Reg | CRA | IEC 62443 | IEC 61508 |
|--------------|-----------|-----|-----------|-----------|
| Hazard analysis (STPA / HARA) | EHSR 1.1.2 | — | Zone risk input | Core requirement |
| SIL/PL allocation + FMEDA | EHSR 1.2.1 | — | — | Core requirement |
| Zone/conduit model + SL-T | EHSR 1.1.9 (partial) | Annex I (architecture) | Core output (3-2) | — |
| Penetration test report | — | Annex I | SL-T verification | — |
| SBOM (signed, per release) | — | **Annex I Part II** | — | — |
| Safety-security interaction register | EHSR 1.1.9 | Annex I | IEC 63069 | IEC 63069 |
| Security risk assessment | EHSR 1.1.9 | Annex I Part I | 3-2 (SRA) | — |
| Functional safety test reports | EHSR 1.2.1 | — | — | Core requirement |
| EMC test reports | — | — | — | IEC 61508-2 | (RED Art 3.1(b)) |
| Technical documentation package | **Annex VII** | **Annex VII** | — | Part 1 reporting |
| EU Declaration of Conformity | **Required** | **Required** | — | — |

---

## 3 — Gap analysis template

For each CPS product, assess coverage against each framework using this matrix. Populate per product in `registers/product-register.md`.

| Obligation | Status | Evidence | Gap | Remediation | Priority |
|-----------|--------|----------|-----|-------------|----------|
| Machinery Reg EHSR 1.1.9 (cybersecurity of controls) | | | | | |
| CRA Annex I Part I (secure-by-default) | | | | | |
| CRA Annex I Part II (SBOM) | | | | | |
| CRA Annex I Part II (vulnerability handling) | | | | | |
| CRA Annex I Part II (ENISA reporting) | | | | | |
| IEC 62443-3-3 SL-T per zone | | | | | |
| IEC 61508 SIL allocation | | | | | |
| EMC/LVD/RED (as applicable) | | | | | |
| CE marking (all directives) | | | | | |

---

## 4 — Safety-security conflict points

| Conflict | Resolution approach | Register entry |
|---------|-------------------|---------------|
| Safety requires <10 ms response → cannot add crypto overhead | Offload authentication to dedicated hardware outside safety timing path | SSI-n (SS-4) |
| Safety-certified firmware cannot be patched → known vulnerability | Compensating network controls + staged re-certification | SSI-n (SS-7) |
| Safety override port → attack vector | Hardwired override only; no network-accessible override | SSI-n (SS-3) |
| Safety fail-open vs. security fail-closed | Architectural separation: safety and security enforce on different components | SSI-n (SS-5) |

See `docs/safety/safety-security-interaction.md` for the full SS-1..SS-7 taxonomy and resolution principles.

---

## 5 — Conformity assessment sequencing

Recommended order for CPS products under multiple directives:

1. **Hazard analysis + SIL/PL** (Machinery Regulation + IEC 61508/13849) — drives the safety architecture
2. **Zone/conduit model + SL-T** (IEC 62443) — drives the security architecture
3. **Safety-security interaction analysis** (IEC 63069) — identifies conflicts
4. **CRA gap assessment** (Annex I Part I + Part II) — cybersecurity properties + SBOM + CVD
5. **EMC/LVD/RED** testing — typically straightforward with existing hEN
6. **Technical documentation** compilation (single package, multi-directive)
7. **Conformity assessment** execution (self-assessment or notified body per route)
8. **EU DoC + CE marking** — after ALL assessments complete

---

*All requirement mappings [S,80]. Verify against current official texts. Machinery Regulation 2023/1230 application 2027-01-20 [S,85]. CRA application dates phased [S,75]. Harmonised standards under development — mark specific hEN references Unknown.*
