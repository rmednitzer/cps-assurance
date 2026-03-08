# cps-assurance

Governance-as-code for cyber-physical systems under EU product regulation.

Covers the three domains that are inseparable in CPS: functional safety, OT/ICS security, and EU product conformity — plus their interaction.

## Purpose

Cyber-physical systems — systems where computational processes interact with physical processes through sensors, actuators, and control loops — are increasingly subject to EU product regulation, functional safety requirements, and cybersecurity obligations simultaneously. Existing IT governance frameworks do not adequately address the failure modes specific to CPS (timing violations, numeric drift, actuator authority, sensor spoofing). Existing safety engineering methods do not adequately address the infrastructure governance and supply chain transparency that EU regulation now demands. This repository bridges both.

The core challenge is that safety and security are not independent in CPS. A security failure can cause a safety hazard (attacker modifies PLC logic → safety function disabled). A safety mechanism can create a security vulnerability (safety-required cleartext protocol → eavesdropping possible). Governing either domain in isolation produces blind spots at the interaction boundary. This repository treats that boundary as the primary object of governance.

## What's in the repository

**Reference architecture.** A CPS reference architecture showing Purdue levels with enforcement boundaries at each tier. Each boundary — sensor ingestion, compute output, actuator command, safety function interface, IT-OT DMZ, zone boundary — has defined invariants, violation response, and monitoring.

**Functional safety.** A STPA-informed hazard analysis methodology producing hazard registers, SIL/PL allocations, safety function specifications, and verification evidence requirements compatible with IEC 61508, ISO 13849-1, and the Machinery Regulation. Includes runtime boundary contracts for safety functions covering sensor ingestion, compute output, actuator command, and safety independence boundaries.

**OT security.** An IEC 62443-based zone and conduit model with Security Level Target (SL-T) allocation per zone, STRIDE threat modelling adapted for OT with physical consequence tracing, Purdue model enforcement rules, and OT-specific controls mapped to IEC 62443 foundational requirements. Safety zones receive special treatment: dedicated isolation, highest SL-T, unidirectional communication, no remote access, joint change management.

**Safety-security interaction analysis.** A seven-type interaction taxonomy (SS-1 through SS-7) covering both directions: security failures causing safety hazards and safety mechanisms creating security vulnerabilities. Joint STPA-STRIDE analysis method. Conflict resolution principles. Joint safety-security requirements specification. Unified assurance case structure arguing both properties. Runtime monitors for safety-security interactions. Change management for interacting controls.

**Regulatory mapping.** A control domain crosswalk mapping Machinery Regulation EHSR, CRA Annex I, IEC 62443, and IEC 61508 requirements to shared controls. Shared evidence catalogue showing which single artifacts satisfy multiple frameworks. Safety-security conflict points with resolution approaches. Conformity assessment sequencing for products under multiple directives.

**Conformity assessment.** A comprehensive guide covering CPS product characterisation, applicable EU directive identification (Machinery Regulation, CRA, RED, LVD, EMC, AI Act, ATEX, PED), CRA classification for CPS products, conformity assessment route selection, unified technical documentation structure serving all applicable directives, EU Declaration of Conformity requirements, and post-market obligations.

**Policies.** Three CPS-specific policies extending the platform-assurance ISMS: functional safety management (IEC 61508 lifecycle), OT security (IEC 62443-2-1), and product conformity with post-market obligations. These complement, not replace, the ten IT-layer policies in platform-assurance.

**Registers and templates.** Hazard register, safety constraint register, threat register, zone/conduit register, safety-security interaction (SSI) register, product register, and a traceability manifest — all with structured templates. Checklists for pre-commissioning (safety and security) and annual review. Templates cover hazard entries, safety constraints, threat entries, zone/conduit entries, SSI entries, assurance cases, traceability manifests, product gap assessments, and safety-security change reviews.

## Design principles

1. **Correctness > Safety > Auditability > Completeness > Speed** — priority ordering for all design and operational decisions.
2. **Enforce at boundaries, not internals.** Component internals may change; boundary contracts must hold.
3. **Measure, don't trust.** Every assurance claim must be backed by observable, measurable evidence.
4. **Degrade, don't fail.** Every component has a defined degraded mode. Hard failure is a design defect.
5. **Safety and security are jointly governed.** No safety change without security review. No security change affecting a safety zone without safety review.

