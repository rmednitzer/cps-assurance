# Joint Safety-Security Change Review Checklist

**Change ID:** [CR-nnnn]
**System / product:** [Name]
**Date:** YYYY-MM-DD
**Change owner:** [Name]
**Reviewers:** Safety engineer + OT security lead

## Change description

- [ ] Change scope clearly defined (what is changing, what is not)
- [ ] Affected components identified (hardware, software, firmware, configuration, network)

## Safety impact

- [ ] Hazard register reviewed; any new or modified hazards identified
- [ ] Safety functions affected? If yes: SIL/PL revalidation required
- [ ] Safety constraints affected? If yes: timing contracts reverified
- [ ] Proof test schedule updated if safety function logic changed
- [ ] FMEDA/reliability recalculated if hardware architecture changed

## Security impact

- [ ] Threat register reviewed; any new or modified threats identified
- [ ] Zone/conduit model affected? If yes: SL-T reallocation required
- [ ] Firewall/ACL rules updated if network topology changed
- [ ] Firmware/software integrity baseline recaptured

## Safety-security interaction

- [ ] SSI register reviewed; any new or modified interactions identified
- [ ] JSSR requirements still met after change
- [ ] Conflict resolution log updated if new conflicts identified

## Product conformity

- [ ] Does this change affect CE marking validity? If yes: conformity reassessment required
- [ ] SBOM updated if software components changed
- [ ] Technical documentation updated

## Evidence

- [ ] Change review record stored in evidence pipeline
- [ ] All verification artifacts from retesting stored

## Sign-off

| Role | Name | Date | Approve? | Signature |
|------|------|------|----------|-----------|
| Safety engineer | | | | |
| OT security lead | | | | |
| Change owner | | | | |
| Compliance lead (if conformity affected) | | | | |
