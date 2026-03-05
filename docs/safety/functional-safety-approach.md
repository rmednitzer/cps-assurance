<!-- TOC -->
- A) System characterisation
- B) Hazard identification (STPA-informed)
- C) Risk assessment and SIL determination
- D) Safety function specification
- E) Safety requirements allocation
- F) Diagnostic coverage and common cause failure
- G) PIAL boundary contracts for safety functions
- H) Verification and validation evidence
- I) Applicable standards matrix
- J) Machinery Regulation EHSR mapping
- K) Cross-references
<!-- /TOC -->

Start with 1 sentence naming the highest-consequence hazard and the safety function that mitigates it.

**POINTER-GATE:** IEC 61508 (2010 edition) is the reference functional safety standard; sector standards (ISO 13849-1:2023, IEC 62061, IEC 61511, IEC 61513, ISO 26262, EN 50128/50129) inherit or adapt from it. Mark specific edition/clause references [S,85] unless user confirms. SIL determination methods (risk graph, risk matrix, LOPA) have standard-specific variants — state which method and edition. ISO 13849-1:2023 supersedes 2015 edition with changes to Category/PL determination — mark [S,80]. Machinery Regulation 2023/1230 application from 2027-01-20 [S,85] — EHSR references to Annex III may change with harmonised standards. Harmonised standards under Machinery Regulation are being developed — mark Unknown for specific hEN references.

**A) System characterisation**
- System name and boundary (what is inside the safety analysis scope)
- Operational modes: normal, startup, shutdown, maintenance, degraded, emergency
- Environment: temperature range, vibration, EMI, human proximity, hazardous atmosphere
- Intended use and reasonably foreseeable misuse
- Prior incident history (if available)
- Existing safety measures and their claimed integrity

**B) Hazard identification (STPA-informed)**

Use STPA methodology adapted for CPS safety. This skill produces a hazard register compatible with IEC 61508 HARA and feeds stpa-full if certification-grade depth is needed.

For each hazard:
```
H-n: [System] in [unsafe state] while [operational context]
  Losses: L-n (harm type: death/injury/environment/property/mission)
  Severity: Catastrophic / Critical / Marginal / Negligible
  Exposure: Frequent / Probable / Occasional / Remote / Improbable
  Avoidability: Impossible / Difficult / Possible
  Control actions involved: CA-n
  UCAs (quick scan — 4 types):
    - Not provided: [description] → H-n
    - Provided incorrectly: [description] → H-n
    - Wrong timing/order: [description] → H-n
    - Applied too long / stopped too soon: [description] → H-n
```

Hazard register columns: ID | Hazard description | Losses | Severity | Exposure | Avoidability | UCAs | Safety function(s) required

**C) Risk assessment and SIL determination**

Method selection (state which is used and why):
- **Risk graph** (IEC 61508 Annex E default): Severity → Exposure → Avoidability → SIL
- **Risk matrix** (IEC 62061 approach): Severity × Probability → SIL
- **LOPA** (IEC 61511 for process safety): independent protection layers with PFD targets
- **Performance Level** (ISO 13849-1): Severity → Frequency → Avoidability → PLr → Category

Output per hazard:
```
H-n → SIL/PL target:
  Method: [risk graph / matrix / LOPA / PL]
  Parameters: S=[severity] F=[exposure] P=[avoidability] W=[consequence weight if LOPA]
  Result: SIL [1-4] or PL [a-e]
  Rationale: [brief justification for parameter choices]
  Assumptions: [what must remain true for this assessment to hold]
```

SIL → PFD/PFH mapping (for reference):
| SIL | PFD (low demand) | PFH (high demand / continuous) |
|-----|------------------|-------------------------------|
| 1   | ≥10⁻² to <10⁻¹   | ≥10⁻⁶ to <10⁻⁵ /h            |
| 2   | ≥10⁻³ to <10⁻²   | ≥10⁻⁷ to <10⁻⁶ /h            |
| 3   | ≥10⁻⁴ to <10⁻³   | ≥10⁻⁸ to <10⁻⁷ /h            |
| 4   | ≥10⁻⁵ to <10⁻⁴   | ≥10⁻⁹ to <10⁻⁸ /h            |

