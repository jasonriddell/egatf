# EGATF Investigation Thread Tracker

**Document type:** Research tracker  
**Status:** Active  
**Repository path:** `research/investigation-thread-tracker.md`

---

## Purpose

This tracker records investigation threads for the EGATF framework that are broader than the first case study.

These threads may influence future framework versions, tooling, schemas, validation methods, articles, or engineering proposals.

They should be tracked separately from `cases/001-template.md` so that important framework work is not lost while the first case study remains focused.

---

## Status Values

| Status | Meaning |
|---|---|
| Backlog | Important but not started. |
| Active | Currently being developed or discussed. |
| Blocked | Waiting on information, review, tooling, or decision. |
| Deferred | Useful but intentionally delayed. |
| Complete | Done for current framework version. |
| Superseded | Replaced by a later idea or decision. |

---

## Thread Summary

| ID | Thread | Loop / Stage | Status | Why it matters | Next step |
|---|---|---|---|---|---|
| T-001 | Three-loop operating model | All loops | Complete for v0.5 | Reframes EGATF from a straight chain into gated loops. | Validate through first case study. |
| T-002 | Judgment terminology | Reasoning Loop | Complete for v0.6 | Replaces Wisdom with a practical human accountability term. | Watch for remaining old terminology in new docs. |
| T-003 | Collection Context | Evidence Loop | Active | Prevents false correlations caused by support bundle timing confusion. | Test in synthetic support bundle case. |
| T-004 | Evidence Preparation taxonomy | Evidence Loop | Active | Separates transformation, extraction, derivation, and correlation. | Validate with wtl and tablet report parser examples. |
| T-005 | Cold and guided analysis isolation | Reasoning Loop | Active | Reduces anchoring bias and contamination between analysis passes. | Define sandbox rules and comparison output. |
| T-006 | Reference knowledge validation | Reasoning Loop | Active | Prevents wrong-version docs, code, or cases from supporting insights. | Add validation checklist and apply to first case study. |
| T-007 | Challenge confidence scoring | Reasoning Loop | Active | Determines whether insight can become Judgment. | Test Low / Medium / High and optional numeric scoring. |
| T-008 | Diagnostic Knowledge Patterns | Knowledge / Reasoning Loop | Active | Captures reusable previous issue patterns without brittle `rg` matching. | Review schema and create first pattern. |
| T-009 | Semantic Observation Vocabulary | Evidence / Knowledge bridge | Active | Provides stable observation names across bundle and tool versions. | Expand vocabulary from real cases. |
| T-010 | Adapter layer for tools | Evidence Preparation | Backlog | Maps bundle/tool outputs into semantic observations. | Define adapter examples for wtl and tablet report parser. |
| T-011 | Support bundle manifest improvements | Evidence Loop / Engineering | Active | Makes evidence packages self-describing for humans, tools, and AI. | Socialize Jira proposal. |
| T-012 | Case study template validation | All loops | Active | Tests whether EGATF is usable in practice. | Run first synthetic support bundle case. |
| T-013 | Publication strategy | Learning / External | Deferred | Determines when to publish article, whitepaper, or GitHub. | Wait until first case study is complete. |
| T-014 | Tooling strategy | Evidence Preparation / Knowledge | Deferred | Avoids building tools before framework stabilizes. | Revisit after 2 to 3 worked cases. |

---

## Active Thread Details

### T-003: Collection Context

**Loop / Stage:** Evidence Loop / Collection Context  
**Status:** Active

#### Question

How much collection context must an evidence package contain to prevent humans and AI from misinterpreting support bundle contents?

#### Current Position

Support bundles should include an Evidence Package Manifest that records bundle provenance, schema version, collector version, environment identity, component windows, metric collection context, component descriptions, and file index.

#### Risks

- Manifest becomes too large.
- AI guidance is mixed with operational metadata.
- Sensitive values are included accidentally.
- Component timing is wrong or incomplete.

#### Next Step

Use the first synthetic case study to show how Collection Context prevents false correlation between historical logs and collection-time tablet metadata.

---

### T-004: Evidence Preparation Taxonomy

**Loop / Stage:** Evidence Loop / Evidence Preparation  
**Status:** Active

#### Question

Can the framework clearly distinguish transformation, extraction, derivation, and correlation in real support tooling?

#### Current Position

- `wtl` is a Source Transformer / Log Structuring Tool.
- Tablet report parser is a hybrid Source Transformer + Derived Evidence Generator if it computes leaderless or under-replicated tablets.

#### Risks

- Tool categories feel too academic.
- Hybrid tools blur boundaries.
- Derived evidence is mistaken for direct evidence.

