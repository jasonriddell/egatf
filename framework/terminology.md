# EGATF Terminology

**Document type:** Working glossary  
**Status:** Draft v0.4  
**Repository path:** `framework/terminology.md`

---

## Purpose

This document defines the core terms used by the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is to keep the language of the framework consistent as the research evolves.

---

## Reported Context

An unvalidated description of the problem provided by a customer, alert, first responder, support engineer, or ticket creator.

Examples:

- Ticket summary
- Customer problem statement
- Alert description
- Customer-provided error message
- First responder notes
- Escalation summary

Reported context answers:

> What does someone currently believe or report is happening?

Rule:

> Reported context is guidance, not ground truth.

---

## Collection Context

Metadata describing how an evidence package was created, what it contains, what time periods its contents represent, and how those contents should be interpreted.

Examples:

- Support bundle version
- Support bundle schema version
- Bundle creation time
- Requested collection window
- Component-specific collection windows
- Universe name and UUID
- Universe YBDB version
- YBA instance and YBA version
- Deployment type
- Provider
- Replication factor
- Node counts
- Metric collection level
- Included components
- File index
- Component descriptions
- Known collection limitations

Collection Context answers:

> How was this evidence package collected and what does it represent?

Rule:

> Collection Context constrains interpretation. It is not diagnosis.

---

## Evidence Package Manifest

A machine-readable description of a collected evidence package.

For support bundles, this may be implemented as an expanded `manifest.json`, or as a combination of:

```text
manifest.json
bundle_context.json
file_index.json
```

The manifest should describe:

- Collection provenance
- Environment identity
- Collection windows
- Component timing semantics
- Component descriptions
- File index
- Known gaps or limitations

The manifest should not attempt to diagnose the issue.

---

## Collection Window

The time period represented by a piece of collected material.

Different evidence sources may have different collection windows.

Examples:

- Logs may represent the requested support bundle duration.
- Metrics may represent a metrics-specific duration and resolution.
- Tablet metadata may represent bundle creation time.
- Consensus metadata may represent bundle creation time.
- Tablet reports may represent bundle creation time.
- YBA metadata may be mixed.

Collection Window answers:

> What time period does this source represent?

---

## Collection-Time Snapshot

Evidence that represents system state at the time the bundle was created, not necessarily during the requested log or metrics window.

Examples:

- Tablet metadata
- Consensus metadata
- Tablet report
- Some YBA metadata
- Some universe metadata

Risk:

AI may incorrectly use collection-time state to explain historical log events from an earlier window.

---

## Duration-Based Evidence

Evidence that represents a requested time duration.

Examples:

- Logs collected for a requested support bundle window
- Metrics exported for a selected metrics duration
- Application logs over a configured range

---

## Raw Source Material

Untouched diagnostic material available to the investigation.

Examples:

- Support bundle archive
- Logs
- Metrics export
- Trace export
- Core dump
- Configuration dump
- Command output
- Database metadata
- Source code snapshot
- Documentation page
- Bug report contents
- Ticket text

Raw source material answers:

> What material is available for analysis?

---

## Evidence Preparation

The process of making raw source material easier to inspect, query, compare, and reason about while preserving provenance.

Evidence Preparation includes:

- Collection
- Transformation
- Parsing
- Normalization
- Indexing
- Extraction
- Derivation
- Correlation

Rule:

> Evidence preparation should reduce noise without adding unsupported meaning.

---

## Prepared Evidence Base

The body of prepared material available for analysis after evidence preparation.

A Prepared Evidence Base may contain:

- Structured Source Material
- Parsed Source Material
- Normalized Source Material
- Indexed Source Material
- Extracted Evidence
- Derived Evidence
- Correlated Evidence

---

## Structured Source Material

Raw source material that has been transformed into a more queryable or structured format without deciding what matters.

Examples:

- Logs converted to parquet
- Text reports converted to SQLite tables
- JSON converted to relational tables
- Log lines split into columns

A tool such as `wtl`, which converts tserver, master, and YBA logs into parquet files without consolidation or filtering, produces Structured Source Material.

It should not be described as producing Extracted Evidence unless it also selects notable observations.

---

## Extracted Evidence

