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

**Registers and templates.** Hazard register, zone/conduit register, safety-security interaction (SSI) register, and product register — all with structured templates. Checklists for pre-commissioning (safety and security) and annual review. Templates for hazard entries, zone/conduit entries, SSI entries, product gap assessments, and safety-security change reviews.

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

## Relationship to platform-assurance

This repo governs the **CPS-specific layer**: physical safety, OT networks, product certification. The [platform-assurance](https://github.com/rmednitzer/platform-assurance) repo governs the **IT platform layer**: ISMS, NIS2 entity obligations, GDPR, evidence pipeline, observability, IAM.

Where they connect: platform-assurance evidence pipeline stores CPS evidence artifacts. Platform-assurance ISMS policies (POL-01..10) apply to the IT layer; CPS policies (POL-CPS-01..03) extend them for the physical layer. NIS2 obligations flow from platform-assurance; CPS-specific controls feed back as NIS2 Art 21 technical measures.

## Getting started

1. Read `docs/architecture/standards-applicability.md` — determine which standards and directives apply
2. Populate `registers/product-register.md` — list CPS products with applicable directives
3. Conduct hazard analysis using `templates/hazard-analysis/` → `registers/hazard-register.md`
4. Build zone/conduit model using `templates/zone-conduit/` → `registers/zone-conduit-register.md`
5. Run safety-security interaction analysis using `templates/safety-security-interaction/`
6. Get legal review on `policies/`; management approval
7. Execute checklists before commissioning

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review process, safety-critical change rules, and commit conventions.

## License

[MIT](LICENSE)
