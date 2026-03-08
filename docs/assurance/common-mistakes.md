# Common Mistakes in CPS Assurance

Ten frequently observed mistakes in CPS safety, security, and conformity analysis. Each entry describes the problem, its impact, how to detect it, and how to fix it.

---

## 1. Hazard with no safety function

**Problem:** A hazard (H-n) exists in the hazard register with no corresponding safety function (SF-n) listed in the `Safety function(s)` column. The hazard is identified but no engineered control mitigates it.

**Impact:** The hazard is unmitigated. If the hazardous event occurs, there is no protective function to bring the system to a safe state. This is a direct violation of IEC 61508-1 clause 7.6 and Machinery Regulation EHSR 1.1.2 (safety integration) [F,90]. A notified body will reject the safety case.

**How to detect:** Run traceability validation: every H-n must have at least one SF-n in the `safety_functions` field (enforced by `schemas/hazard-entry.schema.json`, which requires `safety_functions` array). Review the hazard register for empty `Safety function(s)` cells. `make validate` flags this as a broken traceability chain.

**How to fix:** For each unmitigated hazard, either (a) specify a new safety function that brings the system to a defined safe state, with SIL/PL allocation, or (b) demonstrate through risk assessment that the residual risk is tolerable without a dedicated safety function (document the rationale explicitly with provenance [I,70] or higher). If the hazard is addressed by inherently safe design or an information-for-use measure (ISO 12100 hierarchy), document that as the mitigation instead of an SF-n.

---

## 2. SIL allocated without justifying exposure and avoidability

**Problem:** A SIL or PL target is stated for a safety function but the risk graph parameters (severity, exposure, avoidability) are not documented, or are documented without rationale for the chosen values.

**Impact:** The SIL allocation is unjustified. An auditor or notified body cannot verify whether the SIL is correct — it could be too high (wasting engineering effort and increasing complexity) or too low (leaving residual risk above the tolerable threshold). Indefensible SIL allocation undermines the entire safety case [S,85].

**How to detect:** Review the hazard register: every H-n row should have Severity, Exposure, and Avoidability populated with values from the defined enums (schema enforces enum values). Check that a rationale exists for each parameter choice — the SIL determination section should contain a `Rationale:` line per hazard. Flag any SIL > 1 with Exposure = "Improbable" and Avoidability = "Possible" as suspicious (these parameters typically yield SIL 1 or no requirement).

**How to fix:** For each SIL/PL allocation, document the method used (risk graph, risk matrix, LOPA, PL), the parameter values chosen, and a brief rationale for each. State assumptions that must hold for the assessment to remain valid. Mark the provenance: [S,85] if based on engineering judgement, [F,90] if based on measured operational data.

---

## 3. Forgetting safety-security interaction analysis

**Problem:** Hazard analysis and threat modelling are performed independently with no joint analysis. The SSI register is empty or absent. Safety functions are not evaluated for security vulnerabilities, and threats are not evaluated for safety impact.

**Impact:** Blind spots at the safety-security boundary. A security attack could defeat a safety function (SS-1, SS-2) without the safety case accounting for it. A safety mechanism could create a security vulnerability (SS-3, SS-4) without the threat model accounting for it. Machinery Regulation EHSR 1.1.9 requires protection against corruption of control systems — joint analysis is the mechanism for demonstrating this [S,85]. IEC 63069 requires explicit treatment of the safety-security interface [S,75].

**How to detect:** Check the SSI register (`registers/ssi-register.md`). If it is empty or placeholder-only, the analysis has not been performed. Cross-check: every UCA marked `SSI-relevant? Y` in the hazard register should have a corresponding SSI-n entry. Every safety function in a networked zone should have at least one SSI entry evaluating the network attack vector.

**How to fix:** Perform the three-pass joint STPA-STRIDE analysis described in `docs/safety/safety-security-interaction.md` section C. For each safety function, ask: "Can a security threat cause or contribute to a UCA of this safety function?" For each safety mechanism, ask: "Does this mechanism create an exploitable vulnerability?" Populate the SSI register with findings.

---

## 4. Safety constraint with no verification method

