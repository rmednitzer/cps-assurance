# OT Incident Response Procedure

**Purpose:** Define the incident response process for OT/ICS security incidents affecting cyber-physical systems with safety-relevant functions.

**Scope:** All security incidents in OT zones (Purdue levels 0–3) that may affect safety functions, production integrity, or regulatory compliance.

## 1 — Incident classification

### Priority levels

| Priority | Definition | Examples | SLA: Acknowledge | SLA: Contain |
|----------|-----------|----------|-------------------|--------------|
| **P1 Critical** | Active or imminent threat to safety function integrity | PLC logic modification detected; SIS heartbeat lost; unauthorized device on safety zone (Z-n with safety functions); active exploitation of safety-relevant vulnerability | 15 min | 1 hour |
| **P2 High** | Security breach in OT zone without confirmed safety impact | Unauthorized engineering workstation access; firewall rule violation on zone boundary; failed authentication on safety PLC; known vulnerability in deployed OT firmware (not yet exploited) | 1 hour | 4 hours |
| **P3 Medium** | Anomalous activity without confirmed OT compromise | Anomalous OT network traffic (protocol anomaly, unexpected source); failed MFA on jump server; vendor remote access outside approved window | 4 hours | 24 hours |
| **P4 Low** | Informational or minor policy violation | Informational IDS alerts; minor password policy violations; scheduled vulnerability scan findings; stale vendor accounts detected | Next business day | 1 week |

### Escalation criteria

- P3 → P2: Anomalous traffic confirmed as targeting OT device
- P2 → P1: Security breach confirmed to affect safety zone or safety function
- Any priority → P1: Safety manager determines imminent risk to personnel

## 2 — Response workflow

### Phase 1: Detection and triage

1. Alert received from OT monitoring (IDS, PLC change detection, SIEM)
2. On-call OT security analyst acknowledges alert
3. Verify alert is not false positive (cross-reference with maintenance schedule, approved changes)
4. Classify priority (P1–P4) using criteria above
5. Assign incident commander (P1/P2: OT security lead; P3/P4: on-call analyst)

### Phase 2: Containment

**Critical principle: DO NOT shut down OT processes unless imminent safety risk to personnel.** Unplanned shutdowns can create hazards (pressure relief, thermal runaway, mechanical energy release). Coordinate with operations lead before any process impact.

| Strategy | When to use | How |
|----------|------------|-----|
| **Zone isolation** | Compromise contained within single zone | Block conduit(s) at firewall; maintain safety zone isolation |
| **Account lockout** | Unauthorized access via credentials | Disable compromised accounts; force password reset |
| **Network segment block** | Lateral movement detected | Apply deny rules on switches/firewalls for affected segment |
| **Device quarantine** | Specific device compromised | Disconnect device; replace with spare if safety-critical |
| **Full safety shutdown** | Imminent personnel safety risk ONLY | Execute emergency stop; coordinate with operations; document justification |

**Evidence preservation before containment:**
- Capture network traffic (PCAP) from span port
- Snapshot PLC state (registers, logic hash, diagnostic buffer)
- Export firewall/switch logs
- Screenshot HMI anomalies

### Phase 3: Notification

| Stakeholder | P1 | P2 | P3 | P4 |
|-------------|----|----|----|----|
| Safety manager | Immediate | Within 1h | Daily summary | Weekly report |
| CISO | Immediate | Within 4h | Daily summary | Weekly report |
| Operations lead | Immediate | Within 1h | As needed | N/A |
| Executive management | Within 4h | Within 24h | N/A | N/A |
| ENISA (CRA-scope, actively exploited) | 24h early warning | N/A | N/A | N/A |
| NIS2 CSIRT (essential/important entity) | 24h early warning | 24h early warning | N/A | N/A |

### Phase 4: Investigation

1. Reconstruct timeline of events (first indicator → detection → current state)
2. Identify attack vector and entry point (which conduit? which credential?)
3. Assess scope: which zones, devices, and safety functions affected?
4. Verify safety function integrity:
   - Compare PLC logic hash against known-good baseline
   - Run abbreviated proof test if safety function may be compromised
   - Check safety constraint timing (PST, sample period) against actuals