A selected observation produced from raw or structured source material with provenance.

Examples:

```text
At 2026-06-21 10:14:22 UTC, tserver-3 restarted.
Source: tserver.log line 18422.
```

```text
CPU usage on node-2 exceeded 95 percent for 11 minutes.
Source: metrics.csv.
```

Extracted Evidence answers:

> What notable observation was found in the material?

---

## Derived Evidence

A computed observation generated from raw source material, structured source material, or extracted evidence.

Examples:

- Tablet is leaderless
- Table is under-replicated
- Table is over-replicated
- Node had 17 restarts
- Error rate increased 400 percent
- Leader movement followed disk latency increase

Derived Evidence answers:

> What computed observation follows from the available evidence?

Derived Evidence must preserve the derivation logic and source inputs.

---

## Correlated Evidence

Evidence produced by comparing observations across time, nodes, components, sources, or reports.

Examples:

- Memory pressure began 3 minutes before restart.
- Leader changes increased after disk latency increased.
- The reported error appears outside the customer-reported time window.
- Node-2 shows the error, but node-1 and node-3 do not.

---

## Evidence

Observable, reported, collected, structured, extracted, derived, or correlated material that can support or challenge a claim.

In EGATF v0.4, Evidence includes:

- Reported Context
- Collection Context
- Raw Source Material
- Structured Source Material
- Extracted Evidence
- Derived Evidence
- Correlated Evidence

---

## Information

Evidence that has been structured into meaningful observations, timelines, comparisons, or relationships.

Examples:

- Error rate increased after deployment.
- Memory usage reached 98 percent before restart.
- Leader movement began after disk latency increased.
- The reported error appears in logs, but outside the reported time window.
- Tablet metadata was collected after the log window and should not be treated as proof of tablet state during that window.

Information answers:

> What happened?

Information must remain linked to the evidence it was derived from.

---

## Knowledge

Contextual understanding derived from trusted sources.

Examples:

- Product documentation
- Source code
- Architecture diagrams
- Known bug reports
- Previous incidents
- Operational runbooks
- Domain expertise

Knowledge answers:

> How does this system behave?

---

## Insight

A candidate explanation produced by combining evidence, information, and knowledge.

Insight answers:

> What might this mean?

An insight is a hypothesis, not yet a conclusion.

---

## Challenge

The deliberate attempt to test, weaken, disprove, or qualify an insight.

Challenge questions include:

- What evidence supports this insight?
- What evidence contradicts this insight?
- What evidence is missing?
- What assumptions does this insight depend on?
- Are there alternative explanations?
- Did the timeline happen in the required order?
- Did guided analysis anchor the investigation too strongly?
- Did evidence preparation hide, drop, or misclassify material?
- Did analysis confuse collection-time evidence with duration-based evidence?

Challenge answers:

> Why might this explanation be wrong?

---

## Wisdom

The current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

Status:

**Provisional term.**

Wisdom may be renamed or removed in a future version of the framework.

---

## Decision

The selection of a response based on the current best judgment.

---

## Action

The execution of a decision.

---

## Outcome

The measured result of an action.

---

## Learning

Reusable knowledge captured from an investigation.

---

## Evidence Preparation Operations

### Collection

Gathering raw source material.

### Transformation

Changing the shape or storage format of source material without deciding what matters.

Boundary rule:

> Transformation changes shape. It does not select meaning.

### Parsing

Reading a specific format and identifying fields.

### Normalization

Making values consistent across sources.

### Indexing

Making prepared material searchable or queryable.

### Extraction

Selecting or identifying notable observations from raw or structured material.

Boundary rule:

> Extraction selects observations.

### Derivation

Computing higher-level observations from lower-level source material or evidence.

Boundary rule:

> Derivation computes observations.

### Correlation

Comparing observations across time, nodes, components, or sources.

Boundary rule:

> Correlation compares observations.

---

## Tooling Terms

### Collector

A script, command, or tool that gathers raw source material.

### Source Transformer

A script, command, or tool that converts raw material into a more structured or queryable form without selecting meaning.

Example:

```text
wtl
```

If `wtl` converts tserver, master, and YBA logs into parquet columns without consolidation or filtering, it is best described as:

```text
Source Transformer / Log Structuring Tool
```

### Parser

A script, command, or tool that reads a specific format and exposes fields.

### Normalizer

A script, command, or tool that converts values into consistent forms.

### Indexer

A script, command, or tool that makes material searchable or queryable.

### Evidence Extractor

A script, command, or tool that extracts notable observations from raw or structured source material.

### Derived Evidence Generator

A script, command, or tool that computes higher-level observations from source material or evidence.

If a tablet report parser converts the raw report into SQLite or parquet and also identifies leaderless tablets, under-replicated tables, or over-replicated tables, it is a hybrid:

```text
Source Transformer + Derived Evidence Generator
```

### Correlator

A script, command, or tool that compares observations across time, nodes, components, or sources.

### Helper

A script, command, or tool that assists later workflow tasks after investigation or during communication.

Examples:

- Generate engineering escalation
- Draft customer update
- Create case summary
- Generate post-incident review outline
- Format a bug report

---

## Boundary Rules

### Collection Context versus Raw Source Material

Collection Context describes the evidence package.

Raw Source Material is the collected content.

### Transformation versus Extraction

Transformation changes shape.

Extraction selects observations.

### Extraction versus Derivation

Extraction identifies an observation that exists in the material.

Derivation computes a new observation from available material.

### Derivation versus Information

Derivation computes an observation.

Information places observations into context.

---

## Analysis Modes

### Cold Analysis

Analysis of raw source material or prepared evidence without using reported context as the primary guide.

### Guided Analysis

Analysis that uses reported context to guide search, filtering, and extraction.

Rule:

> Guided analysis should treat reported context as direction, not proof.

### Anchoring Risk

The risk that an investigation becomes overly influenced by the initial problem description, customer statement, alert title, or first hypothesis.

---

## Supporting Terms

### Evidence Chain

A traceable path from final conclusion or decision back to the supporting evidence.

Example:

```text
Decision
    ↓ supported by
Wisdom / Judgment
    ↓ based on
Challenged Insight
    ↓ derived from
Knowledge + Information
    ↓ grounded in
Prepared Evidence Base
    ↓ produced by
Evidence Preparation
    ↓ applied to
Raw Source Material
    ↓ described by
Collection Context
    ↓ optionally guided by
Reported Context
```

### Confidence

The degree of trust assigned to an insight, judgment, or decision.

Confidence should be based on:

- Strength of supporting evidence
- Presence or absence of contradicting evidence
- Quality of sources
- Completeness of timeline
- Number of assumptions
- Availability of alternative explanations
- Reproducibility
- Whether reported context was independently verified
- Whether collection context supports the interpretation
- Whether evidence sources represent the same time window
- Whether cold and guided analysis agree
- Whether derived evidence is supported by clear derivation logic

---

## Working Language Guidelines

When writing about EGATF:

- Use **reported context** for unvalidated problem descriptions.
- Use **collection context** for metadata describing scope, timing, version, source meaning, and collection limitations.
- Use **evidence package manifest** for machine-readable collection context.
- Use **raw source material** for untouched logs, metrics, bundles, dumps, and documents.
- Use **evidence preparation** for collection, transformation, parsing, normalization, indexing, extraction, derivation, and correlation.
- Use **structured source material** for transformed queryable material that has not yet selected meaning.
- Use **extracted evidence** for selected observations with provenance.
- Use **derived evidence** for computed observations.
- Use **correlated evidence** for relationships between observations.
- Use **information** for structured observations and context derived from evidence.
- Use **knowledge** for contextual understanding from trusted sources.
- Use **insight** for candidate explanations.
- Use **challenge** for deliberate testing of an insight.
- Use **decision** for choosing what to do.
- Use **action** for doing it.
- Use **outcome** for measuring what happened.
- Use **learning** for reusable knowledge captured afterward.

Avoid treating structured source material as extracted evidence.

Avoid treating derived evidence as direct evidence.

Avoid treating collection-time evidence as evidence for an earlier requested duration without explicit justification.

Avoid treating insights as conclusions until they have passed through challenge.

Avoid treating reported context as verified cause.

Avoid using AI-generated statements as evidence unless they are directly grounded in cited sources.
