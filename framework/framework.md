# Evidence-Grounded AI Troubleshooting Framework

**Working acronym:** EGATF  
**Status:** Draft v0.3  
**Document type:** Canonical framework definition  
**Repository path:** `framework/framework.md`

---

## 1. Purpose

The Evidence-Grounded AI Troubleshooting Framework is a proposed methodology for using AI to assist with technical diagnosis while preserving a clear evidence chain from raw observations to final decisions.

The framework is intended for situations where engineers need to reason across complex technical material such as:

- Support bundles
- Application logs
- System logs
- Metrics
- Traces
- Core dumps
- Database dumps
- Source code
- Product documentation
- Bug reports
- Ticket summaries
- Customer observations
- Historical incidents

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
- Prepared evidence should preserve provenance back to raw source material.
- Evidence preparation should reduce noise without introducing unsupported diagnosis.

In short:

> Without evidence, an insight is speculation.  
> Without traceability, an insight cannot be trusted.  
> Without challenge, an insight cannot become wisdom.

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

The first major refinement to EGATF is that **Evidence** is not a single simple thing.

At the beginning of a support investigation there may be:

- A customer ticket summary
- A first responder description
- An alert title
- An error message
- A support bundle
- Live access to logs or metrics
- A snapshot of command output
- A set of observations from an engineer

These inputs have different levels of reliability.

For that reason, the Evidence stage is treated as a set of sub-stages:

```text
Reported Context
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

## 8. Cold and Guided Analysis

EGATF distinguishes between cold analysis and guided analysis.

### Cold Analysis

Cold analysis reviews raw source material or prepared evidence without using the reported problem as the primary guide.

Purpose:

- Reduce anchoring bias
- Find unexpected anomalies
- Avoid overfitting to the ticket description
- Establish independent observations

Example instruction to AI:

```text
Review the provided material without assuming the reported cause is correct. Identify notable events, anomalies, timelines, and correlations. Do not diagnose yet.
```

### Guided Analysis

Guided analysis uses reported context to direct search and extraction.

Purpose:

- Focus on relevant time windows
- Search for reported error messages
- Prioritize affected components
- Validate or reject the customer-reported pattern

Example instruction to AI:

```text
Use the reported context as search guidance only. Treat all reported causal claims as unverified hypotheses. Verify each claim against raw source material or prepared evidence before using it as evidence.
```

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

This helps separate what the material shows from what the initial report suggested.

---

## 9. Raw Source Material

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

## 10. Evidence Preparation

Evidence Preparation is the process of making raw source material easier to inspect, query, compare, and reason about while preserving provenance.

Evidence Preparation is a broad activity. It includes several different operations:

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

These operations should not be collapsed into one term because they have different meanings and produce different kinds of output.

### 10.1 Collection

Collection gathers raw source material.

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

### 10.2 Transformation

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

Example:

```text
tserver.log
    ↓ Source Transformer
logs.parquet
```

A log structuring tool such as `wtl`, which converts tserver, master, and YBA logs into parquet columns without filtering or consolidation, is best classified as:

```text
Source Transformer / Log Structuring Tool
```

It does not primarily produce Extracted Evidence. It produces Structured Source Material that can later be queried.

### 10.3 Parsing

Parsing reads a specific source format and identifies fields.

Examples:

- Parse timestamp, severity, component, file, line, and message from a log line
- Parse tablet ID, table ID, peer, role, and state from a tablet report
- Parse metric name, labels, timestamp, and value from a metrics export

Parsing often supports transformation, extraction, or both.

Output:

```text
Parsed Source Material
```

### 10.4 Normalization

Normalization makes values consistent across sources.

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

### 10.5 Indexing

Indexing makes prepared material searchable or queryable.

Examples:

- Load logs into DuckDB
- Create SQLite indexes
- Build search index over log messages
- Partition parquet files by time or component

Output:

```text
Indexed Source Material
```

### 10.6 Extraction

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

Extraction answers:

> What notable observations can be pulled out of the prepared material?

### 10.7 Derivation

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

Derivation answers:

> What computed observation follows from the available evidence?

A tablet report parser that both structures a raw tablet report and identifies leaderless, over-replicated, or under-replicated tables is a hybrid tool:

```text
Source Transformer + Derived Evidence Generator
```

Conceptually, its outputs should distinguish direct structured source tables from derived evidence or findings.

### 10.8 Correlation

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

Correlation answers:

> What relationships exist between observations?

---

## 11. Boundary Rules

The following boundary rules help classify tools and outputs.

### Rule 1: Transformation changes shape

Transformation changes the format or structure of source material.

It does not decide what matters.

Example:

```text
raw logs
    ↓
