# EGATF Terminology

**Document type:** Working glossary  
**Status:** Draft v0.3  
**Repository path:** `framework/terminology.md`

---

## Purpose

This document defines the core terms used by the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is to keep the language of the framework consistent as the research evolves.

Some terms are stable. Others are provisional and may change after testing the framework against real examples.

---

## Core Terms

### Reported Context

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

Reported context is useful for direction, but must not be treated as verified cause.

Rule:

> Reported context is guidance, not ground truth.

---

### Raw Source Material

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

Raw source material is not yet information. It must be prepared, extracted, and interpreted.

---

### Evidence Preparation

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

Evidence Preparation answers:

> How do we turn raw source material into a usable evidence base?

Rule:

> Evidence preparation should reduce noise without adding unsupported meaning.

---

### Prepared Evidence Base

The body of prepared material available for analysis after evidence preparation.

A Prepared Evidence Base may contain:

- Structured Source Material
- Parsed Source Material
- Normalized Source Material
- Indexed Source Material
- Extracted Evidence
- Derived Evidence
- Correlated Evidence

Prepared Evidence Base answers:

> What prepared material is available for analysis and reasoning?

---

### Structured Source Material

Raw source material that has been transformed into a more queryable or structured format without deciding what matters.

Examples:

- Logs converted to parquet
- Text reports converted to SQLite tables
- JSON converted to relational tables
- Log lines split into columns

Structured Source Material answers:

> What does the raw material look like after structure has been added?

A tool such as `wtl`, which converts tserver, master, and YBA logs into parquet files without consolidation or filtering, produces Structured Source Material.

It should not be described as producing Extracted Evidence unless it also selects notable observations.

---

### Extracted Evidence

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

Extracted Evidence should include:

- Observation
- Source
- Timestamp or time range
- Component
- Extraction method
- Confidence in source reliability
- Limitations or missing context

---

### Derived Evidence

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

### Correlated Evidence

Evidence produced by comparing observations across time, nodes, components, sources, or reports.

Examples:

- Memory pressure began 3 minutes before restart.
- Leader changes increased after disk latency increased.
- The reported error appears outside the customer-reported time window.
- Node-2 shows the error, but node-1 and node-3 do not.

Correlated Evidence answers:

> What relationship exists between observations?

---

### Evidence

Observable, reported, collected, structured, extracted, derived, or correlated material that can support or challenge a claim.

In EGATF v0.3, Evidence includes:

- Reported Context
- Raw Source Material
- Structured Source Material
- Extracted Evidence
- Derived Evidence
- Correlated Evidence

Evidence answers:

> What was observed, reported, collected, structured, extracted, derived, or correlated?

Evidence should be recorded with enough context that another person can review it independently.

---

### Information

Evidence that has been structured into meaningful observations, timelines, comparisons, or relationships.

Examples:

- Error rate increased after deployment.
- Memory usage reached 98 percent before restart.
- Leader movement began after disk latency increased.
- The same error occurred across three nodes.
- The failure only appeared after a configuration change.
- The reported error appears in logs, but outside the reported time window.

Information answers:

> What happened?

Information must remain linked to the evidence it was derived from.

Information may include interpretation, but should stop short of root cause diagnosis.

---

### Knowledge

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

Knowledge explains how evidence and information may relate.

Knowledge should also be grounded in sources where possible.

---

### Insight

A candidate explanation produced by combining evidence, information, and knowledge.

Examples:

- The restart was likely caused by memory pressure.
- The timeout appears to be downstream of leader instability.
- The latency spike may be related to compaction backlog.
- The observed CDC lag is more consistent with checkpoint behavior than network failure.

Insight answers:

> What might this mean?

An insight is a hypothesis, not yet a conclusion.

---

### Challenge

The deliberate attempt to test, weaken, disprove, or qualify an insight.

Challenge questions include:

- What evidence supports this insight?
- What evidence contradicts this insight?
- What evidence is missing?
- What assumptions does this insight depend on?
- Are there alternative explanations?
- Did the timeline happen in the required order?
- Is the documentation relevant to the correct product version?
- Does the source code support this interpretation?
- Could the same symptoms be caused by something else?
- Did guided analysis anchor the investigation too strongly?
- Did evidence preparation hide, drop, or misclassify material?

Challenge answers:

> Why might this explanation be wrong?

Challenge is currently considered one of the most important and distinctive stages of EGATF.

---

### Wisdom

The current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

Wisdom answers:

> What should we believe, given the evidence and uncertainty?

Status:

**Provisional term.**

Wisdom may be renamed or removed in a future version of the framework if testing shows that it is unclear, unnecessary, or too abstract.

---

### Decision

The selection of a response based on the current best judgment.

Decision answers:

> What will we do next?

A decision should be linked to the insight or judgment that justified it.

---

### Action