**Problem:** A safety constraint (SC-n) is defined but the `verification_method` field is empty or states only "TBD". The constraint exists on paper but there is no plan to verify it.

**Impact:** The constraint is unverifiable — it cannot be demonstrated to an auditor, notified body, or during commissioning. An unverifiable constraint provides zero assurance. The safety case collapses at the evidence layer. The `verification_method` field is required by `schemas/safety-constraint-entry.schema.json` [F,90].

**How to detect:** Schema validation (`make validate`) will flag missing `verification_method`. Additionally, review the traceability manifest: every SC-n should have a `Verification artifact` entry that names a concrete test, analysis, or inspection.

**How to fix:** For each safety constraint, specify one or more of: (a) functional test (end-to-end test of the safety function under the constraint conditions), (b) analysis (FMEDA, timing analysis, formal verification), (c) inspection (configuration audit, code review). Include acceptance criteria (e.g., "response time < 50 ms in 100 consecutive test runs"). Assign an owner and cadence.

---

## 5. Threat with no zone assignment

**Problem:** A threat (T-n) exists in the threat register but the `zones` and `conduits` fields are empty. The threat is described in abstract terms without being anchored to the zone/conduit model.

**Impact:** The threat cannot be prioritised or mitigated effectively. SL-T allocation depends on threats being mapped to zones — a threat without a zone assignment does not drive any security control selection. The threat is invisible to the zone/conduit gap analysis. IEC 62443-3-2 requires threats to be analysed in the context of the zone/conduit model [F,90].

**How to detect:** Review the threat register for empty `Zones / conduits` columns. The schema (`schemas/threat-entry.schema.json`) does not require `zones` but the traceability closure rule does — `make validate` should flag threats without zone links as incomplete traceability.

**How to fix:** For each threat, identify which zone(s) the attacked asset resides in and which conduit(s) the attack traverses. Populate the `zones` and `conduits` fields. If a threat targets multiple zones (lateral movement), list all affected zones in order.

---

## 6. Zone with no SL-T allocation

**Problem:** A zone (Z-n) is defined in the zone/conduit register but the `sl_t` field is 0 or not assessed. The zone exists in the model but has no security target.

**Impact:** No security controls are driven for this zone. The gap analysis (SL-T minus SL-A) cannot be computed. Assets in the zone have no defined security posture. If the zone contains safety functions, this is a critical gap — safety zones must have SL-T >= 3 [S,80]. The `sl_t` field is required by `schemas/zone-entry.schema.json` [F,90].

**How to detect:** Schema validation flags missing or zero `sl_t`. Review the SL-T allocation table in the zone/conduit register — every zone row must have a non-zero Overall SL-T with a rationale.

**How to fix:** Perform SL-T allocation per IEC 62443-3-2 for every zone. Consider: (a) what assets reside in the zone, (b) whether safety functions are present, (c) what the physical consequences of compromise would be, (d) the threat landscape. Document the rationale. Safety zones: SL-T >= 3. DMZ: SL-T >= 3. Control zones: SL-T >= 2.

---

## 7. Product without trace links

**Problem:** A product (PROD-n) is listed in the product register but has no `trace_links` to hazards, safety functions, threats, zones, SSIs, or JSSRs. The product exists in isolation from the assurance model.

**Impact:** Conformity assessment cannot demonstrate that the product's controls are derived from the actual hazard and threat analysis. The technical documentation required by Machinery Regulation and CRA cannot show the chain from regulatory requirement to product evidence. An auditor cannot verify that the product addresses all applicable risks [S,85].

**How to detect:** Review the product register: the conformity status table should reference specific hazards, threats, and controls. Check the traceability manifest for a PROD-n row linking to H-n, T-n, JSSR-n entries. The schema (`schemas/product-entry.schema.json`) includes an optional `trace_links` array — while not schema-required, it is required by the traceability closure rule in `docs/assurance/data-model-and-traceability.md` section 4.

**How to fix:** For each product, populate `trace_links` with all H-n, SF-n, SC-n, T-n, Z-n, CO-n, SSI-n, and JSSR-n entries that apply to that product. Add a row in the traceability manifest for each regulatory clause with the product's evidence artifacts.

---

## 8. SIS deployed without a dedicated zone

