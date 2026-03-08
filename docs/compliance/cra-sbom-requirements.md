# CRA SBOM Requirements

**Date:** 2026-03-08
**Regulation:** Cyber Resilience Act (EU 2024/2847), Annex I Part II Section 1
**Status:** DRAFT — SBOM format requirements await CRA implementing acts. Verify against current official text.

---

## Confidence notes

The CRA mandates an SBOM as part of technical documentation [F,90]. Specific format requirements (CycloneDX vs. SPDX, minimum fields) are subject to implementing acts and potential harmonised standards — treat format guidance here as best-practice alignment pending final requirements [S,80]. Retention period of 10 years derives from CRA technical documentation retention obligations [S,85].

---

## 1 — Legal basis

**CRA Annex I Part II Section 1** requires manufacturers to:

> "identify and document vulnerabilities and components contained in the product, including by drawing up a software bill of materials in a commonly used and machine-readable format covering at the very least the top-level dependencies of the product." [F,90]

This SBOM must be:

- Part of the **technical documentation** (CRA Annex VII)
- Made available to market surveillance authorities upon request
- Updated when components change

The SBOM is **not** required to be made publicly available — it is part of the confidential technical documentation [F,90]. However, vulnerability information derived from the SBOM feeds into the manufacturer's coordinated vulnerability disclosure obligations.

---

## 2 — Format requirements

### 2.1 Accepted formats

Pending CRA implementing acts on specific format requirements [S,80], align with industry-standard machine-readable formats:

| Format | Version | Status | Notes |
|--------|---------|--------|-------|
| **CycloneDX** | 1.5+ | Recommended [S,80] | OWASP standard; strong vulnerability correlation; supports VEX |
| **SPDX** | 2.3+ | Recommended [S,80] | Linux Foundation / ISO/IEC 5962:2021; strong license analysis |

**Guidance:** Choose one format and apply it consistently across all products. CycloneDX is generally better suited for vulnerability management workflows; SPDX has stronger pedigree for license compliance. Either is acceptable pending implementing acts.

### 2.2 Machine-readable requirement

The CRA explicitly requires a **machine-readable** format [F,90]. This means:

- JSON or XML serialisation (not PDF, not plain text tables)
- Parseable by automated tools without manual intervention
- Structured according to the chosen format's schema

---

## 3 — Required fields

At minimum, the SBOM should contain the following for each component [S,80]:

| Field | Description | Required by CRA | Best practice |
|-------|------------|-----------------|---------------|
| **Component name** | Canonical name of the software component | Yes (implied) | Use upstream project name |
| **Component version** | Exact version string | Yes (implied) | Semantic versioning preferred |
| **Supplier / Author** | Entity that produced the component | Yes (implied) | Include contact or URL |
| **License** | SPDX license identifier | Not explicit in CRA | Include for completeness |
| **Dependency tree** | Relationship between components (direct, transitive) | Yes ("top-level dependencies" minimum) | Include full transitive tree |
| **Known vulnerabilities** | CVE references for known vulnerabilities at time of generation | Yes (implied by vulnerability identification obligation) | Use VEX for status annotation |
| **Package URL (purl)** | Canonical component identifier | Not explicit in CRA | Strongly recommended for tooling interop |
| **Hash / checksum** | Integrity verification of component | Not explicit in CRA | SHA-256 minimum |
| **CPE / SWID** | Alternative identifiers for vulnerability correlation | Not explicit in CRA | Include where available |

### 3.1 CRA "top-level dependencies" minimum

The CRA text specifies "at the very least the top-level dependencies" [F,90]. Best practice is to include **all transitive dependencies** — top-level only is the regulatory minimum but is insufficient for effective vulnerability management. For CPS products with safety implications, incomplete dependency information creates unacceptable risk.

---

## 4 — Generation timing

### 4.1 CI/CD integration

Generate the SBOM **at build time** as part of the CI/CD pipeline [S,85]:

- Trigger: every production build that produces a releasable artifact
- Method: integrate SBOM generation tooling into the build pipeline (not as a separate manual step)
- Output: SBOM artifact co-located with the build artifact, signed

### 4.2 Regeneration requirements

Regenerate the SBOM when:

- Any component (direct or transitive dependency) is added, removed, or updated
- A security patch is applied
- The product version changes

**Timeline:** Regenerate within **24 hours** of a component change for products already on the market [S,80]. For products in development, generate at each build.

### 4.3 Firmware and embedded considerations

For CPS products with firmware:

- Include the RTOS or bare-metal runtime components
- Include bootloader components
- Include any pre-compiled binary blobs with supplier attribution
- For hardware-software integrated components (e.g., FPGA bitstreams), document as components with version tracking even if not traditional software packages

---

## 5 — Validation checklist

