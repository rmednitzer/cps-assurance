# OT Security Incident Response Checklist

**Incident ID:** [IR-nnnn]
**Date/time detected:** YYYY-MM-DD HH:MM
**Priority:** P1 / P2 / P3 / P4
**Reported by:** [Name / System]

## Triage (within 15 min for P1, 1h for P2)

- [ ] Alert verified (not false positive)
- [ ] Priority classification confirmed per P1-P4 criteria
- [ ] Safety impact assessed: does this affect any safety function (SF-n)?
- [ ] Incident commander assigned

## Containment (within 1h for P1, 4h for P2)

- [ ] Affected zone(s) identified (Z-n)
- [ ] Containment strategy selected (isolate zone / block conduit / disable account)
- [ ] WARNING: Do NOT shut down OT process unless imminent safety risk — coordinate with operations
- [ ] Evidence preserved before containment (network capture, logs, PLC state snapshot)
- [ ] Containment action executed and verified

## Notification

- [ ] Safety manager notified (immediate for P1/P2)
- [ ] CISO notified (immediate for P1, within 4h for P2)
- [ ] Operations lead notified
- [ ] ENISA early warning submitted within 24h (if actively exploited vulnerability, CRA-scope product)
- [ ] NIS2 CSIRT notification within 24h (if operator is essential/important entity)

## Investigation

- [ ] Timeline of events reconstructed
- [ ] Attack vector / root cause identified
- [ ] Affected assets inventoried (PLCs, HMIs, network devices)
- [ ] Safety function integrity verified (logic hash comparison, proof test if needed)
- [ ] Lateral movement assessed (did attacker reach other zones?)

## Recovery

- [ ] Remediation plan developed and approved by safety engineer + OT security lead
- [ ] Remediation executed (patch, reconfigure, restore from known-good baseline)
- [ ] Safety functions reverified after remediation
- [ ] Configuration baseline recaptured
- [ ] Monitoring enhanced for recurrence detection

## Post-incident

- [ ] ENISA 72h notification submitted (if applicable)
- [ ] ENISA 14-day final report submitted (if applicable)
- [ ] Root cause analysis documented
- [ ] Corrective actions identified and assigned
- [ ] SSI register updated if new safety-security interaction discovered
- [ ] Threat register updated with new threat entry (T-n)
- [ ] Lessons learned shared with team
- [ ] All incident evidence stored in evidence pipeline (governance_10y)

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Incident commander | | | |
| Safety manager | | | |
| OT security lead | | | |
| CISO | | | |
