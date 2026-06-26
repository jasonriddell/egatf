# EGATF Terminology

**Document type:** Working glossary  
**Status:** Draft v0.6  
**Repository path:** `framework/terminology.md`

---

## Purpose

This document defines the core terms used by the Evidence-Grounded AI Troubleshooting Framework.

---

## Operating Model Terms

### Three-Loop Model

The operating model for EGATF. The linear chain remains useful for teaching, but practical investigation is governed by three loops:

```text
Evidence Loop
Reasoning Loop
Action Loop
```

### Evidence Loop

The loop that turns reported context and raw source material into a prepared evidence base and information.

Question:

> Can we trust what we are reasoning from?

Includes:

```text
Reported Context -> Collection Context -> Raw Source Material -> Evidence Preparation -> Prepared Evidence Base -> Information
```

### Reasoning Loop

The loop that turns information and knowledge into challenged judgment.

Question:

> Can we trust what we believe?

Includes:

```text
Information -> Knowledge -> Insight -> Challenge -> Judgment
```

### Action Loop

The loop that turns judgment into decision, action, outcome, and learning.

Question:

> Can we trust what happened next?

Includes:

```text
Decision -> Action -> Outcome -> Learning
```

### Evidence Sufficiency Gate

The gate between the Evidence Loop and the Reasoning Loop.

Question:

> Do we understand the evidence well enough to reason from it?

Blocks progression when evidence is missing, misunderstood, not traceable, poorly prepared, or time-incompatible.

### Challenge Confidence Gate

The gate inside the Reasoning Loop that decides whether an insight can become responsible judgment.

Question:

> Has the insight survived enough challenge to become responsible judgment?

Possible outcomes:

```text
Strengthened
Weakened
Rejected
Split
More evidence required
```

### Outcome Validation Gate

The gate inside the Action Loop that checks whether the outcome supports the judgment.

Question:

> Did the action produce the expected outcome, and what should be learned or revisited?

Blocks closure when the outcome contradicts or only partially supports the judgment.

---

## One-Line Stage Definitions

| Stage | One-line definition |
|---|---|
| Reported Context | The unvalidated description of the issue, used as guidance but not treated as proof. |
| Collection Context | Metadata describing how the evidence package was collected, what it contains, and what time windows its contents represent. |
| Raw Source Material | The untouched diagnostic material available for analysis, such as logs, metrics, metadata, dumps, and support bundle files. |
| Evidence Preparation | The process of turning raw material into a usable evidence base through collection, transformation, parsing, normalization, indexing, extraction, derivation, and correlation. |
| Prepared Evidence Base | The prepared material available for analysis, including structured source material, extracted evidence, derived evidence, and correlated evidence. |
| Information | Meaningful observations, timelines, comparisons, and relationships derived from evidence. |
| Knowledge | Context from trusted sources such as documentation, source code, bug reports, runbooks, previous incidents, and domain expertise. |
| Insight | A candidate explanation or hypothesis produced by combining evidence, information, and knowledge. |
| Challenge | The deliberate attempt to test, weaken, disprove, or qualify an insight before it influences judgment. |
| Judgment | The current best human assessment after evidence, insight, and challenge have been considered. |
| Decision | The selected next response based on the current best judgment. |
| Action | The execution of the selected decision. |
| Outcome | The measured result of the action. |
| Learning | Reusable knowledge captured from the investigation for future use. |
---

## Core Evidence Terms

### Reported Context

An unvalidated description of the problem provided by a customer, alert, first responder, support engineer, or ticket creator.

Rule:

> Reported Context is guidance, not ground truth.

### Collection Context

Metadata describing how an evidence package was created, what it contains, what time periods its contents represent, and how those contents should be interpreted.

Rule:

> Collection Context constrains interpretation. It is not diagnosis.

### Evidence Package Manifest

A machine-readable description of a collected evidence package.

For support bundles, this may be implemented as an expanded `manifest.json`, or as a combination of:

```text
manifest.json
bundle_context.json
file_index.json
```

### Collection Window

The time period represented by a piece of collected material.

### Collection-Time Snapshot

Evidence that represents system state at the time the bundle was created, not necessarily during the requested log or metrics window.

### Duration-Based Evidence

Evidence that represents a requested time duration.

### Raw Source Material

Untouched diagnostic material available to the investigation.

### Evidence Preparation

The process of making raw source material easier to inspect, query, compare, and reason about while preserving provenance.

### Prepared Evidence Base

The body of prepared material available for analysis after evidence preparation.

### Structured Source Material

Raw source material that has been transformed into a more queryable or structured format without deciding what matters.

### Extracted Evidence

A selected observation produced from raw or structured source material with provenance.