parquet tables
```

### Rule 2: Extraction selects observations

Extraction identifies notable observations from source material or structured source material.

Example:

```text
logs.parquet
    ↓
restart events
```

### Rule 3: Derivation computes new observations

Derivation computes a higher-level observation from lower-level facts.

Example:

```text
tablet peers and roles
    ↓
tablet is leaderless
```

### Rule 4: Correlation compares observations

Correlation identifies relationships across observations.

Example:

```text
restart event + memory pressure metric
    ↓
memory pressure preceded restart by 3 minutes
```

### Rule 5: Information explains context

Information places evidence into a meaningful narrative, timeline, comparison, or relationship.

Example:

```text
The reported error appears in the logs, but only after the first tserver restart.
```

Short version:

```text
Transformation changes shape.
Extraction selects observations.
Derivation computes observations.
Correlation compares observations.
Information explains relationships.
```

---

## 12. Tooling Taxonomy

EGATF distinguishes between several types of scripts and tools.

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

## 13. Stage Definitions

### 13.1 Evidence

Evidence is observable or authoritative material that can support or challenge a claim.

In v0.3, Evidence includes:

- Reported context
- Raw source material
- Structured source material
- Extracted evidence
- Derived evidence
- Correlated evidence

Evidence answers:

> What was observed, reported, collected, structured, extracted, derived, or correlated?

Evidence should be captured with enough context to be independently reviewed.

Useful metadata includes:

- Source
- Timestamp
- System or component
- Version
- Collection method
- Preparation method
- Extraction method
- Derivation logic
- Confidence in source reliability
- Whether the evidence is reported, direct, indirect, structured, extracted, derived, or correlated

### 13.2 Information

Information is evidence that has been structured into meaningful observations, timelines, comparisons, or relationships.

Examples:

- Error count increased after deployment.
- Memory usage reached 98 percent before the service restarted.
- Leader movement began 17 seconds after disk latency increased.
- The same error appears on three nodes, but not on the fourth.
- The failing code path is only used when a specific feature flag is enabled.
- The reported error message appears in logs, but outside the reported time window.

Information answers:

> What happened?

Information must remain linked to the evidence it was derived from.

Information can include interpretation, but should stop short of root cause diagnosis.

### 13.3 Knowledge

Knowledge is contextual understanding derived from trusted sources.

Examples:

- Product documentation explaining expected behavior
- Source code showing actual implementation behavior
- Known bug reports
- Architecture diagrams
- Previous incidents
- Operational runbooks
- Domain expertise

Knowledge explains how evidence and information may relate.

Knowledge answers:

> How does this system behave?

Knowledge must also be grounded. The source of knowledge should be recorded wherever possible.

### 13.4 Insight

Insight is a candidate explanation produced by combining evidence, information, and knowledge.

Examples:

- The restart was likely caused by memory pressure.
- The customer-visible timeout appears to be downstream of leader instability.
- The increased write latency may be caused by compaction backlog.
- The observed CDC lag is more consistent with idle-table checkpoint behavior than network failure.

An insight is not yet a conclusion.

At this stage, an insight should be treated as a hypothesis.

Insight answers:

> What might this mean?

### 13.5 Challenge

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an insight.

This is the defining stage of the framework.

Challenge questions include:

- What evidence supports this insight?
- What evidence contradicts this insight?
- What evidence is missing?
- What assumptions does this insight depend on?
- Are there alternative explanations?
- Did the timeline happen in the required order?
- Is the cited documentation relevant to this version?
- Does the source code support this interpretation?
- Could the same symptoms be caused by something else?
- Did guided analysis anchor the investigation too strongly?
- Did cold analysis find anomalies that guided analysis missed?
- Did evidence preparation tools hide, drop, or misclassify relevant material?
- What would we expect to see if this insight were true?
- What would we expect to see if this insight were false?

Challenge answers:

> Why might this explanation be wrong?

A useful challenge stage should produce one of several outcomes:

- Insight strengthened
- Insight weakened
- Insight rejected
- Insight split into multiple hypotheses
- More evidence required
- Alternative explanation preferred

### 13.6 Wisdom

Wisdom is the current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

This stage is intentionally tentative.

Wisdom may eventually be renamed or removed.

For now, wisdom represents the transition from AI-assisted reasoning to responsible human judgment.

Wisdom answers:

> What should we believe, given the evidence and uncertainty?

Wisdom should include:

- Confidence level
- Remaining uncertainty
- Known assumptions
- Risk of being wrong
- Consequences of action
- Whether more evidence is required

### 13.7 Decision

Decision is the selection of a response based on the current best judgment.

Examples:

- Collect more logs.
- Escalate to engineering.
- Apply a known workaround.
- Change configuration.
- Roll back a release.
- Open a bug.
- Communicate a suspected cause to a customer.
- Take no immediate action and continue observing.

Decision answers:

> What will we do next?

A decision should be linked to the insight or judgment that justified it.

### 13.8 Action

Action is the execution of the decision.

Examples:

- Restarting a service
- Applying a patch
- Changing a timeout
- Running a diagnostic command
- Capturing a core dump
- Enabling additional logging
- Opening a pull request
- Updating a runbook
- Communicating to stakeholders

Action answers:

> What did we actually do?

Actions should be recorded because later outcome analysis depends on knowing what changed.

### 13.9 Outcome

Outcome is the measured result of an action.

Examples:

- Error rate decreased.
- Latency returned to baseline.
- The issue reproduced again.
- The workaround failed.
- The customer impact stopped.
- A new failure mode appeared.
- The hypothesis was disproven.

Outcome answers:

> Did it work?

Outcome should feed back into the evidence base.

A failed action is not wasted effort if it improves the evidence chain.

### 13.10 Learning

Learning is the capture of reusable knowledge from the investigation.

Examples:

- Knowledge base article
- Runbook update
- Bug report
- Test case
- Monitoring rule
- Alert improvement
- Documentation correction
- Source code comment
- Training example
- Case study

Learning answers:

> What should future investigations know?

Learning closes the loop by turning one investigation into improved future diagnosis.

---

## 14. Evidence Chain Requirements

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
    ↓ optionally guided by
Reported Context
```

