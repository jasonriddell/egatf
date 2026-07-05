# Diagnostic Knowledge Patterns

**Document type:** Framework detail  
**Status:** Draft v0.7  
**Repository path:** `framework/diagnostic-knowledge-patterns.md`

---

## Purpose

Diagnostic Knowledge Patterns are reusable descriptions of previously understood issue patterns.

They are intended to act as a **Knowledge source** inside EGATF without becoming brittle command snippets, one-off `rg` searches, or bundle-version-specific parsing logic.

A Diagnostic Knowledge Pattern should describe:

- What kind of issue pattern has been seen before.
- What semantic observations would support it.
- What observations would contradict it.
- What evidence is commonly missing.
- Which versions, components, and deployment types it may apply to.
- Which reference knowledge sources must be validated.
- Which challenge questions must be asked before the pattern can influence Judgment.

A pattern should not declare root cause by itself.

It should help produce a candidate **Insight** that must still pass through **Challenge** before it can become **Judgment**.

---

## One-Line Definition

A Diagnostic Knowledge Pattern is a reusable, version-aware description of an issue pattern expressed in terms of semantic observations, evidence requirements, contradictions, and challenge criteria.

---

## Placement in EGATF

Diagnostic Knowledge Patterns are used in the **Reasoning Loop**.

```text
Evidence Loop
    ↓ produces
Information
    ↓ combined with
Knowledge sources, including Diagnostic Knowledge Patterns
    ↓ suggests
Insight
    ↓ tested by
Challenge
    ↓ may become
Judgment
```

The pattern is a Knowledge source.

It is not itself evidence, insight, judgment, or diagnosis.

---

## Design Goal

The pattern language should be:

- Human-readable.
- Machine-parseable.
- Version-aware.
- Evidence-grounded.
- Expandable.
- Abstract enough to survive support bundle format changes.
- Separated from command-level matching logic.

The most important design principle is:

> Describe what must be true, not how to grep for it.

---

## What Not To Do

Avoid patterns that are just command wrappers.

Bad example:

```yaml
bad_example:
  command: rg "Leader not ready|No leader|Not the leader" */yb-tserver*.log
```

This is brittle because it depends on:

- Current log wording.
- Current file layout.
- Current support bundle format.
- Current parser assumptions.
- A specific search tool.

It also encourages people to treat text matches as diagnosis.

---

## Preferred Approach

Use semantic observations.

Better example:

```yaml
pattern:
  evidence_requirements:
    required:
      - kind: client.timeout_increase
        evidence_class: extracted_or_correlated
        time_relation: during_impact_window

      - kind: raft.leader_instability
        evidence_class: extracted_or_derived
        time_relation: overlaps_or_precedes:client.timeout_increase
```

This describes the evidence needed to support a candidate insight without specifying how that evidence must be extracted.

The extraction logic belongs in an adapter layer.

---

## Three-Layer Model

Diagnostic Knowledge Patterns should be separated into three layers.

```text
Diagnostic Knowledge Pattern
    ↓ uses
Semantic Observation Vocabulary
    ↓ produced by
Versioned Adapters and Evidence Preparation Tools
```

### 1. Diagnostic Knowledge Pattern Layer

This layer describes reusable issue knowledge.

It includes:

- Summary.
- Applies-to metadata.
- Required observations.
- Optional observations.
- Contradicting evidence.
- Missing evidence.
- Time relationships.
- Knowledge source validation requirements.
- Challenge questions.
- Confidence model.
- Permitted candidate insight wording.
- Explicitly disallowed conclusion wording.

This layer should not contain `rg`, SQL, DuckDB, jq, JSONPath, or parser-specific logic.

### 2. Semantic Observation Vocabulary Layer

This layer defines stable observation names.

Examples:

```text
client.timeout_increase
raft.leader_instability
tablet.leaderless
tablet.under_replicated
node.disk_latency_increase
node.cpu_saturation
```

The vocabulary gives tools and AI a stable language for evidence.

The same semantic observation may be produced from different sources in different versions of support bundles.

### 3. Adapter Layer

This layer maps actual source material into semantic observations.

Examples:

- DuckDB query over `wtl` parquet output.
- SQLite query over tablet report parser output.
- JSON parser for support bundle schema version 1.x.
- Version-specific log parser.
- Manual analyst observation.
- AI-assisted extraction with human review.

Adapters may contain commands, SQL, regex, JSON paths, and parser-specific details.

Patterns should not.

---

## Recommended File Extension

Use:

```text
.dkp.yaml
```

Example:

```text
knowledge-patterns/ybdb.raft.leader-instability.client-timeouts.dkp.yaml
```

---

## Minimum Useful Pattern Structure

```yaml
schema_version: "0.1"
kind: diagnostic_knowledge_pattern

id:
title:
status:
owner:
last_reviewed:

applies_to:
  product:
  components:
  versions:
  deployment:

summary:
  one_line:
  description:

reported_context:
  useful_clues:
  anchoring_warning:

evidence_requirements:
  required:
  optional:

contradicting_evidence:

missing_evidence:

time_relationships:

knowledge_sources:

challenge_questions:

confidence_model:

outputs:
  possible_insight:
  not_allowed_as_conclusion:
```

