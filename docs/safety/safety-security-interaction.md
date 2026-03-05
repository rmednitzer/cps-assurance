<!-- TOC -->
- A) Why safety-security interaction analysis is mandatory for CPS
- B) Interaction taxonomy
- C) Analysis method: joint STPA-STRIDE
- D) Conflict resolution principles
- E) Joint requirements specification
- F) Unified assurance case structure
- G) Runtime monitoring for safety-security interactions
- H) Change management for interacting safety-security controls
- I) Worked example patterns
- J) Cross-references
<!-- /TOC -->

Start with 1 sentence naming the most dangerous safety-security interaction in the system: a case where a security failure causes a safety hazard OR a safety mechanism creates a security vulnerability.

**POINTER-GATE:** Safety-security interaction analysis is an emerging discipline. IEC 63069 (Security for industrial process measurement, control and automation — Framework for functional safety and security) is the primary reference but not yet widely adopted [S,75]. IEC TR 63074 provides guidance on the safety and security interface in machinery [S,80]. ISA/IEC 62443 and IEC 61508/61511 each acknowledge the other domain but do not prescribe joint analysis methods in detail. Academic methods (STPA-Sec, STPA-SafeSec, CHASSIS framework) exist but are not standardized — mark [S,70]. The patterns in this reference are synthesized from these sources.

**A) Why safety-security interaction analysis is mandatory for CPS**

Safety and security are NOT independent in CPS. They interact in both directions:

**Security → Safety (attack causes hazard):**
- Attacker modifies PLC logic → safety function disabled → hazardous process state
- DoS on safety communication bus → SIS cannot receive trip signal → protective function fails
- Compromised sensor sends false readings → controller makes unsafe decisions
- Ransomware encrypts HMI → operator blind to process state → delayed emergency response

**Safety → Security (safety mechanism creates vulnerability):**
- Safety bypass/override port → attack vector (maintenance bypass reachable from network)
- Safety communication requires low latency → cannot tolerate encryption overhead → cleartext protocol
- E-stop circuit accessible via network for remote safety → remote attacker can trigger spurious shutdowns (DoS) or worse, disable e-stop
- Safety system forced to use legacy/obsolete hardware (certified, cannot upgrade) → known vulnerabilities, no patches
- Safety-required redundancy → increased attack surface (more controllers to compromise)

**Regulatory requirement for joint analysis:**
- Machinery Regulation 2023/1230 EHSR 1.1.9: control systems must be protected against corruption [S,85]
- IEC 63069: framework for addressing the interface between safety and security [S,75]
- IEC 62443-3-2 requires that safety-relevant zones have appropriate SL-T
- CRA Annex I Part I: products must be resilient against attacks that could affect safety

**B) Interaction taxonomy**

Classify each safety-security interaction into one of these types:

| Type | Direction | Description | Example |
|------|-----------|-------------|---------|
| **SS-1: Security failure → Safety hazard** | Security → Safety | A successful attack directly causes or enables a safety-relevant failure | Attacker modifies safety PLC setpoint → trip level wrong → overpressure |
| **SS-2: Security failure → Safety function defeat** | Security → Safety | Attack disables, degrades, or bypasses a safety function | DoS on safety bus → SIS cannot communicate → protective function inoperable |
| **SS-3: Safety mechanism → Security vulnerability** | Safety → Security | A safety requirement creates an exploitable weakness | Safety-required cleartext protocol → eavesdropping and replay possible |
| **SS-4: Safety mechanism → Security denial** | Safety → Security | A safety constraint prevents implementing a security control | Safety requires <10 ms response → cannot add encryption/authentication overhead |
| **SS-5: Conflicting requirements** | Bidirectional | Safety and security require contradictory properties of the same component | Safety: fail-open (process continues safely) vs. Security: fail-closed (deny access) |
| **SS-6: Shared resource contention** | Bidirectional | Safety and security controls compete for the same resource (CPU, bandwidth, memory) | IDS CPU load on safety controller → safety function response time violated |
| **SS-7: Change coupling** | Bidirectional | Changing one domain's controls impacts the other domain | Security patch breaks safety-certified firmware; safety recertification blocks security update |

**C) Analysis method: joint STPA-STRIDE**

Perform joint analysis in three passes:

**Pass 1 — Safety-first STPA (from functional-safety.md):**
- Identify losses, hazards, control structure, UCAs, safety constraints
- For each UCA, flag if a security threat could cause or contribute to the UCA
- Tag these UCAs as SSI-relevant (safety-security interaction relevant)

**Pass 2 — Security-informed STRIDE (from ot-security.md):**
- For each SSI-relevant UCA, apply STRIDE to the control path:
  - Could spoofing cause this UCA?
  - Could tampering cause this UCA?
  - Could DoS cause this UCA?
  - Could elevation of privilege enable modification of the safety function?
- For each safety mechanism, apply STRIDE to the mechanism itself:
  - Is the safety mechanism an attack target?
  - Does the safety mechanism expose an attack surface?

