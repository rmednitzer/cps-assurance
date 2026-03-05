<!-- TOC -->
- A) CPS product characterisation
- B) Applicable EU directives/regulations matrix
- C) CRA classification for CPS products
- D) Machinery Regulation 2023/1230 conformity
- E) Radio Equipment Directive (RED) cybersecurity
- F) Low Voltage Directive and EMC Directive
- G) Conformity assessment pathway selection
- H) Technical documentation requirements (unified)
- I) EU Declaration of Conformity and CE marking
- J) Post-market obligations
- K) Compliance roadmap for CPS products
- L) Cross-references
<!-- /TOC -->

Start with 1 sentence listing the applicable EU directives/regulations for this CPS product and the conformity assessment with the highest barrier.

**POINTER-GATE:** EU product regulation for CPS is multi-layered and in transition. Machinery Regulation 2023/1230 application from 2027-01-20 [S,85] — replaces Directive 2006/42/EC. CRA (EU 2024/2847) application dates phased [S,75]. RED delegated act on cybersecurity [S,70] — date and scope may overlap with CRA. Harmonised standards (hEN) under each directive are being developed or transitioned — mark specific hEN references Unknown unless verified on the OJ/EUR-Lex. Notified body availability for new regulations is Unknown. CE marking interactions between multiple directives require careful analysis — each directive's conformity assessment is independent but the CE marking is cumulative.

**A) CPS product characterisation**

Capture enough to determine which EU regulatory instruments apply:

- Product name and description
- Functions: control (actuator commands), sensing, communication, safety, processing
- Physical form: embedded controller / gateway / sensor / actuator / complete machine / robot / IoT device / safety component
- Digital elements: firmware, software, AI/ML components, updatable components
- Connectivity: wired (Ethernet, fieldbus), wireless (Wi-Fi, BLE, Zigbee, cellular, LoRa, 5G), none
- Target market: EU placement (manufacturing, import, distribution)
- Role of economic operator: manufacturer / authorised representative / importer / distributor
- Intended use and reasonably foreseeable misuse
- Safety criticality: can this product cause injury/death if it fails? Can it affect a safety function?
- Integration: is this a component within a larger system, or a standalone product?
- Prior certifications: existing CE marking under other directives?

**B) Applicable EU directives/regulations matrix**

Determine all applicable instruments. A typical CPS product may fall under 2–5 simultaneously:

| Regulatory instrument | Applies if | Key obligations |
|----------------------|-----------|----------------|
| **Machinery Regulation 2023/1230** | Product is a machine, partly completed machine, interchangeable equipment, safety component, lifting accessory, chain/rope/webbing, removable mechanical transmission device, or machinery accessory [S,85] | EHSR (Annex III), technical documentation, conformity assessment, DoC, CE marking |
| **Cyber Resilience Act (CRA)** | Product with digital elements placed on EU market with intended/foreseeable network connection | Annex I security requirements, SBOM, vulnerability handling, ENISA reporting, conformity assessment, DoC, CE marking |
| **Radio Equipment Directive (RED) 2014/53/EU** | Product contains radio equipment (Wi-Fi, BLE, cellular, etc.) | Essential requirements Art. 3, including cybersecurity delegated act [S,70] |
| **Low Voltage Directive (LVD) 2014/35/EU** | Electrical equipment 50-1000V AC / 75-1500V DC | Safety objectives, protection against electrical hazards |
| **EMC Directive 2014/30/EU** | Electrical/electronic equipment | Electromagnetic compatibility: emission limits, immunity |
| **AI Act** | Product contains AI system as defined in AI Act | Risk tier classification, conformity assessment per risk tier |
| **ATEX Directive 2014/34/EU** | Equipment for use in explosive atmospheres | Category, group, zone, conformity assessment |
| **Pressure Equipment Directive 2014/68/EU** | Contains pressure vessels | Category, conformity assessment |
| **General Product Safety Regulation (GPSR)** | Consumer product not fully covered by sector legislation | Residual safety obligations |
| **WEEE / RoHS** | Electronic equipment | Waste management, hazardous substance restrictions |

