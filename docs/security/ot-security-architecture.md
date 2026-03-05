<!-- TOC -->
- A) OT environment characterisation
- B) Zone and conduit model (IEC 62443-3-2)
- C) Security level target (SL-T) allocation
- D) OT threat modelling (STRIDE adapted for OT)
- E) Purdue model enforcement
- F) OT-specific security controls
- G) Safety-zone protection requirements
- H) OT network monitoring and detection
- I) OT vulnerability and patch management
- J) IEC 62443 certification and compliance
- K) Cross-references
<!-- /TOC -->

Start with 1 sentence naming the most exposed OT zone and the threat with highest physical consequence.

**POINTER-GATE:** IEC 62443 series (parts 1-1 through 4-2) are the primary OT security standard suite. Part-specific clause references are edition-sensitive — mark [S,85]. ISASecure and IECEE certification scheme details are volatile — mark [S,80]. NIST SP 800-82 Rev 3 is the US reference; content is stable but revision-specific — mark [S,85]. OT product vulnerabilities (Siemens, Rockwell, Schneider, ABB, Honeywell advisories) are volatile by definition — never mark [F] without ICS-CERT/CISA advisory reference verified in this session. Purdue model is a conceptual reference architecture, not a standard — implementations vary widely.

MITRE ATT&CK for ICS is a useful threat knowledge base but is continuously updated — mark specific technique IDs [S,80] as they may be reclassified.

**A) OT environment characterisation**
- Plant/facility type and process description
- Operational technology inventory: PLCs, RTUs, DCS, SCADA, HMIs, historians, engineering workstations
- IT-OT convergence points: DMZ, data diodes, jump servers, remote access
- Safety systems: SIS (IEC 61511), safety PLCs, e-stop circuits
- Communication protocols: Modbus, OPC UA, EtherNet/IP, PROFINET, DNP3, IEC 61850, BACnet, HART
- Legacy systems: age, firmware update capability, vendor support status
- Physical access: who can physically touch OT equipment; how is physical access controlled
- Regulatory environment: NIS2 entity status (essential/important), CRA product status, sector-specific (NERC CIP, IEC 62351 for energy, etc.)

**B) Zone and conduit model (IEC 62443-3-2)**

Build the zone and conduit model following IEC 62443-3-2 System Security Requirements and Security Levels:

Zone definition:
```
Z-n: [Zone name]
  Description: [What assets and functions reside in this zone]
  Purdue level: [0-5]
  Assets: [List of OT/IT assets in zone]
  Safety relevance: [Does this zone contain safety functions? Which SF-n?]
  SL-T: [Target security level — see section C]
  SL-C: [Capability security level of components — assessed or Unknown]
  SL-A: [Achieved security level — measured or Unknown]
  Trust boundary: [What crosses the zone boundary — data, commands, humans, media]
```

Conduit definition:
```
CO-n: [Conduit name] — connects Z-x ↔ Z-y
  Communication: [protocols, ports, direction]
  Data classification: [control commands / telemetry / config / file transfer / diagnostics]
  Direction: unidirectional / bidirectional (prefer unidirectional where possible)
  Protection: [firewall rules / data diode / VPN / encrypted tunnel / application proxy]
  Authentication: [device auth, user auth, certificate-based, none (legacy)]
  Monitoring: [IDS, flow logging, anomaly detection, deep packet inspection for OT protocols]
  Fail mode: [if conduit fails — does the process continue safely? Is the safety function affected?]
```

Zone/conduit model table:
| Zone | Purdue level | Assets | Safety relevance | SL-T | SL-C | SL-A | Gap |
|------|-------------|--------|-----------------|------|------|------|-----|
| Z-1  | | | | | | | |

Conduit table:
| Conduit | Zones connected | Protocols | Direction | Protection | Auth | Monitoring | Fail mode |
|---------|----------------|-----------|-----------|-----------|------|-----------|-----------|
| CO-1    | | | | | | | |

**C) Security level target (SL-T) allocation**

IEC 62443-3-3 defines security levels on a 1–4 scale per foundational requirement (FR):

| FR | Domain | SL-1 | SL-2 | SL-3 | SL-4 |
|----|--------|------|------|------|------|
| FR 1 | Identification and authentication | Basic | Enhanced | Strong | Very strong |
| FR 2 | Use control (authorization) | Basic | Enhanced | Strong | Very strong |
| FR 3 | System integrity | Basic | Enhanced | Strong | Very strong |
| FR 4 | Data confidentiality | Basic | Enhanced | Strong | Very strong |
| FR 5 | Restricted data flow | Basic | Enhanced | Strong | Very strong |
| FR 6 | Timely response to events | Basic | Enhanced | Strong | Very strong |
| FR 7 | Resource availability | Basic | Enhanced | Strong | Very strong |

