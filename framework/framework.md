# Evidence-Grounded AI Troubleshooting Framework

**Working acronym:** EGATF  
**Status:** Draft v0.4  
**Document type:** Canonical framework definition  
**Repository path:** `framework/framework.md`

---

## 1. Purpose

The Evidence-Grounded AI Troubleshooting Framework is a proposed methodology for using AI to assist with technical diagnosis while preserving a clear evidence chain from raw observations to final decisions.

The framework is intended for situations where engineers need to reason across complex technical material such as support bundles, logs, metrics, traces, dumps, source code, documentation, bug reports, ticket summaries, customer observations, and historical incidents.

The purpose is not to make AI the final decision maker.

The purpose is to make AI useful while keeping its reasoning auditable, challengeable, and grounded in evidence.

---

## 2. Problem Statement

AI systems are increasingly capable of reading large volumes of technical material and producing plausible explanations.

However, plausible explanations are not enough in technical diagnosis.

In support engineering, incident response, reliability engineering, and distributed systems troubleshooting, a conclusion must be supported by evidence. An unsupported explanation can waste time, mislead engineers, damage customer trust, or result in unsafe operational changes.

The core problem is:

> AI is often better at generating explanations than demonstrating why those explanations should be trusted.

EGATF explores whether a structured evidence-first workflow can reduce unsupported reasoning and improve the quality of AI-assisted diagnosis.

---

## 3. Research Question

Can AI-assisted troubleshooting be made more reliable by requiring every conclusion to be traceable back to evidence and every insight to survive deliberate challenge before influencing decisions?

---

## 4. Core Principle

Every insight must be traceable to evidence, and every piece of evidence must be traceable to the insight it supports.

This means:

- No insight should stand alone without supporting evidence.
- No evidence should be used without clear relevance.
- No conclusion should be accepted until it has been challenged.
- No action should be taken solely because an explanation sounds plausible.
- Reported context should guide investigation, not replace verification.
- Collection context should describe scope, timing, version, source meaning, and limitations.
- Prepared evidence should preserve provenance back to raw source material.
- Evidence preparation should reduce noise without introducing unsupported diagnosis.

In short:

> Without evidence, an insight is speculation.  
> Without traceability, an insight cannot be trusted.  
> Without challenge, an insight cannot become wisdom.

Collection-context principle:

> Evidence packages should describe their own collection context. AI should not be asked to infer timing, scope, source meaning, or collection limitations from raw files alone.

---

## 5. Draft Framework

Current draft sequence:

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

This sequence is experimental. The names, ordering, and definitions may change as the framework is tested against real examples.

The stage most likely to change is **Wisdom**. The stage currently believed to be most distinctive is **Challenge**.

---

## 6. Evidence Stage Refinement

The Evidence stage is treated as a set of sub-stages:

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

The Prepared Evidence Base may contain:

- Structured Source Material
- Extracted Evidence
- Derived Evidence
- Correlated Evidence

---

## 7. Reported Context

Reported context is an unvalidated description of the problem.

Examples:

- Customer ticket summary
- Customer-provided error message
- First responder notes
- Alert description
- Support engineer initial observation
- Problem statement copied from an escalation

Reported context is useful because it tells the investigation where to begin.

However, reported context must not be treated as verified cause.

Example:

> The database became slow after the upgrade.

This contains several different claims:

| Claim | Initial Treatment |
|---|---|
| The customer experienced slowness | Reported symptom |
| The issue occurred after the upgrade | Timeline claim to verify |
| The upgrade caused the issue | Causal hypothesis only |
| The database was the source of the problem | Component hypothesis only |
| The system was "slow" | Needs measurement |

Rule:

> Reported context is guidance, not ground truth.

---

## 8. Collection Context

Collection Context describes how an evidence package was created and how its contents should be interpreted.

In support-bundle analysis, the support bundle is not just a bag of files. It is a time-bounded evidence package created by a particular collector version, from a particular environment, with different data sources captured from different effective times.

Collection Context answers:

> What was collected, when was it collected, from what environment, using which collector, and what does each source represent?

Examples:

- Support bundle version
- Support bundle schema version
- Bundle creation time
- Requested bundle collection window
- Actual collection windows per component
- Universe name and UUID
- Universe YBDB version at collection time
- YBA instance and YBA version at collection time
- Replication factor and node counts
- Deployment type
- Infrastructure type
- Provider
- Node Agent enabled state
- Metric collection level
- Metric collection duration and resolution
- Included components
- Component descriptions
- File index
- Known gaps or limitations

Collection Context should distinguish between:

- Data representing the requested support bundle duration
- Data representing bundle creation time
- Data using a different metrics-specific duration
- Mixed data sources

Example:

```text
Logs:
Represent the requested support bundle duration.

Metrics:
May represent a metrics-specific duration and resolution.

Tablet metadata:
Represents collection-time snapshot.

Consensus metadata:
Represents collection-time snapshot.

Tablet report:
Represents collection-time snapshot.

YBA metadata:
May be mixed. Some values represent current YBA state at collection time.
```

This distinction is critical because AI may otherwise correlate material from incompatible time windows.

Example risk:

```text
Support bundle created at T.

Logs collected for T - 7 days to T - 5 days.

Tablet report collected at T.

Incorrect conclusion:
Tablet state at T explains log events from T - 7 to T - 5.

Correct handling:
Tablet report is collection-time evidence and may not represent the tablet state during the log window.
```

Rule:

> Collection Context is part of the evidence chain. It is not diagnosis, but it constrains how evidence may safely be interpreted.

---

## 9. Evidence Package Manifest

An Evidence Package Manifest is a machine-readable description of a collected evidence package.

For support bundles, this may be implemented as an expanded `manifest.json`, or as a combination of:

```text
manifest.json
bundle_context.json
file_index.json
```

The manifest should help humans, deterministic tools, and AI understand:

- What was collected
- When each component was collected
- Which system versions are represented
- Which collection software produced the bundle
- What each component means
- Which files and directories are present
- Which evidence sources reflect the requested time window
- Which evidence sources reflect collection time
- Which evidence sources have known limitations

The manifest should not attempt to diagnose the issue.

It should describe the evidence package, not explain the root cause.

---

## 10. Cold and Guided Analysis

EGATF distinguishes between cold analysis and guided analysis.

### Cold Analysis

Cold analysis reviews raw source material or prepared evidence without using the reported problem as the primary guide.

Purpose:

- Reduce anchoring bias
- Find unexpected anomalies
- Avoid overfitting to the ticket description
- Establish independent observations

### Guided Analysis

Guided analysis uses reported context to direct search and extraction.

Purpose:

- Focus on relevant time windows
- Search for reported error messages
- Prioritize affected components
- Validate or reject the customer-reported pattern

Recommended workflow:

```text
Cold pass
    ↓
Guided pass
    ↓
Compare findings
    ↓
Record agreements, differences, and surprises
```

---

## 11. Raw Source Material

Raw source material is the untouched diagnostic material available to the investigation.

Examples:

- Support bundle archive
- Log files
- Metrics export
- Trace export
- Core dump
- Configuration dump
- `kubectl` output
- Database metadata
- Ticket text
- Screenshots
- Source code snapshot
- Documentation pages
- Bug report contents

Raw source material is not yet information.

It is the material from which an evidence base may be prepared.

---

## 12. Evidence Preparation

Evidence Preparation is the process of making raw source material easier to inspect, query, compare, and reason about while preserving provenance.

Evidence Preparation is a broad activity. It includes:

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

### Collection

Collection gathers raw source material.

Output:

```text
Raw Source Material
```

### Transformation

Transformation changes the shape or storage format of source material without deciding what matters.

Examples:

- Convert log files into parquet
- Convert JSON report into SQLite tables
- Convert text report into structured rows
- Split log lines into columns
- Store raw events in a queryable database

Output:

```text
Structured Source Material
```

A log structuring tool such as `wtl`, which converts tserver, master, and YBA logs into parquet columns without filtering or consolidation, is best classified as:

```text
Source Transformer / Log Structuring Tool
```

It does not primarily produce Extracted Evidence. It produces Structured Source Material that can later be queried.

### Parsing

Parsing reads a specific source format and identifies fields.

Examples:

- Parse timestamp, severity, component, file, line, and message from a log line
- Parse tablet ID, table ID, peer, role, and state from a tablet report
- Parse metric name, labels, timestamp, and value from a metrics export