---

## Required Concepts

### Semantic Observation

A stable, abstract observation kind.

Example:

```text
raft.leader_instability
```

This should remain stable even if log formats, support bundle layouts, or extraction tools change.

### Evidence Requirement

A semantic observation required or useful for the pattern.

Example:

```yaml
- id: e1
  kind: raft.leader_instability
  evidence_class: extracted_or_derived
  time_relation: during_or_before_impact_window
```

### Contradicting Evidence

Evidence that weakens or disproves the pattern.

Example:

```yaml
- kind: stable_leadership_during_impact
  meaning: If leadership was stable during the impact window, this pattern is weakened.
```

### Missing Evidence

Evidence that is required to safely accept or reject the pattern but is currently absent.

Example:

```yaml
- kind: time_aligned_tablet_state
  impact: Without time-aligned tablet state, collection-time tablet reports cannot prove historical tablet state.
```

### Knowledge Source Validation

A requirement that reference knowledge must apply to the product version and context under investigation.

Example:

```yaml
knowledge_sources:
  required_validation:
    - type: documentation
      requirement: Must apply to the collected YBDB version.
    - type: source_code
      requirement: Must match or be compatible with the collected YBDB version.
```

### Candidate Insight

A pattern may suggest a candidate insight.

It must not assert final diagnosis.

Example:

```yaml
outputs:
  possible_insight: >
    Client-visible timeouts are consistent with raft leader instability affecting
    tablets involved in the impacted workload.
  not_allowed_as_conclusion: >
    Raft leader instability caused the incident.
```

---

## Relationship to Insight, Challenge, and Judgment

Diagnostic Knowledge Patterns support candidate insight generation.

They do not bypass Challenge.

```text
Pattern matched or partially matched
    ↓
Candidate Insight generated
    ↓
Challenge asks whether the pattern really applies
    ↓
Judgment only if confidence is sufficient
```

A pattern match should be treated as:

```text
This issue may be consistent with a known pattern.
```

Not:

```text
This issue is caused by this pattern.
```

---

## Confidence Handling

A pattern should include a confidence model, but confidence is still evaluated during Challenge.

Recommended confidence labels:

```text
Low
Medium
High
```

A pattern should define:

- What is required for High confidence.
- What allows only Medium confidence.
- What forces Low confidence.
- What conditions reject the pattern.

Example:

```yaml
confidence_model:
  high:
    requires:
      - required_observations_present
      - timeline_order_confirmed
      - time_windows_compatible
      - knowledge_sources_validated
      - no_stronger_alternative
  medium:
    allows:
      - incomplete_metric_coverage
      - partial_time_overlap
      - some_non_blocking_missing_evidence
  low:
    if:
      - collection_time_snapshot_used_for_historical_window
      - stronger_alternative_exists
      - required_observation_missing
```

---

## Reference Knowledge Source Validation

Patterns should not blindly trust documentation, source code, or previous issues.

Each knowledge source should be validated against:

- Product version.
- Component.
- Deployment type.
- Feature flags or configuration.
- Known fixed versions.
- Known affected versions.
- Source authority.
- Date last reviewed.

This prevents wrong-version knowledge from producing false confidence.

---

## Relationship to Existing Formats

Several existing formats are adjacent but not sufficient on their own.

| Format | Useful idea | Limitation for EGATF |
|---|---|---|
| Sigma | Simple YAML-style detection rules | Too detection/query oriented for diagnostic reasoning. |
| STIX | Object and relationship modeling | Too cybersecurity/threat-intel oriented and heavy. |
| SARIF | Structured result reporting | Better for tool output than reusable diagnostic knowledge. |
| OCSF | Taxonomy and schema discipline | Cybersecurity-event focused rather than support diagnosis focused. |

EGATF Diagnostic Knowledge Patterns should borrow from these ideas but remain focused on support diagnosis and evidence-grounded reasoning.

---

## Validation Questions

When reviewing a Diagnostic Knowledge Pattern, ask:

1. Is it abstract enough to survive support bundle format changes?
2. Does it use semantic observations rather than command matches?
3. Are required observations clear?
4. Are contradictions clear?
5. Are missing evidence conditions clear?
6. Are version applicability rules explicit?
7. Are knowledge sources validated?
8. Does the pattern avoid declaring root cause?
9. Does it generate a candidate insight suitable for Challenge?
10. Can adapters be changed without changing the pattern?

---

## Open Questions

1. Should Diagnostic Knowledge Patterns be stored as YAML only, or compiled to JSON?
2. Should semantic observations have their own formal schema?
3. Should adapters be part of EGATF or a separate tooling project?
4. Should patterns support inheritance or composition?
5. How should pattern review and expiry work?
6. How should conflicting patterns be handled?
7. Should confidence scoring be standardized across patterns?
8. How should AI-generated pattern suggestions be reviewed?
9. Should previous case studies generate new patterns automatically?
10. How should sensitive customer-specific details be excluded from reusable patterns?
