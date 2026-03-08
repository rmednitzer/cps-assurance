# Proof Test Methodology

**Purpose:** Define how proof test intervals are determined, how tests are conducted, and what evidence is required for IEC 61508 compliance.

## 1 — Why proof testing matters

Safety functions in low-demand mode rely on dangerous undetected failures (λ_DU) being revealed before a demand occurs. Proof tests are the primary mechanism for detecting these latent failures. The proof test interval directly affects the average probability of failure on demand (PFDavg), which determines whether the allocated SIL is achieved [F,90].

## 2 — Proof test interval determination

### 2.1 Key variables

| Variable | Description | Source |
|----------|-------------|--------|
| λ_DU | Dangerous undetected failure rate | FMEDA or vendor data |
| λ_DD | Dangerous detected failure rate | FMEDA or vendor data |
| λ_S | Safe failure rate | FMEDA or vendor data |
| DC | Diagnostic coverage | FMEDA analysis |
| β | Common cause failure factor | IEC 61508-6 Annex D scoring |
| T1 | Proof test interval | Calculated or assigned |
| MTTR | Mean time to restoration | Operational data |

### 2.2 PFDavg estimation (simplified)

For a **1oo1 architecture** (single channel, no redundancy):

```
PFDavg ≈ (1 - DC) × λ_D × T1 / 2
```

Where `λ_D = λ_DU + λ_DD` and `(1 - DC) × λ_D = λ_DU`.

For **1oo2 architecture** (parallel redundancy):

```
PFDavg ≈ (1 - β) × ((1 - DC) × λ_D)² × T1² / 3 + β × (1 - DC) × λ_D × T1 / 2
```

For **2oo3 architecture** (voting):

```
PFDavg ≈ (1 - β) × ((1 - DC) × λ_D)² × T1² + β × (1 - DC) × λ_D × T1 / 2
```

[S,80] — These are simplified formulas. For precise calculations, use IEC 61508-6 Annex B or vendor reliability tools.

### 2.3 Target PFDavg per SIL

| SIL | PFDavg range | PFH range (high demand / continuous) |
|-----|-------------|--------------------------------------|
| 1 | ≥ 10⁻² to < 10⁻¹ | ≥ 10⁻⁷ to < 10⁻⁶ |
| 2 | ≥ 10⁻³ to < 10⁻² | ≥ 10⁻⁸ to < 10⁻⁷ |
| 3 | ≥ 10⁻⁴ to < 10⁻³ | ≥ 10⁻⁹ to < 10⁻⁸ |
| 4 | ≥ 10⁻⁵ to < 10⁻⁴ | ≥ 10⁻¹⁰ to < 10⁻⁹ |

[F,90]

### 2.4 Interval selection process

1. Determine λ_DU from FMEDA or vendor reliability data
2. Select target SIL → read PFDavg target from table above
3. Choose architecture (1oo1, 1oo2, 2oo3) based on HFT requirements
4. Calculate maximum T1 that keeps PFDavg within SIL band
5. Apply practical constraint: T1 should align with planned maintenance windows
6. Document: chosen T1, calculation method, assumptions, sensitivity analysis

**Rule of thumb [S,75]:** For SIL 2 with typical industrial sensors/actuators (λ_DU ≈ 500 FIT), a 1oo1 architecture requires T1 ≤ 1 year. Adding a second channel (1oo2) extends allowable T1 significantly.

## 3 — Diagnostic coverage assessment

### 3.1 DC determination methods

| Method | Applicability | Confidence |
|--------|--------------|------------|
| FMEDA (vendor-provided) | Preferred when available | [F,85] if from accredited lab |
| FMEDA (self-conducted) | When vendor data unavailable | [I,70] — requires deep component knowledge |
| Fault injection testing | Validation of FMEDA results | [F,90] — direct measurement |
| IEC 61508-2 Table A.1 | Conservative estimates by diagnostic type | [S,80] — may be pessimistic |

### 3.2 DC ranges per IEC 61508-2

| DC range | Classification |
|----------|---------------|
| < 60% | None |
| 60% to < 90% | Low |
| 90% to < 99% | Medium |
| ≥ 99% | High |

### 3.3 Fault injection methodology

1. Identify failure modes from FMEDA (stuck-high, stuck-low, drift, open, short)
2. For each failure mode: inject fault (hardware injection or simulation)
3. Measure: is the fault detected by diagnostics? Within what time?
4. Calculate: DC = (detected dangerous failures) / (total dangerous failures)
5. Document: fault type, injection method, detection result, response time

## 4 — Safe failure fraction (SFF)

```
SFF = (λ_S + λ_DD) / (λ_S + λ_DD + λ_DU)
```

SFF determines architectural constraints per IEC 61508-2:

