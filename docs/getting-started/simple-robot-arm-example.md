# Worked Example: Simple Industrial Robot Arm

A complete walkthrough of the 12 getting-started steps from README.md using a fictional 6-axis industrial robot arm system.

**System:** Simple Industrial Robot Arm
**Baseline date:** 2026-03-08
**Analysis scope:** Robot controller, safety-rated e-stop, speed/force limiting, protective fence with interlocked gate
**Applicable standards:** IEC 61508, ISO 13849-1:2023, IEC 62443, ISO 10218-1, ISO/TS 15066
**Author:** [Name] | Safety reviewer: [Name] | Security reviewer: [Name]

---

## Step 1 — Standards applicability (`docs/architecture/standards-applicability.md`)

The robot arm is a machine placed on the EU market with wired Ethernet connectivity, safety functions, and digital elements (firmware, updatable software). Walking through the applicability decision tree:

- Product placed on EU market? **Yes** — Section 2 (product regulation) applies.
- Safety-relevant? **Yes** — Section 3 (functional safety) applies.
- Network-connected OT? **Yes** — Section 4 (OT security) applies.

Applicable instruments:

| Instrument | Applies? | Rationale |
|-----------|----------|-----------|
| Machinery Regulation 2023/1230 | Y | Robot arm is a machine per Art. 2(1) [F,90] |
| CRA (EU 2024/2847) | Y | Controller has digital elements with network connectivity [F,90] |
| RED 2014/53/EU | N | No radio equipment — wired Ethernet only |
| LVD 2014/35/EU | Y | Electrical equipment within voltage range [F,90] |
| EMC 2014/30/EU | Y | Electronic equipment [F,90] |
| AI Act | N | No AI/ML components |
| ATEX 2014/34/EU | N | Not intended for explosive atmospheres |
| PED 2014/68/EU | N | No pressure equipment |
| IEC 61508 / ISO 13849-1 | Y | Safety-related control system [F,90] |
| IEC 62443 | Y | OT system with network connectivity [F,90] |
| ISO 10218-1 / ISO/TS 15066 | Y | Industrial robot with collaborative mode [S,85] |

---

## Step 2 — Product register (`registers/product-register.md`)

### Products table

| ID | Product name | Type | Role | Connectivity | Safety-relevant | Target market |
|----|-------------|------|------|-------------|----------------|---------------|
| PROD-1 | Robot Controller RC-100 | Embedded controller | Manufacturer | Wired | Y | EU (DE, AT, FR, IT) |

### Regulatory applicability

| Product | Mach. Reg | CRA | CRA class | RED | LVD | EMC | AI Act | ATEX | PED |
|---------|-----------|-----|-----------|-----|-----|-----|--------|------|-----|
| PROD-1 | Y | Y | II | N | Y | Y | N | N | N |

CRA Class II rationale: Robot safety component used in industrial automation — Annex III Part II applies [S,80].

### Conformity status

| Product | Directive | hEN applied | Conformity route | NB engaged | Assessment status | DoC | CE marked |
|---------|-----------|------------|-----------------|------------|------------------|-----|-----------|
| PROD-1 | Mach. Reg | ISO 10218-1, EN ISO 13849-1 | Annex VII (high-risk) | Y | In progress | N | N |
| PROD-1 | CRA | pending | Class II (third-party) | Y | Not started | N | N |
| PROD-1 | LVD | IEC 60204-1 | Internal | N | In progress | N | N |
| PROD-1 | EMC | EN 61000-6-2, EN 61000-6-4 | Internal | N | In progress | N | N |

### Support period and post-market

| Product | Support period start | Support end | SBOM current | CVD policy published | Last vuln scan | ENISA reporting ready |
|---------|---------------------|------------|-------------|---------------------|---------------|---------------------|
| PROD-1 | 2027-01-01 | 2037-01-01 | Y | N | 2026-02-15 | N |

---

## Step 3 — Hazard analysis (`templates/hazard-analysis/` -> `registers/hazard-register.md`)

