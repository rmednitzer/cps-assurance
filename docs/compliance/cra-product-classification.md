# CRA Product Classification Decision Tree

**Date:** 2026-03-08
**Regulation:** Cyber Resilience Act (EU 2024/2847), Articles 6–8, Annex III, Annex IV
**Status:** DRAFT — classification examples are indicative [S,80]. Verify product-specific classification against the official Annex III/IV lists.

---

## Confidence notes

CRA classification tiers and the decision logic are established in the regulation text [F,90]. The product category lists in Annex III and Annex IV are exhaustive (closed lists) [F,90], but determining whether a specific product falls within a category requires interpretation — marked [S,80] unless otherwise noted. CPS-specific classification guidance is inference-based [I,75].

---

## 1 — Classification tiers

The CRA establishes four classification tiers for products with digital elements [F,90]:

| Tier | Legal basis | Conformity route | Notified body? |
|------|-----------|-----------------|----------------|
| **Default** | Article 6(2) — not listed in Annex III or IV | Module A (internal) | No |
| **Important — Class I** | Article 7(1), Annex III Part I | Module A if hEN applied; else Module B+C or H | Only if no hEN |
| **Important — Class II** | Article 7(2), Annex III Part II | Module B+C or Module H | **Yes** |
| **Critical** | Article 8, Annex IV | Module B+C or Module H | **Yes** |

The classification determines the **conformity assessment burden** and whether a **notified body** must be involved.

---

## 2 — Annex III: Important products with digital elements

### 2.1 Class I (Annex III Part I) — summary of key categories [S,80]

Products that perform functions where cybersecurity weaknesses pose a higher risk:

- Identity management systems and privileged access management software/hardware
- Standalone and embedded browsers
- Password managers
- Software for searching, removing, or quarantining malware
- Products with digital elements with the function of a VPN
- Network management systems
- Security information and event management (SIEM) systems
- Boot managers
- Public key infrastructure and digital certificate issuance software
- Physical and virtual network interfaces
- Operating systems not covered by Class II
- Routers, modems for internet connection, and switches not covered by Class II
- Microprocessors and microcontrollers with security-relevant functionalities
- Application-specific integrated circuits (ASICs) and FPGAs with security-relevant functionalities
- **Industrial automation and control systems (IACS)** not covered by Class II
- **Industrial IoT** not covered by Class II or Critical

### 2.2 Class II (Annex III Part II) — summary of key categories [S,80]

Products where exploitation could cause more severe impact:

- Operating systems for servers, desktops, and mobile devices
- Hypervisors and container runtime systems
- Public key infrastructure and digital certificate issuance
- Firewalls, intrusion detection/prevention systems for industrial use
- Tamper-resistant microprocessors/microcontrollers
- **Industrial IoT devices for entities subject to NIS2 as essential entities**
- **Robot sensing and actuator components** subject to safety requirements
- **Smart meters** and industrial IoT gateways in critical infrastructure
- Hardware security modules (HSMs)

### 2.3 Class I vs. Class II boundary

The key differentiator is **severity of impact** from exploitation:

- Class I: cybersecurity weaknesses pose a risk, but not at critical infrastructure level
- Class II: exploitation could have serious impact on health, safety, or critical infrastructure

For CPS products, the practical heuristic: if the product is deployed in **critical infrastructure** (as defined by NIS2) or has **safety functions**, it is more likely Class II than Class I.

---

## 3 — Annex IV: Critical products with digital elements

Annex IV lists a narrow set of product categories where the highest assurance is required [F,90]:

- Hardware devices with security boxes (HSMs, smart cards, secure elements) used as a root of trust
- Smart meter gateways in advanced metering infrastructure (and embedded software)
- Other products where implementing acts may extend the list

**Note:** Annex IV is a short list. Most CPS products will fall under Default, Class I, or Class II — not Critical. The Critical tier primarily targets the security primitive components that other products rely upon [S,85].

---

## 4 — Decision algorithm

Apply the following steps in order to classify a product with digital elements:

```
Step 1: Is it a product with digital elements?
        (Article 3(1): any software or hardware product and its remote data
        processing solutions, including software/hardware components placed
        on the market separately)
        │
        ├── NO → CRA not applicable. Stop.
        │
        └── YES ↓

Step 2: Does it have network connectivity (intended or reasonably foreseeable)?
        (Article 3(1): includes direct or indirect logical or physical
        data connections to a device or network)
        │
        ├── NO → CRA not applicable. Stop.
        │
        └── YES ↓

Step 3: Is it listed in Annex IV (Critical)?
        │
        ├── YES → Classification: CRITICAL
        │         Conformity: Module B+C or Module H
        │         Notified body: Required
        │         Stop.
        │
        └── NO ↓

Step 4: Is it listed in Annex III Part II (Class II)?
        │
        ├── YES → Classification: CLASS II
        │         Conformity: Module B+C or Module H
        │         Notified body: Required
        │         Stop.
        │
        └── NO ↓

Step 5: Is it listed in Annex III Part I (Class I)?
        │
        ├── YES → Classification: CLASS I
        │         Conformity: Module A if hEN applied and covers all
        │                     Annex I requirements;
        │                     otherwise Module B+C or Module H
        │         Notified body: Only if hEN not applied
        │         Stop.
        │
        └── NO ↓

Step 6: Classification: DEFAULT
        Conformity: Module A (internal)
        Notified body: Not required
```

