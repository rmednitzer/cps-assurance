# Schema-Register-Column Mapping

Canonical mapping between JSON schema properties (in `schemas/`), Markdown register table columns (in `registers/`), and template fields (in `templates/`) for each entity type. Common properties inherited from `schemas/common.schema.json` apply to all entity types.

---

## Common properties (all entity types)

Source: `schemas/common.schema.json`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `{PREFIX}-\d+` per entity type |
| `object_type` | Yes | (implicit in register) | (implicit) | Enum constant per entity type |
| `title` | No | (varies by register) | (varies) | Human-readable name |
| `status` | Yes | Status | Status | Enum: `draft`, `in_review`, `verified`, `accepted`, `retired` |
| `owner` | Yes | Owner | Owner | Single accountable person/role |
| `review_cycle` | No | (register header) | (header) | Enum: `annual`, `quarterly`, `monthly`, `on_change`, `on_incident`, `none` |
| `links.mitigated_by` | No | (embedded in other columns) | (cross-ref) | Array of SF-n references |
| `links.constrained_by` | No | (embedded in other columns) | (cross-ref) | Array of SC-n references |
| `links.interacts_with` | No | (embedded in other columns) | (cross-ref) | Array of SSI-n references |
| `links.related_to` | No | (not a standard column) | (free-form) | Array of any ID |
| `provenance.basis` | Yes (within provenance) | (inline notation) | (inline) | Pattern: `[F,90]`, `[S,80]`, `[I,70]` etc. |
| `provenance.verified_on` | No | (inline or review log) | (review log) | ISO 8601 date |

---

## L-n: Loss

Source: `schemas/loss-entry.schema.json` — Register: `registers/hazard-register.md` (Losses table) — Template: `templates/hazard-analysis/TEMPLATE-hazard-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^L-\d+$` |
| `object_type` | Yes | (implicit — "loss") | (implicit) | Const: `loss` |
| `description` | Yes | Loss description | Loss description | Free text |
| `category` | Yes | Category | Category | Enum: `personnel_safety`, `environmental`, `property_mission`, `operational`, `reputational` |
| `severity` | No | (not in loss table; used in hazard table) | (not in loss template) | Enum: `catastrophic`, `critical`, `marginal`, `negligible` |

---

## H-n: Hazard

Source: `schemas/hazard-entry.schema.json` — Register: `registers/hazard-register.md` (Hazards table) — Template: `templates/hazard-analysis/TEMPLATE-hazard-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^H-\d+$` |
| `object_type` | Yes | (implicit — "hazard") | (implicit) | Const: `hazard` |
| `losses` | Yes | Losses | Losses | Array of L-n; min 1 item |
| `safety_functions` | Yes | Safety function(s) | Safety function(s) | Array of SF-n |
| `severity` | No | Severity | Severity | Enum: `Catastrophic`, `Critical`, `Marginal`, `Negligible` |
| `exposure` | No | Exposure | Exposure | Enum: `Frequent`, `Probable`, `Occasional`, `Remote`, `Improbable` |
| `avoidability` | No | Avoidability | Avoidability | Enum: `Impossible`, `Difficult`, `Possible` |

Register-only columns not in schema:

| Register column | Notes |
|----------------|-------|
| Hazard description | Carried in `title` (common) or as free text; not a dedicated schema property |
| SIL/PL target | Derived from severity/exposure/avoidability; not a schema property on H-n — lives on SF-n instead |
| SSI-relevant? | Derived from SSI register cross-reference; not a schema property |

---

## SF-n: Safety Function

Safety functions are defined in the hazard register (Safety functions table) and the hazard entry template. There is no dedicated `sf-entry.schema.json` — safety function data is embedded in the hazard register.

