# CPS Standards and Regulatory Applicability

**Date:** 2026-03-05
**Scope:** Determine which safety, security, and product regulation instruments apply to a CPS product or installation.
**Status:** DRAFT — populate per system/product; verify with legal counsel.

---

## 1 — Applicability decision tree

```
Is this a product placed on the EU market?
  │
  ├── YES → Section 2 (product regulation)
  │         + Section 3 (functional safety, if safety-relevant)
  │         + Section 4 (OT security, if network-connected or part of OT environment)
  │
  └── NO (internal deployment / OT infrastructure only)
      → Section 3 (functional safety, if safety functions present)
      + Section 4 (OT security)
      + Section 5 (operator obligations: NIS2 if essential/important entity)
```

---

## 2 — EU product regulation instruments

Determine all applicable directives/regulations. A CPS product typically falls under 2–5 simultaneously.

| Instrument | Applies if | Key obligations | Conformity route |
|-----------|-----------|----------------|-----------------|
| **Machinery Regulation 2023/1230** | Product is a machine, partly completed machine, safety component, lifting accessory, etc. [S,85] | EHSR (Annex III), risk assessment, technical documentation, DoC, CE marking | Annex V (self) / VII (NB) / VIII (NB-QA) |
| **CRA (EU 2024/2847)** | Product with digital elements placed on EU market with intended/foreseeable network connection | Annex I security requirements, SBOM, vulnerability handling, ENISA reporting | Internal / Class I / Class II / Critical |
| **RED 2014/53/EU** | Product contains radio equipment (Wi-Fi, BLE, cellular, etc.) | Art. 3 essential requirements including cybersecurity delegated act [S,70] | Internal / EU-type exam |
| **LVD 2014/35/EU** | Electrical equipment 50–1000V AC / 75–1500V DC | Safety objectives, electrical hazard protection | Internal |
| **EMC 2014/30/EU** | Electrical/electronic equipment | Emission limits, immunity requirements | Internal / EU-type exam |
| **AI Act** | Product contains AI system as defined | Risk tier classification, conformity per tier | Per risk tier |
| **ATEX 2014/34/EU** | Equipment for explosive atmospheres | Category/group/zone, conformity assessment | Category-dependent |
| **PED 2014/68/EU** | Contains pressure vessels | Category, conformity assessment | Category-dependent |

**Application dates (volatile):**
- Machinery Regulation: 2027-01-20 [S,85]
- CRA: phased — vulnerability/incident reporting first, full conformity later [S,75]
- RED cybersecurity delegated act: Unknown — may be superseded by CRA [S,70]

**Action:** Complete the product register (`registers/product-register.md`) with Y/N/Unknown per instrument for each product.

---

## 3 — Functional safety standards

| Domain | Primary standard | Sector standard | SIL/PL method |
|--------|-----------------|----------------|---------------|
| Generic E/E/PE safety | IEC 61508 (2010) | — | Risk graph (Annex E) |
| Machinery | ISO 13849-1:2023 / IEC 62061 | EN ISO 13849-1 (hEN) | Performance Level (PL) |
| Process industry | IEC 61511 | — | LOPA / risk graph |
| Collaborative robots | ISO 13482 / ISO 10218 / ISO/TS 15066 | — | PL + force/pressure limits |
| Railway | EN 50126/50128/50129 | — | CENELEC SIL |
| Automotive | ISO 26262 | — | ASIL |

**Machinery Regulation EHSR — key safety clauses:**
- 1.1.2 — Safety integration principles (inherent safety → safeguarding → information)
- 1.1.9 — Protection against corruption (**cybersecurity of control systems**) [S,85]
- 1.2.1 — Safety and reliability of control systems (SIL/PL origin)
- 1.2.4 — Stopping functions (normal, operational, emergency)
- 1.2.6 — Failure of power supply

**Action:** For each CPS with safety functions, determine the governing standard, conduct hazard analysis, and populate `registers/hazard-register.md`.

---

## 4 — OT/ICS security standards

| Standard | Scope | Applies to |
|---------|-------|-----------|
| **IEC 62443** (all parts) | Industrial automation and control system security | Asset owners (2-1), integrators (2-4), products (4-1, 4-2), systems (3-3) |
| NIST SP 800-82 Rev 3 | Guide to OT security | US reference; useful for controls even in EU context |
| IEC 63069 | Safety-security interface framework | Systems where safety and security interact [S,75] |
| IEC TR 63074 | Safety and security for machinery | Machinery Regulation EHSR 1.1.9 guidance [S,80] |

**IEC 62443 parts and their audience:**

| Part | Title | Who | Output |
|------|-------|-----|--------|
| 2-1 | Security management system | Asset owner / operator | Security programme, policies, risk assessment |
| 2-4 | Security programme for service providers | Integrators / maintenance | Service provider requirements |
| 3-2 | System security requirements and security levels | System designer | Zone/conduit model, SL-T allocation |
| 3-3 | System security requirements for components | System/solution | Security levels per FR |
| 4-1 | Secure product development lifecycle | Component vendor | SDL requirements |
| 4-2 | Technical security requirements for components | Component | Component-level security requirements |

**Action:** Build the zone/conduit model (`registers/zone-conduit-register.md`), allocate SL-T per zone, and identify gaps.

---

## 5 — Operator obligations (NIS2)

If the organisation operating the CPS is an essential or important entity under NIS2:
- NIS2 Art 21 technical measures apply to the OT environment
- IEC 62443 controls map well to NIS2 Art 21 obligations
- Incident reporting (Art 23) applies to OT security incidents
- Supply chain due diligence (Art 21.2(d)) applies to CPS product suppliers

**Austrian transposition:** NISG 2026, effective 2026-10-01 [S,85].

**Cross-reference:** platform-assurance regulatory-mapping.md for the full NIS2/GDPR/CRA crosswalk at the IT layer.

---

## 6 — Framework interaction matrix

| Control domain | Mach. Reg | CRA | IEC 62443 | IEC 61508 | RED | NIS2 (operator) |
|---------------|-----------|-----|-----------|-----------|-----|-----------------|
| Risk assessment | EHSR 1.1.2 | Annex I | 3-2 (SL-T) | Part 1 (SIL) | — | Art 21.1 |
| Cybersecurity of controls | EHSR 1.1.9 | Annex I Part I | 3-3, 4-2 | — (but see IEC 63069) | Art 3.3(d) | Art 21.2(e) |
| Safety functions | EHSR 1.2.1 | — | Safety zone SL-T | Core scope | — | — |
| SBOM | — | Annex I Part II (mandatory) | — | — | — | Art 21.2(d) implied |
| Vulnerability handling | — | Annex I Part II | 4-1 | — | — | Art 21.2(e) |
| Incident reporting | — | 24h/72h/14d ENISA | — | — | — | 24h/72h/1mo CSIRT |
| Secure update | EHSR 1.2.1 (no regression) | Annex I Part I | 4-1, 4-2 | Mod mgmt | — | Art 21.2(e) |
| Physical safety | EHSR 1.3–1.5 | — | — | Core scope | — | — |
| CE marking | Required | Required | — | — | Required | — |

[S,80] — verify requirement IDs against current official texts.

---

*All applicability claims [I,80] unless noted. Specific standard edition/clause references [S,85]. EU regulation application dates are volatile — verify on EUR-Lex. Austrian NISG 2026 effective 2026-10-01 [S,85].*
