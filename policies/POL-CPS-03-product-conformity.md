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

## SBOM generation and management

- SBOMs shall be generated in CI at build time using CycloneDX 1.5+ or SPDX 2.3+ format.
- SBOMs shall be regenerated within 24h when components are added, removed, or updated.
- SBOM retention: governance_10y (CRA requires technical documentation retention for 10 years from last unit placed on market).
- SBOM validation: all direct and transitive dependencies included; no component gaps.
- Reference: `docs/compliance/cra-sbom-requirements.md`

## Support period definition

- Support period shall be published and communicated to customers before purchase.
- Minimum support period: 5 years from product release or expected product lifetime, whichever is longer.
- During support period: free security updates for all severity levels.
- End-of-support: critical vulnerability patches provided for additional 2 years; customers notified 12 months before end-of-support.
- End-of-life: product removed from market; DoC withdrawn if no longer conformant.

## Vulnerability response timeline

- Critical: assessment within 24h, patch within 48h, customer notification within 72h.
- High: assessment within 72h, patch within 2 weeks, customer notification within 1 week.
- Medium: patch within next planned release, customer notification via release notes.
- Low: patch at discretion, documented in release notes.
- Actively exploited vulnerabilities: ENISA reporting per POL-CPS-04.

## Notified body engagement

- Products requiring NB assessment (Machinery Reg Annex VII/VIII, CRA Class II/Critical): engage NB minimum 6 months before intended market release.
- Pre-notification review: submit draft technical documentation to NB for gap identification.
- NB selection criteria: accreditation scope covers all applicable directives, capacity available, references from similar CPS products.
- If NB rejects conformity package: document gaps, remediate, re-submit within 4 weeks.

## Third-party vulnerability management

- Monitor NVD, ICS-CERT, and vendor advisories for all third-party components in product SBOMs.
- Responsibility: product owner accountable; security team conducts monitoring.
- If third-party vulnerability affects product: assess impact within 48h; apply patch or document compensating controls.
- If third-party component is end-of-life with no patch: replace component or document risk acceptance with safety-security impact analysis.

## Post-market monitoring process

- Continuous monitoring of: NVD/CVE databases, ICS-CERT advisories, customer incident reports, field failure data.
- Quarterly review of monitoring results by product owner + compliance lead.
- Conformity re-assessment triggered by: critical vulnerability in product, regulatory change affecting product, field safety incident, customer complaint indicating non-compliance.
- Re-assessment timeline: within 4 weeks of trigger event.

## Regulatory change management

- Legal/compliance team monitors EUR-Lex for: new directives, harmonised standards, delegated acts, implementing acts.
- Regulatory changes assessed for impact within 4 weeks of publication.
- If impact identified: conformity re-assessment scheduled within next planned release or urgent if critical.
- hEN tracking per `docs/compliance/hEN-tracker.md`

## Review and approval

| Date | Version | Approved by | Signature |
|------|---------|-------------|-----------|
| YYYY-MM-DD | 1.0 | [Name, Title] | [Signature] |