| Register column | Template field | Notes |
|----------------|----------------|-------|
| ID | ID | Pattern: SF-n |
| Name | Name | Human-readable function name |
| Mitigates | Mitigates | H-n reference(s) |
| SIL/PL | SIL/PL | Target integrity level |
| Demand mode | Demand mode | Low demand / High demand / Continuous |
| Process safety time | Process safety time | In ms; maps to `process_safety_time_ms` on SC-n |
| Sample period | Sample period | In ms; maps to `sample_period_ms` on SC-n |
| End-to-end latency budget | End-to-end latency budget | In ms; maps to `latency_budget_ms` on SC-n |
| Jitter budget | Jitter budget | In ms; maps to `jitter_budget_ms` on SC-n |
| Safe state | Safe state | Description of safe state |
| Degraded mode trigger | Degraded mode trigger | Condition that triggers degraded mode |
| Actuator authority limit | Actuator authority limit | Maps to `actuator_authority_limit` on SC-n |
| Zone | Zone | Z-n reference — which zone this SF resides in |

Note: SF-n numeric contract fields are authoritatively captured on the corresponding SC-n entries, where they are schema-validated. The SF table in the hazard register provides a summary view.

---

## UCA-n: Unsafe Control Action

Source: `schemas/uca-entry.schema.json` — Register: `registers/hazard-register.md` (UCAs table) — Template: `templates/hazard-analysis/TEMPLATE-hazard-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^UCA-\d+$` |
| `object_type` | Yes | (implicit — "uca") | (implicit) | Const: `uca` |
| `control_action` | Yes | Control action | Control action | Name of the control action being analysed |
| `uca_type` | Yes | Type | Type | Enum: `not_provided`, `provided_incorrectly`, `wrong_timing_order`, `applied_too_long_stopped_too_soon` |
| `description` | Yes | Description | Description | Free text describing the unsafe control action |
| `hazards` | Yes | Hazard(s) | Hazard(s) | Array of H-n; min 1 item |
| `safety_functions` | No | (not a standard register column) | (not in register) | Array of SF-n — which safety functions address this UCA |

Register-only columns not in schema:

| Register column | Notes |
|----------------|-------|
| SSI-relevant? | Derived from SSI analysis; not a schema property — indicates whether a security threat could cause this UCA |

---

## SC-n: Safety Constraint

Source: `schemas/safety-constraint-entry.schema.json` — Register: `registers/safety-constraint-register.md` — Template: `templates/safety-constraints/TEMPLATE-safety-constraint-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^SC-\d+$` |
| `object_type` | Yes | (implicit — "safety_constraint") | (implicit) | Const: `safety_constraint` |
| `derived_from` | Yes | Derived from | Derived from | Array of UCA-n / H-n / SF-n references |
| `applies_to` | Yes | Applies to | Applies to | Array of SF-n / Z-n / CO-n references |
| `process_safety_time_ms` | No | Numeric contract (PST) | PST | Milliseconds |
| `sample_period_ms` | No | Numeric contract (sample period) | Sample period | Milliseconds |
| `latency_budget_ms` | No | Numeric contract (latency) | Latency budget | Milliseconds |
| `jitter_budget_ms` | No | Numeric contract (jitter) | Jitter budget | Milliseconds |
| `stale_data_timeout_ms` | No | Numeric contract (stale data) | Stale data timeout | Milliseconds |
| `watchdog_threshold_cycles` | No | Numeric contract (watchdog) | Watchdog threshold | Integer >= 1 |
| `actuator_authority_limit` | No | Numeric contract (authority) | Authority limit | Free text (units vary) |
| `verification_method` | Yes | Verification method | Verification method | Test / analysis / inspection |
| `platform_controls` | No | (not a standard column) | (cross-ref) | Array of CTL-nnnn references to platform-assurance |

Register-only columns not in schema:

| Register column | Notes |
|----------------|-------|
| Constraint | Free text description; carried in `title` (common) |
| Owner | Inherited from common schema |
| Status | Inherited from common schema |

Note: The register column "Numeric contract" is a composite column packing multiple schema properties (PST, sample period, latency, jitter, watchdog, authority) into a single cell. In machine-readable records, use the individual schema properties.

---

## T-n: Threat