**D) Safety function specification**

Per safety function:
```
SF-n: [Name]
  Purpose: Mitigates H-n by [mechanism]
  SIL target: SIL [n] / PL [x]
  Demand mode: Low demand / High demand / Continuous
  Process safety time: [time from hazardous event detection to safe state]
  Safe state: [explicit description of what "safe" means for this function]
  Inputs: [sensors, signals, process variables — with required accuracy/freshness]
  Outputs: [actuator commands — with authority limits]
  Logic: [decision criteria — when to trigger, when to reset]
  Independence: [separation from BPCS/non-safety systems; common cause mitigation]
  Manual override: [conditions under which operator can override; re-enable logic]
  Degraded mode: [behavior when SF itself is impaired; fallback to mechanical/manual]
```

**E) Safety requirements allocation**

Allocate safety requirements to hardware, software, and human actions:

Hardware integrity:
- HFT (hardware fault tolerance) requirement per SIL
- Diagnostic coverage (DC) requirement per SIL
- SFF (safe failure fraction) calculation
- Architecture constraints (1oo1, 1oo2, 2oo3, etc.)
- Proof test interval and strategy

Software integrity (IEC 61508-3 / IEC 62443-4-1 overlap):
- Software SIL requirement (systematic capability)
- Required techniques per SIL (structured programming, defensive programming, formal methods at SIL 3-4)
- V-model lifecycle phases with required evidence per phase
- Modification management: any change to safety-related software requires impact analysis and re-verification

Human factors:
- Operator actions credited in safety analysis must have: defined response time, training requirements, procedure, alarm management, and periodic validation
- Automation bias mitigation if automated safety function has operator override

**F) Diagnostic coverage and common cause failure**

Diagnostic coverage (DC):
| Category | DC range |
|----------|---------|
| None | <60% |
| Low | 60% to <90% |
| Medium | 90% to <99% |
| High | ≥99% |

Common cause failure (CCF) defense:
- [ ] Separation/segregation of safety channels
- [ ] Diversity (different hardware/software/technology for redundant channels)
- [ ] Complexity management (simple, well-understood components preferred)
- [ ] Assessment (IEC 61508 beta-factor model or equivalent)
- [ ] Competence (trained personnel for design, maintenance, operation)
- [ ] Environmental (protection against shared environmental stressors)

CCF beta factor estimation: state method, assumed beta, and sensitivity analysis.

**G) PIAL boundary contracts for safety functions**

Every safety function interface is a PIAL boundary. Produce contracts using the pattern from cps-and-numeric (runtime-contracts reference):

Sensor ingestion boundary:
- Input invariants: range [min, max], rate [samples/s], freshness [max age], resolution, noise floor
- Violation: if out-of-range or stale → flag sensor fault → SF enters diagnostic mode → degraded/halt

Compute output boundary:
- Output invariants: value bounds [min, max], rate-of-change limit, timing deadline [ms]
- Violation: if compute exceeds deadline → hold last safe output → increment watchdog counter → halt if persistent

Actuator command boundary:
- Authority limits: maximum force/torque/pressure/flow, rate-of-change ramp limit
- Violation: if command exceeds authority → clamp to limit → log → alert

Safety function independence boundary:
- No shared memory/bus/power with BPCS unless explicitly analyzed for CCF
- Communication between safety and non-safety via defined protocol with integrity checking

**H) Verification and validation evidence**

Per safety function:
| Evidence type | Method | Acceptance criteria | Artifact | Owner | Cadence |
|--------------|--------|-------------------|----------|-------|---------|
| Hardware reliability | FMEDA / parts count | PFD/PFH meets SIL target | FMEDA report | [owner] | On change / 3yr |
| Software verification | Unit/integration/system test + code review | 100% requirement coverage; MC/DC at SIL 3-4 | Test report + coverage report | [owner] | On change |
| Functional test | End-to-end safety function test | SF triggers within process safety time; safe state reached | Test report with timing evidence | [owner] | Proof test interval |
| Diagnostic coverage | Analysis + injection test | DC meets SIL requirement | DC analysis report | [owner] | On change |
| CCF analysis | Beta-factor analysis | Beta ≤ assumed value; defenses documented | CCF report | [owner] | On change / 3yr |
| EMC / environmental | Type test per IEC 61508-2 | No dangerous failure under rated environmental conditions | Type test certificate | [owner] | On change / product variant |
| Operator competence | Training records + drill | Operator responds within credited time | Training + drill records | [owner] | Annual |