### Losses

| ID | Loss description | Category |
|----|-----------------|----------|
| L-1 | Personnel injury or death from robot contact | Personnel safety |
| L-2 | Damage to workpiece, tooling, or surrounding equipment | Property / mission |

### Hazards

| ID | Hazard description | Losses | Severity | Exposure | Avoidability | SIL/PL target | Safety function(s) | SSI-relevant? |
|----|-------------------|--------|----------|----------|-------------|---------------|-------------------|---------------|
| H-1 | Robot arm in unexpected motion while operator is in hazard zone | L-1 | Catastrophic | Probable | Difficult | SIL 2 | SF-1 | Y |
| H-2 | Robot arm exerts excessive force during collaborative task | L-1 | Critical | Frequent | Difficult | PL d | SF-2 | Y |
| H-3 | Loss of protective stop function due to cyber attack on safety bus | L-1 | Catastrophic | Remote | Impossible | SIL 2 | SF-1, SF-3 | Y |

SIL/PL determination method: Risk graph per IEC 61508 Annex E [S,85].

H-1 parameters: S=4 (death/serious injury), F=2 (probable exposure — operator enters zone regularly), P=1 (difficult to avoid — robot moves fast) -> SIL 2.

H-2 parameters: ISO 13849-1 PL method — S2 (serious injury), F2 (frequent exposure during collaborative task), P1 (difficult avoidability) -> PLr = d [S,80].

H-3 parameters: S=4, F=1 (remote — requires successful cyber attack), P=2 (impossible to avoid if e-stop fails) -> SIL 2 (same as H-1; the safety function must achieve this regardless of attack cause).

### Safety functions

| ID | Name | Mitigates | SIL/PL | Demand mode | Process safety time | Sample period | End-to-end latency budget | Jitter budget | Safe state | Degraded mode trigger | Actuator authority limit | Zone |
|----|------|-----------|--------|-------------|--------------------|--------------|-----------------------------|--------------|-----------|----------------------|------------------------|------|
| SF-1 | Emergency stop | H-1, H-3 | SIL 2 | Low demand | 50 ms | 5 ms | 30 ms | 2 ms | All axes braked, servo power removed | Watchdog timeout (3 cycles) | Max deceleration 10 rad/s^2 | Z-1 |
| SF-2 | Speed and force limiting | H-2 | PL d | Continuous | 100 ms | 10 ms | 50 ms | 5 ms | Speed clamped to 250 mm/s, force clamped to 150 N per ISO/TS 15066 | Sensor stale > 20 ms | 250 mm/s, 150 N | Z-1 |
| SF-3 | Protective fence interlock | H-1 | SIL 1 | Low demand | 200 ms | 10 ms | 100 ms | 10 ms | Robot halted, restart inhibited until gate closed | Interlock signal lost | N/A (binary stop) | Z-1 |

### UCAs (quick scan)

| ID | Control action | Type | Description | Hazard(s) | SSI-relevant? |
|----|---------------|------|-------------|-----------|---------------|
| UCA-1 | E-stop command | Not provided | E-stop not provided when operator is in hazard zone and robot is moving | H-1 | Y |
| UCA-2 | Speed limit setpoint | Wrong timing/order | Speed limit applied too late after operator enters collaborative zone | H-2 | Y |
| UCA-3 | Fence interlock halt | Not provided | Interlock halt not provided when gate is open and robot is in automatic mode | H-1 | Y |
| UCA-4 | Speed limit setpoint | Provided incorrectly | Speed limit setpoint set to unsafe value due to corrupted configuration | H-2 | Y |

---

## Step 4 — Safety constraints (`templates/safety-constraints/` -> `registers/safety-constraint-register.md`)