#### Next Step

Define example adapter outputs for `wtl` and tablet report parser.

---

### T-005: Cold and Guided Analysis Isolation

**Loop / Stage:** Evidence Loop / Reasoning Loop  
**Status:** Active

#### Question

How should cold and guided analysis be run so that guided context does not contaminate independent findings?

#### Current Position

Cold and guided analysis should run in isolated analysis sandboxes.

- Cold analysis sees collection context, raw source material, and prepared evidence, but not the reported causal framing.
- Guided analysis sees reported context as search guidance, but must treat causal claims as hypotheses.
- A comparison step identifies agreement, disagreement, surprises, and anchoring risk.

#### Risks

- Cold analysis still receives implicit clues from file names or support bundle scope.
- Guided analysis overfits to the reported issue.
- Comparison becomes subjective.

#### Next Step

Define sandbox rules and a comparison table for the case study template.

---

### T-006: Reference Knowledge Validation

**Loop / Stage:** Reasoning Loop / Knowledge  
**Status:** Active

#### Question

How should documentation, source code, bug reports, known issues, and previous cases be validated before they support an Insight?

#### Current Position

Reference knowledge must be validated against:

- Product version.
- Component.
- Deployment type.
- Feature flags or configuration.
- Known affected versions.
- Known fixed versions.
- Source authority.
- Last review date.

#### Risks

- Wrong-version documentation supports an incorrect insight.
- Previous issues become false analogies.
- AI retrieves plausible but irrelevant knowledge.

#### Next Step

Add a knowledge validation checklist to future case studies and Diagnostic Knowledge Patterns.

---

### T-007: Challenge Confidence Scoring

**Loop / Stage:** Reasoning Loop / Challenge  
**Status:** Active

#### Question

What confidence model is useful enough to gate Judgment without becoming too heavy?

#### Current Position

Use Low / Medium / High as the default.

An optional numeric model can score dimensions such as support, contradiction, missing evidence, assumptions, alternatives, timeline order, time-window compatibility, knowledge applicability, preparation quality, and cold/guided agreement.

#### Risks

- Numeric scoring gives false precision.
- Low / Medium / High may be too subjective.
- Blocking conditions need to override aggregate scores.

#### Next Step

Use first synthetic case to test whether Low / Medium / High is enough.

---

### T-008: Diagnostic Knowledge Patterns

**Loop / Stage:** Knowledge / Reasoning Loop  
**Status:** Active

#### Question

How can previous issues be captured as reusable Knowledge sources without becoming brittle `rg` patterns?

#### Current Position

Use YAML-based Diagnostic Knowledge Patterns that describe semantic observations, evidence requirements, contradictions, missing evidence, time relationships, knowledge validation, challenge questions, and confidence model.

Patterns should not contain `rg`, SQL, jq, DuckDB queries, or parser-specific logic.

#### Risks

- Pattern language becomes too complex.
- Semantic observations are not stable enough.
- Teams use patterns as diagnosis shortcuts.

#### Next Step

Review the first example pattern and validate it during a case study.

---

### T-009: Semantic Observation Vocabulary

**Loop / Stage:** Evidence / Knowledge bridge  
**Status:** Active

#### Question

What stable observation names should EGATF use across different bundle versions and extraction tools?

#### Current Position

Start with a small vocabulary including:

- `client.timeout_increase`
- `client.latency_increase`
- `raft.leader_instability`
- `raft.no_leader_observed`
- `tablet.leaderless`
- `tablet.under_replicated`
- `tablet.over_replicated`
- `node.disk_latency_increase`
- `node.cpu_saturation`
- `process.restart_observed`
- `metrics.coverage_gap`
- `knowledge.version_mismatch`

#### Risks

- Vocabulary becomes too product-specific.
- Names become inconsistent.
- Observations are too broad or too narrow.

#### Next Step

Expand vocabulary only when a case study requires a new observation kind.

---

## Backlog Threads

### T-010: Adapter Layer for Tools

**Loop / Stage:** Evidence Preparation  
**Status:** Backlog

Adapters map versioned tool outputs into semantic observations.

Examples:

- `wtl` parquet + DuckDB query produces `process.restart_observed`.
- Tablet report parser derived table produces `tablet.leaderless`.

This is important, but not immediately required for the first case study.

---

## Review Cadence

Review this tracker after each major artefact:

- New case study.
- Framework version update.
- Slide deck update.
- Engineering proposal.
- New diagnostic knowledge pattern.
- New semantic observation vocabulary entry.

The tracker should prevent useful framework threads from being lost while the first case study remains focused.
