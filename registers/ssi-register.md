# Safety-Security Interaction Register

**Owner:** Safety Manager + OT Security Lead (joint)
**Review cycle:** Quarterly + after any safety or security change
**Last reviewed:** YYYY-MM-DD

## Interaction types reference

| Type | Direction | Description |
|------|-----------|-------------|
| SS-1 | Security → Safety | Security failure directly causes safety hazard |
| SS-2 | Security → Safety | Attack disables/degrades safety function |
| SS-3 | Safety → Security | Safety mechanism creates exploitable vulnerability |
| SS-4 | Safety → Security | Safety constraint prevents security control |
| SS-5 | Bidirectional | Conflicting requirements on same component |
| SS-6 | Bidirectional | Shared resource contention (CPU, bandwidth) |
| SS-7 | Bidirectional | Change coupling (patching one breaks the other) |

## Register

| ID | Type | Safety element | Security element | Consequence | Severity | Resolution | Status |
|----|------|---------------|-----------------|-------------|----------|-----------|--------|
| SSI-1 | [Populate] | H-n / SF-n | T-n / Z-n | [Physical outcome] | | [Approach] | Open |

## Joint requirements (derived from SSI analysis)

| ID | Requirement | Safety rationale | Security rationale | From SSI | Verified? |
|----|------------|-----------------|-------------------|---------|-----------|
| JSSR-1 | [Populate] | | | SSI-n | |

## Conflict resolution log

| SSI | Conflict | Resolution | Residual risk | Safety sign-off | Security sign-off | Date |
|-----|---------|-----------|---------------|----------------|-------------------|------|
| | | | | | | |

## Review log

| Date | Safety reviewer | Security reviewer | Changes | Next review |
|------|----------------|-------------------|---------|-------------|
| YYYY-MM-DD | [Name] | [Name] | Initial creation | +3 months |