| ID | Constraint | Derived from | Applies to | Numeric contract | Verification method | Owner | Status |
|----|-----------|--------------|-----------|------------------|---------------------|-------|--------|
| SC-1 | E-stop shall achieve safe state within 50 ms of button activation | UCA-1 / H-1 / SF-1 | SF-1 / Z-1 | PST 50 ms, latency 30 ms, jitter 2 ms, watchdog 3 cycles | End-to-end timing test with oscilloscope measurement at actuator | Safety Manager | Draft |
| SC-2 | Force limit shall be continuously monitored with sample period no greater than 10 ms | UCA-4 / H-2 / SF-2 | SF-2 / Z-1 | Sample period 10 ms, stale data timeout 20 ms, authority 150 N | Force sensor calibration test + continuous monitoring audit | Safety Manager | Draft |
| SC-3 | Fence interlock shall inhibit automatic mode within 200 ms of gate opening | UCA-3 / H-1 / SF-3 | SF-3 / Z-1 | PST 200 ms, latency 100 ms | Gate-open trigger test with timing measurement | Safety Manager | Draft |
| SC-4 | Speed limit setpoint shall not be modifiable from any network segment above Purdue L1 | UCA-4 / H-2 / SF-2 | SF-2 / Z-1 / CO-1 | N/A | Network penetration test + configuration audit | OT Security Lead | Draft |

---

## Step 5 — Threat model (`templates/threat-model/` -> `registers/threat-register.md`)

| ID | Threat title | STRIDE | Entry point | Preconditions | Affected assets | Zones / conduits | Safety relevance | Physical consequence | Existing controls | Required controls | Verification | Status |
|----|-------------|--------|-------------|---------------|----------------|------------------|-----------------|---------------------|------------------|------------------|-------------|--------|
| T-1 | Attacker modifies speed limit setpoint via Ethernet | Tampering | CO-2 (control zone to enterprise) | Attacker has L2+ network access | Robot controller, SF-2 | Z-2, CO-2 | H-2 / SF-2 / SSI-1 | Robot exceeds safe speed in collaborative mode, operator injured | Firewall between Z-2 and Z-3 | Unidirectional data diode on CO-1; setpoint write-protect at controller | Penetration test + configuration audit | Draft |
| T-2 | DoS attack on safety bus disrupts e-stop communication | Denial of service | CO-1 (safety zone to control zone) | Attacker on control network floods safety bus | Safety PLC, SF-1, SF-3 | Z-1, CO-1 | H-1 / H-3 / SF-1 / SSI-2 | E-stop and fence interlock fail to trigger, robot continues moving | Dedicated safety bus (separate VLAN) | Hardware data diode; dedicated physical safety bus; bus load monitoring | Bus flood test + timing measurement under load | Draft |

---

## Step 6 — Zone and conduit model (`templates/zone-conduit/` -> `registers/zone-conduit-register.md`)

### Zones

| ID | Zone name | Purdue level | Assets | Safety functions | SL-T | SL-C | SL-A | Gap |
|----|-----------|-------------|--------|-----------------|------|------|------|-----|
| Z-1 | Safety zone | 0-1 | Safety PLC, e-stop relay, servo drives, force/torque sensor, fence interlock switch | SF-1, SF-2, SF-3 | 3 | Unknown | Unknown | Assess |
| Z-2 | Control zone | 1-2 | Robot controller (PROD-1), HMI panel, teach pendant, motion PLC | None (BPCS only) | 2 | Unknown | Unknown | Assess |
| Z-3 | Enterprise zone | 4-5 | Engineering workstation, MES, historian, corporate IT | None | 1 | Unknown | Unknown | Assess |

### Conduits

| ID | Zones connected | Protocols | Direction | Protection | Auth | Monitoring | Safety impact if failed |
|----|----------------|-----------|-----------|-----------|------|-----------|----------------------|
| CO-1 | Z-1 -> Z-2 | Safety-over-EtherNet/IP (CIP Safety) | Unidirectional | Hardware data diode | Certificate-based (CIP Safety) | Dedicated IDS, DPI for CIP Safety | SF-1, SF-2, SF-3 status not visible to BPCS; safe state maintained by SIS independence |
| CO-2 | Z-2 <-> Z-3 | OPC UA, HTTPS | Bidirectional | DMZ firewall, application proxy | MFA + certificate | IDS, flow logging, anomaly detection | No direct safety impact; loss of HMI/MES visibility |

