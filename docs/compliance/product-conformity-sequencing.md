# Multi-Directive Conformity Assessment Sequencing

**Date:** 2026-03-08
**Scope:** CPS products subject to multiple EU directives/regulations simultaneously
**Status:** DRAFT — sequencing recommendations are based on regulatory analysis and practical experience [S,85].

---

## Confidence notes

The principle that each directive's conformity assessment is independent and that CE marking is cumulative is established in the Blue Guide [F,90]. Recommended sequencing is practical guidance [S,85]. Typical assessment durations are estimates based on industry norms [I,70]. Shared evidence opportunities are analytically derived [S,80].

---

## 1 — The multi-directive challenge

CPS products routinely fall under **3–5 EU directives/regulations simultaneously** [S,85]:

| Typical CPS product | Applicable instruments | Count |
|---------------------|----------------------|-------|
| Networked safety PLC | Machinery Reg, CRA, LVD, EMC | 4 |
| Wireless industrial gateway | Machinery Reg (if machinery component), CRA, RED, EMC | 3–4 |
| Robot controller with Wi-Fi | Machinery Reg, CRA, RED, LVD, EMC | 5 |
| Smart sensor (SIL-rated, cellular) | Machinery Reg, CRA, RED, LVD, EMC | 5 |
| AI-enabled vision system for machinery | Machinery Reg, CRA, AI Act, EMC, (possibly RED) | 4–5 |

Each instrument has its own essential requirements, conformity assessment procedures, and documentation obligations. The manufacturer must satisfy **all** of them before affixing the CE marking.

---

## 2 — Sequencing principles

### 2.1 Independence of assessments

Each directive's conformity assessment is **legally independent** [F,90]:

- A Machinery Regulation assessment does not satisfy CRA requirements (and vice versa)
- A notified body certificate under one directive does not cover another
- Failure under one directive does not invalidate conformity under another (but CE marking cannot be affixed until all pass)

### 2.2 Cumulative CE marking

The CE marking is **cumulative**: it indicates conformity with ALL applicable directives [F,90]:

- A single CE mark is affixed to the product
- The EU Declaration of Conformity must reference ALL applicable directives
- If a notified body is involved under any directive, its identification number appears next to the CE mark
- CE marking must NOT be affixed until ALL applicable conformity assessments are complete

### 2.3 Per-directive Declaration of Conformity

The EU Declaration of Conformity (DoC) may be structured as [F,90]:

- A **single combined DoC** listing all applicable directives, or
- **Separate DoCs** per directive (which together form the complete declaration)

A combined DoC is recommended for simplicity, listing each directive with its specific essential requirements, harmonised standards applied, and notified body details (if any).

---

## 3 — Recommended assessment sequence for CPS products

### 3.1 Phase 0: Determine full regulatory applicability

**Before starting any assessment:**

1. Complete product characterisation (see `docs/compliance/conformity-assessment-guide.md`, Section A)
2. Populate the applicability matrix (Section B of the same document)
3. Identify ALL applicable directives/regulations — missing one invalidates the entire CE marking

### 3.2 Phase 1: LVD and EMC (simplest, most mature)

**Why first:**
- Mature standards landscape — hENs readily available
- Well-established testing procedures
- Self-assessment (internal production control) for most products
- Testing can begin on prototypes; results rarely require design changes
- Typically the fastest to complete

**Activities:**
- LVD: apply EN 60204-1 (machinery electrical safety) or EN 62368-1 (ICT equipment) or sector-specific EN; test against safety objectives
- EMC: apply EN 55032/55035 or sector-specific EN; emission + immunity testing
- Duration: 2–4 weeks for testing; 1–2 weeks for documentation [I,70]

**Output:** Test reports, standards compliance checklists, LVD/EMC sections of technical documentation

### 3.3 Phase 2: Machinery Regulation (if applicable)

**Why second:**
- The safety risk assessment (ISO 12100 / STPA) **drives the fundamental product architecture**
- SIL/PL allocation for safety functions determines hardware and software design constraints
- Safety architecture decisions constrain subsequent cybersecurity choices
- May require notified body involvement (Annex I high-risk machinery)

**Activities:**
1. Hazard identification and risk assessment (ISO 12100)
2. SIL/PL determination and allocation (ISO 13849-1 / IEC 62061)
3. FMEDA and reliability calculations
4. Safety function testing
5. EHSR compliance matrix (Annex III)
6. EHSR 1.1.9 (cybersecurity of control systems) — note: feeds into CRA assessment
7. Conformity assessment per applicable Annex (V, VII, or VIII)
8. Duration: 3–12 months depending on complexity and NB involvement [I,70]

