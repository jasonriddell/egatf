# EGATF Changelog

**Document type:** Framework change history  
**Status:** Active  
**Repository path:** `framework/changelog.md`

---

## Purpose

This changelog records the evolution of the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is to preserve a clear history of how the framework changes over time, including:

- Stage names
- Stage ordering
- Terminology changes
- Major design decisions
- Open questions
- Removed ideas
- Validation findings

This document should help maintain provenance and make the development of the framework auditable.

---

## Versioning Approach

EGATF uses simple research-stage versioning.

Example:

```text
v0.1 - Initial draft
v0.2 - Evidence stage refinement
v0.3 - Evidence preparation taxonomy
v1.0 - First stable public framework
```

A version does not imply software compatibility. It represents the maturity of the framework definition.

---

## v0.3 - Evidence Preparation Taxonomy

**Date:** 2026-06-24  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Refined the meaning of Evidence Preparation.

The previous v0.2 model introduced Evidence Preparation as a sub-stage between Raw Source Material and Extracted Evidence.

v0.3 clarifies that Evidence Preparation is not the same as extraction.

Evidence Preparation includes several different operations:

```text
Collection
Transformation
Parsing
Normalization
Indexing
Extraction
Derivation
Correlation
```

### Added

Added the following terms:

- Prepared Evidence Base
- Structured Source Material
- Parsed Source Material
- Normalized Source Material
- Indexed Source Material
- Derived Evidence
- Correlated Evidence
- Source Transformer
- Parser
- Indexer
- Derived Evidence Generator
- Report Structuring Tool
- Log Structuring Tool

Added new document:

```text
framework/evidence-preparation.md
```

### Changed

Updated `framework/framework.md` to:

- Replace the simple Raw Source Material to Evidence Preparation to Extracted Evidence sequence with a richer preparation model.
- Distinguish Structured Source Material from Extracted Evidence.
- Distinguish Extraction from Derivation.
- Add tool classification for `wtl` and tablet report parser examples.
- Add boundary rules for transformation, extraction, derivation, correlation, and information.
- Update evidence chain requirements.
- Update AI roles to warn that derived evidence should not be mistaken for direct evidence.

Updated `framework/terminology.md` to:

- Add Evidence Preparation operations.
- Add output types.
- Add Source Transformer.
- Add Derived Evidence Generator.
- Clarify the difference between `wtl` style tools and true extractors.
- Clarify hybrid tools such as tablet report parser.

Updated `README.md` to:

- Add Evidence Preparation taxonomy to the high-level overview.
- Add Source Transformation and Derived Evidence Generation to focus areas.

Updated `research/research-log.md` to:

- Record the v0.3 refinement and rationale.

### Rationale

The term Evidence Extractor was too broad for some tools.

Example:

`wtl` converts tserver, master, and YBA logs into structured parquet files so they can be queried with DuckDB rather than searched with ripgrep.

It does not consolidate, filter, or diagnose.

Therefore it is better classified as:

```text
Source Transformer / Log Structuring Tool
```

It produces:

```text
Structured Source Material
```

not:

```text
Extracted Evidence
```

unless it also selects notable observations.

A tablet report parser may perform several roles. If it loads a raw tablet report into SQLite or parquet, it is performing transformation. If it identifies leaderless tablets, under-replicated tables, or over-replicated tables, it is performing derivation.

Therefore it may be a hybrid:

```text
Source Transformer + Derived Evidence Generator
```

### Design Decision: Preparation Is Broader Than Extraction

Evidence Preparation now means:

> Making raw source material easier to inspect, query, compare, and reason about while preserving provenance.

Extraction is only one activity inside preparation.

### Design Decision: Transformation Changes Shape

Transformation changes the representation or storage format of source material.

It does not decide what matters.

Example:

```text
raw logs
    ↓
parquet tables
```

### Design Decision: Extraction Selects Observations

Extraction identifies notable observations from raw or structured material.

Example:

```text
logs.parquet
    ↓
restart events
```

### Design Decision: Derivation Computes Observations

Derivation computes higher-level observations from lower-level material.

Example:

```text
tablet peer roles
    ↓
tablet is leaderless
```

### Design Decision: Hybrid Tools Are Allowed

Tools do not have to be physically split into separate binaries.

However, their outputs should distinguish between:

- Structured Source Material
- Extracted Evidence
- Derived Evidence
- Correlated Evidence
- Findings

### Current Framework Sequence

The top-level framework remains:

```text
Evidence
    ↓
Information
    ↓
Knowledge
    ↓
Insight
    ↓
Challenge
    ↓
Wisdom
    ↓
Decision
    ↓
Action
    ↓
Outcome
    ↓
Learning
```

The Evidence stage now contains:

```text
Reported Context
    ↓
Raw Source Material
    ↓
Evidence Preparation
    ↓
Prepared Evidence Base
```

The Prepared Evidence Base may contain:

```text
Structured Source Material
Extracted Evidence
Derived Evidence
Correlated Evidence
```

### Open Questions Added

1. Should Evidence Preparation become a top-level framework stage?
2. Should every preparation tool declare its role?
3. Should outputs use standard names such as `structured_source`, `extracted_evidence`, and `derived_evidence`?
4. Should derived evidence include machine-readable derivation metadata?
5. How should hybrid tools expose their output layers?
6. How should extractor precision and recall be tested?
7. Should EGATF define a minimal evidence schema?
8. Should source transformation outputs be considered evidence or prepared source material?
9. How should AI be told which prepared evidence is direct, extracted, derived, or correlated?
10. What level of preparation is enough before AI analysis begins?