Output: applicability matrix with Y/N/Unknown per instrument and rationale.

**C) CRA classification for CPS products**

CPS products with digital elements typically fall into these CRA categories:

**Standard products (internal assessment):**
- Simple sensors with network connectivity
- Non-safety consumer IoT
- Industrial gateways without safety function

**Important — Class I (Annex III Part I) [S,80]:**
- Industrial automation and control system interfaces
- Network management/monitoring for industrial systems
- IoT devices for non-critical infrastructure

**Important — Class II (Annex III Part II) [S,80]:**
- Industrial IoT devices in critical infrastructure
- Firewalls for industrial use
- Smart grid components
- Robot safety components
- Smart meters

**Critical (Annex IV) [S,75]:**
- Hardware security devices (HSMs, TPMs, secure elements) used as root of trust in CPS

Note: if the CPS product is a safety component under Machinery Regulation AND an important/critical product under CRA, both conformity assessments apply independently.

**D) Machinery Regulation 2023/1230 conformity**

Conformity assessment routes for machinery [S,85]:

| Machine type | Annex | Route | Notes |
|-------------|-------|-------|-------|
| Most machinery (not in Annex I categories) | Annex V | Internal production control | Manufacturer self-assessment |
| Annex I categories (high-risk machinery) | Annex VII | EU-type examination by notified body | List includes: woodworking, presses, injection moulding, underground machinery, municipal waste collection, vehicle servicing lifts, etc. |
| Annex I categories (alternative) | Annex VIII | Full quality assurance by notified body | Alternative for series production |
| Partly completed machinery | Annex IX | Assembly instructions + declaration of incorporation | Not CE-marked; downstream integrator completes |

EHSR compliance steps:
1. Risk assessment per ISO 12100 (identifying hazards, estimating/evaluating risk, reducing risk by inherently safe design → safeguarding → information)
2. Apply relevant harmonised standards (hEN) — these create presumption of conformity with the EHSR they cover
3. For safety-related control systems: apply ISO 13849-1 or IEC 62061 for SIL/PL determination
4. For cybersecurity of control systems: EHSR 1.1.9 — demonstrate protection against corruption. Evidence can come from IEC 62443 controls, CRA conformity, or other appropriate measures.
5. Prepare technical documentation (section H)
6. Execute conformity assessment per applicable Annex
7. Draw up EU Declaration of Conformity
8. Affix CE marking

**E) Radio Equipment Directive (RED) cybersecurity**

If the CPS product contains radio equipment, RED Article 3 essential requirements apply:

- Art. 3.1(a): Health and safety (LVD alignment)
- Art. 3.1(b): EMC
- Art. 3.2: Efficient use of radio spectrum
- Art. 3.3(d), (e), (f): Cybersecurity, personal data protection, fraud prevention — activated by delegated act [S,70]

RED cybersecurity delegated act status: Unknown — verify whether the delegated act has been published and is in force. The CRA is expected to eventually replace RED cybersecurity requirements for products in CRA scope, but transition period and interaction are volatile.

If RED cybersecurity delegated act applies:
- Network and data protection measures
- Protection against fraud
- Personal data protection (Art. 3.3(e))
- Harmonised standards under development (ETSI EN 303 645 for consumer IoT is a reference)

**F) Low Voltage Directive and EMC Directive**

LVD (2014/35/EU):
- Applies to electrical equipment 50–1000V AC / 75–1500V DC
- Safety objectives: protection against electrical, thermal, mechanical, chemical, radiation hazards
- Internal production control (manufacturer self-assessment)
- Harmonised standards: IEC/EN 60204-1 (machinery electrical safety), IEC/EN 62368-1 (audio/video/ICT), sector-specific EN