SL-T allocation per zone:
- **Zones with safety functions (SIS, safety PLCs):** SL-T ≥ 3 recommended [S,80]. Rationale: compromise of safety function can cause loss of life. Security must not be the weak link in safety integrity.
- **Level 0-1 zones (physical process, basic control):** SL-T ≥ 2 minimum; ≥ 3 if safety-relevant.
- **Level 2 zones (supervisory control, HMI):** SL-T ≥ 2.
- **Level 3 zones (site operations, historian):** SL-T ≥ 2.
- **Level 3.5 / DMZ:** SL-T ≥ 3 (this is the IT-OT trust boundary; highest attack surface).
- **Level 4-5 (enterprise IT):** Out of OT scope; governed by IT security policy (ISO 27001 / NIS2).

SL-T allocation table per zone:
| Zone | FR1 | FR2 | FR3 | FR4 | FR5 | FR6 | FR7 | Overall SL-T | Rationale |
|------|-----|-----|-----|-----|-----|-----|-----|-------------|-----------|
| Z-n  | | | | | | | | | |

Gap = SL-T − SL-A per FR. Positive gap = remediation required.

**D) OT threat modelling (STRIDE adapted for OT)**

Apply STRIDE to OT context with physical consequence tracing:

| STRIDE category | OT manifestation | Physical consequence |
|----------------|-----------------|---------------------|
| **Spoofing** | Forged Modbus commands, MITM on EtherNet/IP, rogue engineering workstation | Actuator receives unauthorized command → unsafe process state |
| **Tampering** | Modified PLC logic, altered setpoints, firmware implant, historian data manipulation | Process operates outside safe envelope; safety function logic corrupted |
| **Repudiation** | No logging on OT devices, unsigned firmware updates, no change audit trail | Cannot prove who made a change; incident forensics impossible |
| **Information disclosure** | OT protocol eavesdropping (Modbus cleartext), historian exfiltration, process IP theft | Process knowledge enables targeted physical attack; competitive intelligence loss |
| **Denial of service** | Network flood on control bus, PLC CPU exhaustion, safety system communication disruption | Loss of control → process runs open-loop → potential hazardous state |
| **Elevation of privilege** | Engineering workstation compromise → PLC access, IT-to-OT lateral movement, default credentials | Attacker gains ability to modify safety-critical logic |

Per threat:
```
T-n: [STRIDE category] — [specific OT threat]
  Attack vector: [network / physical / supply chain / insider]
  Target zone: Z-n
  Affected assets: [PLC, SIS, HMI, etc.]
  Physical consequence: [what happens in the physical process]
  Safety impact: [does this affect a safety function? Which SF-n / H-n?]
  Existing controls: [what currently mitigates this]
  Residual risk: [High / Medium / Low]
  Recommended mitigation: [specific control]
  IEC 62443 FR mapping: FR-n, SR-n.n
  ATT&CK for ICS: [technique ID if known — mark [S,80]]
```

**E) Purdue model enforcement**

Reference architecture for OT network segmentation:

```
Level 5: Enterprise Network (corporate IT, cloud, internet)
  ↕ [Firewall / proxy — strict access control, no direct OT access]
Level 4: Enterprise IT (business planning, ERP, email)
  ↕ [Firewall — conduit CO-n]
Level 3.5: IT-OT DMZ (historian replica, patch server, AV server, jump server)
  ↕ [Firewall / data diode — conduit CO-n]
Level 3: Site Operations (historian, engineering workstation, OPC server)
  ↕ [Firewall / VLAN — conduit CO-n]
Level 2: Area Supervisory Control (HMI, SCADA server)
  ↕ [Switch / VLAN — conduit CO-n]
Level 1: Basic Control (PLC, RTU, DCS controller)
  ↕ [Direct / fieldbus]
Level 0: Physical Process (sensors, actuators, field instruments)
```