**Problem:** A Safety Instrumented System (SIS) or safety PLC is deployed in the same zone as the BPCS or general OT infrastructure, without a dedicated safety zone with elevated SL-T.

**Impact:** The SIS inherits the security posture of the general OT zone, which is typically SL-T 2 or lower. An attacker who compromises the BPCS zone can reach the SIS. This violates the independence requirement of IEC 61511-1 and the safety-zone protection requirements in `docs/security/ot-security-architecture.md` section G [F,90]. It also violates IEC 62443-3-2 guidance that safety systems should be in their own zone with the highest SL-T [S,80].

**How to detect:** Review the zone/conduit register: every SF-n in the hazard register should appear in the `Safety functions` column of exactly one zone, and that zone should have SL-T >= 3. If any SF-n appears in a zone with SL-T < 3, or if the zone also contains BPCS assets, flag it.

**How to fix:** Create a dedicated safety zone (Z-n) for the SIS. Move the safety PLC, safety I/O, and safety-related sensors/actuators into this zone. Set SL-T >= 3. Define a conduit from the safety zone to the BPCS zone as unidirectional (safety zone sends status; BPCS cannot write to safety zone). Apply the six safety-zone protection requirements from `docs/security/ot-security-architecture.md` section G.

---

## 9. Ignoring CCF in redundant systems

**Problem:** A redundant architecture (1oo2, 2oo3) is claimed for a safety function, but no common cause failure analysis has been performed. The beta factor is not estimated, and CCF defenses are not documented.

**Impact:** Redundancy provides no additional integrity if both channels can fail from the same cause (environmental stress, software bug, supply chain defect, same sensor type). The PFD/PFH calculation is invalid without a beta factor — the actual failure probability may be orders of magnitude higher than claimed. IEC 61508-6 Annex D requires CCF analysis for all redundant architectures [F,90].

**How to detect:** For each safety function with HFT >= 1 (redundant architecture), check for a CCF analysis artifact in the verification evidence table. The beta factor should be stated with the analysis method. Check the CCF defense checklist in `docs/safety/functional-safety-approach.md` section F — at least separation, diversity, and environmental protection should be documented.

**How to fix:** Perform a CCF analysis using the IEC 61508-6 Annex D beta-factor method (or equivalent). Score each defense category (separation, diversity, complexity, assessment, competence, environmental). Estimate the beta factor. Conduct a sensitivity analysis: if beta doubles, does the safety function still meet its SIL target? Document defenses and residual CCF risk. For CPS specifically: also consider cyber-induced CCF — a single vulnerability in common firmware across redundant channels is a CCF source (this is an SS-1 or SS-7 interaction; add to the SSI register).

---

## 10. Not updating proof test schedule after SF logic change

**Problem:** A safety function's logic, setpoints, or architecture is modified (e.g., adding a sensor input, changing a trip threshold, updating firmware), but the proof test interval and procedure are not re-assessed.

**Impact:** The proof test may no longer cover the modified logic paths. Dangerous undetected failures introduced by the change will accumulate until the next proof test — but the proof test procedure may not detect them because it was designed for the prior logic. The PFD calculation assumes a specific proof test interval and coverage; if the test no longer achieves the assumed coverage, the actual PFD degrades beyond the SIL target [S,85]. IEC 61508-1 clause 7.16 (modification) and IEC 61511-1 clause 17 require impact analysis on all changes [F,90].

**How to detect:** Cross-reference the change management log with the proof test schedule. Every change to SF-n logic should trigger a review of the associated proof test procedure and interval. If the most recent change date is after the most recent proof test review date, flag it. In the SSI register, this is an SS-7 interaction (change coupling) — a logic change may also affect security properties.

**How to fix:** After any change to a safety function: (a) re-assess the proof test procedure to ensure it covers the new/modified logic paths, (b) re-assess the proof test interval using the updated PFD/PFH calculation (the new logic may have different diagnostic coverage or failure modes), (c) execute a proof test before returning the modified safety function to service, (d) update the safety constraint register and traceability manifest with the new proof test evidence, (e) if the change also affects security (e.g., firmware update), run the SSI analysis for SS-7 and update the SSI register.