### Current Hypothesis

The v0.3 hypothesis is:

> Classifying evidence preparation tools by function reduces confusion and helps prevent structured or derived outputs from being mistaken for verified diagnosis.

### Next Planned Work

1. Update the case study template to include:
   - Reported Context
   - Raw Source Material
   - Evidence Preparation
   - Prepared Evidence Base
   - Structured Source Material
   - Extracted Evidence
   - Derived Evidence
   - Correlated Evidence
   - Information

2. Create a synthetic worked example showing:
   - `wtl` as a Source Transformer
   - a query as an Evidence Extractor
   - a tablet report parser as a hybrid Source Transformer and Derived Evidence Generator

3. Consider a future document:
   - `framework/evidence-schema.md`

---

## v0.2 - Evidence Stage Refinement

**Date:** 2026-06-24  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Refined the early part of the framework to better represent how support investigations actually begin.

The original v0.1 model moved directly from:

```text
Evidence
    ↓
Information
```

v0.2 expanded the Evidence stage into a set of sub-stages:

```text
Reported Context
    ↓
Raw Source Material
    ↓
Evidence Preparation
    ↓
Extracted Evidence
    ↓
Information
```

This change recognized that customer ticket summaries, alert descriptions, support bundles, logs, metrics, and extracted observations have different reliability levels and should not be treated as the same type of input.

### Added

Added the following concepts:

- Reported Context
- Raw Source Material
- Evidence Preparation
- Extracted Evidence
- Cold Analysis
- Guided Analysis
- Anchoring Risk
- Collector
- Evidence Extractor
- Normalizer
- Correlator
- Helper

### Rationale

Support investigations usually do not start with clean evidence.

They often start with a mixture of:

- Unvalidated problem description
- Customer-reported symptoms
- Customer-reported cause
- Alert wording
- Error message
- Support bundle snapshot
- Live telemetry
- Logs
- Metrics
- Command output

The framework needs to distinguish between:

1. What someone reported.
2. What raw material is available.
3. How that material was prepared.
4. What evidence was extracted.
5. What information was inferred from that evidence.

### Design Decision: Reported Context

Reported context is useful but unvalidated.

Rule added:

> Reported context is guidance, not ground truth.

### Design Decision: Cold and Guided Analysis

Added two analysis modes:

```text
Cold Analysis
Guided Analysis
```

Recommended workflow:

```text
Cold pass
    ↓
Guided pass
    ↓
Compare findings
```

### Design Decision: Evidence Preparation

Evidence preparation was introduced as the term for mechanical extraction, filtering, parsing, normalizing, indexing, and correlating of raw source material.

Rule added:

> Evidence preparation should reduce noise without adding unsupported meaning.

### Design Decision: Evidence Extractors

The preferred name for scripts that parse raw material into structured observations was:

> Evidence Extractors

v0.3 later refined this by distinguishing Source Transformers from Evidence Extractors.

---

## v0.1 - Initial Framework Definition

**Date:** 2026-06-22  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Created the initial working definition of the Evidence-Grounded AI Troubleshooting Framework.

The framework is intended to explore how AI and humans can work together to transform technical evidence into trustworthy decisions while reducing unsupported reasoning and hallucination.

### Initial Framework Sequence

```text
Evidence
    ↓
Information
    ↓
Knowledge
    ↓
Insight
    ↓
Challenge
    ↓
Wisdom
    ↓
Decision
    ↓
Action
    ↓
Outcome
    ↓
Learning
```

### Core Principle Added

> Every insight must be traceable to evidence, and every piece of evidence must be traceable to the insight it supports.

Supporting statements:

> Without evidence, an insight is speculation.  
> Without traceability, an insight cannot be trusted.  
> Without challenge, an insight cannot become wisdom.

### Initial Research Question

Can AI-assisted troubleshooting be made more reliable by requiring every conclusion to be traceable back to evidence and every insight to survive deliberate challenge before influencing decisions?

### Initial Design Decisions

#### Evidence-first framing

The framework begins with **Evidence** rather than **Data**.

Reason:

In technical troubleshooting, the raw material is not just data. It includes logs, metrics, dumps, source code, documentation, bug reports, observations, and historical context. The term **Evidence** better captures the need for traceability and source reliability.

#### Challenge as a required stage

The framework includes **Challenge** between Insight and Wisdom.

Reason:

AI can generate plausible hypotheses quickly. The framework should require those hypotheses to be tested, weakened, contradicted, or rejected before they influence human judgment and decisions.

#### Human judgment retained

The framework does not position AI as the final decision maker.

Reason:

AI can assist with extraction, summarization, retrieval, hypothesis generation, and challenge, but humans remain accountable for judgment, decisions, and actions.

---

## Future Version Notes

Use the following format for future entries:

```text
## vX.Y - Short Title

Date:
Status:
Stage:

### Summary

### Added

### Changed

### Removed

### Rationale

### Open Questions

### Next Planned Work
```

---

## Revision Notes

This changelog begins with v0.1 and should be updated whenever the framework definition, terminology, or major research direction changes.
