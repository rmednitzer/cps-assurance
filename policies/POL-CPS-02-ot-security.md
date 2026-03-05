# POL-CPS-02: OT/ICS Security Policy

**Version:** 1.0 DRAFT
**Owner:** CISO + OT Security Lead
**Approved by:** [Board / Executive management — name and date]
**Review cycle:** Annual + after any OT security incident or zone/conduit change
**Classification:** Internal

## Purpose

Establish the security management system for operational technology (OT) and industrial control system (ICS) environments per IEC 62443-2-1.

## Scope

All OT environments including PLCs, RTUs, DCS, SCADA, HMIs, historians, engineering workstations, safety instrumented systems (SIS), and the network infrastructure connecting them.

## Policy statements

1. All OT environments shall have a documented zone/conduit model per IEC 62443-3-2 (`registers/zone-conduit-register.md`).
2. Security Level Targets (SL-T) shall be allocated per zone. Zones containing safety functions shall have SL-T ≥ 3 [S,80].
3. Purdue model segmentation shall be enforced: no direct Level 4/5 → Level 0/1 communication.
4. Safety Instrumented Systems (SIS) shall reside in dedicated zones with the highest SL-T, unidirectional communication where possible, and no remote access.
5. Remote access to OT shall terminate in the DMZ with MFA, session recording, and time-limited access.
6. Engineering workstation access to Level 0–1 requires jump server, MFA, change management approval, and logged session.
7. All OT network changes require pre-change security review per CONTRIBUTING.md.
8. OT vulnerability management follows the process in `docs/security/ot-security-architecture.md` §I — availability-first patching with compensating controls for unpatchable legacy.
9. OT-specific monitoring shall be deployed (passive network monitoring, PLC change detection, safety system communication monitoring).
10. Vendor remote access shall use a dedicated conduit with vendor-specific firewall rules, session recording, and automatic timeout.

## Change management for OT

OT changes follow platform-assurance POL-10 (Change Management) with these additions:
- All OT changes require OT Security Lead approval
- Changes affecting safety zones require joint safety-security review
- No changes to SIS zone without safety manager + CISO dual approval
- Emergency changes to OT require post-hoc review within 24h

## Cross-references

| Requirement | Source |
|-------------|--------|
| IEC 62443-2-1 (IACS security management system) | IEC 62443 |
| IEC 62443-3-2 (system security requirements, zone/conduit) | IEC 62443 |
| Machinery Regulation EHSR 1.1.9 (protection against corruption) | EU 2023/1230 |
| NIS2 Art 21.2(e) (network and information systems security) | NIS2 |
| CRA Annex I Part I (if OT products placed on market) | EU 2024/2847 |

## Review and approval

| Date | Version | Approved by | Signature |
|------|---------|-------------|-----------|
| YYYY-MM-DD | 1.0 | [Name, Title] | [Signature] |