## Regulatory scope

| Framework | CPS relevance |
|-----------|---------------|
| Machinery Regulation (EU 2023/1230) | Safety requirements, EHSR 1.1.9 cybersecurity of controls, CE marking (application 2027-01-20) |
| Cyber Resilience Act (EU 2024/2847) | Security requirements for products with digital elements, SBOM, vulnerability handling |
| RED 2014/53/EU | Radio equipment cybersecurity (delegated act) |
| LVD 2014/35/EU | Electrical safety |
| EMC 2014/30/EU | Electromagnetic compatibility |
| EU AI Act (EU 2024/1689) | If CPS contains AI components |
| IEC 61508 / ISO 13849-1 / IEC 62061 | Functional safety (SIL/PL determination) |
| IEC 62443 (all parts) | OT/ICS security (zone/conduit, security levels) |
| IEC 63069 / IEC TR 63074 | Safety-security interface |
| NIS2 (operator obligations) | If operator is essential/important entity |

## Methodology

- **STPA (System-Theoretic Process Analysis)** for hazard identification — adapted for CPS with security threat overlay
- **STRIDE** for OT threat modelling with physical consequence tracing
- **IEC 62443-3-2** for zone/conduit modelling and SL-T allocation
- **Joint STPA-STRIDE** for safety-security interaction analysis
- **GSN/CAE** for structured assurance cases arguing both safety and security properties

Evidence is tagged by provenance: `[F]` verified fact, `[I]` inference, `[S]` heuristic — with confidence levels {50,70,80,90}.

The typed schema layer lives in `schemas/`; implementation guidance for machine-readable entries and generated traceability lives in `docs/assurance/data-model-and-traceability.md`. The AI-facing artifact classification index lives in `artifact-index.yaml`.

## Relationship to platform-assurance

This repo governs the **CPS-specific layer**: physical safety, OT networks, product certification. The [platform-assurance](https://github.com/rmednitzer/platform-assurance) repo governs the **IT platform layer**: ISMS, NIS2 entity obligations, GDPR, evidence pipeline, observability, IAM.

Where they connect:

- **Evidence pipeline:** CPS evidence artifacts flow into the platform-assurance evidence pipeline (MinIO WORM, cosign signing, OpenSearch indexing, daily hash chain). CPS evidence types, metadata schema, and storage paths are defined in `docs/evidence/cps-evidence-types.md`.
- **Change management:** Platform-assurance POL-10 applies to all changes; CPS policies (POL-CPS-01..03) add OT-specific review gates. Changes affecting OT infrastructure, safety zones, or CPS-scope products must pass both POL-10 and the CPS-specific gates.
- **Incident escalation:** OT security alerts escalate to the platform-assurance incident response workflow (POL-04) per the priority mapping in `docs/evidence/cps-evidence-types.md` §6.
- **Regulatory split:** NIS2 entity-level obligations live in platform-assurance; CPS-specific controls (Machinery Reg, IEC 62443, IEC 61508) live here; CRA spans both.
- **Control cross-references:** CPS zone/conduit and safety-constraint schemas accept `platform_controls` references (CTL-nnnn) to trace dependencies on IT-layer controls.

## Getting started

1. Read `docs/architecture/standards-applicability.md` — determine which standards and directives apply
2. Populate `registers/product-register.md` — list CPS products with applicable directives
3. Conduct hazard analysis using `templates/hazard-analysis/` → `registers/hazard-register.md`
4. Derive safety constraints using `templates/safety-constraints/` → `registers/safety-constraint-register.md`
5. Build a threat model using `templates/threat-model/` → `registers/threat-register.md`
6. Build zone/conduit model using `templates/zone-conduit/` → `registers/zone-conduit-register.md`
7. Run safety-security interaction analysis using `templates/safety-security-interaction/` → `registers/ssi-register.md`
8. Populate the traceability manifest using `templates/traceability/` → `registers/traceability-manifest.md`
9. Review `docs/assurance/data-model-and-traceability.md` and `schemas/` before automating or generating evidence
10. Run `make validate` before review or merge
11. Get legal review on `policies/`; management approval
12. Execute checklists before commissioning

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review process, safety-critical change rules, and commit conventions.

## License

[MIT](LICENSE)