### SL-T allocation (per zone per FR)

| Zone | FR1 | FR2 | FR3 | FR4 | FR5 | FR6 | FR7 | Overall | Rationale |
|------|-----|-----|-----|-----|-----|-----|-----|---------|-----------|
| Z-1 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | Contains safety functions SF-1, SF-2, SF-3; compromise could cause loss of life [S,80] |
| Z-2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | BPCS control; no safety functions; compromise could cause production loss |
| Z-3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | Enterprise IT; governed by ISO 27001 / platform-assurance |

---

## Step 7 — Safety-security interaction analysis (`templates/safety-security-interaction/` -> `registers/ssi-register.md`)

### Interaction summary

| ID | Type | Safety element | Security element | Consequence | Severity | Status |
|----|------|---------------|-----------------|-------------|----------|--------|
| SSI-1 | SS-1 | SF-2 (speed/force limiting), H-2 | T-1, Z-2, CO-2 | Robot exceeds safe speed in collaborative mode; operator injury | Catastrophic | Open |
| SSI-2 | SS-3 | SF-1 (e-stop), H-3 | T-2, Z-1, CO-1 | Hardwired e-stop creates physical access requirement; attacker with physical access could tamper with e-stop wiring | Critical | Open |

### Detailed interaction records

#### SSI-1: Network-modifiable speed limit setpoint

- **Type:** SS-1 — Security failure directly causes safety hazard
- **Safety side:** SF-2 (speed/force limiting), H-2 (excessive force during collaborative task), UCA-4 (speed limit setpoint corrupted), SC-4 (setpoint not modifiable from L2+)
- **Security side:** T-1 (attacker modifies speed limit via Ethernet), Z-2 (control zone), CO-2 (Z-2 to Z-3 conduit)
- **Timing/numeric contract touched:** Speed limit setpoint value (250 mm/s), force limit (150 N)
- **Interaction mechanism:** If an attacker gains access to the control zone network (Z-2) via the enterprise conduit (CO-2), they could send a write command to the robot controller modifying the speed limit setpoint from 250 mm/s to an unsafe value.
- **Physical consequence:** Robot arm moves at unsafe speed during collaborative operation; operator sustains crush/impact injury.
- **Severity:** Catastrophic
- **Likelihood (unmitigated):** Medium
- **Current mitigation:** Firewall on CO-2; VLAN separation between Z-1 and Z-2
- **Gap:** Speed limit setpoint is writable from Z-2 network; no hardware enforcement of setpoint integrity
- **Resolution approach:** (1) Hardware write-protect on safety-critical setpoints in the safety PLC (Z-1). (2) Data diode on CO-1 ensuring Z-2 cannot write to Z-1. (3) Setpoint change requires physical key-switch + two-person integrity.
- **Joint requirement:** JSSR-1
- **Verification:** Penetration test from Z-2 attempting to modify speed limit setpoint; verify write is blocked
- **Evidence:** Penetration test report + data diode configuration audit
- **Owner:** Safety Manager + OT Security Lead
- **Review trigger:** Any change to CO-1, CO-2, Z-1 network, or SF-2 logic
- **Status:** Open

#### SSI-2: Hardwired e-stop physical access vulnerability

