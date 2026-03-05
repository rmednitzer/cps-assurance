# CPS Product Regulatory Gap Assessment

## Product: [Product name]
## Manufacturer: [Company name]
## Assessment date: [YYYY-MM-DD]
## Author: [Name] | Reviewer: [Name] | Approved: [Name, Date]

---

## 1. Product Characterisation

- **Product name and model:**
- **Description:**
- **Functions:** Control / Sensing / Communication / Safety / Processing
- **Physical form:** Embedded controller / Gateway / Sensor / Actuator / Machine / Robot / IoT device / Safety component
- **Digital elements:** Firmware / Software / AI-ML / Updatable components
- **Connectivity:** Wired (Ethernet/Fieldbus) / Wireless (Wi-Fi/BLE/Cellular/LoRa) / None
- **Target market:** EU (Y/N) — member states: [list]
- **Economic operator role:** Manufacturer / Authorised rep / Importer / Distributor
- **Intended use:**
- **Reasonably foreseeable misuse:**
- **Safety criticality:** Can cause injury/death on failure (Y/N) — describe
- **Integration:** Standalone / Component in larger system
- **Existing certifications:**

---

## 2. Applicable Directives/Regulations Matrix

| Instrument | Applies? | Rationale | Conformity route | Status |
|-----------|---------|-----------|-----------------|--------|
| Machinery Regulation 2023/1230 | Y/N/Unknown | | Internal / NB | Not started / In progress / Complete |
| CRA (EU 2024/2847) | Y/N/Unknown | | Internal / Class I / Class II / Critical | |
| RED 2014/53/EU | Y/N/Unknown | | | |
| LVD 2014/35/EU | Y/N/Unknown | | | |
| EMC 2014/30/EU | Y/N/Unknown | | | |
| AI Act | Y/N/Unknown | | | |
| ATEX 2014/34/EU | Y/N/Unknown | | | |
| PED 2014/68/EU | Y/N/Unknown | | | |
| GPSR | Y/N/Unknown | | | |
| Other: [specify] | Y/N/Unknown | | | |

---

## 3. Machinery Regulation EHSR Gap Assessment

| EHSR | Requirement summary | Evidence available | Gap | Remediation | Priority |
|------|--------------------|--------------------|-----|-------------|----------|
| 1.1.2 | Safety integration principles | | | | |
| 1.1.9 | Protection against corruption (cybersecurity) | | | | |
| 1.2.1 | Safety/reliability of control systems (SIL/PL) | | | | |
| 1.2.2 | Control devices | | | | |
| 1.2.4 | Stopping (normal, operational, emergency) | | | | |
| 1.2.5 | Mode selection | | | | |
| 1.2.6 | Failure of power supply | | | | |
| 1.3.x | Mechanical hazard protection | | | | |
| 1.5.x | Other hazards (electrical, thermal, etc.) | | | | |
| 1.6.x | Maintenance | | | | |
| 1.7.x | Information and warnings | | | | |

---

## 4. CRA Annex I Gap Assessment

### Part I — Security Properties

| Requirement | Status | Evidence | Gap | Remediation |
|------------|--------|----------|-----|-------------|
| No known exploitable vulnerabilities | | | | |
| Secure-by-default configuration | | | | |
| Protection against unauthorised access | | | | |
| Data protection at rest and in transit | | | | |
| Minimal attack surface | | | | |
| DoS resilience | | | | |
| Data minimisation | | | | |
| Secure update mechanism | | | | |
| Security event logging | | | | |
| Secure disposal | | | | |

### Part II — Vulnerability Handling

| Requirement | Status | Evidence | Gap | Remediation |
|------------|--------|----------|-----|-------------|
| SBOM (machine-readable) | | | | |
| Vulnerability addressing without delay | | | | |
| Regular security testing | | | | |
| Published vulnerability disclosure policy | | | | |
| CVD process | | | | |
| ENISA reporting (24h/72h/14d) | | | | |
| Security updates for support period (≥5yr) | | | | |
| Free security updates, separable from features | | | | |

---

## 5. RED Gap Assessment (if applicable)

| Requirement | Status | Evidence | Gap | Remediation |
|------------|--------|----------|-----|-------------|
| Art. 3.1(a) Health and safety | | | | |
| Art. 3.1(b) EMC | | | | |
| Art. 3.2 Spectrum efficiency | | | | |
| Art. 3.3(d) Network protection | | | | |
| Art. 3.3(e) Personal data | | | | |
| Art. 3.3(f) Fraud prevention | | | | |

---

## 6. Standards Applied

| Standard | Edition | Covers which EHSR/requirement | Presumption of conformity |
|---------|---------|------------------------------|--------------------------|
| ISO 13849-1 | 2023 | Mach Reg 1.2.1 (SIL/PL) | Y |
| IEC 62443-4-2 | | CRA Annex I (pending hEN) | Unknown |
| EN 55032 | | EMC emission | Y |
| [add as needed] | | | |

---

## 7. Gap Summary and Prioritised Remediation

| Priority | Gap ID | Directive | Requirement | Gap description | Remediation | Owner | Due |
|----------|--------|-----------|-------------|----------------|-------------|-------|-----|
| P1 | | | | | | | |
| P2 | | | | | | | |
| P3 | | | | | | | |

---

## 8. Conformity Assessment Plan

| Directive | Route | Notified body needed | NB selected | Timeline |
|-----------|-------|---------------------|-------------|----------|
| Machinery Reg | Annex V / VII / VIII | Y/N | | |
| CRA | Internal / Class I / Class II | Y/N | | |
| RED | Internal / EU-type exam | Y/N | | |
| LVD | Internal | N | — | |
| EMC | Internal | N | — | |

---

## 9. Technical Documentation Readiness

| Section | Status | Location | Gap |
|---------|--------|----------|-----|
| Product description | | | |
| Risk assessment (safety) | | | |
| Risk assessment (security) | | | |
| Design documentation | | | |
| SBOM | | | |
| Test reports (safety) | | | |
| Test reports (security/pentest) | | | |
| EMC test reports | | | |
| Electrical safety test reports | | | |
| User instructions | | | |
| Vulnerability handling procedures | | | |
| DoC draft | | | |

---

## Assumptions and Unknowns

| ID | Item | Status | Verification method |
|----|------|--------|-------------------|
| | Machinery Regulation application date 2027-01-20 | [S,85] | Verify EUR-Lex |
| | CRA application dates | [S,75] | Verify EUR-Lex |
| | Harmonised standards availability | Unknown | Monitor OJ publications |
| | Notified body availability | Unknown | Check NANDO database |

---

## Revision history

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [YYYY-MM-DD] | [name] | Initial draft |
