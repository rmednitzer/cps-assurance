# Safety-Security Change Review: [CHANGE-ID]

**Change description:** [Brief description]
**Requestor:** [Name]
**Date:** YYYY-MM-DD

## 1. Change classification

- [ ] Affects a safety function (SF-n): ___
- [ ] Affects a safety zone (Z-n): ___
- [ ] Affects a conduit to/from a safety zone (CO-n): ___
- [ ] Modifies PLC/SIS logic or firmware
- [ ] Changes network topology in OT environment
- [ ] Affects a CRA-scope product (PROD-n): ___
- [ ] None of the above (standard change — use platform-assurance POL-10)

**If any box checked → this is a safety-critical change. Joint review required.**

## 2. Blast radius

- **Systems directly affected:** [list]
- **Safety functions affected:** [SF-n or "none"]
- **Zones affected:** [Z-n or "none"]
- **SSI entries affected:** [SSI-n or "none"]
- **Conduits affected:** [CO-n or "none"]
- **Physical consequence if change fails:** [description]

## 3. Safety impact analysis

- Does this change weaken any safety constraint (SC-n)? [Yes/No — which?]
- Does this change modify a SIL/PL allocation? [Yes/No — which?]
- Does this change affect a safety function's timing budget? [Yes/No — how?]
- Does this change introduce a new safety-security interaction? [Yes/No — describe]

## 4. Security impact analysis

- Does this change modify a zone boundary or SL-T? [Yes/No — which?]
- Does this change open a new conduit or modify an existing one? [Yes/No — which?]
- Does this change affect authentication/authorization on an OT asset? [Yes/No]
- Does this change require a firmware update to a certified component? [Yes/No]

## 5. Rollback plan

- **Rollback steps:** [exact steps]
- **Rollback time estimate:** [minutes/hours]
- **Safe state during rollback:** [what happens to the physical process]
- **Stop conditions:** [when to abort the change and roll back]

## 6. Verification criteria

- [ ] Safety function response time verified post-change
- [ ] Zone/conduit model still accurate post-change
- [ ] No new safety-security interactions introduced (or documented in SSI register)
- [ ] OT monitoring confirms normal traffic patterns post-change
- [ ] Smoke test for affected safety function(s)

## 7. Approval

| Role | Name | Approve? | Date | Signature |
|------|------|----------|------|-----------|
| Safety engineer | | Yes / No | | |
| OT security lead | | Yes / No | | |
| Safety manager (if SIL/PL change) | | Yes / No | | |
| CISO (if zone boundary change) | | Yes / No | | |

## 8. Post-change evidence

| Artifact | Location | Hash |
|----------|----------|------|
| Before-state snapshot | | |
| Change execution log | | |
| Verification test results | | |
| After-state snapshot | | |