Source: `schemas/threat-entry.schema.json` — Register: `registers/threat-register.md` — Template: `templates/threat-model/TEMPLATE-threat-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^T-\d+$` |
| `object_type` | Yes | (implicit — "threat") | (implicit) | Const: `threat` |
| `stride` | Yes | STRIDE | STRIDE | Enum: `Spoofing`, `Tampering`, `Repudiation`, `Information disclosure`, `Denial of service`, `Elevation of privilege` |
| `entry_point` | Yes | Entry point | Entry point | Interface or conduit name |
| `zones` | No | Affected assets/zones | Zones / conduits | Array of Z-n references |
| `conduits` | No | Affected assets/zones | Zones / conduits | Array of CO-n references |
| `safety_links` | No | (embedded in threat template) | Safety relevance | Array of H-n / SF-n / SSI-n references |
| `physical_consequence` | Yes | Physical consequence | Physical consequence | Free text |

Register-only / template-only columns not in schema:

| Register/template column | Notes |
|-------------------------|-------|
| Threat (title) | Carried in `title` (common) |
| Preconditions | Template-only; not a schema property |
| Affected assets | Template-only; asset inventory reference |
| Existing controls | Register column; not a schema property |
| Required level | Register column (SL-T / JSSR reference) |
| Required controls | Template-only |
| Verification | Template-only |
| Status | Inherited from common schema |

---

## Z-n: Zone

Source: `schemas/zone-entry.schema.json` — Register: `registers/zone-conduit-register.md` (Zones table) — Template: `templates/zone-conduit/TEMPLATE-zone-conduit-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^Z-\d+$` |
| `object_type` | Yes | (implicit — "zone") | (implicit) | Const: `zone` |
| `purdue_level` | Yes | Purdue level | Purdue level | Integer 0-5 |
| `safety_functions` | No | Safety functions | Safety functions | Array of SF-n references |
| `sl_t` | Yes | SL-T | SL-T | Integer 0-4 |
| `physical_access_control` | No | (not a standard column) | (detailed record) | Free text |
| `platform_controls` | No | (not a standard column) | (cross-ref) | Array of CTL-nnnn |

Register-only columns not in schema:

| Register column | Notes |
|----------------|-------|
| Zone name | Carried in `title` (common) |
| Assets | Asset inventory; not a schema property |
| SL-C | Capability security level — assessed per component; not a schema property |
| SL-A | Achieved security level — measured; not a schema property |
| Gap | SL-T minus SL-A; computed, not stored |

Note: SL-C and SL-A are tracked in the register but not in the schema because they are assessment outputs, not design inputs. The schema captures the target (SL-T) as the authoritative design requirement.

---

## CO-n: Conduit

Source: `schemas/conduit-entry.schema.json` — Register: `registers/zone-conduit-register.md` (Conduits table) — Template: `templates/zone-conduit/TEMPLATE-zone-conduit-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^CO-\d+$` |
| `object_type` | Yes | (implicit — "conduit") | (implicit) | Const: `conduit` |
| `source_zone` | Yes | Zones connected (first) | Zones connected | Z-n reference (from) |
| `destination_zone` | Yes | Zones connected (second) | Zones connected | Z-n reference (to) |
| `direction` | Yes | Direction | Direction | Enum: `unidirectional`, `bidirectional` |
| `protocols` | No | Protocols | Protocols | Array of protocol names |
| `safety_impact` | No | Safety impact if failed | Safety impact if failed | Free text |

Register-only columns not in schema:

| Register column | Notes |
|----------------|-------|
| Protection | Firewall / data diode / VPN; not a schema property |
| Auth | Certificate / password / none; not a schema property |
| Monitoring | IDS / DPI / none; not a schema property |

---

## SSI-n: Safety-Security Interaction

Source: `schemas/ssi-entry.schema.json` — Register: `registers/ssi-register.md` — Template: `templates/safety-security-interaction/TEMPLATE-ssi-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^SSI-\d+$` |
| `object_type` | Yes | (implicit — "ssi") | (implicit) | Const: `ssi` |
| `interaction_type` | Yes | Type | Type | Enum: `SS-1` through `SS-7` |
| `safety_links` | Yes | Safety element | Safety side | Array of H-n / SF-n / UCA-n / SC-n references |
| `security_links` | Yes | Security element | Security side | Array of T-n / Z-n / CO-n references |
| `jssr_links` | No | (JSSR table cross-ref) | Joint requirement | Array of JSSR-n references |
| `physical_consequence` | Yes | Consequence | Physical consequence | Free text |
| `resolution` | Yes | Resolution | Resolution approach | Free text |

