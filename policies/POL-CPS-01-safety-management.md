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

## Review and approval

| Date | Version | Approved by | Signature |
|------|---------|-------------|-----------|
| YYYY-MM-DD | 1.0 | [Name, Title] | [Signature] |
