# CPS Hazard Register Template

## System: [System name]
## Baseline date: [YYYY-MM-DD]
## Analysis scope: [What is inside the safety analysis boundary]
## Applicable standards: [IEC 61508, ISO 13849-1, IEC 61511, etc.]
## Author: [Name] | Reviewer: [Name] | Approved: [Name, Date]

---

## Losses

| ID | Loss description | Category |
|----|-----------------|----------|
| L-1 | [Highest-consequence loss] | Personnel safety |
| L-2 | | |
| L-3 | | |

Categories: Personnel safety / Environmental / Property / Mission / Legal-regulatory

---

## Hazards

| ID | Hazard description | Losses | Severity | Exposure | Avoidability | SIL/PL target | Safety function(s) | SSI-relevant? |
|----|-------------------|--------|----------|----------|-------------|---------------|-------------------|---------------|
| H-1 | [System] in [unsafe state] while [context] | L-1 | Catastrophic | | | SIL [n] | SF-1 | Y/N |
| H-2 | | | | | | | | |

Severity: Catastrophic / Critical / Marginal / Negligible
Exposure: Frequent / Probable / Occasional / Remote / Improbable
Avoidability: Impossible / Difficult / Possible

---

## Safety Functions

| ID | Name | Mitigates | SIL/PL | Demand mode | Process safety time | Safe state | Inputs | Outputs |
|----|------|-----------|--------|-------------|--------------------|-----------|---------|---------| 
| SF-1 | | H-1 | SIL [n] | Low/High/Continuous | [ms] | [description] | [sensors] | [actuators] |
| SF-2 | | | | | | | | |

---

## UCAs (quick scan)

| ID | Control action | Type | Description | Hazard(s) | SSI-relevant? |
|----|---------------|------|-------------|-----------|---------------|
| UCA-1 | CA-1 | Not provided | | H-1 | Y/N |
| UCA-2 | CA-1 | Provided incorrectly | | H-1 | Y/N |
| UCA-3 | CA-1 | Wrong timing/order | | H-1 | Y/N |
| UCA-4 | CA-1 | Applied too long / stopped too soon | | H-1 | Y/N |

SSI-relevant = a security threat could cause or contribute to this UCA

---

## Safety-Security Interactions (if any)

| ID | Type | Safety element | Security element | Consequence | Severity | Resolution |
|----|------|---------------|-----------------|-------------|----------|-----------|
| SSI-1 | SS-[1-7] | H-n / SF-n / UCA-n | T-n / Z-n | | | |

---

## Assumptions

| ID | Assumption | Impact if violated | Monitor |
|----|-----------|-------------------|---------|
| A-1 | | | |

---

## Open items

| ID | Item | Owner | Resolution criteria | Due |
|----|------|-------|-------------------|-----|
| OI-1 | | | | |

---

## Revision history

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [YYYY-MM-DD] | [name] | Initial draft |
