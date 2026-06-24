# Evidence Preparation

**Document type:** Framework detail  
**Status:** Draft v0.4  
**Repository path:** `framework/evidence-preparation.md`

---

## Purpose

This document defines Evidence Preparation within EGATF.

Evidence Preparation is the set of activities that turns raw diagnostic material into a usable evidence base while preserving provenance.

The purpose is to avoid sending large, noisy, unstructured source material directly into AI when deterministic preparation tools can make the material cleaner, more consistent, and easier to reason about.

---

## Core Principle

Evidence Preparation should reduce noise without adding unsupported meaning.

A preparation tool should make material easier to inspect, query, compare, or reason about.

It should not hide provenance.

It should not silently convert assumptions into facts.

---

## Preparation Flow

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
    ↓
Information
```

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

Collection Context should be consulted before preparation because it describes what was collected, which component windows apply, which versions generated the evidence package, and which files are expected to exist.

---

## Collection Context Dependency

Evidence Preparation tools should use Collection Context when available.

Examples:

- Use support bundle schema version to choose parser logic.
- Use YBDB version to select version-aware parsing behavior.
- Use YBA version to understand support bundle format.
- Use component list to determine expected files.
- Use file index to validate presence or absence of directories.
- Use collection windows to avoid correlating incompatible evidence.
- Use metric collection settings to explain why some metrics are absent or low resolution.

Collection Context should help preparation tools distinguish:

```text
missing because not collected
missing because unsupported
missing because collection failed
missing because no data existed
```

---

## Outputs

Evidence Preparation can produce several output types.

```text
Raw Source Material
Structured Source Material
Parsed Source Material
Normalized Source Material
Indexed Source Material
Extracted Evidence
Derived Evidence
Correlated Evidence
```

These are not all the same.

A key EGATF discipline is to label outputs accurately.

---

## Transformation

Transformation changes the shape or storage format of source material without deciding what matters.

Examples:

- Convert logs to parquet
- Convert JSON reports to SQLite tables
- Convert text reports into structured rows
- Split log lines into columns
- Store raw events in a queryable database

Transformation produces:

```text
Structured Source Material
```

Example:

```text
tserver.log
    ↓ Source Transformer
logs.parquet
```

A tool like `wtl` is best described as:

```text
Source Transformer / Log Structuring Tool
```

because it converts log lines into structured parquet records without filtering, consolidating, or interpreting them.

This is not primarily extraction.

---

## Extraction

Extraction selects or identifies notable observations that may matter.

Examples:

- Find restart events
- Find FATAL log lines
- Find failed backups
- Find memory pressure events
- Find leader changes
- Find tablets with no leader

Extraction produces:

```text
Extracted Evidence
```

Extraction answers:

> What notable observations can be pulled out of the prepared material?

---

## Derivation

Derivation computes higher-level observations from lower-level source material or extracted evidence.

Examples:

- Tablet is leaderless
- Table is under-replicated
- Table is over-replicated
- Node had 17 restarts
- Error rate increased 400 percent

Derivation produces:

```text
Derived Evidence
```

Derived evidence should record:

- Inputs used
- Logic applied
- Output produced
- Confidence or limitations
- Link back to source material
- Whether inputs represent requested duration or collection-time snapshot

---

## Correlation

Correlation compares observations across time, nodes, components, or sources.

Examples:

- Compare restart time against memory pressure
- Compare leader changes against disk latency
- Compare customer-reported time window against log evidence
- Compare error rates across nodes

Correlation produces:

```text
Correlated Evidence
```

Correlation should be collection-window aware.

For example, collection-time tablet metadata should not be correlated with a historical log event as if both represented the same time window.

---

## Example: wtl

`wtl` takes tserver, master, and YBA logs and converts each line into structured columns, then writes the result to parquet.

It does not consolidate, filter, or diagnose.

Classification:

```text
Tool type:
Source Transformer / Log Structuring Tool

Input:
Raw log files

Output:
Structured Source Material

Not:
Evidence Extractor, unless it also identifies notable observations.
```

Reason:

`wtl` changes shape. It does not select meaning.

It enables later queries such as:

```text
logs.parquet
    ↓ DuckDB query
restart events
```

The DuckDB query may be an Evidence Extractor if it selects notable events.

---

## Example: Tablet Report Parser

A tablet report parser may perform multiple roles.

If it converts a raw tablet report into SQLite or parquet tables, it is acting as:

```text
Source Transformer / Report Structuring Tool
```

If it identifies leaderless tablets, over-replicated tables, or under-replicated tables, it is also acting as:

```text
Derived Evidence Generator
```

Classification:

```text
Tool type:
Hybrid

Roles:
Source Transformer
Derived Evidence Generator

Input:
Raw tablet report

Outputs:
Structured Source Material
Derived Evidence
```

Recommended conceptual output separation:

```text
source_tables/
    tablet_raw
    tablet_peer_raw
    tablet_replica_raw

derived_evidence/
    tablet_leader_status
    table_replication_status
    tablet_placement_status

findings/
    leaderless_tablets
    under_replicated_tables
    over_replicated_tables
```

The same binary may perform all of these functions, but the outputs should identify which layer they belong to.

---

## Boundary Rules

### Transformation changes shape

```text
raw logs
    ↓
parquet tables
```

### Extraction selects observations

```text
logs.parquet
    ↓
restart events
```

### Derivation computes observations

```text
tablet peer roles
    ↓
tablet is leaderless
```

### Correlation compares observations

```text
restart event + memory metric
    ↓
memory pressure preceded restart by 3 minutes
```

### Information explains relationships

```text
The reported error appears in the logs, but only after the first tserver restart.
```

---

## Why This Matters for AI

A safe AI-assisted diagnostic workflow should not always begin by sending raw bundles directly into AI.

A safer pattern is:

```text
Collection Context
    ↓
Raw Source Material
    ↓
Deterministic Evidence Preparation
    ↓
Prepared Evidence Base
    ↓
AI-assisted Information Synthesis
    ↓
AI-assisted Insight Generation
    ↓
Challenge
```

This improves the workflow because:

- AI receives cleaner input.
- Token usage is reduced.
- Noise is reduced.
- Provenance is preserved.
- Deterministic tools can be tested.
- Derived evidence can be reviewed.
- AI can spend more effort reasoning and less effort parsing.
- AI can avoid false correlations across incompatible time windows.

The safety rule is:

> Use deterministic tools to prepare evidence where possible. Use AI to reason over prepared evidence, but require traceability back to raw source material and collection context.