EMC (2014/30/EU):
- Applies to all electrical/electronic equipment
- Emission limits + immunity requirements
- Internal production control or EU-type examination
- Harmonised standards: EN 55032/55035 (multimedia), EN 61000 series

Both LVD and EMC are typically mature for CPS products — standards exist, notified bodies available. The risk is often in neglecting EMC for industrial environments with high-frequency inverters, motors, or welding equipment.

**G) Conformity assessment pathway selection**

Decision tree for CPS product conformity:

1. **Identify all applicable directives** (section B matrix)
2. **For each directive, determine the conformity assessment route** (self-assessment vs. notified body)
3. **Identify the most demanding route** — this sets the bar. If any directive requires a notified body, that assessment must be completed.
4. **Check for harmonised standards** that cover the essential requirements. Where hEN exist: applying them creates a presumption of conformity. Where hEN are absent: manufacturer must demonstrate compliance by other means and document the approach.
5. **Sequence assessments:**
   - Machinery Regulation first (drives the risk assessment and safety analysis)
   - CRA second (cybersecurity requirements, SBOM, vulnerability handling)
   - RED third (if applicable — may defer to CRA when transition completes)
   - LVD and EMC in parallel (typically straightforward with existing hEN)
   - AI Act if applicable (runs in parallel; may share risk assessment with Machinery Regulation)
6. **Single technical file** can serve all directives — organize with directive-specific sections.

**H) Technical documentation requirements (unified)**

Build a single technical documentation package satisfying all applicable directives. Structure:

```
CPS Product Technical Documentation
├── 1. General
│   ├── 1.1 Product description (name, model, variants, intended use)
│   ├── 1.2 Identification of economic operator
│   ├── 1.3 Applicable legislation and standards
│   ├── 1.4 Document control (version, date, author, approval)
│
├── 2. Risk Assessment
│   ├── 2.1 Hazard identification (ISO 12100 + STPA) [Machinery Regulation]
│   ├── 2.2 Cybersecurity risk assessment (CRA Annex I + IEC 62443) [CRA]
│   ├── 2.3 EMC risk assessment [EMC Directive]
│   ├── 2.4 Electrical safety assessment [LVD]
│   ├── 2.5 AI risk assessment [AI Act, if applicable]
│
├── 3. Design and Architecture
│   ├── 3.1 System architecture (hardware, software, communication)
│   ├── 3.2 Safety architecture (SIL/PL allocation, safety functions, independence)
│   ├── 3.3 Security architecture (zone/conduit model, SL-T allocation)
│   ├── 3.4 Electrical design (schematics, PCB, cable routing)
│   ├── 3.5 Mechanical design (drawings, materials, stress analysis)
│
├── 4. Safety Evidence
│   ├── 4.1 SIL/PL determination and allocation
│   ├── 4.2 FMEDA / reliability calculations
│   ├── 4.3 Safety function test reports
│   ├── 4.4 Functional safety management plan
│
├── 5. Cybersecurity Evidence
│   ├── 5.1 CRA Annex I Part I compliance matrix
│   ├── 5.2 SBOM (machine-readable)
│   ├── 5.3 Vulnerability handling procedures
│   ├── 5.4 Penetration test report
│   ├── 5.5 Secure development lifecycle evidence (IEC 62443-4-1)
│
├── 6. EMC and Electrical Safety
│   ├── 6.1 EMC test reports (EN 55032/55035 or sector hEN)
│   ├── 6.2 Electrical safety test reports (IEC 60204-1 or sector hEN)
│
├── 7. Standards Applied
│   ├── 7.1 List of harmonised standards applied (with edition)
│   ├── 7.2 For requirements not covered by hEN: description of alternative solutions
│
├── 8. Instructions and Labelling
│   ├── 8.1 User instructions (in all official languages of target member states)
│   ├── 8.2 Maintenance and decommissioning instructions
│   ├── 8.3 Safety warnings and labelling
│   ├── 8.4 End-of-support date and update information [CRA]
│
├── 9. EU Declaration of Conformity
│
├── 10. Notified Body Certificates (if applicable)
│
└── 11. Post-Market Information
    ├── 11.1 Vulnerability disclosure policy [CRA]
    ├── 11.2 Incident reporting procedures [CRA, NIS2 for operator]
    └── 11.3 Product registration (if required by CRA implementing acts)
```