### Derived Evidence

A computed observation generated from raw source material, structured source material, or extracted evidence.

### Correlated Evidence

Evidence produced by comparing observations across time, nodes, components, sources, or reports.

---

## Evidence Preparation Operations

| Operation | Definition |
|---|---|
| Collection | Gathering raw source material. |
| Transformation | Changing the shape or storage format of source material without deciding what matters. |
| Parsing | Reading a specific format and identifying fields. |
| Normalization | Making values consistent across sources. |
| Indexing | Making prepared material searchable or queryable. |
| Extraction | Selecting or identifying notable observations from raw or structured material. |
| Derivation | Computing higher-level observations from lower-level source material or evidence. |
| Correlation | Comparing observations across time, nodes, components, or sources. |

Boundary rules:

```text
Transformation changes shape.
Extraction selects observations.
Derivation computes observations.
Correlation compares observations.
Information explains relationships.
```

---

## Reasoning Terms

### Information

Evidence structured into meaningful observations, timelines, comparisons, or relationships.

### Knowledge

Contextual understanding from trusted sources such as documentation, source code, bug reports, runbooks, previous incidents, and domain expertise.

### Insight

A candidate explanation or hypothesis produced by combining evidence, information, and knowledge.

### Challenge

The deliberate attempt to test, weaken, disprove, or qualify an insight before it influences judgment.

### Judgment

The current best human assessment after evidence, information, knowledge, insight, and challenge have been considered.

### Decision

The selected next response based on the current best judgment.

### Action

The execution of the decision.

### Outcome

The measured result of the action.

### Learning

Reusable knowledge captured from the investigation.

---

## Analysis Technique Terms

### Cold Analysis

Analysis performed without using the reported problem statement, reported cause, or guided prompt as the primary direction.

Cold Analysis answers:

> What does the evidence show before we assume the reported context is correct?

---

### Guided Analysis

Analysis that uses reported context to guide search and verification while treating all causal claims as hypotheses.

Guided Analysis answers:

> What do we find when we use the reported context as guidance, not proof?

---

### Isolated Analysis Sandbox

A separated analysis pass where cold and guided analyses are run independently so their outputs can be compared without contaminating one with the assumptions of the other.

Isolated Analysis Sandbox answers:

> Did the same finding emerge independently, or only when the investigation was guided by the reported context?

---

### Reference Knowledge Validation

The process of checking whether a knowledge source is authoritative, version-relevant, context-relevant, and directly applicable before it is used to support an insight.

Reference Knowledge Validation answers:

> Can this knowledge source safely support this claim in this environment?

---

## Tooling Terms

| Tool type | Definition |
|---|---|
| Collector | A script, command, or tool that gathers raw source material. |
| Source Transformer | A tool that converts raw material into a structured or queryable form without selecting meaning. |
| Parser | A tool that reads a specific format and exposes fields. |
| Normalizer | A tool that converts values into consistent forms. |
| Indexer | A tool that makes material searchable or queryable. |
| Evidence Extractor | A tool that extracts notable observations from raw or structured source material. |
| Derived Evidence Generator | A tool that computes higher-level observations from source material or evidence. |
| Correlator | A tool that compares observations across time, nodes, components, or sources. |
| Helper | A tool that assists communication, escalation, reporting, or follow-up. |

Example:

`wtl` is a Source Transformer / Log Structuring Tool when it converts logs to parquet without selecting meaning.

A tablet report parser is a hybrid tool if it both structures the report and derives leaderless or under-replicated tablet findings.

---

## Working Language Guidelines

- Use **Evidence Loop** for evidence formation and information synthesis.
- Use **Reasoning Loop** for knowledge application, insight generation, challenge, and judgment.
- Use **Action Loop** for decision, action, outcome, and learning.
- Use **Evidence Sufficiency Gate** to block reasoning from weak evidence.
- Use **Challenge Confidence Gate** to block unsupported insights from becoming judgment.
- Use **Outcome Validation Gate** to block closure when outcomes contradict judgment.
- Use **reported context** for unvalidated problem descriptions.
- Use **collection context** for metadata describing scope, timing, version, source meaning, and collection limitations.
- Use **raw source material** for untouched diagnostic material.
- Use **structured source material** for transformed queryable material that has not yet selected meaning.
- Use **extracted evidence** for selected observations.
- Use **derived evidence** for computed observations.
- Use **information** for observations, timelines, and relationships.
- Use **insight** for candidate explanations.
- Use **challenge** for deliberate testing of insight.
- Use **judgment** for the current best human conclusion under uncertainty.

Avoid treating the framework as a one-way pipeline. Each loop has a gate that can stop, rework, or return the investigation to an earlier stage.
