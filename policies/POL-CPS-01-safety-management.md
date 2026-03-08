# POL-CPS-01: Functional Safety Management Policy

**Version:** 1.0 DRAFT
**Owner:** Safety Manager
**Approved by:** [Board / Executive management — name and date]
**Review cycle:** Annual + after any safety-relevant change or incident
**Classification:** Internal

## Purpose

Establish the functional safety management system for the design, development, operation, and decommissioning of safety-related electrical, electronic, and programmable electronic (E/E/PE) systems.

## Scope

All CPS products and installations containing safety functions. Applies to safety-related hardware, software, and human actions credited in safety analyses.

## Policy statements

1. Every CPS with safety functions shall have a documented hazard analysis (STPA-informed per `docs/safety/functional-safety-approach.md`).
2. Safety Integrity Levels (SIL) or Performance Levels (PL) shall be allocated for each safety function based on risk assessment.
3. Safety functions shall be independent from non-safety functions unless common cause failure (CCF) is explicitly analysed and mitigated.
4. Changes to safety-related systems require joint safety-security review per CONTRIBUTING.md.
5. Safety function verification evidence (FMEDA, test reports, DC analysis) shall be maintained and stored in the evidence pipeline.
6. Periodic proof testing shall be conducted per the intervals determined in the hazard analysis.
7. Operator actions credited in safety analysis shall have defined response times, training requirements, and periodic validation.

## Safety lifecycle

Per IEC 61508-1 overall safety lifecycle (adapted):
1. Concept and scope definition
2. Hazard and risk analysis → `registers/hazard-register.md`
3. Safety requirements allocation (SIL/PL + hardware/software/human)
4. Design and development (per applicable sector standard)
5. Verification and validation
6. Installation and commissioning → `checklists/pre-commissioning-safety.md`
7. Operation and maintenance
8. Modification → safety-critical change process (CONTRIBUTING.md)
9. Decommissioning

## Roles

- **Safety Manager:** Approve safety analyses; oversee lifecycle; report to management.
- **Safety Engineer:** Conduct hazard analysis; specify safety functions; review changes.
- **OT Security Lead:** Joint review for safety-security interactions.
- **Operations:** Execute proof tests; report safety anomalies.

## Cross-references

| Requirement | Source |
|-------------|--------|
| IEC 61508-1 Clause 6–8 (safety lifecycle) | IEC 61508 |
| ISO 13849-1:2023 (PL determination, Category) | ISO 13849 |
| Machinery Regulation EHSR 1.2.1 (control system reliability) | EU 2023/1230 |
| IEC 63069 (safety-security interface) | IEC 63069 |

## Proof test strategy

- Proof test intervals shall be determined using IEC 61508-1 methods (risk graph, PFD calculation) and documented in the hazard register.
- Proof tests shall be conducted by qualified personnel (safety engineer or trained operator under supervision).
- Proof test evidence shall include: date, tester identity, safety function tested, test stimulus, measured response time, pass/fail determination, deviations noted.
- Proof test records are governance_10y retention tier.
- Reference: `docs/safety/proof-test-methodology.md`

## FMEDA and reliability analysis

- All safety functions allocated SIL 2 or higher (or PL d/e) shall have FMEDA or equivalent reliability analysis.
- Analysis shall document: diagnostic coverage (DC), safe failure fraction (SFF), hardware fault tolerance (HFT), common cause failure beta-factor.
- Results shall demonstrate that the allocated SIL/PL is achievable with the selected hardware architecture.
- FMEDA evidence is governance_10y retention tier.

## Hardware fault tolerance and diagnostic coverage

- Hardware architecture shall achieve HFT and DC targets per IEC 61508-2 Table 2/3.
- SIL 1: HFT 0 with DC ≥60%; SIL 2: HFT 0 with DC ≥90% or HFT 1 with DC ≥60%; SIL 3: HFT 1 with DC ≥90% or HFT 2 with DC ≥60%.
- Calculations shall use beta-factor model for CCF per IEC 61508-6 Annex D.

## Software integrity

- Software for safety functions shall be developed using techniques per IEC 61508-3 Annex F appropriate to the target SIL.
- SIL 1-2: structured design, defensive programming, static analysis, functional testing.
- SIL 3-4: formal methods or semi-formal methods, model-based testing, independent verification.
- Software modification management: impact analysis required before any change; full re-verification for changes affecting safety function logic; partial re-verification for non-safety-affecting changes.

## Operator competency

- Operator actions credited in safety analysis shall have documented response time requirements and training plans.
- Training shall be conducted before initial operation and revalidated annually.
- Competency records are governance_10y retention tier.

## Decommissioning

- Safety functions being decommissioned shall follow a documented safe disablement procedure.
- Notification to all affected stakeholders before decommissioning.
- Decommissioned evidence retained per governance_10y tier.

## Review and approval

| Date | Version | Approved by | Signature |
|------|---------|-------------|-----------|
| YYYY-MM-DD | 1.0 | [Name, Title] | [Signature] |