| SFF | HFT 0 | HFT 1 | HFT 2 |
|-----|-------|-------|-------|
| < 60% | Not allowed | SIL 1 | SIL 2 |
| 60% - < 90% | SIL 1 | SIL 2 | SIL 3 |
| 90% - < 99% | SIL 2 | SIL 3 | SIL 4 |
| ≥ 99% | SIL 3 | SIL 4 | SIL 4 |

[F,90] — Per IEC 61508-2 Tables 2 and 3 (Type A and Type B subsystems have different tables; consult standard for Type B).

## 5 — Common cause failure (CCF) beta-factor

### 5.1 Beta-factor scoring worksheet

Score each defence against CCF using IEC 61508-6 Annex D:

| Factor | Defence | Score range | Your score |
|--------|---------|-------------|------------|
| Physical separation | Channels in separate enclosures, different power supplies | 0–25 | |
| Diversity | Different sensor types, different manufacturers | 0–20 | |
| Complexity/design | Simple, well-understood components | 0–10 | |
| Assessment/analysis | Formal CCF analysis performed | 0–15 | |
| Maintenance management | Staggered testing, separate test procedures per channel | 0–15 | |
| Environmental control | Temperature, vibration, EMI within spec | 0–15 | |

Total score determines β:
- Score ≥ 85: β = 1% (excellent CCF defence)
- Score 65–84: β = 2%
- Score 45–64: β = 5%
- Score < 45: β = 10% (poor CCF defence)

[S,80] — Simplified from IEC 61508-6 Annex D. Refer to standard for full scoring tables.

### 5.2 CCF scenarios in CPS

| Scenario | CCF risk | Mitigation |
|----------|----------|-----------|
| Shared power supply for redundant channels | High | Separate power supplies with independent protection |
| Same CPU core for BPCS and SIS logic | High | Separate controllers; hardware-isolated SIS |
| Common environmental stress (temperature, vibration) | Medium | Rate components for worst-case environment; diverse mounting |
| Same firmware version on redundant PLCs | Medium | Use firmware from different development teams if possible |
| Single communication bus for redundant sensors | High | Independent wiring per channel |

## 6 — Proof test execution

### 6.1 Test procedure requirements

Each proof test procedure shall specify:

1. **Safety function under test** (SF-n reference)
2. **Test stimulus**: what input is applied (e.g., simulate sensor failure, press e-stop)
3. **Expected response**: what the system should do (e.g., close valve, stop motor)
4. **Timing measurement**: response time from stimulus to safe state
5. **Acceptance criteria**: response time ≤ process safety time (PST)
6. **Number of iterations**: minimum 1; recommend 3 to detect intermittent failures
7. **Bypass management**: how to safely bypass the safety function during test without creating hazard

### 6.2 Acceptance criteria

| Criterion | Pass | Fail |
|-----------|------|------|
| Response time | ≤ PST specified in SC-n | > PST |
| Output state | Reaches defined safe state | Does not reach safe state |
| Diagnostic indication | Diagnostics correctly report test condition | Diagnostics fail to detect |
| Bypass behaviour | Bypass activates cleanly, times out, logs | Bypass fails or no logging |
| Return to service | Normal operation resumes after test | System stuck in test mode |

### 6.3 Failed proof test handling

1. Record the failure with all measured data
2. Classify: systematic fault vs. random hardware fault
3. If random: replace failed component, repeat proof test
4. If systematic: escalate to safety engineer; may require design change
5. Assess: has the safety function been unavailable since last proof test? Calculate actual PFD exposure
6. Update hazard register and proof test schedule if root cause affects interval assumptions

## 7 — Proof test evidence requirements

Each proof test record shall contain:

| Field | Content |
|-------|---------|
| Date | Test date |
| Tester | Name and qualification |
| Safety function | SF-n reference |
| Test procedure version | Procedure document ID and version |
| Stimulus applied | Description of input |
| Response observed | Description of output |
| Response time measured | In milliseconds |
| PST budget | From SC-n |
| Pass / Fail | Determination |
| Deviations | Any anomalies observed |
| Corrective actions | If failed or anomalies detected |
| Next proof test due | Based on interval T1 |

**Retention:** governance_10y tier.

## 8 — Example: SF-1 emergency stop proof test

| Field | Value |
|-------|-------|
| Safety function | SF-1 (emergency stop) |
| SIL target | SIL 2 |
| Architecture | 1oo2 with diagnostics |
| λ_DU (per channel) | 450 FIT |
| DC | 92% |
| β | 2% |
| Calculated max T1 | 18 months |
| Assigned T1 | 12 months (aligned with annual maintenance) |
| PST | 50 ms |
| Test procedure | Press e-stop → verify motor stops within 50 ms → verify PLC logs event → release e-stop → verify system returns to standby |
| Acceptance | Response time ≤ 50 ms; all channels respond; diagnostics log correctly |

*Reference: IEC 61508-1 clause 7.4.10, IEC 61508-2 Tables 2/3, IEC 61508-6 Annex B and D.*
