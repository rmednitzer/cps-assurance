# IEC 62443 Zone and Conduit Model Template

## System: [System/plant/facility name]
## Baseline date: [YYYY-MM-DD]
## Scope: [What OT environment is covered]
## IEC 62443 parts applied: [3-2, 3-3, 4-1, 4-2 — as applicable]
## Author: [Name] | Reviewer: [Name] | Approved: [Name, Date]

---

## OT Asset Inventory

| Asset ID | Name | Type | Purdue level | Zone | Firmware/SW version | Vendor | Support status | Safety-relevant |
|----------|------|------|-------------|------|--------------------|---------|-----------|----|
| A-1 | | PLC / RTU / HMI / DCS / etc. | 0-5 | Z-n | | | Active/EOL/Unknown | Y/N |

---

## Zone Definitions

### Z-1: [Zone name]

- **Description:** [Purpose and function]
- **Purdue level:** [0-5]
- **Assets:** [A-1, A-2, ...]
- **Safety relevance:** [SF-n if any; otherwise "None"]
- **SL-T:** [1-4] per FR (see SL-T allocation table below)
- **SL-C:** [Current capability — assessed / Unknown]
- **SL-A:** [Achieved — measured / Unknown]
- **Trust boundary:** [What crosses: data, commands, humans, media]
- **Physical access control:** [Locked cabinet / restricted area / open]

### Z-2: [Zone name]
...

---

## Conduit Definitions

### CO-1: [Conduit name] — Z-x ↔ Z-y

- **Protocols:** [Modbus TCP / OPC UA / EtherNet/IP / etc.]
- **Ports:** [502 / 4840 / etc.]
- **Direction:** Unidirectional (Z-x → Z-y) / Bidirectional
- **Data classification:** Control commands / Telemetry / Config / File transfer / Diagnostics
- **Protection:** [Firewall rules / Data diode / VPN / Application proxy / None]
- **Authentication:** [Certificate / Password / Device-level / None (legacy)]
- **Encryption:** [TLS / OPC UA SecureChannel / None]
- **Monitoring:** [IDS / Flow logging / DPI / None]
- **Fail mode:** [If conduit fails: process continues safely / degraded mode / halt]
- **Safety impact of conduit failure:** [Affects SF-n? Y/N — describe]

### CO-2: ...
...

---

## SL-T Allocation per Zone

| Zone | FR1 (IAC) | FR2 (UC) | FR3 (SI) | FR4 (DC) | FR5 (RDF) | FR6 (TRE) | FR7 (RA) | Overall SL-T | Rationale |
|------|-----------|----------|----------|----------|-----------|-----------|----------|-------------|-----------|
| Z-1 | | | | | | | | | |
| Z-2 | | | | | | | | | |

FR: Foundational Requirement
IAC: Identification and Authentication Control
UC: Use Control
SI: System Integrity
DC: Data Confidentiality
RDF: Restricted Data Flow
TRE: Timely Response to Events
RA: Resource Availability

---

## SL Gap Analysis

| Zone | FR | SL-T | SL-A | Gap | Remediation | Priority | Owner | Due |
|------|----|----|-----|-----|-------------|----------|-------|-----|
| Z-1 | FR1 | 3 | 1 | +2 | [Specific action] | High | | |

---

## Purdue Model Diagram (text)

```
L5 Enterprise Network
  │ [FW: deny-all; allow specific enterprise services]
L4 Enterprise IT
  │ [FW: CO-n]
L3.5 IT-OT DMZ [Z-dmz]
  │ [FW/Diode: CO-n]
L3 Site Operations [Z-ops]
  │ [FW/VLAN: CO-n]
L2 Area Supervisory [Z-area]
  │ [Switch/VLAN: CO-n]
L1 Basic Control [Z-control]
  │ [Direct/fieldbus]
L0 Physical Process [Z-process]

SIS Zone [Z-sis] — separate from L1, connected via CO-sis
```

---

## Safety Zone Special Requirements

| Zone | Safety functions | SL-T minimum | Remote access | Change management | Monitoring |
|------|-----------------|-------------|---------------|------------------|-----------|
| Z-sis | SF-1, SF-2 | SL-T 3 | Prohibited | Joint safety-security review | Dedicated IDS |

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
