# Harmonised European Norm (hEN) Tracker

**Date:** 2026-03-08
**Status:** DRAFT — hEN availability is rapidly evolving. Review and update quarterly.
**Next review:** 2026-06-08

---

## Confidence notes

Harmonised standard status is time-sensitive. Entries reflect the situation as of 2026-03-08. OJ citations and hEN publication status must be verified against EUR-Lex and the relevant standardisation body (CEN, CENELEC, ETSI). Where status is uncertain, provenance is marked accordingly.

---

## 1 — What are harmonised European Norms?

Harmonised European Norms (hENs) are standards developed by European Standardisation Organisations (CEN, CENELEC, ETSI) at the request of the European Commission and cited in the Official Journal of the European Union (OJEU) [F,90].

**Why they matter:**

- **Presumption of conformity:** A product manufactured in accordance with a harmonised standard (or the relevant parts of it) is presumed to conform to the essential requirements covered by that standard [F,90]
- **Simplified conformity assessment:** For CRA Class I products, applying hENs allows the manufacturer to use Module A (internal assessment) instead of requiring a notified body [S,85]
- **Legal certainty:** hENs provide a concrete, testable interpretation of otherwise abstract essential requirements
- **Defence in enforcement:** If a market surveillance authority challenges conformity, application of a cited hEN shifts the burden of proof

**Without hENs:** The manufacturer must demonstrate compliance with essential requirements by **other appropriate means** — typically by referencing international standards, conducting risk assessments, or obtaining third-party opinions. This is more burdensome and provides less legal certainty.

---

## 2 — Current hEN status per regulation (as of 2026-03-08)

### 2.1 Machinery Regulation 2023/1230

| Aspect | Status |
|--------|--------|
| **General application date** | 2027-01-20 [F,90] |
| **hEN status** | Under development by CEN/CENELEC [S,75] |
| **Transitional standards** | Standards harmonised under the Machinery Directive 2006/42/EC may continue to apply during a transitional period. Many existing EN standards (e.g., EN ISO 12100, EN ISO 13849-1, EN ISO 13849-2, EN IEC 62061, EN 60204-1) are expected to be transitioned or re-cited under the new Regulation [S,75] |
| **Key gap** | EHSR 1.1.9 (protection against corruption / cybersecurity of control systems) is new — no existing hEN covers it directly. IEC 62443 series may serve as a reference but is not an hEN under this Regulation [S,80] |
| **Monitoring** | Track CEN/CENELEC work programme and OJ citations |

### 2.2 Cyber Resilience Act (CRA) 2024/2847

| Aspect | Status |
|--------|--------|
| **Full application date** | 2027-12-11 [F,90] |
| **hEN status** | No hENs published yet [S,80] |
| **Standardisation mandate** | CEN/CENELEC mandates issued by the Commission to develop harmonised standards covering CRA Annex I essential requirements [S,80] |
| **Expected timeline** | First CRA hENs expected 2027–2028; unlikely before full application date [I,70] |
| **Implication** | Class I products cannot use Module A until hENs are available and applied. All Class I products will likely need notified body involvement in the initial period [S,85] |
| **Reference standards** | ETSI EN 303 645 (consumer IoT security), IEC 62443 series (industrial cybersecurity), ISO/IEC 27001/27002 — these are not hENs under CRA but may serve as evidence of state-of-the-art compliance |
| **Monitoring** | Track CEN/CENELEC mandated work items and OJ citations |

### 2.3 Radio Equipment Directive (RED) 2014/53/EU

| Aspect | Status |
|--------|--------|
| **Cybersecurity delegated act** | Delegated Regulation (EU) 2022/30, applies from 2025-08-01 [F,90] |
| **hEN status for Art. 3.3(d)(e)(f)** | EN 18031 series (EN 18031-1, EN 18031-2, EN 18031-3) published by ETSI/CEN/CENELEC but **not yet cited in the OJ** as of 2026-03-08 [S,80] |
| **Implication** | Without OJ citation, EN 18031 does not create a formal presumption of conformity. Manufacturers applying EN 18031 demonstrate good practice but cannot claim presumption [S,80] |
| **RED-CRA transition** | The Commission has proposed repealing the cybersecurity delegated act from 2027-12-11 to align with CRA. Monitor adoption status [S,80] |
| **Monitoring** | Track OJ citation of EN 18031 series; monitor RED-CRA transition timeline |

### 2.4 IEC 62443 series

| Aspect | Status |
|--------|--------|
| **Harmonised status** | Not harmonised under any EU directive/regulation [F,85] |
| **Role** | Widely recognised as **state-of-the-art** for industrial cybersecurity. Referenced by Machinery Regulation EHSR 1.1.9 guidance, CRA recitals, and NIS2 implementing guidance |
| **CPS relevance** | Core standard suite for OT/ICS security: IEC 62443-4-1 (secure development lifecycle), IEC 62443-4-2 (component security requirements), IEC 62443-3-3 (system security requirements) |
| **Adoption path** | May become the basis for CRA hENs (via EN IEC adoption), but this is not confirmed [I,70] |
| **Practical use** | Apply IEC 62443 as the primary cybersecurity evidence framework for CPS products, supplementing with CRA Annex I mapping. Even without hEN status, IEC 62443 compliance provides strong evidence of meeting essential requirements |

---

## 3 — Monitoring process

### 3.1 Responsibilities

| Role | Responsibility |
|------|---------------|
| **Regulatory affairs lead** | Monitor EUR-Lex OJ for hEN citations; assess impact on product conformity |
| **Standards engineer** | Track CEN/CENELEC/ETSI work programmes for draft standards under development |
| **Product owner** | Evaluate whether new/updated hENs affect product conformity claims |

### 3.2 Monitoring frequency