**Important:** Evaluate against the **intended and reasonably foreseeable** use. A product designed without network connectivity but that is reasonably foreseeable to be connected (e.g., via USB, serial-to-Ethernet converter) may still be in scope [S,80].

---

## 5 — Classification by CPS product type

### 5.1 Programmable Logic Controllers (PLCs)

| Product characteristic | Likely classification | Rationale |
|-----------------------|----------------------|-----------|
| Standard PLC with Ethernet connectivity | Class I [S,80] | IACS component — Annex III Part I |
| Safety PLC (SIL-rated) | Class II [S,80] | Safety function + IACS — likely Annex III Part II |
| PLC deployed in critical infrastructure (NIS2 essential entity) | Class II [S,80] | IACS in critical infrastructure — Annex III Part II |

### 5.2 Industrial gateways

| Product characteristic | Likely classification | Rationale |
|-----------------------|----------------------|-----------|
| Protocol converter (e.g., Modbus-TCP to OPC UA) | Class I [S,80] | IACS network component |
| IoT gateway in critical infrastructure | Class II [S,80] | Industrial IoT in critical infrastructure |
| Gateway with firewall / IDS function | Class II [S,80] | Firewall/IDS for industrial use — Annex III Part II |

### 5.3 Safety controllers

| Product characteristic | Likely classification | Rationale |
|-----------------------|----------------------|-----------|
| Safety relay with network diagnostics | Class I [S,80] | IACS component with safety function |
| Networked safety controller (SIL 2/3) | Class II [S,80] | Robot/machinery safety component — Annex III Part II |

### 5.4 Human-Machine Interfaces (HMIs)

| Product characteristic | Likely classification | Rationale |
|-----------------------|----------------------|-----------|
| Basic HMI panel with Ethernet | Class I [I,75] | IACS component; risk depends on function |
| HMI with embedded browser and remote access | Class I [S,80] | Embedded browser and IACS functions |
| Safety HMI (SIL-rated display) | Class II [I,75] | Safety function — likely Annex III Part II |

### 5.5 Sensors and actuators

| Product characteristic | Likely classification | Rationale |
|-----------------------|----------------------|-----------|
| Simple networked sensor (temperature, pressure) | Default [I,75] | Not specifically listed in Annex III/IV |
| Smart sensor with embedded processing and safety function | Class I [S,80] | IACS component |
| Robot sensing/actuator with safety function | Class II [S,80] | Robot safety component — Annex III Part II |

---

## 6 — CPS-specific considerations

### 6.1 Safety-relevant products

Products that perform a **safety function** (as defined under Machinery Regulation or IEC 61508) are more likely to be Class I or Class II [I,75]:

- Safety functions create a higher impact from cybersecurity compromise (integrity/availability attacks could cause physical harm)
- The CRA classification reflects this — Annex III Part II specifically includes products subject to safety requirements
- Dual assessment is required: Machinery Regulation conformity (safety) AND CRA conformity (cybersecurity) run independently

### 6.2 Multi-function products

If a product has multiple functions spanning different classification categories:

- The **highest applicable classification** applies to the entire product [S,85]
- Example: a gateway with both protocol conversion (Class I) and firewall function (Class II) is classified as Class II

### 6.3 Components vs. complete systems

- A **component** placed on the market separately (e.g., a safety controller sold as a standalone product) is classified individually
- A component integrated into a **larger system** and not placed on the market separately may be covered by the system manufacturer's assessment
- For CPS integrators: verify with component suppliers that their CRA obligations are met, or assume responsibility

### 6.4 Open-source components

- Open-source software placed on the market as part of a commercial product: the **product manufacturer** bears the CRA obligations, not the open-source project
- Open-source stewards (as defined in CRA Article 3) have limited obligations (security policy, cooperation with market surveillance)
- Include all open-source components in the SBOM regardless

---

## Cross-references

- `docs/compliance/cra-chapter-iv-implementation.md` — conformity assessment procedures per classification tier
- `docs/compliance/cra-sbom-requirements.md` — SBOM obligations apply to all tiers
- `docs/compliance/hEN-tracker.md` — hEN availability determines Module A eligibility for Class I
- `docs/compliance/conformity-assessment-guide.md` — Section C (CRA classification for CPS products)
- `docs/compliance/regulatory-mapping.md` — cross-framework mapping including CRA classification

---

*Classification tiers [F,90]. Annex III/IV lists are exhaustive [F,90]. Product-specific classification [S,80]. CPS product examples [I,75]. Verify specific product classification against official Annex III/IV text.*
