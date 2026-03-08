# Pre-Commissioning Safety Checklist

**System:** [Name]
**Date:** YYYY-MM-DD
**Checklist owner:** Safety Manager
**Completed by:** [Name]

## Prerequisites

- [ ] Hazard analysis complete and approved (H-n entries in hazard register)
- [ ] SIL/PL allocation documented and reviewed
- [ ] Safety functions specified and implemented (SF-n entries)
- [ ] FMEDA / reliability calculations complete and meet SIL target
- [ ] FMEDA / reliability analysis confirms SIL/PL target is achievable
- [ ] Common cause failure (CCF) analysis complete for redundant architectures
- [ ] Safety-security interaction analysis complete (SSI register populated)
- [ ] All open items from hazard analysis resolved or accepted with documented rationale

## Hardware

- [ ] Safety-related hardware installed per design
- [ ] Wiring verified against schematics
- [ ] E-stop circuit tested (all e-stop devices, all safety relays)
- [ ] Physical safeguarding installed and verified (guards, barriers, interlocks)
- [ ] Safety PLC / SIS powered and communicating
- [ ] Redundancy verified (if 1oo2, 2oo3: all channels active)
- [ ] Diagnostic coverage verified (online diagnostics reporting correctly)

## Software / logic

- [ ] Safety PLC logic matches approved version (hash comparison)
- [ ] Safety function end-to-end test: stimulus → detection → response within process safety time
- [ ] All safety function test cases executed and passed
- [ ] Setpoints and trip levels verified against hazard analysis
- [ ] Safety override/bypass logic tested: activates correctly, times out, logs
- [ ] Proof test baseline captured (as-commissioned configuration stored)
- [ ] Degraded mode behaviour tested (loss of single sensor, single channel, etc.)

## Network / security

- [ ] Safety zone (Z-n) isolated per zone/conduit model
- [ ] Conduits to safety zone verified: correct protocols, direction, protection
- [ ] No unauthorized network paths to SIS (verify with network scan)
- [ ] Safety PLC credentials changed from defaults
- [ ] PLC logic hash baseline captured and stored
- [ ] OT monitoring active on safety zone (IDS, PLC change detection)

## Operator competency

- [ ] Operators trained on safety function behaviour and emergency procedures
- [ ] Operator response times validated against assumptions in safety analysis
- [ ] Training records documented and stored

## Documentation

- [ ] Technical documentation package complete (per applicable Annex VII)
- [ ] User instructions available in required languages
- [ ] Safety warnings and labels affixed to equipment
- [ ] Maintenance instructions documented
- [ ] Proof test interval defined and scheduled

## Regulatory

- [ ] Conformity assessment complete for all applicable directives
- [ ] EU Declaration of Conformity drawn up
- [ ] CE marking ready to affix (after ALL assessments pass)
- [ ] SBOM generated, validated complete (all direct and transitive dependencies), and stored (if CRA-scope)
- [ ] Vulnerability disclosure policy published (if CRA-scope)

## Sign-off

| Role | Name | Date | Pass? | Signature |
|------|------|------|-------|-----------|
| Safety engineer | | | | |
| OT security lead | | | | |
| Safety manager | | | | |
| Operations lead | | | | |

**Commissioning authorized:** Yes / No
**Conditions (if conditional):** [list with deadlines]