Parsing often supports transformation, extraction, or both.

### Normalization

Normalization makes values consistent across sources.

Examples:

- Normalize timestamps to UTC
- Normalize hostnames
- Normalize node names
- Normalize log severity
- Normalize component names
- Normalize units

### Indexing

Indexing makes prepared material searchable or queryable.

Examples:

- Load logs into DuckDB
- Create SQLite indexes
- Build search index over log messages
- Partition parquet files by time or component

### Extraction

Extraction selects or identifies observations that may matter to an investigation.

Examples:

- Find restart events
- Find FATAL log lines
- Find failed backups
- Find memory pressure events
- Find leader changes
- Find tablets with no leader

Output:

```text
Extracted Evidence
```

### Derivation

Derivation computes higher-level observations from lower-level source material or extracted evidence.

Examples:

- Tablet is leaderless
- Table is under-replicated
- Table is over-replicated
- Node had 17 restarts
- Error rate increased 400 percent
- Leader movement followed disk latency increase

Output:

```text
Derived Evidence
```

A tablet report parser that both structures a raw tablet report and identifies leaderless, over-replicated, or under-replicated tables is a hybrid tool:

```text
Source Transformer + Derived Evidence Generator
```

Conceptually, its outputs should distinguish direct structured source tables from derived evidence or findings.

### Correlation

Correlation compares evidence across time, components, nodes, or sources.

Examples:

- Compare restart time against memory pressure
- Compare leader changes against disk latency
- Compare customer-reported time window against log evidence
- Compare error rates across nodes
- Compare cold analysis findings against guided analysis findings

Output:

```text
Correlated Evidence
```

---

## 13. Boundary Rules

### Rule 1: Transformation changes shape

Transformation changes the format or structure of source material.

It does not decide what matters.

### Rule 2: Extraction selects observations

Extraction identifies notable observations from raw or structured material.

### Rule 3: Derivation computes new observations

Derivation computes a higher-level observation from lower-level facts.

### Rule 4: Correlation compares observations

Correlation identifies relationships across observations.

### Rule 5: Information explains context

Information places evidence into a meaningful narrative, timeline, comparison, or relationship.

Short version:

```text
Transformation changes shape.
Extraction selects observations.
Derivation computes observations.
Correlation compares observations.
Information explains relationships.
```

---

## 14. Tooling Taxonomy

| Tool Type | Purpose | Example |
|---|---|---|
| Collector | Collects raw source material | support bundle collector |
| Source Transformer | Converts raw material into queryable structure without selecting meaning | `wtl` log to parquet |
| Parser | Reads a specific format and exposes fields | log parser, tablet report parser |
| Normalizer | Standardizes values across sources | timestamp or hostname normalization |
| Indexer | Makes source material searchable or queryable | DuckDB catalogue, SQLite indexes |
| Evidence Extractor | Pulls out notable observations | restart extractor, fatal error extractor |
| Derived Evidence Generator | Computes higher-level observations | leaderless tablet detector |
| Correlator | Compares observations across time, nodes, or components | restart versus latency correlation |
| Helper | Produces later workflow artefacts | escalation summary, customer update |

Rule:

> Extractors, derivation tools, and correlators support evidence preparation. Helpers support communication, escalation, or follow-up.

---

## 15. Stage Definitions

### Evidence

Evidence is observable or authoritative material that can support or challenge a claim.

In v0.4, Evidence includes:

- Reported context
- Collection context
- Raw source material
- Structured source material
- Extracted evidence
- Derived evidence
- Correlated evidence

Evidence answers:

> What was observed, reported, collected, structured, extracted, derived, or correlated?

Useful metadata includes:

- Source
- Timestamp
- System or component
- Version
- Collection method
- Collection window
- Preparation method
- Extraction method
- Derivation logic
- Confidence in source reliability
- Whether the evidence is reported, collection context, direct, indirect, structured, extracted, derived, or correlated

### Information

Information is evidence that has been structured into meaningful observations, timelines, comparisons, or relationships.

Examples:

- Error count increased after deployment.
- Memory usage reached 98 percent before the service restarted.
- Leader movement began 17 seconds after disk latency increased.
- The same error appears on three nodes, but not on the fourth.
- Tablet metadata is not valid evidence for the requested log window because it was collected later at bundle creation time.