- **Type:** SS-3 — Safety mechanism creates security vulnerability
- **Safety side:** SF-1 (emergency stop), H-1 (unexpected motion), SC-1 (e-stop response < 50 ms)
- **Security side:** T-2 (DoS on safety bus), Z-1 (safety zone physical boundary)
- **Timing/numeric contract touched:** PST 50 ms, watchdog 3 cycles
- **Interaction mechanism:** The hardwired e-stop circuit is a safety requirement (independence from network, direct actuator authority). However, the e-stop cabinet and wiring are physically accessible at the robot cell perimeter, creating a physical access vector for tampering (cutting wires to disable e-stop, or bridging contacts to prevent future activation).
- **Physical consequence:** E-stop function disabled without detection; robot continues moving when e-stop is pressed.
- **Severity:** Critical
- **Likelihood (unmitigated):** Low
- **Current mitigation:** E-stop cabinet has standard lock
- **Gap:** No tamper detection on e-stop circuit; standard lock is easily defeated
- **Resolution approach:** (1) Locked e-stop cabinet with tamper detection (door switch + wire break detection in safety PLC). (2) Periodic e-stop proof test. (3) Physical access monitoring (camera, access log).
- **Joint requirement:** JSSR-2
- **Verification:** Tamper detection test (open cabinet, verify alarm); proof test execution
- **Evidence:** Tamper detection test report + proof test records
- **Owner:** Safety Manager
- **Review trigger:** Any physical modification to e-stop circuit or cabinet
- **Status:** Open

### Joint safety-security requirements

| ID | Requirement | Safety rationale | Security rationale | Derived from | Enforcer | Verification | Status |
|----|------------|-----------------|-------------------|-------------|----------|-------------|--------|
| JSSR-1 | Speed limit setpoint shall not be modifiable from any network segment at Purdue L2 or above; changes require physical key-switch and two-person integrity at the safety PLC | Prevents corruption of SF-2 setpoint that could cause H-2 | Eliminates remote attack vector for T-1; reduces attack surface of safety-critical parameter | SSI-1 | Hardware data diode (CO-1) + safety PLC write-protect + physical key-switch | Penetration test from Z-2/Z-3 attempting setpoint write; verify rejection | Draft |
| JSSR-2 | E-stop cabinet shall be locked with tamper detection (door switch + wire break monitoring) alarming to safety PLC and security monitoring | Ensures SF-1 availability; detects physical tampering that could defeat e-stop | Detects physical attack on safety mechanism; compensates for physical access vulnerability inherent in hardwired e-stop design | SSI-2 | Safety PLC tamper input + locked cabinet + security camera | Tamper detection functional test (open cabinet, verify alarm within 1 s); wire break simulation | Draft |

---

## Step 8 — Traceability manifest (`templates/traceability/` -> `registers/traceability-manifest.md`)