The execution of a decision.

Action answers:

> What did we actually do?

Actions should be recorded because outcome analysis depends on knowing what changed.

---

### Outcome

The measured result of an action.

Outcome answers:

> Did it work?

Outcome should feed back into the evidence base.

---

### Learning

Reusable knowledge captured from an investigation.

Learning answers:

> What should future investigations know?

Learning closes the loop by turning one investigation into improved future diagnosis.

---

## Evidence Preparation Operations

### Collection

Gathering raw source material.

Examples:

- Collect support bundle
- Collect logs
- Export metrics
- Capture configuration
- Collect Kubernetes events

Output:

```text
Raw Source Material
```

---

### Transformation

Changing the shape or storage format of source material without deciding what matters.

Examples:

- Convert logs to parquet
- Convert JSON report to SQLite tables
- Convert text report into structured rows
- Split log lines into columns

Output:

```text
Structured Source Material
```

Boundary rule:

> Transformation changes shape. It does not select meaning.

---

### Parsing

Reading a specific format and identifying fields.

Examples:

- Parse timestamp, severity, component, file, line, and message from logs.
- Parse tablet ID, table ID, peer, role, and state from tablet reports.
- Parse metric name, labels, timestamp, and value from metrics.

Output:

```text
Parsed Source Material
```

Parsing may support transformation, extraction, or derivation.

---

### Normalization

Making values consistent across sources.

Examples:

- Normalize timestamps to UTC
- Normalize hostnames
- Normalize node names
- Normalize log severity
- Normalize component names
- Normalize units

Output:

```text
Normalized Source Material
```

---

### Indexing

Making prepared material searchable or queryable.

Examples:

- Load logs into DuckDB
- Create SQLite indexes
- Build search indexes
- Partition parquet files by time or component

Output:

```text
Indexed Source Material
```

---

### Extraction

Selecting or identifying notable observations from raw or structured material.

Examples:

- Find restarts
- Find FATAL log lines
- Find failed backups
- Find memory pressure events
- Find leader changes

Output:

```text
Extracted Evidence
```

Boundary rule:

> Extraction selects observations.

---

### Derivation

Computing higher-level observations from lower-level source material or evidence.

Examples:

- Tablet is leaderless
- Table is under-replicated
- Table is over-replicated
- Node had 17 restarts
- Error rate increased 400 percent

Output:

```text
Derived Evidence
```

Boundary rule:

> Derivation computes observations.

---

### Correlation

Comparing observations across time, nodes, components, or sources.

Examples:

- Compare restart time against memory pressure
- Compare leader changes against disk latency
- Compare reported time window against log evidence
- Compare error rates across nodes

Output:

```text
Correlated Evidence
```

Boundary rule:

> Correlation compares observations.

---

## Tooling Terms

### Collector

A script, command, or tool that gathers raw source material.

---

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

It produces:

```text
Structured Source Material
```

not:

```text
Extracted Evidence
```

unless it also selects notable observations.

---

### Parser

A script, command, or tool that reads a specific format and exposes fields.

A parser may be used by a Source Transformer, Evidence Extractor, or Derived Evidence Generator.

---

### Normalizer

A script, command, or tool that converts values into consistent forms.

---

### Indexer

A script, command, or tool that makes material searchable or queryable.

---

### Evidence Extractor

A script, command, or tool that extracts notable observations from raw or structured source material.

Preferred use:

- Restart extractor
- Fatal error extractor
- Failed backup extractor
- Memory pressure event extractor

---

### Derived Evidence Generator

A script, command, or tool that computes higher-level observations from source material or evidence.

Example:

A tablet report parser that identifies leaderless tablets, under-replicated tables, or over-replicated tables is performing derivation.

If the same tool also converts the raw report into SQLite or parquet, it is a hybrid:

```text
Source Transformer + Derived Evidence Generator
```

---

### Correlator

A script, command, or tool that compares observations across time, nodes, components, or sources.

---

### Helper

A script, command, or tool that assists later workflow tasks after investigation or during communication.

Examples:

- Generate engineering escalation
- Draft customer update
- Create case summary
- Generate post-incident review outline
- Format a bug report

Rule:

> Extractors and correlators prepare evidence. Helpers support communication, escalation, or follow-up.

---

## Boundary Rules

### Transformation versus Extraction

Transformation changes shape.

Extraction selects observations.

Example:

```text
wtl converts raw logs into parquet.
```

This is transformation.

```text
A query finds restart events in the parquet logs.
```

This is extraction.

---

### Extraction versus Derivation

Extraction identifies an observation that exists in the material.

Derivation computes a new observation from available material.

Example:

```text
A tablet report contains peer role data.
```

Extracting peer role data is extraction.

```text
A tablet has no leader.
```

Computing this from peer role data is derivation.

---

### Derivation versus Information