- **EUR-Lex OJ review:** Quarterly (minimum). Check the L-series of the Official Journal for hEN citation notices [S,80]
- **CEN/CENELEC work programme:** Quarterly. Review active mandates and standard development stage
- **ETSI deliverables:** Quarterly. For RED-related standards
- **Ad hoc:** When a regulatory change or industry alert indicates an imminent hEN publication or withdrawal

### 3.3 Monitoring sources

| Source | URL | What to look for |
|--------|-----|-----------------|
| EUR-Lex Official Journal | https://eur-lex.europa.eu/oj/direct-access.html | Communications listing harmonised standards per directive |
| CEN Work Programme | https://standards.cen.eu/ | Standards under mandate, development stage |
| CENELEC Work Programme | https://www.cenelec.eu/ | Electrotechnical standards under mandate |
| ETSI Standards | https://www.etsi.org/standards | EN deliverables, especially EN 18031, EN 303 645 |
| NANDO database | https://ec.europa.eu/growth/tools-databases/nando/ | Notified body availability (related to hEN applicability) |
| Blue Guide (2022) | Commission guidance on EU product rules | General hEN procedures and effects |

### 3.4 Impact assessment process

When a new hEN is published or an existing one is withdrawn:

1. **Identify affected products** — which products claim conformity based on the old standard or lack a standard?
2. **Gap analysis** — compare current product compliance evidence against the new/updated standard requirements
3. **Transition timeline** — determine the date of withdrawal of the old standard (coexistence period) and the date from which the new standard must be applied
4. **Action plan** — schedule testing, documentation updates, and any product modifications needed
5. **Update tracking table** (Section 5 below)

---

## 4 — Decision tree: hEN applicability

```
Is a harmonised standard (hEN) published and cited in the OJ
for the relevant essential requirement(s)?
│
├── YES → Is the hEN current (not withdrawn, within coexistence period)?
│         │
│         ├── YES → APPLY the hEN.
│         │         Claim presumption of conformity for the requirements
│         │         covered by the standard.
│         │         Document: standard reference, edition, clauses applied.
│         │         For CRA Class I: Module A is available.
│         │
│         └── NO (hEN withdrawn or superseded) →
│                   REMOVE the presumption claim.
│                   Apply the replacement hEN if available.
│                   If no replacement: treat as "no hEN" below.
│
└── NO (no hEN published) →
          DEMONSTRATE COMPLIANCE BY OTHER MEANS:
          - Apply relevant international standards (ISO, IEC) as evidence
          - Conduct risk assessment specific to the essential requirements
          - Obtain third-party assessment or expert opinion
          - Document the approach and rationale
          For CRA Class I: Module A is NOT available — use Module B+C or H.
```

---

## 5 — hEN tracking table template

Maintain one row per applicable standard per directive. Update quarterly.

| Directive/Regulation | hEN reference | Edition | Status | OJ citation date | Applicable from | Withdrawal date | Replacement | Impact on products | Action required | Owner | Last reviewed |
|---------------------|---------------|---------|--------|-------------------|-----------------|-----------------|-------------|-------------------|-----------------|-------|---------------|
| Machinery Reg 2023/1230 | EN ISO 12100 | 2010 | Transitional (from MD 2006/42/EC) | TBD | TBD | TBD | TBD | Risk assessment methodology — all products | Monitor OJ for re-citation | [Name] | 2026-03-08 |
| Machinery Reg 2023/1230 | EN ISO 13849-1 | 2023 | Transitional (from MD 2006/42/EC) | TBD | TBD | TBD | TBD | Safety PL determination — safety controllers, PLCs | Monitor OJ for re-citation | [Name] | 2026-03-08 |
| CRA 2024/2847 | None yet | — | No hEN published | — | — | — | — | All CPS products with digital elements | Monitor CEN/CENELEC mandate progress | [Name] | 2026-03-08 |
| RED 2014/53/EU | EN 18031-1 | 2024 | Published, not OJ-cited | — | — | — | — | Products with radio equipment | Monitor OJ for citation | [Name] | 2026-03-08 |
| RED 2014/53/EU | EN 18031-2 | 2024 | Published, not OJ-cited | — | — | — | — | Products with radio equipment | Monitor OJ for citation | [Name] | 2026-03-08 |
| RED 2014/53/EU | EN 18031-3 | 2024 | Published, not OJ-cited | — | — | — | — | Products with radio equipment | Monitor OJ for citation | [Name] | 2026-03-08 |
| — | IEC 62443-4-1 | Ed. 1.0 (2018) | Not harmonised | — | — | — | — | SDL evidence for all CPS products | Apply as state-of-the-art | [Name] | 2026-03-08 |
| — | IEC 62443-4-2 | Ed. 1.0 (2019) | Not harmonised | — | — | — | — | Component security for all CPS products | Apply as state-of-the-art | [Name] | 2026-03-08 |

---

## Cross-references

- `docs/compliance/cra-chapter-iv-implementation.md` — hEN availability determines Module A eligibility for CRA Class I
- `docs/compliance/cra-product-classification.md` — classification tier determines the impact of hEN availability on conformity route
- `docs/compliance/product-conformity-sequencing.md` — hEN availability affects assessment timeline
- `docs/compliance/conformity-assessment-guide.md` — Section G (conformity assessment pathway selection) references hEN as a decision factor
- `docs/compliance/regulatory-mapping.md` — standards applied in the shared evidence catalogue

---

*hEN presumption of conformity mechanism [F,90]. Machinery Regulation transitional standards [S,75]. CRA hEN status [S,80]. RED EN 18031 OJ citation status [S,80]. IEC 62443 state-of-the-art role [F,85]. All entries subject to quarterly review — verify against EUR-Lex.*