Retain for 10 years after last product placed on market [Machinery Regulation, CRA — verify].

**I) EU Declaration of Conformity and CE marking**

DoC requirements:
- Must reference ALL applicable directives/regulations
- Separate DoC per directive permitted, or single combined DoC
- Contents: product identification (name, model, serial/type), manufacturer details, list of all applicable directives with article references, list of harmonised standards applied, notified body details (if used), signature of authorised person, date and place
- Language: official language(s) of member state(s) where product is placed on market

CE marking:
- Affixed to the product or its data plate
- Visible, legible, indelible
- If notified body involved: NB identification number next to CE marking
- CE marking must not be affixed until ALL applicable conformity assessments are completed and ALL DoCs are drawn up

**J) Post-market obligations**

CPS manufacturers have ongoing obligations:

Machinery Regulation:
- Maintain technical documentation and DoC for 10 years
- Implement corrective actions if hazard identified post-market
- Cooperate with market surveillance authorities

CRA:
- Provide free security updates for support period (≥5 years or expected product lifetime)
- Operate vulnerability handling process
- Report actively exploited vulnerabilities to ENISA (24h early warning, 72h notification, 14 days final report [S,80])
- Maintain and update SBOM when components change
- Published coordinated vulnerability disclosure policy

RED (if applicable):
- Post-market monitoring per manufacturer obligations

NIS2 (for operators):
- If the operator using the CPS product is an essential/important entity, the manufacturer may receive supply chain security requirements from the operator
- Vulnerability information sharing between manufacturer and operator

**K) Compliance roadmap for CPS products**

Phased approach:
1. **Product characterisation and applicability analysis** (section A + B) — determine full regulatory scope
2. **Risk assessment** (safety: ISO 12100/STPA; security: CRA Annex I/IEC 62443; EMC/electrical) — produce unified risk register
3. **Design for compliance** — safety architecture (SIL/PL), security architecture (zone/conduit, secure-by-default), EMC/electrical safety
4. **Evidence production** — tests, analyses, SBOM, development lifecycle evidence
5. **Conformity assessment** — self-assessment where permitted; notified body engagement where required
6. **Technical documentation** (section H) — compile and review
7. **DoC and CE marking** — after all assessments complete
8. **Post-market** — vulnerability handling, updates, monitoring, ENISA reporting

Timeline considerations:
- Machinery Regulation 2023/1230 application: 2027-01-20 [S,85]
- CRA phased application: vulnerability/incident reporting first; full conformity later [S,75] — verify EUR-Lex
- Start with longest-lead items: notified body engagement, SIL certification, CRA SBOM infrastructure

**L) Cross-references**

- **functional-safety.md** (in this skill): SIL/PL determination and safety evidence feed Machinery Regulation EHSR compliance.
- **ot-security.md** (in this skill): IEC 62443 controls feed CRA Annex I evidence and Machinery Regulation EHSR 1.1.9.
- **safety-security-interaction.md** (in this skill): Joint analysis when safety and security requirements interact in the product.
- **eu-regulatory (cra reference)**: Pure software CRA classification. This reference extends for CPS products with physical coupling.
- **eu-regulatory (multi-framework reference)**: Sequencing strategy when 3+ frameworks apply (common for CPS).
- **eu-regulatory (ai-act reference)**: If CPS product contains AI.
- **supply-chain-security**: SBOM generation for firmware/embedded components; CRA SBOM obligation.
- **security-depth (vulnerability-pipeline reference)**: CRA ENISA reporting workflow; CVD process.
- **assurance-case-builder**: Build structured compliance assurance case mapping product evidence to regulatory requirements.