**Output:** Safety risk assessment, SIL/PL certificates, FMEDA reports, safety test reports, NB certificate (if applicable), Machinery Regulation section of technical documentation

### 3.4 Phase 3: RED (if wireless)

**Why third:**
- Builds on EMC testing (Article 3.1(b) overlaps with EMC Directive)
- Cybersecurity requirements under Delegated Regulation (EU) 2022/30 overlap with CRA — assess together
- Radio spectrum efficiency testing is product-specific

**Activities:**
1. Article 3.1(a) — health and safety (may reference LVD results)
2. Article 3.1(b) — EMC (may reference EMC test results)
3. Article 3.2 — radio spectrum efficiency (RF testing)
4. Article 3.3(d)(e)(f) — cybersecurity (Delegated Regulation 2022/30): network protection, fraud prevention, personal data protection
5. Apply EN 18031 series if cited in OJ by assessment date; otherwise demonstrate compliance by other means
6. Duration: 4–8 weeks for RF testing; cybersecurity assessment aligns with CRA [I,70]

**Output:** RF test reports, EN 18031 compliance assessment (or equivalent), RED section of technical documentation

### 3.5 Phase 4: CRA (newest, most complex)

**Why fourth:**
- Benefits from having the safety architecture (Machinery Regulation) established — cybersecurity design builds on safety constraints
- Benefits from RF testing (RED) being complete — security of radio interfaces is a CRA concern
- Most complex for CPS products: Annex I Part I (security properties) + Part II (vulnerability handling, SBOM, reporting)
- hENs not yet available — assessment burden is higher
- May require notified body (Class I without hEN, Class II, Critical)

**Activities:**
1. Product classification (see `docs/compliance/cra-product-classification.md`)
2. CRA Annex I Part I compliance: security risk assessment, secure-by-default configuration, access control, cryptography, data protection, resilience, update mechanism, event logging, DoS resilience
3. CRA Annex I Part II compliance: SBOM (see `docs/compliance/cra-sbom-requirements.md`), vulnerability handling process, ENISA reporting process, coordinated vulnerability disclosure
4. Conformity assessment per classification (Module A, B+C, or H)
5. Notified body engagement if required (see `docs/compliance/cra-chapter-iv-implementation.md`)
6. Duration: 3–9 months depending on classification and NB involvement [I,70]

**Output:** CRA compliance matrix, SBOM, vulnerability handling documentation, penetration test report, NB certificate (if applicable), CRA section of technical documentation

### 3.6 Phase 5: AI Act (if ML/AI components)

**Why last:**
- Only applies if the product contains an AI system as defined in the AI Act
- AI risk classification is product-context dependent — benefits from having the full product architecture defined
- May share risk assessment elements with Machinery Regulation (high-risk AI in safety machinery)

**Activities:**
1. Determine if the product contains an AI system
2. Classify AI risk tier (prohibited, high-risk, limited risk, minimal risk)
3. For high-risk AI: risk management system, data governance, technical documentation, transparency, human oversight, accuracy/robustness/cybersecurity
4. Conformity assessment per risk tier
5. Duration: 2–6 months for high-risk AI [I,70]

**Output:** AI risk classification, AI-specific risk management documentation, AI Act section of technical documentation

---

## 4 — Shared evidence opportunities

A single evidence artifact can satisfy requirements across multiple directives [S,80]:

| Evidence artifact | Machinery Reg | CRA | RED | LVD | EMC | AI Act |
|------------------|--------------|-----|-----|-----|-----|--------|
| **Risk assessment (ISO 12100 + cybersecurity)** | EHSR 1.1.2 | Annex I (security risk) | — | — | — | Art. 9 (risk mgmt) |
| **EMC test report** | — | — | Art. 3.1(b) | — | **Primary** | — |
| **Electrical safety test report** | EHSR 1.5 (electrical) | — | Art. 3.1(a) | **Primary** | — | — |
| **Penetration test report** | EHSR 1.1.9 (partial) | Annex I | Art. 3.3(d) | — | — | Art. 15 (cybersecurity) |
| **SIL/PL analysis** | EHSR 1.2.1 | — | — | — | — | Art. 15 (robustness) |
| **SBOM** | — | **Annex I Part II** | — | — | — | — |
| **Security architecture documentation** | EHSR 1.1.9 | Annex I | Art. 3.3(d) | — | — | Art. 15 |
| **Update mechanism documentation** | EHSR 1.2.1 (no safety regression) | Annex I (secure update) | — | — | — | Art. 15 |
| **RF emission/immunity test report** | — | — | Art. 3.1(b), 3.2 | — | Shared | — |