Enforcement rules:
- **No direct L4/5 → L0/1 communication.** All traffic traverses DMZ.
- **Safety systems (SIS) are in a separate zone** from BPCS, even at the same Purdue level. Conduit between SIS zone and BPCS zone must be tightly controlled and unidirectional where possible.
- **Engineering workstation access to L0-1** requires jump server in DMZ, MFA, session recording, and change management approval.
- **Remote access to OT** must terminate in DMZ with MFA + session recording + time-limited access. Never direct VPN to L0-1.
- **Vendor remote access** via separate conduit with vendor-specific firewall rules, session recording, and automatic timeout. Prefer escorted access (vendor accesses via operator's monitored session).
- **USB / removable media policy:** Scanning station at DMZ; no direct insertion at L0-1 without scanning + approval.

**F) OT-specific security controls**

Controls mapped to IEC 62443 foundational requirements:

FR1 — Identification and authentication:
- Device-level auth: PLC/RTU access credentials rotated; default credentials eliminated
- User auth: role-based access per IEC 62443-3-3 SR 1.1–1.13
- Engineering workstation: individual accounts with MFA; no shared admin accounts
- Protocol-level auth: OPC UA security (Sign / SignAndEncrypt); PROFINET security profiles where supported

FR2 — Use control:
- Role-based authorization: operator / engineer / administrator / auditor
- Least privilege: operators cannot modify PLC logic; engineers cannot bypass safety
- Physical key-switch for safety override (hardware interlock where applicable)
- Change management: all PLC logic changes require approval workflow and hash comparison

FR3 — System integrity:
- Firmware integrity: signed firmware; verify before flashing
- PLC logic integrity: hash baseline after commissioning; monitor for unauthorized changes
- Patch management: see section I
- Application whitelisting on HMI and engineering workstations

FR4 — Data confidentiality:
- Encrypt historian replication across zones (TLS)
- OPC UA encryption for cross-zone communication
- Protect process IP in transit (design recipes, setpoints)
- Legacy protocol caveat: Modbus, EtherNet/IP, DNP3 without native encryption → rely on network segmentation + encrypted tunnels

FR5 — Restricted data flow:
- Zone/conduit enforcement (see section B)
- Data diodes for safety-critical unidirectional flows
- Network ACLs per conduit with explicit allow rules (deny-all default)

FR6 — Timely response to events:
- OT security monitoring (see section H)
- Incident response plan specific to OT (different from IT IR — must consider process safety during response)
- NIS2 / CRA ENISA notification timelines for OT incidents

FR7 — Resource availability:
- Redundancy for safety-critical controllers (hot standby, voted architectures)
- DoS protection on OT networks (rate limiting, protocol-aware filtering)
- Graceful degradation: if security infrastructure fails, process must continue safely (security must not cause safety failure)

**G) Safety-zone protection requirements**

Safety systems (SIS, safety PLCs, e-stop circuits) require special treatment:

1. **Isolation:** SIS in dedicated zone with highest SL-T in the facility.
2. **Communication:** SIS → BPCS conduit is read-only (SIS sends trip status; BPCS cannot write to SIS). Use hardware-enforced unidirectional gateway if SIL ≥ 3.
3. **No remote access to SIS.** Engineering changes to SIS require physical presence + key-switch + two-person integrity.
4. **Change management:** Safety PLC logic changes follow functional safety change management (IEC 61511-1 Clause 17) AND security change management (IEC 62443-2-1).
5. **Monitoring:** SIS zone has dedicated network monitoring; anomalous traffic is a safety concern, not just a security concern.
6. **Vendor access to SIS:** On-site only, escorted, with verified identity and logged session.

**H) OT network monitoring and detection**

OT-specific monitoring (differs from IT):
- **Passive network monitoring:** Span/mirror port on OT switches; deep packet inspection for industrial protocols (Modbus, OPC UA, EtherNet/IP, PROFINET, DNP3). Tools: Claroty, Nozomi, Dragos, Armis, or open-source (Zeek with OT parsers, Suricata with OT rules).
- **Baseline learning:** OT networks have predictable traffic patterns. Establish baseline; alert on deviation (new device, new protocol, changed communication pattern, new Modbus function code).
- **PLC change detection:** Monitor PLC logic hash; alert on any unauthorized change. Compare against approved baseline from change management system.
- **Safety system monitoring:** SIS communication monitored separately; any communication anomaly is a safety event.
- **Log aggregation:** Syslog from managed OT devices → historian zone → SIEM in DMZ. Do not pull logs from L0-1 to enterprise directly.
- **Physical indicators:** Unexplained actuator movement, process variable deviation without process change, alarm without corresponding process event.

