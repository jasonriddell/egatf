# EGATF Changelog

**Document type:** Framework change history  
**Status:** Active  
**Repository path:** `framework/changelog.md`

---

## Purpose

This changelog records the evolution of the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is to preserve a clear history of how the framework changes over time.

---

## Versioning Approach

EGATF uses simple research-stage versioning.

Example:

```text
v0.1 - Initial draft
v0.2 - Evidence stage refinement
v0.3 - Evidence preparation taxonomy
v0.4 - Collection context and evidence package manifests
v0.5 - Three-loop operating model
v0.6 - Judgment terminology update
v1.0 - First stable public framework
```

---

## v0.6 - Judgment Terminology Update

**Date:** 2026-06-26  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Renamed the former **Wisdom** stage to **Judgment**.

The concept remains the same: this stage represents the current best human assessment after evidence, information, knowledge, insight, and challenge have been considered.

The new name is clearer, more practical, and better aligned with the purpose of EGATF.

The chain is now:

```text
Evidence -> Information -> Knowledge -> Insight -> Challenge -> Judgment -> Decision -> Action -> Outcome -> Learning
```

### Changed

- Replaced the stage name **Wisdom** with **Judgment** across framework documents, terminology, process flow, challenge evaluation, case template, diagrams, and slide materials.
- Reworded the core principle from "Without challenge, an insight cannot become wisdom" to "Without challenge, an insight should not become judgment".
- Updated the Reasoning Loop to end with Judgment.
- Updated the Challenge Confidence Gate to describe progression from challenged insight to responsible judgment.
- Updated case study headings and evidence chain summaries.

### Rationale

The term **Wisdom** was too abstract and created the wrong tone. It suggested philosophy or mysticism rather than an accountable engineering assessment.

The term **Judgment** better reflects the intended meaning:

- A human or team owns the assessment.
- The assessment is evidence-aware.
- The assessment remains uncertainty-aware.
- The assessment can be revised.
- The assessment is distinct from Decision and Action.

### Current Hypothesis

> Replacing Wisdom with Judgment makes EGATF clearer, more practitioner-friendly, and easier to explain to engineering teams.

---

## v0.5 - Three-Loop Operating Model

**Date:** 2026-06-25  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Reframed EGATF from a straight-line chain into three related gated loops.

The chain remains useful for teaching:

```text
Evidence -> Information -> Knowledge -> Insight -> Challenge -> Judgment -> Decision -> Action -> Outcome -> Learning
```

The operating model is now:

```text
Loop 1: Evidence Loop
Can we trust what we are reasoning from?

Loop 2: Reasoning Loop
Can we trust what we believe?

Loop 3: Action Loop
Can we trust what happened next?
```

### Added

- Evidence Loop
- Reasoning Loop
- Action Loop
- Evidence Sufficiency Gate
- Challenge Confidence Gate
- Outcome Validation Gate

### Changed

Updated the framework, terminology, process flow, stage deep dives, challenge evaluation, case template, diagrams, and slide deck to use the three-loop model consistently.

### Rationale

The original chain is helpful, but real troubleshooting is iterative. Investigations should not progress simply because a previous stage produced an answer.

Each loop now has a gate that can stop progression and force rework:

- Evidence Loop blocks reasoning from weak or misunderstood evidence.
- Reasoning Loop blocks unsupported insights from becoming judgment.
- Action Loop blocks closure when outcomes contradict the judgment.

### Current Hypothesis

The v0.5 hypothesis is:

> The three-loop model makes EGATF more usable as an operating process because it gives practitioners clear gates that prevent weak evidence, unsupported reasoning, or contradictory outcomes from progressing unnoticed.

## v0.4 - Collection Context and Evidence Package Manifests

**Date:** 2026-06-24  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Added Collection Context as a distinct concept inside the Evidence stage.

Collection Context describes how an evidence package was created, what it contains, which time periods its contents represent, which versions are involved, and how the contents should be interpreted.

This was prompted by support bundle analysis, where different files may represent different effective times.

Example:

```text
Support bundle created at:
T

Logs collected for:
T - 7 days to T - 5 days

Tablet metadata collected at:
T

Tablet report collected at:
T
```

Without explicit Collection Context, AI may incorrectly correlate collection-time tablet state with historical log events.

### Added

Added the following terms:

- Collection Context
- Evidence Package Manifest
- Collection Window
- Collection-Time Snapshot
- Duration-Based Evidence
- Component Descriptions
- File Index
- Bundle Provenance
- Environment Identity
- Metric Collection Context