**Key efficiency gains:**

- A **single EMC test campaign** can produce reports satisfying both the EMC Directive and RED Art. 3.1(b)
- A **unified risk assessment** covering both safety hazards and cybersecurity threats satisfies Machinery Regulation EHSR 1.1.2, CRA Annex I security risk assessment, and AI Act Article 9 (if applicable)
- A **penetration test report** can serve Machinery Regulation EHSR 1.1.9, CRA Annex I, RED Art. 3.3(d), and AI Act Article 15
- **Security architecture documentation** serves multiple instruments — write once, reference from each directive's compliance matrix

---

## 5 — Unified technical documentation structure

Organise a **single technical documentation package** with directive-specific sections:

```
CPS Product Technical Documentation
├── 0. Document control (version, date, approval, distribution)
├── 1. Product description (all directives)
├── 2. Regulatory applicability analysis
├── 3. Risk assessment (unified: safety + security + AI)
├── 4. Design documentation (shared across directives)
├── 5. Directive-specific compliance
│   ├── 5.1 Machinery Regulation (EHSR matrix, safety evidence)
│   ├── 5.2 CRA (Annex I matrix, SBOM, CVD, vulnerability handling)
│   ├── 5.3 RED (Art. 3 matrix, RF testing, cybersecurity)
│   ├── 5.4 LVD (safety objectives, test reports)
│   ├── 5.5 EMC (emission/immunity test reports)
│   └── 5.6 AI Act (risk classification, AI-specific requirements)
├── 6. Standards applied (all directives)
├── 7. Test reports and certificates
├── 8. Instructions and labelling
├── 9. EU Declaration(s) of Conformity
├── 10. Notified body certificates
└── 11. Post-market obligations
```

See `docs/compliance/conformity-assessment-guide.md`, Section H for the detailed structure.

---

## 6 — Documentation traceability matrix

Use this template to trace each documentation section to directive-specific requirements and evidence artifacts:

| Doc section | Machinery Reg Annex III EHSR | CRA Annex I | RED Article | LVD Annex I | EMC Annex I | AI Act Article | Evidence artifact |
|------------|----------------------------|-------------|-------------|-------------|-------------|---------------|------------------|
| Risk assessment | 1.1.2 (integration of safety) | Part I (security risk) | — | — | — | Art. 9 | `risk-assessment-report.pdf` |
| Safety architecture | 1.2.1 (SIL/PL) | — | — | — | — | Art. 15 (robustness) | `safety-architecture.pdf`, `sil-allocation.xlsx` |
| Security architecture | 1.1.9 (corruption protection) | Part I (all security properties) | 3.3(d) | — | — | Art. 15 (cybersecurity) | `security-architecture.pdf`, `zone-conduit-model.pdf` |
| Access control | — | Part I (AuthN/AuthZ) | 3.3(d) | — | — | Art. 14 (human oversight) | `access-control-design.pdf` |
| Cryptography | — | Part I (encryption) | 3.3(d) | — | — | — | `crypto-architecture.pdf` |
| SBOM | — | Part II (mandatory) | — | — | — | — | `sbom.cdx.json` |
| Vulnerability handling | — | Part II (CVD process) | — | — | — | — | `cvd-policy.pdf` |
| Update mechanism | 1.2.1 (no safety regression) | Part I (secure update) | — | — | — | — | `update-mechanism-design.pdf` |
| EMC test results | — | — | 3.1(b) | — | Obj. 1, 2 | — | `emc-test-report.pdf` |
| Electrical safety | 1.5 (electrical hazards) | — | 3.1(a) | Obj. 1–3 | — | — | `electrical-safety-report.pdf` |
| RF performance | — | — | 3.2 | — | — | — | `rf-test-report.pdf` |
| Penetration testing | 1.1.9 (partial) | Part I (testing) | 3.3(d) | — | — | Art. 15 | `pentest-report.pdf` |
| Instructions | 1.7.4 (instructions) | Part II (user info) | Art. 10.8 | Annex III.2 | Annex I.1(b) | Art. 13 (transparency) | `user-manual.pdf` |

---

## 7 — Timeline planning

### 7.1 Typical durations per directive assessment