Register-only / template-only columns not in schema:

| Register/template column | Notes |
|-------------------------|-------|
| Severity | Register column; not a schema property |
| Status | Inherited from common schema |
| Timing/numeric contract touched | Template-only detail |
| Interaction mechanism | Template-only detail |
| Likelihood (unmitigated) | Template-only detail |
| Current mitigation | Template-only detail |
| Gap | Template-only detail |
| Verification | Template-only detail |
| Evidence | Template-only detail |
| Review trigger | Template-only detail |

---

## JSSR-n: Joint Safety-Security Requirement

Source: `schemas/jssr-entry.schema.json` — Register: `registers/ssi-register.md` (Joint requirements table) — Template: `templates/safety-security-interaction/TEMPLATE-ssi-entry.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^JSSR-\d+$` |
| `object_type` | Yes | (implicit — "jssr") | (implicit) | Const: `jssr` |
| `requirement` | Yes | Requirement | Requirement | Free text — specific, testable statement |
| `safety_rationale` | Yes | Safety rationale | Safety rationale | Why needed for safety |
| `security_rationale` | Yes | Security rationale | Security rationale | Why needed for security |
| `derived_from` | Yes | From SSI | Derived from | Array of SSI-n; min 1 item |
| `enforcer` | No | Enforcer | Enforcer | Who/what enforces this |
| `verification_method` | Yes | Verification | Verification | How compliance is demonstrated |
| `acceptance_criteria` | No | (not a standard column) | (detailed record) | Testable threshold |
| `evidence_type` | No | (not a standard column) | Evidence | Artifact type |

Register-only columns not in schema:

| Register column | Notes |
|----------------|-------|
| Verified? | Status indicator; maps to common `status` field |
| Status | Inherited from common schema |

---

## PROD-n: Product

Source: `schemas/product-entry.schema.json` — Register: `registers/product-register.md` — Template: `templates/product-certification/TEMPLATE-product-gap-assessment.md`

| Schema property | Required? | Register column | Template field | Notes |
|----------------|-----------|-----------------|----------------|-------|
| `id` | Yes | ID | ID | Pattern: `^PROD-\d+$` |
| `object_type` | Yes | (implicit — "product") | (implicit) | Const: `product` |
| `type` | Yes | Type | Type | Free text (Embedded/Gateway/Sensor/Actuator/Machine/Robot/IoT) |
| `role` | Yes | Role | Role | Enum: `manufacturer`, `authorised_rep`, `importer`, `distributor`, `operator` |
| `connectivity` | Yes | Connectivity | Connectivity | Enum: `wired`, `wireless`, `none`, `mixed` |
| `safety_relevant` | Yes | Safety-relevant | Safety-relevant | Boolean |
| `applicable_instruments` | No | (Regulatory applicability table) | Applicable directives | Array of directive/regulation names |
| `trace_links` | No | (Traceability manifest) | (cross-ref) | Array of L/H/SF/UCA/SC/T/Z/CO/SSI/JSSR-n references |

Register-only columns not in schema:

| Register column | Notes |
|----------------|-------|
| Product name | Carried in `title` (common) |
| Target market | Not a schema property |
| CRA class | Derived from assessment; not a schema property |
| hEN applied | Not a schema property |
| Conformity route | Not a schema property |
| NB engaged | Not a schema property |
| Assessment status | Maps to common `status` |
| DoC | Not a schema property |
| CE marked | Not a schema property |
| Support period start/end | Not schema properties |
| SBOM current | Not a schema property |
| CVD policy published | Not a schema property |
| ENISA reporting ready | Not a schema property |

Note: The product register contains significantly more operational and compliance-tracking columns than the schema captures. The schema defines the minimum machine-readable identity and classification; the register and template carry the full conformity assessment lifecycle state.