A well-formed evidence chain should show:

- Which reported context was used
- Which raw source material was available
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

## 15. AI Roles in the Framework

AI may assist at multiple stages, but should not be treated as equally reliable at every stage.

### Reported Context

AI can decompose ticket summaries into symptoms, timeline claims, component claims, and causal claims.

Risk:

- Treating reported cause as verified truth
- Anchoring on customer wording
- Missing ambiguity in the report

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

## 16. Intended Use Cases

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

## 17. Non-Goals

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

The framework is intended to improve reasoning discipline, not remove human responsibility.

---

## 18. Open Questions

The framework is still experimental. Current open questions include:

1. Should **Wisdom** remain as a distinct stage?
2. Should **Challenge** be renamed to Validation, Adversarial Review, or Pressure Test?
3. Should Evidence and Information remain top-level stages, with sub-stages inside Evidence?
4. Should Evidence Preparation become a top-level framework stage?
5. How should confidence be represented?
6. How should reported context be scored?
7. How should contradictory evidence be tracked?
8. What metadata is required for a useful evidence item?
9. Can the framework be applied consistently across different technical domains?
10. Does the Challenge stage measurably improve outcomes?
11. How should case studies be anonymized and sanitized?
12. What is the smallest useful tool that could support the workflow?
13. How should extractor quality be tested?
14. How should cold and guided analysis findings be compared?
15. How should anchoring risk be represented?
16. How should Source Transformer output be distinguished from Extracted Evidence?
17. Should Derived Evidence have a formal confidence model?
18. Should hybrid tools expose separate output layers?

---

## 19. Success Criteria

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
- Reduce anchoring bias from guided statements
- Produce cleaner evidence for AI analysis without losing provenance
- Distinguish transformation from extraction
- Distinguish extracted evidence from derived evidence

The most important validation question is:

> Does introducing a formal Challenge stage improve the quality and trustworthiness of AI-assisted troubleshooting?

A second important validation question is:

> Does evidence preparation improve AI-assisted diagnosis by reducing noise while preserving traceability?

A third validation question is:

> Does classifying preparation tools by function reduce confusion and prevent prepared data from being mistaken for diagnosis?

---

## 20. Current Status

This document is an early draft.

It should be treated as a working hypothesis for review, criticism, and testing against real diagnostic examples.

Future revisions should be recorded in `framework/changelog.md`.