Derivation computes an observation.

Information places observations into context.

Example:

```text
Tablet X is leaderless.
```

This is derived evidence.

```text
Leaderless tablets appeared after tserver-2 restarted and were limited to tables in one placement.
```

This is information.

---

## Analysis Modes

### Cold Analysis

Analysis of raw source material or prepared evidence without using reported context as the primary guide.

Purpose:

- Reduce anchoring bias
- Find unexpected anomalies
- Establish independent observations
- Avoid overfitting to the ticket description

Cold analysis answers:

> What does the material show before we assume the ticket summary is correct?

---

### Guided Analysis

Analysis that uses reported context to guide search, filtering, and extraction.

Purpose:

- Focus on relevant time windows
- Search for reported error messages
- Prioritize affected components
- Verify or reject reported claims

Guided analysis answers:

> What do we find when we use the reported context as search guidance?

Rule:

> Guided analysis should treat reported context as direction, not proof.

---

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
    ↓ optionally guided by
Reported Context
```

---

### Source of Truth

A source considered authoritative for a specific claim.

Examples:

- Product documentation for documented behavior
- Source code for implemented behavior
- Metrics system for observed runtime values
- Logs for emitted runtime events
- Bug tracker for known defects
- Customer report for customer-observed impact

A source of truth is context-dependent.

---

### Unsupported Insight

An insight that sounds plausible but lacks sufficient supporting evidence.

---

### Contradicting Evidence

Evidence that weakens or disproves an insight.

---

### Missing Evidence

Evidence required to support or reject an insight but not currently available.

---

### Assumption

A claim used in reasoning that has not yet been proven by available evidence.

---

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
- Whether cold and guided analysis agree
- Whether derived evidence is supported by clear derivation logic

---

### Hypothesis

A testable candidate explanation.

In EGATF, most insights begin as hypotheses.

---

### Traceability

The ability to move backward and forward through the reasoning chain.

Backward traceability:

> Why did we believe this?

Forward traceability:

> What did this evidence influence?

---

### Auditability

The ability for another person to review the reasoning process and understand how a conclusion was reached.

---

### Human-in-the-Loop

A design principle where humans retain responsibility for judgment, decisions, and actions.

---

### Hallucination

A generated claim that is false, unsupported, or not grounded in the available sources.

---

### Pressure Test

A possible alternative name for the Challenge stage.

---

### Validation

A possible alternative name for the Challenge stage.

---

## Provisional Terms Under Review

| Current Term | Reason Under Review |
|---|---|
| Wisdom | May be too abstract or difficult to distinguish from judgment |
| Challenge | May be renamed to Pressure Test, Validation, or Adversarial Review |
| Knowledge | May need clearer separation between retrieved knowledge and human domain knowledge |
| Insight | May need clearer distinction from hypothesis |
| Evidence | May need subtypes such as reported, direct, indirect, structured, extracted, derived, and authoritative evidence |
| Evidence Preparation | May need to become a named top-level stage |
| Source Transformer | May need a simpler practitioner-facing name |
| Derived Evidence Generator | May need to be shortened |

---

## Working Language Guidelines

When writing about EGATF:

- Use **reported context** for unvalidated problem descriptions.
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
- Use **Source Transformer** for tools like `wtl` that convert raw material into queryable structure.
- Use **Evidence Extractor** for tools that select notable observations.
- Use **Derived Evidence Generator** for tools that compute higher-level observations.
- Use **Helper** for scripts that create follow-up artefacts, summaries, or communications.

Avoid treating structured source material as extracted evidence.

Avoid treating derived evidence as direct evidence.

Avoid treating insights as conclusions until they have passed through challenge.

Avoid treating reported context as verified cause.

Avoid using AI-generated statements as evidence unless they are directly grounded in cited sources.

---

## Open Questions

1. Should wisdom remain as a named stage?
2. Should challenge be renamed for clarity?
3. Should insight and hypothesis be separate terms?
4. Should evidence be classified into multiple levels of reliability?
5. Should confidence use a formal scoring model?
6. How much metadata should be required for an evidence item?
7. How should source authority be represented?
8. How should contradictory evidence be visualized?
9. How should missing evidence affect confidence?
10. What terminology will be clearest to support engineers, SREs, and architects?
11. Should Evidence Preparation become a top-level framework stage?
12. How should cold and guided analysis be compared?
13. How should anchoring risk be measured?
14. How should Evidence Extractors be validated?
15. Should Extractors, Normalizers, and Correlators become formal tool categories?
16. Should Source Transformers and Evidence Extractors have different output schemas?
17. How should hybrid tools label direct, structured, extracted, and derived outputs?

---

## Revision Notes

This draft updates the terminology to include the v0.3 evidence-preparation taxonomy.

Future revisions should be recorded in `framework/changelog.md`.
