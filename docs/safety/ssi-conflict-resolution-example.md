# Safety-Security Conflict Resolution — Worked Example

**Purpose:** Demonstrate the conflict resolution process for a real-world safety-security interaction using the SS-type taxonomy and joint STPA-STRIDE method.

## Scenario

**System:** Industrial robot controller with safety-rated speed and force limiting (SF-2, PL d).

**The conflict:** The robot controller uses Modbus TCP to read safety diagnostic data from the safety PLC to the engineering workstation (HMI). This diagnostic channel is required for safety monitoring (IEC 61508-1 clause 7.4.7: "The safety-related system shall provide adequate diagnostic capability").

- **Safety requirement:** Modbus TCP diagnostic readout must operate with ≤ 5 ms latency to ensure real-time display of safety function status on HMI. Cleartext protocol required because the safety PLC firmware is certified with Modbus TCP only — adding TLS would require re-certification [S,80].
- **Security requirement:** All OT protocols traversing zone boundaries must be authenticated and encrypted per POL-CPS-02 and IEC 62443-3-3 SR 3.1 (communication integrity) and SR 4.1 (information confidentiality).

## Conflict classification

This is a combination of:

- **SS-3** (Safety mechanism creates security vulnerability): The safety-required cleartext Modbus TCP protocol exposes diagnostic data to eavesdropping and enables potential packet injection.
- **SS-4** (Safety constraint prevents security control): The 5 ms latency requirement and PLC firmware certification status prevent adding TLS encryption to the Modbus TCP channel.

## Analysis: Joint STPA-STRIDE

### Pass 1 — Safety perspective (STPA)

**Control action:** Safety PLC sends diagnostic data to HMI via Modbus TCP.

| UCA type | Unsafe control action | Hazard |
|----------|----------------------|--------|
| Not provided | Diagnostic data not sent → HMI shows stale status → operator unaware of SF-2 degradation | H-2 |
| Provided incorrectly | Diagnostic data tampered → HMI shows healthy when SF-2 is faulted → operator enters hazard zone | H-1, H-2 |
| Wrong timing | Diagnostic data delayed > 5 ms → HMI displays outdated status | H-2 |

### Pass 2 — Security perspective (STRIDE)

| STRIDE category | Threat | Entry point | Physical consequence |
|-----------------|--------|-------------|---------------------|
| Tampering | Attacker injects false Modbus TCP responses | CO-1 (if cleartext) | Operator sees false "healthy" status; enters hazard zone |
| Information Disclosure | Attacker reads diagnostic data | CO-1 network tap | Learns safety PLC configuration, firmware version, enabled functions |
| Denial of Service | Attacker floods Modbus TCP port | CO-1 network | Diagnostic readout fails; HMI goes stale |

### Pass 3 — Interaction analysis

The safety requirement (cleartext Modbus TCP) **directly enables** the security threats (tampering, eavesdropping, DoS). This is the core SS-3/SS-4 conflict.

## Resolution options evaluated

### Option A: Add TLS to Modbus TCP

| Criterion | Assessment |
|-----------|-----------|
| Security improvement | High — eliminates eavesdropping and tampering |
| Safety impact | **Negative** — TLS handshake adds 10–50 ms latency; exceeds 5 ms budget |
| Certification impact | **Blocking** — safety PLC firmware certified without TLS; re-certification required (6+ months, high cost) |
| Verdict | **Rejected** — violates safety timing constraint and certification status |

### Option B: Dedicated physically isolated diagnostic port

| Criterion | Assessment |
|-----------|-----------|
| Security improvement | High — physical isolation eliminates remote attack vector |
| Safety impact | **Neutral** — no change to Modbus TCP protocol or timing |
| Certification impact | **None** — PLC firmware unchanged |
| Implementation | Dedicated Ethernet port on safety PLC connected directly to engineering workstation via point-to-point cable. No switch, no router, no connection to general OT network. |
| Residual risk | Physical access to cable allows eavesdropping/injection — mitigated by physical security controls (locked cabinet, tamper detection) |
| Verdict | **Accepted as primary resolution** |

### Option C: Protocol gateway in DMZ

| Criterion | Assessment |
|-----------|-----------|
| Security improvement | Medium — gateway terminates Modbus TCP, re-publishes diagnostic data over TLS-secured API |
| Safety impact | **Minimal** — gateway adds 1–2 ms latency to non-safety path (the re-published data is informational, not safety-critical) |
| Certification impact | **None** — gateway is outside safety PLC boundary |
| Implementation | Gateway reads Modbus TCP from isolated port, publishes summary to enterprise network over HTTPS |
| Residual risk | Gateway itself becomes attack surface — mitigate with hardened appliance in DMZ |
| Verdict | **Accepted as complementary measure** for enterprise visibility |

## Final resolution

**Primary:** Option B — Dedicated physically isolated diagnostic port.

**Complementary:** Option C — Protocol gateway in DMZ for enterprise visibility of non-safety-critical summary data.

**Resolution principle applied:** "Safety wins at the actuator; security wins at the boundary" (from `docs/safety/safety-security-interaction.md` Section D).

## SSI register entry

```markdown
| SSI-3 | SS-3 + SS-4 | SF-2 (speed/force limiting diagnostics) | T-3 (Modbus TCP eavesdropping/injection) | Operator receives false safety status; enters hazard zone | High | Physically isolated diagnostic port + DMZ gateway for enterprise | Verified |
```

## JSSR generated

```markdown
| JSSR-3 | Safety diagnostic Modbus TCP channel shall use dedicated physically isolated Ethernet port with no connection to general OT network | Safety: preserves 5 ms latency and certified PLC firmware | Security: eliminates remote attack vector for diagnostic channel | SSI-3 | Safety PLC hardware design | Physical inspection + network scan confirming no path from L2+ to diagnostic port | Verified |
```

## Conflict resolution log entry

```markdown
| SSI-3 | Safety requires cleartext Modbus TCP with ≤5 ms latency; security requires encryption on all OT protocols | Physical isolation (Option B) + DMZ gateway (Option C) | Physical access attack on isolated cable — mitigated by cabinet lock + tamper detection | Safety manager (name, date) | OT security lead (name, date) | YYYY-MM-DD |
```

## Lessons learned

1. **Not all conflicts require protocol changes.** Physical isolation can resolve SS-3/SS-4 conflicts without modifying certified safety firmware.
2. **Separate safety-critical from informational data paths.** The DMZ gateway provides enterprise visibility without compromising the safety channel.
3. **Document the residual risk explicitly.** Physical access is a residual risk — the resolution shifts the attack from remote (high likelihood) to physical (lower likelihood), which is an acceptable risk trade.
4. **Involve both safety and security leads early.** The joint review prevented a costly path (Option A: TLS + re-certification) that would have delayed the project by 6+ months.

*Reference: IEC 63069 (safety-security framework), IEC 62443-3-3 SR 3.1/4.1, IEC 61508-1 clause 7.4.7.*