**Pass 3 — Interaction analysis:**
For each identified interaction:
```
SSI-n: [Interaction type: SS-1..SS-7]
  Safety side: [H-n, SF-n, UCA-n, SC-n]
  Security side: [T-n, zone Z-n, SL-T, control]
  Interaction: [How the safety and security elements interact]
  Consequence: [Physical outcome if interaction is not managed]
  Severity: [Catastrophic / Critical / Marginal / Negligible]
  Current mitigation: [What currently addresses this interaction, if anything]
  Gap: [What is missing]
  Resolution approach: [See section D]
```

SSI register columns: ID | Type | Safety element | Security element | Interaction | Consequence | Severity | Mitigation | Gap | Resolution

**D) Conflict resolution principles**

When safety and security requirements conflict, apply these principles in order:

1. **Safety takes precedence over security for immediate physical harm.** A security control must never make a safety function slower, less reliable, or less available than the safety analysis requires. If a security control would violate a safety constraint, the security control must be redesigned — not the safety function.

2. **Security must not be sacrificed for convenience.** The fact that a safety-certified component is difficult to update does not excuse leaving known vulnerabilities unpatched. Find a path: compensating controls, secure update with re-verification, staged rollout.

3. **Resolve conflicts by design, not by compromise.** Rather than weakening either safety or security, seek architectural solutions:
   - Separate the safety function from the network-exposed function (hardware separation)
   - Use a hardware security module for authentication without adding latency to the safety path
   - Place a security proxy/gateway in front of the legacy safety component
   - Use data diodes for unidirectional safety data flow (eliminates network-based attack vector entirely)

4. **Document unresolved conflicts explicitly.** If a conflict cannot be resolved with current technology/budget, document it as a residual risk in both the safety case and the security risk register. Assign an owner and a review cadence.

5. **Change management must be joint.** Any change to a safety component is also a security-relevant change (and vice versa). Change requests must be reviewed by both safety and security before approval.

Resolution patterns per interaction type:

| Type | Primary resolution pattern |
|------|--------------------------|
| SS-1 | Increase SL-T of zone containing safety function; add independent monitor |
| SS-2 | Hardware-isolated safety communication (data diode, dedicated bus); independent watchdog |
| SS-3 | Compensating network controls (segmentation, monitoring) around legacy safety component |
| SS-4 | Offload security processing to dedicated hardware (HSM, security coprocessor) outside safety timing path |
| SS-5 | Architectural separation: safety and security enforce their fail modes on different components |
| SS-6 | Dedicated resources: separate CPU/NIC for safety function; resource reservation (cgroups, QoS) |
| SS-7 | Joint change review board; dual-track V-model (safety re-verification + security re-assessment) |

**E) Joint requirements specification**

Produce joint safety-security requirements for each SSI:

```
JSSR-n: [Joint Safety-Security Requirement]
  Derived from: SSI-n [interaction], SC-n [safety constraint], T-n [security threat]
  Requirement: [Specific, testable statement]
  Safety rationale: [Why this is needed for safety]
  Security rationale: [Why this is needed for security]
  Enforcer: [Who/what enforces this — hardware, software, process, human]
  Verification method: [How compliance is demonstrated]
  Evidence: [What artifact proves this requirement is met]
  Owner: [Single accountable person/role]
  Review trigger: [When this requirement must be re-assessed]
```

Examples:
- JSSR-1: The safety PLC shall not be reachable from any network segment above Purdue Level 2. (Safety: prevents remote modification of safety logic. Security: reduces attack surface.)
- JSSR-2: Firmware updates to the safety controller shall be cryptographically signed AND verified against the safety-certified firmware hash before activation. (Safety: prevents regression. Security: prevents malicious firmware.)
- JSSR-3: The safety communication bus shall use dedicated physical cabling not shared with BPCS. (Safety: independence per IEC 61511. Security: eliminates network-layer attack vector.)

**F) Unified assurance case structure**

Build a single assurance case arguing BOTH safety AND security, using the assurance-case-builder skill pattern:

```
TLC [G1]: [CPS product/system] is acceptably safe AND secure for operation in [context].
  Context [C1]: Applicable standards: IEC 61508 / ISO 13849 (safety); IEC 62443 (security)
  Context [C2]: Applicable regulations: Machinery Regulation EHSR 1.1.9; CRA
  Context [C3]: System description and operational environment

  Strategy [S1]: Argue by safety-security interaction — all identified interactions are resolved

    Sub-claim [G2]: All safety hazards are identified and mitigated (safety case)
      [Decompose per functional-safety.md hazard register]

    Sub-claim [G3]: All security threats to safety functions are identified and mitigated
      [Decompose per SSI register — SS-1 and SS-2 interactions]

    Sub-claim [G4]: All security vulnerabilities introduced by safety mechanisms are identified and mitigated
      [Decompose per SSI register — SS-3 and SS-4 interactions]

    Sub-claim [G5]: All safety-security conflicts are resolved without degrading either property
      [Decompose per SSI register — SS-5, SS-6, SS-7 interactions]

    Sub-claim [G6]: Joint change management prevents regression of either property
      [Evidence: joint change review process, dual-track V-model, test records]

  Undeveloped [G7]: Long-term co-evolution of safety and security posture
  [Operational data not yet available; monitoring plan established]
```

