# CRA Chapter IV — Notification of Conformity Assessment Bodies

**Date:** 2026-03-08
**Regulation:** Cyber Resilience Act (EU 2024/2847), Chapter IV (Articles 35–51)
**Status:** DRAFT — verify against current official text before use in regulatory engagement.

---

## Confidence notes

CRA Chapter IV applies from **2026-06-11** [F,90]. This is the earliest substantive application date of the CRA, preceding the Article 14 reporting obligation (2026-09-11) and full application (2027-12-11). The purpose is to allow notified bodies to be designated and operational before manufacturers must use them for conformity assessment. Specific notified body availability and fee structures are [I,70] — contact candidate bodies directly.

---

## 1 — Chapter IV overview

Chapter IV establishes the framework for **notified bodies** — organisations designated by EU Member States to perform third-party conformity assessment under the CRA. It covers:

- Requirements for notification of conformity assessment bodies (Articles 35–38)
- Requirements that notified bodies must meet (Article 39)
- Presumption of conformity of notified bodies (Article 40)
- Subsidiaries and subcontracting (Article 41)
- Application for notification (Article 42)
- Notification procedure (Article 43)
- Identification numbers and lists (Article 44)
- Changes to notifications (Article 45)
- Challenge of competence of notified bodies (Article 46)
- Operational obligations of notified bodies (Article 47)
- Appeal against decisions of notified bodies (Article 48)
- Information obligation (Article 49)
- Coordination of notified bodies (Article 50)
- Exchange of experience (Article 51)

**Application date:** 2026-06-11 [F,90]. From this date, Member States must have processes in place to designate notified bodies, and bodies may begin applying for designation.

---

## 2 — Notified body roles and designation

### 2.1 What is a notified body?

A notified body is a conformity assessment body designated by a Member State's notifying authority and notified to the Commission and other Member States. It performs third-party conformity assessment activities specified in the CRA (EU-type examination, quality assurance system assessment) [F,90].

### 2.2 Requirements for notified bodies (Article 39)

A notified body must:

- Be established under national law of a Member State
- Have legal personality
- Be independent of the product it assesses and of the manufacturer
- Demonstrate technical competence, relevant experience, and adequate staffing
- Have appropriate liability insurance
- Ensure confidentiality of information obtained during assessment
- Participate in coordination and standardisation activities

Competence is typically demonstrated through **accreditation** by a national accreditation body (e.g., DAkkS in Germany, UKAS in UK, COFRAC in France) against EN ISO/IEC 17065 (product certification) or EN ISO/IEC 17021 (management system certification), supplemented by CRA-specific scope [S,85].

### 2.3 Presumption of conformity (Article 40)

A conformity assessment body that demonstrates conformity with criteria laid down in relevant harmonised standards (or parts thereof) referenced in the OJEU shall be presumed to comply with the Article 39 requirements to the extent those standards cover them [F,90].

### 2.4 Identification and listing (Article 44)