5. Assess lateral movement: did attacker reach other zones?
6. Identify root cause: vulnerability, misconfiguration, credential compromise, insider threat

### Phase 5: Recovery

1. Develop remediation plan (approved by safety engineer + OT security lead)
2. Execute remediation:
   - Apply patch or configuration fix
   - Restore from known-good baseline if integrity cannot be verified
   - Replace compromised hardware if needed
3. Re-verify safety functions after remediation (proof test or equivalent)
4. Recapture configuration baseline (hash and store)
5. Enhance monitoring for recurrence detection (additional IDS rules, tighter alert thresholds)
6. Restore normal operations (coordinated with operations lead)

### Phase 6: Post-incident review

1. Submit regulatory reports (ENISA 72h notification, 14d final report; NIS2 CSIRT 72h, 1-month)
2. Conduct root cause analysis within 2 weeks of incident closure
3. Identify corrective actions with owners and deadlines
4. Update registers:
   - Threat register: add new threat entry (T-n) if not already covered
   - SSI register: update if new safety-security interaction discovered
   - Zone/conduit register: update if segmentation changes made
5. Share lessons learned with team (safety + security + operations)
6. Store all incident evidence in evidence pipeline (governance_10y retention)

## 3 — OT-specific considerations

### What is different from IT incident response

| Aspect | IT | OT |
|--------|----|----|
| Priority | Confidentiality first | Safety and availability first |
| Shutdown | Acceptable to isolate/shut down | May create physical hazards; avoid unless safety risk |
| Patching | Patch immediately | Test in staging first; coordinate with maintenance window |
| Evidence | Forensic image of disk | PLC state snapshot, network capture, logic hash comparison |
| Recovery | Restore from backup | Restore from known-good baseline + proof test safety functions |
| Monitoring | EDR, SIEM | Passive network monitoring, PLC change detection, protocol DPI |

### Safety-critical incident handling

If a P1 incident affects a safety function (SF-n):

1. **Immediate:** Verify safety function is still operational (check diagnostics, run quick test)
2. **If safety function compromised:** Assess whether to shut down process (decision by safety manager + operations lead)
3. **If process continues:** Implement compensating measures (increased operator monitoring, reduced speed, restricted access)
4. **After resolution:** Full proof test of affected safety function before returning to normal operation
5. **Document:** Safety impact assessment, compensating measures, proof test results

## 4 — Tabletop exercise template

### Exercise design

| Element | Content |
|---------|---------|
| **Scenario** | Attacker gains access to engineering workstation via compromised vendor VPN credentials. Attacker modifies speed limit setpoint on safety PLC from 250 mm/s to 2500 mm/s. PLC change detection triggers P1 alert. |
| **Participants** | OT security lead, safety engineer, operations lead, network engineer, CISO (observer) |
| **Duration** | 90 minutes |

### Decision points

1. **Alert received (T+0):** PLC logic hash mismatch detected on Z-1 (safety zone). What do you do first?
2. **Triage (T+5 min):** Is this a false positive (planned change) or real incident? How do you verify?
3. **Classification (T+10 min):** What priority? Who do you notify?
4. **Containment (T+15 min):** The robot is currently operating in automatic mode with an operator nearby. Do you stop the process? How do you contain without creating a new hazard?
5. **Investigation (T+30 min):** How do you determine what was changed? Can you compare current PLC logic to the baseline?
6. **Recovery (T+60 min):** How do you restore the correct speed limit? Do you need to proof test SF-2 before resuming?
7. **Post-incident (T+75 min):** What registers need updating? Do you need to report to ENISA? What would you change about the security architecture?

### Debrief questions

- Was the P1 classification correct? Would you change it?
- Was the containment decision appropriate? Could it have been faster?
- Did the team know who to notify and in what order?
- Were safety considerations adequately prioritized during response?
- What gaps in procedures or tools were identified?
- What SSI register or threat register updates are needed?

*Reference: IEC 62443-2-1 (security management system), POL-CPS-02 (OT security policy), POL-CPS-04 (vulnerability disclosure), CRA Article 14 (vulnerability reporting).*