| Phase | Activities | Typical duration | Dependencies |
|-------|-----------|-----------------|-------------|
| Phase 0: Applicability | Product characterisation, regulatory analysis | 2–4 weeks | None |
| Phase 1: LVD + EMC | Standard selection, testing, documentation | 4–8 weeks | Phase 0 |
| Phase 2: Machinery Reg | Risk assessment, SIL/PL, safety testing, NB (if needed) | 3–12 months | Phase 0; partly parallel with Phase 1 |
| Phase 3: RED | RF testing, cybersecurity assessment | 4–8 weeks | Phase 1 (EMC results); partly parallel with Phase 2 |
| Phase 4: CRA | Classification, Annex I compliance, SBOM, NB (if needed) | 3–9 months | Phase 2 (safety architecture); Phase 3 (if wireless) |
| Phase 5: AI Act | AI risk classification, AI-specific assessment | 2–6 months | Phase 2 (risk assessment) |
| Final: DoC + CE | Compile DoC, verify all assessments complete, affix CE | 2–4 weeks | All phases complete |

### 7.2 Parallelisation opportunities

```
Month:  1   2   3   4   5   6   7   8   9  10  11  12  13  14
        ├───────────────────────────────────────────────────────┤
Ph 0:   ████
Ph 1:       ████████
Ph 2:       ████████████████████████████████████████
Ph 3:               ████████████
Ph 4:                       ████████████████████████████
Ph 5:                       ████████████████████
Final:                                              ████████
        ├───────────────────────────────────────────────────────┤
```

- Phases 1, 2, and 3 can overlap significantly
- Phase 4 (CRA) benefits from Phase 2 (Machinery Reg) safety architecture being established, but can start classification and SBOM preparation earlier
- Phase 5 (AI Act) can run largely in parallel with Phases 4 and 5
- **Critical path** is typically Phase 2 (Machinery Regulation) for safety-critical CPS, or Phase 4 (CRA) for complex cybersecurity assessments requiring a notified body

### 7.3 Total timeline estimate

| Product complexity | Estimated total | Key driver |
|-------------------|----------------|-----------|
| Simple CPS (Default CRA, no Machinery Reg NB) | 4–6 months [I,70] | LVD/EMC testing + CRA self-assessment |
| Medium CPS (Class I CRA, Machinery Reg self-assessment) | 6–10 months [I,70] | CRA NB (if no hEN) + safety documentation |
| Complex CPS (Class II CRA, Machinery Reg NB, RED) | 10–16 months [I,70] | NB engagement for both Machinery Reg and CRA |
| Complex CPS + AI Act | 12–18 months [I,70] | AI Act adds parallel workstream |

---

## 8 — CE marking

### 8.1 When to affix

CE marking is affixed **only after ALL applicable conformity assessments are complete** and ALL Declarations of Conformity are drawn up [F,90].

Do not affix CE marking after completing one directive while others are pending — this is a legal requirement, not a best practice.

### 8.2 Single CE mark, all directives

- One CE marking on the product covers ALL applicable directives [F,90]
- If any notified body was involved (under any directive), its four-digit identification number is placed next to the CE mark
- If multiple notified bodies were involved (e.g., one for Machinery Regulation, another for CRA), all identification numbers appear next to the CE mark

### 8.3 CE marking placement

- Affixed to the product or its data plate
- Visible, legible, indelible
- Minimum height 5 mm
- If the product is too small: on the packaging and/or accompanying documents

---

## Cross-references

- `docs/compliance/conformity-assessment-guide.md` — unified conformity assessment guide (Sections A–L)
- `docs/compliance/regulatory-mapping.md` — cross-framework control mapping and shared evidence catalogue
- `docs/compliance/cra-chapter-iv-implementation.md` — CRA notified body engagement (Phase 4 detail)
- `docs/compliance/cra-product-classification.md` — CRA classification (determines Phase 4 scope)
- `docs/compliance/cra-sbom-requirements.md` — SBOM requirements (Phase 4 deliverable)
- `docs/compliance/hEN-tracker.md` — hEN availability affects assessment route and timeline
- `docs/safety/functional-safety-approach.md` — SIL/PL determination (Phase 2 input)
- `docs/safety/safety-security-interaction.md` — safety-security conflicts affecting Phase 2 ↔ Phase 4

---

*Assessment independence and cumulative CE marking [F,90]. Sequencing recommendations [S,85]. Shared evidence opportunities [S,80]. Timeline estimates [I,70]. Verify directive-specific requirements against current official texts.*