| Source type | Source ID | Requirement / claim | Derived artifact(s) | Verification artifact | Evidence location | Risk acceptance / sign-off | Status |
|------------|-----------|---------------------|---------------------|-----------------------|------------------|----------------------------|--------|
| Loss | L-1 | No personnel injury from robot operation | H-1, H-2, H-3 | Hazard register review | `registers/hazard-register.md` | Safety Manager / YYYY-MM-DD | Draft |
| Loss | L-2 | No property damage from robot malfunction | H-1 | Hazard register review | `registers/hazard-register.md` | Safety Manager / YYYY-MM-DD | Draft |
| Hazard | H-1 | Unexpected motion mitigated to SIL 2 | SF-1, SF-3, SC-1, SC-3 | E-stop timing test, interlock test | `evidence/SF-1-timing-test.pdf` | Safety Manager / YYYY-MM-DD | Draft |
| Hazard | H-2 | Excessive force mitigated to PL d | SF-2, SC-2, SC-4 | Force limiting test, setpoint integrity test | `evidence/SF-2-force-test.pdf` | Safety Manager / YYYY-MM-DD | Draft |
| Hazard | H-3 | Cyber-caused protective stop loss mitigated to SIL 2 | SF-1, SSI-1, SSI-2, JSSR-1, JSSR-2 | Penetration test, tamper detection test | `evidence/pentest-report.pdf` | Safety Manager + OT Security Lead / YYYY-MM-DD | Draft |
| Safety function | SF-1 | E-stop achieves safe state within 50 ms PST | SC-1 | End-to-end timing test | `evidence/SF-1-timing-test.pdf` | Safety Manager / YYYY-MM-DD | Draft |
| Safety function | SF-2 | Speed/force limit continuously enforced | SC-2, SC-4, JSSR-1 | Force sensor calibration + monitoring audit | `evidence/SF-2-force-test.pdf` | Safety Manager / YYYY-MM-DD | Draft |
| Threat | T-1 | Setpoint not modifiable from L2+ | JSSR-1, Z-1 (SL-T 3), CO-1 (data diode) | Penetration test | `evidence/pentest-report.pdf` | OT Security Lead / YYYY-MM-DD | Draft |
| Threat | T-2 | Safety bus resilient to DoS | JSSR-2, Z-1 (SL-T 3), CO-1 (data diode) | Bus flood test | `evidence/bus-flood-test.pdf` | OT Security Lead / YYYY-MM-DD | Draft |
| SSI | SSI-1 | T-1 cannot disable SF-2 | JSSR-1 | Penetration test + data diode config audit | `evidence/pentest-report.pdf` | Safety Manager + OT Security Lead / YYYY-MM-DD | Draft |
| SSI | SSI-2 | Physical tampering with e-stop detected | JSSR-2 | Tamper detection test | `evidence/tamper-test.pdf` | Safety Manager / YYYY-MM-DD | Draft |
| Regulatory clause | Mach. Reg EHSR 1.1.9 | Control system protected against corruption | JSSR-1, JSSR-2, Z-1 (SL-T 3) | SSI analysis + penetration test | `evidence/pentest-report.pdf`, `registers/ssi-register.md` | Safety Manager + OT Security Lead / YYYY-MM-DD | Draft |
| Regulatory clause | CRA Annex I | PROD-1 secure by design | T-1, T-2, SBOM, CVD policy | CRA compliance matrix | `evidence/cra-compliance-matrix.xlsx` | Compliance Lead / YYYY-MM-DD | Draft |
| Product | PROD-1 | Conforms to Mach. Reg + CRA + LVD + EMC | All of above | Technical documentation package | `evidence/tech-doc/` | Compliance Lead / YYYY-MM-DD | Draft |

### Release gate

| Release / product | Manifest complete | Open gaps | Residual risks accepted | Safety sign-off | Security sign-off | Compliance sign-off |
|------------------|-------------------|-----------|-------------------------|----------------|-------------------|---------------------|
| PROD-1 v1.0 | N | 14 | N | Pending | Pending | Pending |

---

## Step 9 — Data model and schemas (`docs/assurance/data-model-and-traceability.md` + `schemas/`)

Before automating or generating evidence, review the typed schema layer. Below is a sample machine-readable record for H-1 in YAML front matter format, following `schemas/hazard-entry.schema.json`:

```yaml
id: H-1
object_type: hazard
title: Unexpected robot motion while operator in hazard zone
status: draft
owner: Safety Manager
review_cycle: quarterly
losses: [L-1]
safety_functions: [SF-1]
severity: Catastrophic
exposure: Probable
avoidability: Difficult
links:
  mitigated_by: [SF-1, SF-3]
  constrained_by: [SC-1, SC-3]
  interacts_with: [SSI-1, SSI-2]
provenance:
  basis: "[F,90]"
  verified_on: "2026-03-08"
```

All numeric runtime-contract fields from `docs/assurance/data-model-and-traceability.md` section 3 are populated in the safety constraint and safety function entries above. Every SSI references at least one SC and one T. Every JSSR references at least one SSI. These rules are enforced by `make validate`.

---

## Step 10 — Validate (`make validate`)

Run `make validate` before any review or merge. This checks:

- All IDs are unique within their namespace
- Every `SSI-n` references at least one `SC-n` and one `T-n`
- Every `JSSR-n` references at least one `SSI-n`
- Every product conformity assessment links back to hazards, threats, constraints, and interactions
- Provenance tags use only `[F]`, `[I]`, or `[S]` with confidence levels {50,70,80,90}
- Numeric runtime-contract fields are present for all objects affecting physical behaviour