Designated notified bodies are assigned an identification number by the Commission and listed in the **NANDO database** (New Approach Notified and Designated Organisations): [https://ec.europa.eu/growth/tools-databases/nando/](https://ec.europa.eu/growth/tools-databases/nando/) [F,90].

**Current status (2026-03-08):** The NANDO database may not yet list CRA-notified bodies, as the designation process is only beginning. Monitor NANDO quarterly for updates [S,80].

---

## 3 — Conformity assessment procedures

The CRA defines three conformity assessment modules, aligned with Decision 768/2008/EC:

### 3.1 Module A — Internal production control (CRA Annex VI)

- **Performed by:** Manufacturer (self-assessment)
- **Scope:** Manufacturer ensures product meets CRA Annex I essential requirements, prepares technical documentation, performs internal checks
- **Notified body:** Not required
- **Certificate:** None — manufacturer draws up EU Declaration of Conformity

### 3.2 Module B + C — EU-type examination + Conformity to type (CRA Annex VII)

- **Module B (EU-type examination):** Notified body examines the technical design of the product (and possibly a specimen) and certifies it meets CRA Annex I requirements
- **Module C (Conformity to type):** Manufacturer ensures production conforms to the approved type; notified body may conduct periodic checks
- **Certificate:** EU-type examination certificate issued by notified body (Module B); valid for up to 5 years, renewable [S,85]

### 3.3 Module H — Full quality assurance (CRA Annex VIII)

- **Performed by:** Notified body assesses the manufacturer's quality management system covering design, production, final product inspection, and testing
- **Scope:** Entire lifecycle from design to production
- **Certificate:** Quality system approval; notified body conducts surveillance audits
- **Advantage:** Efficient for manufacturers with many products — single QA system approval covers the portfolio

---

## 4 — When each module applies

The applicable conformity assessment module depends on the product's CRA classification [S,85]:

| Classification | Conformity route | Notified body required? |
|---------------|-----------------|------------------------|
| **Default** (not in Annex III or IV) | Module A (internal) | No |
| **Class I** (Annex III Part I) — hEN applied and covers all Annex I requirements | Module A (internal) | No |
| **Class I** (Annex III Part I) — hEN NOT applied or not covering all requirements | Module B+C **or** Module H | **Yes** |
| **Class II** (Annex III Part II) | Module B+C **or** Module H | **Yes** |
| **Critical** (Annex IV) | Module B+C **or** Module H | **Yes** |

**Key insight for CPS manufacturers:** Since harmonised standards under the CRA have not yet been published (as of 2026-03-08) [S,80], Class I products currently cannot rely on Module A and will require notified body involvement until hENs are available and applied. Plan accordingly.

**European cybersecurity certification schemes** (under the Cybersecurity Act) may also be referenced as an alternative demonstration of compliance for certain requirements, subject to implementing acts [S,75].

---

## 5 — Certificate management

### 5.1 Validity and renewal

- EU-type examination certificates (Module B) are valid for a maximum of **5 years** [S,85]
- Renewal must be requested before expiry; the notified body re-examines the type
- Changes to the product, the applicable harmonised standards, or the state of the art may require re-examination before expiry

### 5.2 Suspension and revocation

A notified body may suspend or revoke a certificate if:

- The manufacturer no longer meets the requirements
- The product no longer conforms to the approved type
- The manufacturer fails to fulfil conditions attached to the certificate

The manufacturer may appeal (Article 48).

### 5.3 Tracking obligations

Maintain a register of:

- Certificate number, issuing body, scope, validity dates
- Surveillance audit schedule and results
- Any restrictions, suspensions, or conditions
- Expiry reminders (trigger renewal process 6 months before expiry)

---

## 6 — Notified body engagement checklist

### 6.1 Timeline

Start notified body engagement **at least 6 months before planned market placement** [I,70]. For novel or complex CPS products, 9–12 months is advisable. Consider:

- Notified body availability: limited capacity in early CRA period (2026–2027)
- Assessment duration: Module B typically 3–6 months; Module H initial assessment 2–4 months
- Iteration: address findings, re-submit documentation, re-test

### 6.2 Pre-engagement preparation

Before approaching a notified body:

1. **Complete product classification** — confirm CRA classification tier (see `docs/compliance/cra-product-classification.md`)
2. **Identify applicable hENs** — check if any CRA harmonised standards have been published (see `docs/compliance/hEN-tracker.md`)
3. **Prepare technical documentation** to CRA Annex VII requirements:
   - Product description and intended use
   - Design and manufacturing documentation
   - CRA Annex I compliance matrix with evidence references
   - SBOM (see `docs/compliance/cra-sbom-requirements.md`)
   - Vulnerability handling procedures
   - Security risk assessment
   - Test reports (functional testing, penetration testing)
4. **Prepare a compliance summary** mapping each Annex I requirement to evidence
5. **Budget allocation** — NB fees vary; expect EUR 15,000–80,000 depending on scope and module [I,60]

### 6.3 Selection criteria for notified body

- Designated under CRA (check NANDO database)
- Relevant sector experience (industrial automation, embedded systems, CPS)
- Geographic accessibility for surveillance audits
- Capacity and lead time
- Fee structure transparency
- Experience with adjacent regulations (Machinery Regulation, RED) — beneficial for multi-directive products

### 6.4 Documentation requirements for NB submission

| Document | Module B+C | Module H |
|----------|-----------|----------|
| Technical documentation (CRA Annex VII) | Required | Required |
| Product specimen or access to test environment | Required | On request |
| SBOM | Required | Required |
| Security risk assessment | Required | Required |
| Vulnerability handling process | Required | Required |
| Quality management system documentation | Not required | Required |
| Design review records | As needed | Required |
| Production control records | Module C | Required |

---

## 7 — How to find notified bodies

### 7.1 NANDO database

The primary source for identifying CRA-notified bodies:

- URL: [https://ec.europa.eu/growth/tools-databases/nando/](https://ec.europa.eu/growth/tools-databases/nando/)
- Search by: legislation (CRA / EU 2024/2847), product category, Member State, body name
- Each entry shows: scope of designation, contact details, identification number

### 7.2 Industry associations

- ENISA may publish guidance on notified body landscape
- Sector associations (e.g., VDMA, ZVEI for industrial automation) may maintain lists of recommended bodies

### 7.3 Early engagement

Given that CRA notified body designation is in its early phase (Chapter IV applies from 2026-06-11), manufacturers should:

- Contact candidate bodies now to understand timeline for designation
- Consider bodies already notified under Machinery Regulation or RED — they may seek CRA designation
- Monitor NANDO quarterly for new CRA-designated bodies

---

## 8 — Integration with Machinery Regulation notified body processes

### 8.1 Can the same notified body cover both?

Yes, in principle. A single conformity assessment body can be designated under multiple directives/regulations, provided it meets the requirements for each [S,85]. Benefits:

- Coordinated assessment schedule
- Shared understanding of product architecture
- Potential for combined audits (Module H / Annex VIII under Machinery Regulation)
- Reduced administrative overhead

### 8.2 Practical considerations

- The body must hold **separate designations** under each regulation — CRA designation does not automatically cover Machinery Regulation, and vice versa
- Assessment scopes are different: Machinery Regulation focuses on EHSR (safety); CRA focuses on Annex I (cybersecurity)
- Combined audits require careful planning to avoid scope creep and ensure each regulation's requirements are fully addressed
- The technical documentation can be a **single unified package** with directive-specific sections (see `docs/compliance/conformity-assessment-guide.md`, Section H)

### 8.3 Sequencing with Machinery Regulation assessment

For CPS products requiring notified body involvement under both Machinery Regulation and CRA:

1. **Machinery Regulation first** — safety assessment drives the fundamental architecture
2. **CRA second** — cybersecurity assessment builds on the established safety architecture
3. **Joint review** of safety-security interaction points (EHSR 1.1.9 ↔ CRA Annex I)

See `docs/compliance/product-conformity-sequencing.md` for the full multi-directive sequencing guide.

---

## Cross-references

- `docs/compliance/cra-product-classification.md` — CRA classification decision tree (determines which module applies)
- `docs/compliance/cra-sbom-requirements.md` — SBOM requirements for NB submission
- `docs/compliance/hEN-tracker.md` — harmonised standard availability (determines Module A eligibility for Class I)
- `docs/compliance/product-conformity-sequencing.md` — multi-directive assessment sequencing
- `docs/compliance/conformity-assessment-guide.md` — unified conformity assessment guide
- `docs/compliance/regulatory-mapping.md` — cross-framework control mapping

---

*Chapter IV application date 2026-06-11 [F,90]. Module applicability per classification [S,85]. Notified body fees and timelines [I,70]. Verify NANDO database for current CRA-designated bodies.*
