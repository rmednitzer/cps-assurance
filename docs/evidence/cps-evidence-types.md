# CPS Evidence Types

**Purpose:** Define the evidence artifact types, metadata schema, storage convention, and retention tiers for CPS-layer evidence that flows into the platform-assurance evidence pipeline.

**Integration:** This document specifies the interface between cps-assurance (producer) and the platform-assurance evidence pipeline (transport, storage, indexing). The platform-assurance evidence pipeline (`evidence-pipeline/ci/evidence-stage.yml`, `evidence-pipeline/collectors/daily-hash-chain.sh`, `evidence-pipeline/verification/verify-evidence.sh`) handles signing, WORM storage, hash chaining, and OpenSearch indexing. This document defines what the CPS layer produces and how it must be tagged.

---

## 1 — Evidence artifact types

| Artifact type | Description | Producer | Trigger | Retention tier |
|--------------|-------------|----------|---------|---------------|
| `hazard_analysis` | Approved hazard register snapshot (H-n, SF-n, UCA-n) | Safety engineer | Register change merged to main | `governance_10y` |
| `sil_pl_allocation` | SIL/PL determination with risk graph parameters and rationale | Safety engineer | New or changed hazard | `governance_10y` |
| `fmeda_report` | FMEDA / reliability calculation per safety function | Safety engineer | New SF-n or component change | `governance_10y` |
| `safety_function_test` | End-to-end safety function test report with timing evidence | Safety engineer | Proof test interval; commissioning; change | `governance_10y` |
| `plc_logic_hash` | PLC/SIS logic hash baseline capture | OT security lead | Commissioning; logic change | `governance_10y` |
| `zone_conduit_verification` | Zone/conduit model verification (network scan, firewall rule audit) | OT security lead | Commissioning; OT network change | `governance_10y` |
| `ssi_review` | SSI register review record with joint safety-security sign-off | Safety manager + OT security lead | Quarterly; safety or security change | `governance_10y` |
| `threat_assessment` | Threat register snapshot with STRIDE analysis per zone | OT security lead | Register change merged to main | `governance_10y` |
| `conformity_package` | Technical documentation package per product per directive | Compliance lead | Pre-market; post-market change | `governance_10y` |
| `doc_of_conformity` | EU Declaration of Conformity (signed) | Compliance lead | Conformity assessment complete | `governance_10y` |
| `sbom_cps` | SBOM for CPS product firmware/software (CycloneDX/SPDX) | Build pipeline | Build; component change | `ci_3y` |
| `pentest_ot` | OT penetration test report | OT security lead | Annual; major architecture change | `governance_10y` |
| `proof_test_record` | Proof test execution record per safety function | Operations | Proof test interval | `governance_10y` |
| `pre_commissioning_safety` | Completed pre-commissioning safety checklist (signed) | Safety manager | Commissioning | `governance_10y` |
| `pre_commissioning_security` | Completed pre-commissioning security checklist (signed) | OT security lead | Commissioning | `governance_10y` |
| `annual_review` | Completed annual CPS assurance review checklist (signed) | Safety manager + OT security lead | Annual | `governance_10y` |
| `change_review` | Completed safety-security change review (signed) | Safety engineer + OT security lead | Safety-critical change | `governance_10y` |
| `traceability_manifest` | Release-gated traceability manifest snapshot | Safety manager + Compliance lead | Release candidate | `governance_10y` |
| `assurance_case` | Assurance case snapshot (GSN/CAE claim-evidence structure) | Safety manager | Release; audit preparation | `governance_10y` |

## 2 — Evidence manifest metadata

Every CPS evidence artifact uploaded to the platform-assurance evidence pipeline must include the following metadata fields in its evidence manifest entry. These fields extend the platform-assurance manifest schema with CPS-specific tags.

```json
{
  "artifact_id": "uuid",
  "artifact_type": "hazard_analysis",
  "source": "cps-assurance",
  "project": "cps-assurance",
  "created_at": "2026-03-08T12:00:00Z",
  "sha256_hash": "abc123...",
  "s3_bucket": "evidence",
  "s3_key": "governance/cps/2026/hazard_analysis/H-register-v1.2.json",
  "signing_method": "cosign-keyless",
  "retention_tier": "governance_10y",
  "framework_tags": ["Machinery-Reg", "IEC-61508", "IEC-62443", "CRA"],
  "cps_ids": ["H-1", "H-2", "SF-1"],
  "product_ids": ["PROD-1"],
  "review_signoff": {
    "safety_manager": {"name": "", "date": ""},
    "ot_security_lead": {"name": "", "date": ""}
  },
  "description": "Hazard register v1.2 — added H-3 for new actuator mode"
}
```

## 3 — Storage path convention

```
evidence/governance/cps/{year}/{artifact_type}/{artifact_id_or_filename}
```

Examples:

- `evidence/governance/cps/2026/hazard_analysis/H-register-v1.2.json`
- `evidence/governance/cps/2026/plc_logic_hash/SIS-PLC-01-hash-2026-03-08.txt`
- `evidence/governance/cps/2026/conformity_package/PROD-1-tech-doc-v2.0.tar.gz`
- `evidence/governance/cps/2026/sbom_cps/PROD-1-sbom-cdx-v3.1.json`

## 4 — Retention tiers

| Tier | Duration | Basis |
|------|----------|-------|
| `governance_10y` | 10 years from last product placement on market | Machinery Regulation Annex VII; CRA; IEC 61508 Part 1 |
| `ci_3y` | 3 years | CI build evidence (SBOMs, vuln scans) — regenerable |

## 5 — Signing and integrity

All CPS evidence artifacts must be signed using the same mechanism as platform-assurance evidence (cosign keyless signing via Sigstore). The daily hash chain maintained by the platform-assurance evidence pipeline includes CPS evidence artifacts — no separate chain is needed.

## 6 — Incident escalation interface

When the OT monitoring stack generates a P1 or P2 alert (as defined in `docs/security/ot-security-architecture.md` §H alert priority table), the alert enters the platform-assurance incident response workflow (POL-04) as follows:

| OT alert priority | Platform IR classification | Notification chain trigger |
|-------------------|--------------------------|---------------------------|
| P1 (safety system anomaly, PLC logic change, new device on safety zone) | P1 Critical | NIS2 Art 23 (if significant incident); CRA Art 14 (if actively exploited vuln in manufactured product) |
| P2 (cross-zone violation, default credential use) | P2 High | NIS2 Art 23 (assess significance); GDPR Art 33 (if personal data affected) |
| P3 (reconnaissance, failed auth threshold) | P3 Medium | Assess and document; escalate if pattern indicates targeted attack |
| P4 (firmware version mismatch) | P4 Low | Document; include in next scheduled review |

The OT Security Lead classifies whether an OT event meets the NIS2 "significant incident" threshold. The CISO (platform-assurance POL-04 IC) coordinates the parallel notification chain. Evidence from the OT monitoring stack flows to the platform-assurance evidence store under `evidence/incidents/{incident-id}/ot/`.

---

*This document defines the CPS → platform-assurance evidence interface. Platform-assurance evidence pipeline implementation details are in the platform-assurance repository.*