Added new document:

```text
framework/collection-context.md
```

Added engineering feature request:

```text
engineering/support-bundle-manifest-improvements.md
```

### Changed

Updated `framework/framework.md` to:

- Add Collection Context between Reported Context and Raw Source Material.
- Add Evidence Package Manifest.
- Add collection-window handling.
- Add support bundle timing semantics.
- Update evidence chain requirements.
- Update AI roles to include Collection Context.
- Add challenge questions related to collection-time versus duration-based evidence.

Updated `framework/terminology.md` to:

- Add Collection Context.
- Add Evidence Package Manifest.
- Add Collection Window.
- Add Collection-Time Snapshot.
- Add Duration-Based Evidence.
- Update Evidence Chain.
- Update Confidence to consider whether collection context supports interpretation.

Updated `framework/evidence-preparation.md` to:

- Add Collection Context as a dependency for preparation.
- Explain how preparation tools should use schema version, file index, component windows, and collection limitations.

Updated `README.md` to:

- Add Collection Context to the Evidence stage overview.
- Add support bundle metadata and evidence package manifests to focus areas.

Updated `research/research-log.md` to:

- Record the v0.4 refinement and rationale.

### Rationale

Support bundles need to be self-describing for humans, deterministic tools, and AI-assisted workflows.

The existing manifest already describes some collection details, including bundle UUID, path, scope UUID, start and end dates, components, and metric types.

However, AI-assisted analysis benefits from richer context, including:

- Support bundle schema version
- Collector version
- Bundle creation time
- Universe identity and version
- YBA identity and version
- Deployment type
- Infrastructure type
- Metric collection settings
- Per-component collection windows
- Component descriptions
- File index
- Known limitations

This is especially important as YBA may move toward a release model where YBA is on the latest released version while managed universes may run different YBDB versions. Explicit support bundle schema and collector versions allow automated analysis tools to choose version-aware parsers and fail safely when formats change.

### Design Decision: Collection Context Is Not Diagnosis

Collection Context describes the evidence package.

It should not state the root cause.

### Design Decision: Evidence Package Manifest

The preferred formal term is:

```text
Evidence Package Manifest
```

For support bundles, this can be implemented as an expanded `manifest.json`, or as a combination of:

```text
manifest.json
bundle_context.json
file_index.json
```

### Design Decision: Component-Specific Timing Semantics

A single global start and end time is not enough.

Each component should expose timing semantics such as:

```text
requested_duration
metrics_duration
collection_time_snapshot
mixed
unknown
not_applicable
```

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
Judgment
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
Collection Context
    ↓
Raw Source Material
    ↓
Evidence Preparation
    ↓
Prepared Evidence Base
```

### Current Hypothesis

The v0.4 hypothesis is:

> Explicit collection context reduces AI-assisted diagnostic errors caused by time-window confusion, version confusion, missing file ambiguity, and misunderstanding of support bundle contents.

---

## v0.3 - Evidence Preparation Taxonomy

**Date:** 2026-06-24  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Refined the meaning of Evidence Preparation.

Evidence Preparation includes:

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

### Rationale

The term Evidence Extractor was too broad for some tools.

Example:

`wtl` converts tserver, master, and YBA logs into structured parquet files so they can be queried with DuckDB rather than searched with ripgrep.

It does not consolidate, filter, or diagnose.

Therefore it is better classified as:

```text
Source Transformer / Log Structuring Tool
```

A tablet report parser may perform several roles. If it loads a raw tablet report into SQLite or parquet, it is performing transformation. If it identifies leaderless tablets, under-replicated tables, or over-replicated tables, it is performing derivation.

Therefore it may be a hybrid:

```text
Source Transformer + Derived Evidence Generator
```

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

### Rationale

Support investigations usually do not start with clean evidence.

They often start with a mixture of unvalidated problem descriptions, customer-reported symptoms, alert wording, support bundle snapshots, live telemetry, logs, metrics, and command output.

---

## v0.1 - Initial Framework Definition

**Date:** 2026-06-22  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Created the initial working definition of the Evidence-Grounded AI Troubleshooting Framework.

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
Judgment
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

### Initial Research Question

Can AI-assisted troubleshooting be made more reliable by requiring every conclusion to be traceable back to evidence and every insight to survive deliberate challenge before influencing decisions?