Information answers:

> What happened?

Information must remain linked to the evidence it was derived from.

Information can include interpretation, but should stop short of root cause diagnosis.

### Knowledge

Knowledge is contextual understanding derived from trusted sources.

Examples:

- Product documentation explaining expected behavior
- Source code showing actual implementation behavior
- Known bug reports
- Architecture diagrams
- Previous incidents
- Operational runbooks
- Domain expertise

Knowledge answers:

> How does this system behave?

### Insight

Insight is a candidate explanation produced by combining evidence, information, and knowledge.

An insight is not yet a conclusion.

At this stage, an insight should be treated as a hypothesis.

Insight answers:

> What might this mean?

### Challenge

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an insight.

Challenge questions include:

- What evidence supports this insight?
- What evidence contradicts this insight?
- What evidence is missing?
- What assumptions does this insight depend on?
- Are there alternative explanations?
- Did the timeline happen in the required order?
- Did evidence preparation tools hide, drop, or misclassify relevant material?
- Did AI confuse collection-time evidence with duration-based evidence?
- Did AI use tablet metadata, consensus metadata, or tablet reports outside their valid time context?

Challenge answers:

> Why might this explanation be wrong?

### Wisdom

Wisdom is the current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

This stage is intentionally tentative.

Wisdom may eventually be renamed or removed.

Wisdom answers:

> What should we believe, given the evidence and uncertainty?

### Decision

Decision is the selection of a response based on the current best judgment.

Decision answers:

> What will we do next?

### Action

Action is the execution of the decision.

Action answers:

> What did we actually do?

### Outcome

Outcome is the measured result of an action.

Outcome answers:

> Did it work?

### Learning

Learning is the capture of reusable knowledge from the investigation.

Learning answers:

> What should future investigations know?

---

## 16. Evidence Chain Requirements

For an EGATF investigation to be considered evidence-grounded, it should be possible to trace backward from any decision to the evidence that supported it.

Example trace:

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

A well-formed evidence chain should show:

- Which reported context was used
- Which collection context constrained interpretation
- Which raw source material was available
- Which collection windows applied
- Which preparation methods were applied
- Which tools were used
- Which outputs were structured source material
- Which outputs were extracted evidence
- Which outputs were derived evidence
- Which outputs were correlated evidence
- Which information was produced
- Which knowledge sources were applied
- Which insights were generated
- Which challenges were performed
- Which uncertainty remained
- Why a decision was made
- What action was taken
- What outcome resulted

---

## 17. AI Roles in the Framework

AI may assist at multiple stages, but should not be treated as equally reliable at every stage.

### Reported Context

AI can decompose ticket summaries into symptoms, timeline claims, component claims, and causal claims.

Risk:

- Treating reported cause as verified truth
- Anchoring on customer wording
- Missing ambiguity in the report

### Collection Context

AI can use the manifest to understand scope, timing, component meaning, versions, collection windows, and known limitations.

Risk:

- Ignoring collection windows
- Confusing requested log duration with collection-time snapshots
- Treating absent components as absent problems without checking collection scope
- Mixing YBA version and YBDB version

### Raw Source Material

AI can inspect samples, identify file types, and suggest preparation paths.

Risk:

- Token waste
- Missing important files
- Overfitting to noisy data

### Evidence Preparation

AI can help design transformers, parsers, extractors, filters, and correlation scripts.

Risk:

- Scripts may encode assumptions
- Extractors may omit important signals
- Generated parsing logic may be wrong
- Derived evidence may be mistaken for direct evidence

### Prepared Evidence Base

AI can summarize prepared evidence and identify gaps.

Risk:

- Overstating reliability
- Losing provenance
- Converting observations into diagnosis too early

### Information

AI can summarize, normalize, deduplicate, cluster, and timeline observations.

Risk:

- Over-compression
- Loss of important detail
- Incorrect grouping

### Knowledge

AI can retrieve relevant documentation, code, bug reports, and prior incidents.

Risk:

- Using outdated sources
- Mixing versions
- Confusing similar concepts

### Insight

AI can generate hypotheses and candidate explanations.

Risk:

- Hallucination
- Overconfidence
- Plausible but unsupported explanations

### Challenge

AI can adversarially test its own hypotheses.

Risk:

- Weak challenge if prompted poorly
- Missing alternative causes
- Confirmation bias from earlier context

### Wisdom

AI can assist human judgment, but should not replace accountability.

Risk:

- Over-delegation
- False confidence
- Treating probability as certainty

### Decision and Action

AI can suggest options and consequences.

Risk:

- Unsafe operational changes
- Ignoring business or customer context
- Acting without sufficient authority

### Outcome and Learning

AI can summarize results and generate reusable artifacts.

Risk:

- Capturing incorrect lessons
- Institutionalizing a false root cause

---

## 18. Intended Use Cases

EGATF is intended for complex technical diagnosis where evidence quality matters.

Possible use cases include:

- Support bundle analysis
- Incident response
- Root cause analysis
- Distributed database troubleshooting
- Kubernetes platform investigations
- Performance investigations
- Reliability engineering
- Security investigations
- Customer support escalation
- Software defect analysis
- Post-incident reviews

---

## 19. Non-Goals

EGATF is not intended to be:

- A replacement for experienced engineers
- A fully automated RCA system
- A guarantee of correctness
- A generic prompt template
- A vendor-specific AIOps architecture
- A claim that AI can safely diagnose without human review
- A reason to trust customer-reported cause without verification
- A reason to trust prepared data without provenance
- A reason to treat derived evidence as direct evidence
- A reason to ignore collection windows or component-specific timing

The framework is intended to improve reasoning discipline, not remove human responsibility.

---

## 20. Open Questions

1. Should **Wisdom** remain as a distinct stage?
2. Should **Challenge** be renamed to Validation, Adversarial Review, or Pressure Test?
3. Should Evidence and Information remain top-level stages, with sub-stages inside Evidence?
4. Should Collection Context become a top-level framework stage?
5. Should Evidence Preparation become a top-level framework stage?
6. How should confidence be represented?
7. How should reported context be scored?
8. How should contradictory evidence be tracked?
9. What metadata is required for a useful evidence item?
10. Can the framework be applied consistently across different technical domains?
11. Does the Challenge stage measurably improve outcomes?
12. How should case studies be anonymized and sanitized?
13. What is the smallest useful tool that could support the workflow?
14. How should extractor quality be tested?
15. How should cold and guided analysis findings be compared?
16. How should anchoring risk be represented?
17. How should Source Transformer output be distinguished from Extracted Evidence?
18. Should Derived Evidence have a formal confidence model?
19. Should hybrid tools expose separate output layers?
20. Should support bundle manifests include AI-friendly content descriptions?
21. Should support bundle manifests include component-specific collection window semantics?
22. Should support bundle manifests include schema versions for parser compatibility?

---

## 21. Success Criteria

The framework will be considered useful if it helps practitioners:

- Find unsupported AI conclusions earlier
- Preserve evidence chains
- Improve diagnostic confidence
- Reduce hallucination-driven troubleshooting errors
- Compare competing hypotheses more clearly
- Record uncertainty explicitly
- Convert investigations into reusable learning
- Improve collaboration between humans and AI during diagnosis
- Separate reported context from verified evidence
- Separate collection context from raw source material
- Reduce anchoring bias from guided statements
- Produce cleaner evidence for AI analysis without losing provenance
- Distinguish transformation from extraction
- Distinguish extracted evidence from derived evidence
- Avoid false correlations across incompatible collection windows
- Help deterministic tools select appropriate parsers based on support bundle schema version

The most important validation question is:

> Does introducing a formal Challenge stage improve the quality and trustworthiness of AI-assisted troubleshooting?

A second important validation question is:

> Does evidence preparation improve AI-assisted diagnosis by reducing noise while preserving traceability?

A third validation question is:

> Does classifying preparation tools by function reduce confusion and prevent prepared data from being mistaken for diagnosis?

A fourth validation question is:

> Does explicit collection context reduce AI errors caused by time-window confusion, version confusion, or misunderstanding of support bundle contents?

---

## 22. Current Status

This document is an early draft.

It should be treated as a working hypothesis for review, criticism, and testing against real diagnostic examples.

Future revisions should be recorded in `framework/changelog.md`.