**G) Runtime monitoring for safety-security interactions**

Deploy monitors that detect when a safety-security interaction is occurring at runtime:

| Monitor | Detects | Response |
|---------|---------|----------|
| Safety function timing monitor | Safety function response exceeds budget (SS-6: resource contention) | Alert + isolate contending workload |
| Safety communication integrity monitor | Unexpected traffic on safety bus (SS-2: attack on safety comms) | Alert + isolate safety bus |
| PLC logic hash monitor | Safety PLC logic hash mismatch (SS-1: logic modification) | P1 alert + process safety review + potential safe halt |
| Security control health monitor | IDS/firewall protecting safety zone is down (SS-1: defense gap) | Alert + compensating manual monitoring + escalation |
| Firmware version monitor | Safety component firmware changed without approval (SS-7: change coupling) | Alert + block activation until verified |
| Safety override state monitor | Safety override active beyond expected maintenance window (SS-3: override as attack vector) | Alert + automatic override timeout + escalation |

Integrate these monitors into the OT monitoring stack (observability-stack-ops) with priority routing (all safety-security interaction alerts are ≥P2).

**H) Change management for interacting safety-security controls**

Change request involving a safety component or a security control protecting a safety zone:

1. **Classify:** Is this a safety change, security change, or both?
2. **Impact analysis:** Run CACE blast radius (analysis-and-impact) spanning both domains. Identify which SSI-n entries are affected.
3. **Joint review:** Safety authority AND security authority review before approval. Neither can approve independently.
4. **Verification plan:** Define what must be re-tested for both safety and security.
5. **Execute:** Smallest safe increment; checkpoint; verify.
6. **Evidence:** Capture evidence for both safety and security audit trails.
7. **Update registers:** Update hazard register, SSI register, risk register, SBOM.

**I) Worked example patterns**

**Pattern 1: Networked safety PLC**
- Safety: PLC executes SIL 2 safety function. Must respond within 100 ms.
- Security: PLC on Ethernet network reachable from L2. Default credentials.
- SSI-1 (SS-1): Attacker changes PLC logic via default credentials → safety function corrupted → H-1.
- SSI-2 (SS-4): Adding authentication to PLC adds 5 ms overhead → timing budget squeezed.
- Resolution: Change default credentials (immediate). Add hardware firewall on dedicated port with allow-list. Authentication offloaded to network-layer (no CPU overhead on safety PLC). Place PLC in dedicated safety zone with SL-T 3. Monitor PLC logic hash.

**Pattern 2: Safety-critical firmware update**
- Safety: Actuator controller firmware is SIL 3 certified. Certification tied to specific firmware hash.
- Security: CVE discovered in actuator firmware communication stack. Patch available from vendor.
- SSI-3 (SS-7): Applying security patch changes firmware → safety certification invalid. NOT applying patch leaves exploitable vulnerability.
- Resolution: Apply patch in staging. Re-run safety verification test suite. If safety requirements still met → update certified hash → deploy to production. If safety tests fail → negotiate modified patch with vendor. Meanwhile: compensating network control (block exploitation path via firewall rule).

**Pattern 3: Emergency stop over network**
- Safety: Remote e-stop function via network for large distributed machinery.
- Security: Network-accessible e-stop is DoS target (attacker triggers spurious shutdown) and attack vector (attacker disables e-stop).
- SSI-4 (SS-3 + SS-2): Safety mechanism (e-stop) creates security vulnerabilities in both directions.
- Resolution: Hardwired e-stop as primary (never depends on network). Network e-stop as supplementary only, with authenticated command, rate limiting, and physical hardwired override always available. Monitor e-stop command source and frequency.

**J) Cross-references**

- **functional-safety.md** (in this skill): Source of hazard register, safety functions, SIL allocation, UCAs.
- **ot-security.md** (in this skill): Source of zone/conduit model, threat model, SL-T allocation.
- **cps-product-regulation.md** (in this skill): Regulatory drivers for joint analysis (Machinery Regulation EHSR 1.1.9, CRA).
- **stpa-full**: For certification-grade causal analysis of safety-security interactions (attacker as controller in control structure).
- **analysis-and-impact (threat-model reference)**: STRIDE analysis; also blast-radius for changes affecting both domains.
- **cps-and-numeric (runtime-contracts reference)**: PIAL boundary contracts that enforce both safety and security invariants.
- **assurance-case-builder**: Unified safety-security assurance case (section F pattern).
- **sociotechnical-control-design**: Operator response to safety-security events; alarm prioritization when safety and security alarms compete for attention.
- **operational-workflows (change-runbook reference)**: Joint change management process for interacting controls.
