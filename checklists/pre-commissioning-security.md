# Pre-Commissioning OT Security Checklist

**System / zone:** [Name / Z-n]
**Date:** YYYY-MM-DD
**Checklist owner:** OT Security Lead
**Completed by:** [Name]

## Zone/conduit model

- [ ] Zone boundaries defined and documented in zone-conduit register
- [ ] SL-T allocated per zone per foundational requirement
- [ ] Conduit protection implemented per conduit register (firewall rules, data diodes, VPNs)
- [ ] Default-deny network policy active on all OT zone switches/firewalls
- [ ] Purdue level enforcement verified: no direct L4/5 → L0/1 path

## Authentication and access

- [ ] All default credentials changed on OT devices (PLCs, HMIs, switches, historians)
- [ ] Role-based access configured (operator / engineer / administrator)
- [ ] Engineering workstation access requires jump server + MFA + approval
- [ ] Remote access terminates in DMZ with MFA + session recording + timeout
- [ ] Vendor access via dedicated conduit with vendor-specific rules

## Integrity

- [ ] PLC/SIS firmware verified against vendor baseline (hash or signed image)
- [ ] PLC logic hash baseline captured post-commissioning
- [ ] Application whitelisting active on HMI and engineering workstations
- [ ] Firmware integrity checking enabled where supported

## Monitoring

- [ ] Passive network monitoring deployed (span/mirror port; DPI for OT protocols)
- [ ] PLC change detection active (logic hash monitoring)
- [ ] Safety zone network monitoring active (separate from general OT monitoring)
- [ ] Log aggregation configured: OT device logs → DMZ syslog → SIEM
- [ ] Alert routing configured per priority table (P1 safety events → immediate)

## Patch management

- [ ] OT asset inventory current (firmware/software versions documented)
- [ ] ICS-CERT/CISA advisory subscription active for all OT vendors
- [ ] Staging/simulation environment available for patch testing
- [ ] Compensating controls documented for unpatchable legacy devices

## Documentation

- [ ] Zone/conduit model diagram current and version-controlled
- [ ] Firewall/ACL rules documented and version-controlled
- [ ] OT incident response procedure documented (different from IT IR)
- [ ] Vendor remote access procedure documented

## Sign-off

| Role | Name | Date | Pass? | Signature |
|------|------|------|-------|-----------|
| OT security lead | | | | |
| Network engineer | | | | |
| Safety engineer (if safety zones affected) | | | | |
| CISO | | | | |

**Go-live authorized:** Yes / No
**Conditions (if conditional):** [list with deadlines]