For this example, `make validate` would flag:

- SL-C and SL-A are Unknown for all zones — gap assessment required
- Evidence locations reference placeholder paths — actual artifacts must be produced
- DoC and CE marking status is N — conformity assessment not yet complete

---

## Step 11 — Legal review and management approval (`policies/`)

Submit `policies/POL-CPS-01-safety-management.md`, `policies/POL-CPS-02-ot-security.md`, and `policies/POL-CPS-03-product-conformity.md` for:

- Legal review: Confirm regulatory applicability assessment (Machinery Regulation + CRA + LVD + EMC) is complete and correct
- Management approval: Accept the risk assessment parameters (severity, exposure, avoidability), SIL/PL allocations, and SL-T allocations
- Resource commitment: Approve notified body engagement for Machinery Regulation Annex VII and CRA Class II assessment

---

## Step 12 — Pre-commissioning checklists

Execute checklists before commissioning the robot cell:

**Safety checklist (summary):**

- [ ] All safety functions (SF-1, SF-2, SF-3) tested end-to-end with timing evidence
- [ ] E-stop response measured < 50 ms PST (SC-1)
- [ ] Force limiting verified at 150 N threshold per ISO/TS 15066 (SC-2)
- [ ] Fence interlock tested — gate open inhibits automatic mode within 200 ms (SC-3)
- [ ] CCF analysis complete — beta factor documented for redundant channels
- [ ] Proof test schedule established and documented
- [ ] Operator training completed and recorded

**Security checklist (summary):**

- [ ] Zone boundaries enforced — Z-1 isolated with SL-T 3 controls
- [ ] Data diode on CO-1 verified — no write path from Z-2 to Z-1
- [ ] DMZ firewall on CO-2 configured — explicit allow rules, deny-all default
- [ ] Default credentials eliminated on all OT devices
- [ ] PLC logic hash baseline recorded after commissioning
- [ ] IDS operational on safety zone and control zone networks
- [ ] SBOM current and stored in evidence pipeline

**Joint safety-security checklist (summary):**

- [ ] SSI register reviewed — all interactions have resolution approach
- [ ] JSSR-1 verified — speed limit setpoint not writable from L2+ (penetration test passed)
- [ ] JSSR-2 verified — tamper detection on e-stop cabinet functional
- [ ] Joint change management process documented and signed by safety and security authorities

---

## Summary of all register entries

This example produces the following register entries, ready for copy-paste into the register templates:

| Register | Entries |
|----------|---------|
| Product register | PROD-1 |
| Hazard register (losses) | L-1, L-2 |
| Hazard register (hazards) | H-1, H-2, H-3 |
| Hazard register (safety functions) | SF-1, SF-2, SF-3 |
| Hazard register (UCAs) | UCA-1, UCA-2, UCA-3, UCA-4 |
| Safety constraint register | SC-1, SC-2, SC-3, SC-4 |
| Threat register | T-1, T-2 |
| Zone/conduit register (zones) | Z-1, Z-2, Z-3 |
| Zone/conduit register (conduits) | CO-1, CO-2 |
| SSI register (interactions) | SSI-1, SSI-2 |
| SSI register (JSSRs) | JSSR-1, JSSR-2 |
| Traceability manifest | 14 rows covering all artifacts |

Traceability chain closure for PROD-1:

```
Regulatory clause (Mach. Reg EHSR 1.1.9, CRA Annex I)
  -> Hazards (H-1, H-2, H-3)
    -> Safety functions (SF-1, SF-2, SF-3)
      -> Safety constraints (SC-1..SC-4)
        -> SSI analysis (SSI-1, SSI-2)
          -> JSSRs (JSSR-1, JSSR-2)
            -> Verification (timing test, force test, pentest, tamper test)
              -> Evidence (artifacts in evidence/)
                -> Sign-off (Safety Manager + OT Security Lead + Compliance Lead)
```
