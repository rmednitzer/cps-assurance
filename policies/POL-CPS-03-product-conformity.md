# POL-CPS-03: Product Conformity and Post-Market Obligations Policy

**Version:** 1.0 DRAFT
**Owner:** Compliance Lead + Product Owner
**Approved by:** [Board / Executive management — name and date]
**Review cycle:** Annual + after new product placement or regulatory change
**Classification:** Internal

## Purpose

Ensure all CPS products placed on the EU market comply with applicable directives and regulations, maintain conformity post-market, and meet ongoing vulnerability handling and reporting obligations.

## Scope

All products with digital elements that the organisation manufactures, imports, or distributes on the EU market. Includes complete machines, safety components, embedded controllers, gateways, sensors, actuators, and IoT devices.

## Policy statements

1. Every product shall be registered in `registers/product-register.md` with all applicable directives identified before market placement.
2. Conformity assessment shall be completed for ALL applicable directives before CE marking is affixed. A single missing assessment blocks CE marking.
3. Technical documentation (per applicable Annex VII) shall be compiled and maintained for 10 years after last product placed on market.
4. EU Declaration of Conformity shall reference all applicable directives and be available in the official languages of target member states.
5. For CRA-scope products:
   a. SBOM shall be generated at build time and updated when components change.
   b. Vulnerability disclosure policy shall be published.
   c. Actively exploited vulnerabilities shall be reported to ENISA: 24h early warning, 72h notification, 14d final report [S,80].
   d. Free security updates shall be provided for the defined support period (≥ 5 years or expected product lifetime) [S,75].
6. For Machinery Regulation products, EHSR 1.1.9 (cybersecurity of control systems) compliance shall be demonstrated and documented.
7. Post-market monitoring: new vulnerability discoveries, field incidents, and regulatory changes shall trigger conformity re-assessment.
8. All conformity evidence shall be stored in the evidence pipeline: `evidence/governance/cps/products/{product-id}/`.

## Conformity assessment management

- **Pre-market:** Gap assessment using `templates/product-certification/TEMPLATE-product-gap-assessment.md`
- **Notified body engagement:** Required for Machinery Regulation Annex VII/VIII and CRA Class II/Critical. Engage early — NB capacity is constrained.
- **Post-market:** Vulnerability monitoring → SBOM-based CVE matching → response per CRA timeline

## Cross-references

| Requirement | Source |
|-------------|--------|
| Machinery Regulation 2023/1230 Annex VII (technical documentation) | EU 2023/1230 |
| CRA Annex I Part I + Part II (essential requirements) | EU 2024/2847 |
| RED Art 3 (essential requirements) | 2014/53/EU |
| LVD Art 3 (safety objectives) | 2014/35/EU |
| EMC Art 6 (essential requirements) | 2014/30/EU |
| CRA vulnerability reporting obligations | EU 2024/2847 |

## Review and approval

| Date | Version | Approved by | Signature |
|------|---------|-------------|-----------|
| YYYY-MM-DD | 1.0 | [Name, Title] | [Signature] |
