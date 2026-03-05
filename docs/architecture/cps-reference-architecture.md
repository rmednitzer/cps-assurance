# CPS Reference Architecture

**Date:** 2026-03-05
**Scope:** Generic CPS reference architecture showing Purdue levels, PIAL boundaries, and trust boundaries for safety and security analysis.
**Status:** DRAFT — adapt to specific system.

---

## 1 — Purdue model with PIAL boundaries

```
Level 5: Enterprise Network (corporate IT, internet)
  │
  │  [PIAL boundary: IT-OT demarcation — no direct L5→L0/1]
  │  Firewall / proxy — strict allow-list; no OT protocol passthrough
  │
Level 4: Enterprise IT (ERP, email, business apps)
  │
  │  [PIAL boundary: DMZ admission]
  │  Firewall with conduit CO-dmz; application proxy; jump server
  │
Level 3.5: IT-OT DMZ
  │  Historian replica, patch server, AV server, remote access gateway
  │
  │  [PIAL boundary: OT admission]
  │  Firewall / data diode; conduit CO-ops
  │
Level 3: Site Operations
  │  Historian, engineering workstation, OPC UA server
  │
  │  [PIAL boundary: supervisory-to-control]
  │  Switch / VLAN; conduit CO-area
  │
Level 2: Area Supervisory Control
  │  HMI, SCADA server
  │
  │  [PIAL boundary: control commands]
  │  Switch / VLAN / direct; conduit CO-ctrl
  │
Level 1: Basic Control
  │  PLC, RTU, DCS controller
  │
  │  [PIAL boundary: sensor-actuator interface]
  │  Direct / fieldbus
  │
Level 0: Physical Process
     Sensors, actuators, field instruments

─── SIS Zone (separate) ───
  Safety PLCs, SIS logic solvers
  [PIAL boundary: safety independence — dedicated zone, highest SL-T]
  Conduit CO-sis: unidirectional where possible (SIS → BPCS read-only)
```

## 2 — PIAL boundary contracts for CPS

Every boundary in the architecture above is a PIAL enforcement point. Each must have:

| Boundary | Invariants | Violation response | Monitor |
|----------|-----------|-------------------|---------|
| Sensor ingestion | Range [min,max], rate [samples/s], freshness [max age] | Flag sensor fault → diagnostic mode → degraded/halt | Sensor health metric |
| Compute output | Value bounds, rate-of-change limit, timing deadline [ms] | Hold last safe output → increment watchdog → halt if persistent | Loop timing histogram |
| Actuator command | Max force/torque/pressure, rate-of-change ramp | Clamp to limit → log → alert | Actuator position/force |
| Safety function interface | Independence from BPCS, diagnostic coverage | Dedicated bus; no shared memory/power | SIS communication monitor |
| IT-OT DMZ | Protocol allow-list, direction enforcement, auth | Block + log + alert | IDS on DMZ conduit |
| Zone boundary (any) | Conduit rules per IEC 62443-3-2 | Block + log + alert | Network flow monitor |

## 3 — Trust boundaries for threat modelling

CPS has trust boundaries at both the IT-OT and the safety-control layers:

| TB | Location | Safety-relevant? | Primary threats |
|----|----------|-----------------|----------------|
| TB1 | Internet → IT-OT DMZ | Indirect (pivot path to OT) | External attacker; DDoS; recon |
| TB2 | DMZ → Site operations | Yes (path to controllers) | Lateral movement; compromised jump server |
| TB3 | Operations → Control (L3→L1) | Yes (direct control path) | Engineering workstation compromise; rogue commands |
| TB4 | Control → Physical process (L1→L0) | Yes (actuator commands) | PLC logic modification; sensor spoofing |
| TB5 | BPCS ↔ SIS | Critical (safety function) | Attack on safety communication; CCF |
| TB6 | Remote access → OT | Yes | Credential theft; vendor access abuse |
| TB7 | USB / removable media → OT | Yes | Malware delivery to air-gapped systems |

**Action:** Use these trust boundaries as inputs to the OT threat model and the safety-security interaction analysis.

---

*Architecture patterns [I,80]. Specific protocol/product references [S,75] — verify against deployment.*