Alert priority for OT:
| Alert type | Priority | Rationale |
|-----------|----------|-----------|
| Safety system communication anomaly | P1 — immediate | Direct safety impact |
| PLC logic change (unauthorized) | P1 — immediate | Could be active attack on process |
| New device on safety zone network | P1 — immediate | Unauthorized physical access |
| Cross-zone communication violation | P2 — urgent | Zone model breach |
| Default credential use detected | P2 — urgent | Exploitation risk |
| Reconnaissance traffic in OT network | P3 — high | Early attack indicator |
| Failed authentication (threshold) | P3 — high | Credential attack in progress |
| Firmware version mismatch | P4 — medium | Potential unauthorized update |

**I) OT vulnerability and patch management**

OT patching differs fundamentally from IT patching:

- **Availability-first:** OT systems often cannot be rebooted during production. Patch windows require planned shutdown or redundancy.
- **Vendor dependency:** PLC firmware updates require vendor validation. Applying generic OS patches to HMI/engineering workstations may break vendor software.
- **Legacy:** Many OT devices are 10-20+ years old with no vendor patch support.
- **Testing:** Patches must be tested on staging/simulation environment before production OT. Never patch production OT without testing.

OT patch management process:
1. **Inventory:** Maintain asset inventory with firmware/software versions (feeds SBOM for CRA).
2. **Monitor:** Subscribe to ICS-CERT/CISA advisories, vendor advisories (Siemens ProductCERT, Rockwell, Schneider, ABB), and NVD for OT CVEs.
3. **Triage:** Assess impact on process safety and availability. Prioritize: exploitable remotely + safety impact → immediate planning.
4. **Test:** Apply in staging/simulation environment; verify process behavior unchanged.
5. **Schedule:** Coordinate with operations for maintenance window.
6. **Apply:** Document change; verify post-patch; update asset inventory and SBOM.
7. **Compensating controls:** When patching is not possible (legacy, vendor delay): network segmentation, application whitelisting, enhanced monitoring, virtual patching (IDS/IPS rules).

**J) IEC 62443 certification and compliance**

IEC 62443 certification landscape:

| Part | Scope | Who | Certification body |
|------|-------|-----|-------------------|
| 2-1 | IACS security management system | Asset owner / operator | Audit by assessor |
| 2-4 | Security program requirements for service providers | Integrators / maintenance | Audit by assessor |
| 3-3 | System security requirements and security levels | System / solution | ISASecure SSA / IECEE |
| 4-1 | Secure product development lifecycle | Component vendor | ISASecure SDLA / IECEE |
| 4-2 | Technical security requirements for components | Component | ISASecure CSA / IECEE |

Certification route:
- **Asset owner (operating the plant):** IEC 62443-2-1 (management system) + 3-2 (zone/conduit model) + 3-3 (SL-T/SL-A gap closure). Often combined with ISO 27001.
- **System integrator:** IEC 62443-2-4 + 3-3 (for the integrated system).
- **Product vendor (PLC, sensor, actuator, SCADA):** IEC 62443-4-1 (SDL) + 4-2 (component requirements). CRA may require this for EU market.

NIS2 interaction: essential/important entities operating OT in scope for NIS2 Article 21 measures. IEC 62443 controls map well to NIS2 obligations — use eu-regulatory (control-mapper reference) for the crosswalk.

CRA interaction: products with digital elements used in OT (PLCs, smart sensors, gateways, industrial IoT) are in scope for CRA. CRA conformity assessment can reference IEC 62443-4-2 as evidence (when harmonised standards are published).

**K) Cross-references**

- **functional-safety.md** (in this skill): Safety functions must reside in protected zones. SL-T for safety zones must ensure security cannot defeat safety integrity.
- **cps-product-regulation.md** (in this skill): CRA applies to OT products placed on EU market. NIS2 applies to operators of OT in essential/important entities.
- **safety-security-interaction.md** (in this skill): Joint analysis when security controls affect safety function availability or when safety mechanisms create security vulnerabilities.
- **analysis-and-impact (threat-model reference)**: Escalate for formal STRIDE at IT-OT boundary.
- **security-depth (egress-network reference)**: Network segmentation patterns (Cilium, Calico) for container-based OT edge; firewall-as-code for OT zone enforcement.
- **security-depth (vulnerability-pipeline reference)**: CRA ENISA reporting obligations for OT product vulnerabilities.
- **eu-regulatory (nis2 reference)**: NIS2 obligations for OT operators.
- **operational-workflows (evidence-pack reference)**: Assemble evidence for IEC 62443 certification audit.
- **observability-stack-ops**: OT monitoring stack deployment and operation.
- **sociotechnical-control-design**: OT operator alarm management, control room design, shift handover safety.
