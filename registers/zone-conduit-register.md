# Zone and Conduit Register

**Owner:** OT Security Lead
**Review cycle:** Quarterly + after any OT network change
**Last reviewed:** YYYY-MM-DD
**Standard:** IEC 62443-3-2

## Zones

| ID | Zone name | Purdue level | Assets | Safety functions | SL-T | SL-C | SL-A | Gap | Trust boundary | Physical access |
|----|-----------|-------------|--------|-----------------|------|------|------|-----|----------------|-----------------|
| Z-1 | [Populate: e.g., Safety PLC zone] | 1 | [Asset list] | SF-1 | 3 | Unknown | Unknown | Assess | [What crosses: data, commands, humans, media] | [Locked cabinet / restricted area / open] |
| Z-2 | | | | | | | | | | |

## Conduits

| ID | Zones connected | Protocols | Direction | Protection | Auth | Monitoring | Safety impact if failed |
|----|----------------|-----------|-----------|-----------|------|-----------|----------------------|
| CO-1 | Z-1 ↔ Z-2 | [Populate] | Uni/Bi | [FW/Diode/VPN] | [Cert/Pwd/None] | [IDS/DPI/None] | [Describe] |

## SL-T allocation (per zone per FR)

| Zone | FR1 | FR2 | FR3 | FR4 | FR5 | FR6 | FR7 | Overall | Rationale |
|------|-----|-----|-----|-----|-----|-----|-----|---------|-----------|
| Z-1 | | | | | | | | | |

## SL gap analysis

| Zone | FR | SL-T | SL-A | Gap | Remediation | Priority | Owner | Due |
|------|----|----|-----|-----|-------------|----------|-------|-----|
| | | | | | | | | |

## Review log

| Date | Reviewer | Changes | Next review |
|------|----------|---------|-------------|
| YYYY-MM-DD | [Name] | Initial creation | +3 months |