Before accepting an SBOM as release-quality evidence:

- [ ] **All direct dependencies** listed with name, version, supplier
- [ ] **All transitive dependencies** listed (not just top-level)
- [ ] **No gaps:** every binary component in the shipped product traces to an SBOM entry
- [ ] **Signed:** SBOM is cryptographically signed by the build pipeline (not an individual)
- [ ] **Machine-readable:** validates against CycloneDX or SPDX schema
- [ ] **Vulnerability scan:** SBOM has been correlated against current vulnerability databases (NVD, OSV)
- [ ] **VEX document:** vulnerability exploitability assessment completed for any known CVEs
- [ ] **Version match:** SBOM version identifier matches the product release version
- [ ] **Timestamp:** generation timestamp present and matches build timestamp
- [ ] **Reproducible:** regenerating from the same source/build produces an equivalent SBOM

---

## 6 — Retention

### 6.1 Retention period

**governance_10y** — retain SBOMs for **10 years** after the last unit of the product version is placed on the EU market [S,85].

**Rationale:** CRA requires technical documentation (which includes the SBOM) to be kept at the disposal of market surveillance authorities for 10 years after the product is placed on the market. This aligns with Machinery Regulation technical documentation retention.

Do **not** use the `ci_3y` retention tier. While CI build artifacts may use shorter retention, the SBOM is a regulatory document, not merely a build artifact.

### 6.2 Retention of historical SBOMs

Retain the SBOM for **every released product version**, not just the current version. Market surveillance may request the SBOM for any version that was placed on the market within the 10-year window.

---

## 7 — Storage and evidence pipeline

### 7.1 Storage path convention

Follow the evidence pipeline path convention:

```
evidence/
└── {product-id}/
    └── {version}/
        └── sbom/
            ├── {product-id}-{version}-sbom.cdx.json       # CycloneDX
            ├── {product-id}-{version}-sbom.cdx.json.sig   # Signature
            ├── {product-id}-{version}-vex.cdx.json        # VEX (if applicable)
            └── sbom-validation-report.json                 # Validation results
```

### 7.2 Integration with evidence pipeline

- SBOM generation is a **pipeline stage**, not a manual upload
- The signed SBOM artifact is stored in the evidence repository alongside other compliance evidence
- The SBOM feeds into the vulnerability management process (continuous monitoring)
- Cross-reference the SBOM in the CRA Annex I Part II compliance matrix in the technical documentation

---

## 8 — Versioning

### 8.1 SBOM version tracking

- The SBOM version **tracks the product version**: product v2.3.1 → SBOM for v2.3.1
- If a component is updated without a product version change (e.g., emergency patch), create a new SBOM with a build identifier suffix (e.g., v2.3.1+build.42)
- The SBOM metadata must include the product version it corresponds to

### 8.2 Differential tracking

For audit and vulnerability management purposes, maintain the ability to diff SBOMs between product versions to identify:

- Newly added components
- Removed components
- Version changes in existing components
- New or resolved vulnerabilities

---

## 9 — Tools (awareness, not endorsement)

The following tools can generate SBOMs in CRA-compatible formats. This list is for awareness only — evaluate fitness for your specific toolchain [I,70]:

**CycloneDX ecosystem:**
- `cyclonedx-cli` — validation and conversion
- `cdxgen` — multi-language SBOM generator
- Language-specific plugins: `cyclonedx-maven-plugin`, `cyclonedx-python`, `cyclonedx-node-module`

**SPDX ecosystem:**
- `spdx-sbom-generator` — multi-language SBOM generator
- `tools-python` — SPDX Python library for parsing and validation

**Multi-format:**
- `syft` (Anchore) — generates both CycloneDX and SPDX
- `trivy` (Aqua Security) — vulnerability scanning with SBOM generation

**For embedded/firmware:**
- Manual component inventory may be necessary for binary blobs, RTOS components, and proprietary libraries where automated scanning is insufficient
- Supplement automated generation with a manual review for completeness

---

## Cross-references

- `docs/compliance/conformity-assessment-guide.md` — Section 5 (Cybersecurity Evidence) for SBOM placement in technical documentation
- `docs/compliance/cra-chapter-iv-implementation.md` — SBOM as part of notified body submission package
- `docs/compliance/cra-product-classification.md` — classification determines conformity route, which affects SBOM scrutiny level
- `docs/compliance/regulatory-mapping.md` — SBOM in the shared evidence catalogue
- `docs/evidence/cps-evidence-types.md` — evidence type definitions and retention tiers

---

*SBOM obligation [F,90]. Format requirements pending implementing acts [S,80]. Retention period 10 years [S,85]. Tool recommendations [I,70]. Verify CRA implementing acts when published for binding format requirements.*