**I) Applicable standards matrix**

Select the governing standard based on application domain:

| Domain | Primary standard | Sector standard | Notes |
|--------|-----------------|----------------|-------|
| Generic E/E/PE | IEC 61508 | — | Reference standard for all others |
| Machinery | ISO 13849-1 / IEC 62061 | EN ISO 13849-1 (hEN) | Machinery Regulation 2023/1230 EHSR |
| Process industry | IEC 61511 | — | SIS, BPCS, LOPA |
| Power / energy | IEC 61513 | — | Nuclear; other energy sector standards exist |
| Railway | EN 50126/50128/50129 | — | CENELEC suite |
| Automotive | ISO 26262 | — | ASIL instead of SIL |
| Collaborative robots | ISO 13482 / ISO 10218 / ISO/TS 15066 | — | Human-robot interaction safety |
| Medical devices | IEC 62304 / IEC 82304-1 | — | MDR; not covered in depth here |
| Elevators / lifts | EN 81-20/50 | — | Specific to vertical transportation |

State which standard(s) govern the system under analysis. If multiple apply (common in CPS), note the interaction.

**J) Machinery Regulation EHSR mapping**

The Machinery Regulation 2023/1230 Annex III defines Essential Health and Safety Requirements (EHSR). Key EHSRs relevant to CPS:

- 1.1.2: Principles of safety integration (inherently safe design → safeguarding → information)
- 1.1.6: Ergonomics
- 1.2.1: Safety and reliability of control systems (SIL/PL requirement origin)
- 1.2.2: Control devices (actuators, HMI, e-stop)
- 1.2.3: Starting
- 1.2.4: Stopping (normal, operational, emergency)
- 1.2.5: Selection of control or operating modes
- 1.2.6: Failure of the power supply
- 1.3: Protection against mechanical hazards
- 1.5: Protection against other hazards (electrical, thermal, fire, noise, vibration, radiation, materials)
- 1.6: Maintenance
- 1.7: Information and warnings
- 1.1.9: Protection against corruption — **NEW in 2023/1230** [S,85]: control systems must be protected against intentional or unintentional corruption that could lead to a hazardous situation. This is the Machinery Regulation's cybersecurity hook — connects directly to OT security (ot-security.md) and CRA.

Map each relevant EHSR to: safety function(s), SIL/PL target, evidence, and gap status.

**K) Cross-references**

- **stpa-full**: Escalate for full causal analysis when certification evidence is required. This reference produces the quick hazard register; stpa-full produces the complete UCA/scenario/constraint/evidence chain.
- **cps-and-numeric (timing-budget reference)**: Derive timing budgets for safety function response times (process safety time → compute deadline → actuator response).
- **cps-and-numeric (runtime-contracts reference)**: Produce the enforceable PIAL boundary contracts specified in section G.
- **ot-security.md** (in this skill): Safety functions must be in protected zones with appropriate SL-T. Machinery Regulation 1.1.9 requires cybersecurity of control systems.
- **cps-product-regulation.md** (in this skill): CE marking requires conformity with all applicable directives including Machinery Regulation. SIL/PL evidence feeds the technical documentation.
- **safety-security-interaction.md** (in this skill): Joint analysis when safety mechanisms are attack targets or security measures could impair safety functions.
- **digital-twins-robotics (robotics-safety reference)**: Collaborative robot safety (ISO/TS 15066 force/pressure limits, safeguarding, workspace design).
- **sociotechnical-control-design**: Operator interface for safety-critical actions — alarm philosophy, override management, mode awareness.
- **assurance-case-builder**: Build the safety case (GSN/CAE) using hazards, safety functions, SIL allocations, and evidence from this reference as claim/evidence nodes.
