# Evidence-Grounded AI Troubleshooting Framework

**Working acronym:** EGATF  
**Status:** Draft v0.2  
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
- Prepared evidence should preserve provenance back to raw source material.

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

At the beginning of a support investigation there may be a customer ticket summary, first responder description, alert title, error message, support bundle, live access to logs or metrics, command output, or observations from an engineer.

These inputs have different levels of reliability.

For that reason, the Evidence stage is now treated as a set of sub-stages:

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

### 6.1 Reported Context

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

### 6.2 Cold and Guided Analysis

EGATF distinguishes between cold analysis and guided analysis.

Cold analysis reviews raw source material without using the reported problem as the primary guide.

Purpose:

- Reduce anchoring bias
- Find unexpected anomalies
- Avoid overfitting to the ticket description
- Establish independent observations

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

This helps separate what the data says from what the initial report suggested.

### 6.3 Raw Source Material

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

It is the material from which evidence may be extracted.

### 6.4 Evidence Preparation

Evidence preparation is the process of extracting, filtering, parsing, normalizing, indexing, and correlating raw source material without adding unsupported diagnosis.

Examples:

- Extract restart events
- Extract ERROR and FATAL log lines
- Parse version and build information
- Extract configuration values
- Build a node inventory
- Build a timeline of process starts and stops
- Extract top metric anomalies
- Group repeated stack traces
- Normalize timestamps to UTC
- Compare events across nodes
- Identify gaps in available data

Evidence preparation should reduce noise while preserving provenance.

Rule:

> Evidence preparation should make raw material easier to reason about without turning observations into unsupported conclusions.

### 6.5 Extracted Evidence

Extracted evidence is a clean observation with provenance back to raw source material.

Examples:

```text
At 2026-06-21 10:14:22 UTC, tserver-3 restarted.
Source: tserver.log line 18422.
```

```text
CPU usage on node-2 exceeded 95 percent for 11 minutes.
Source: metrics.csv, node=node-2, time window 10:03 to 10:14 UTC.
```

```text
The flag ysql_output_buffer_size was set to 262144.
Source: gflags.json.
```

Extracted evidence should include:

- Observation
- Source
- Timestamp or time range
- Component
- Extraction method
- Confidence in source reliability
- Any limitations or missing context

Extracted evidence is still not diagnosis.

It is the prepared factual base used to produce information.

---

## 7. Stage Definitions

### 7.1 Evidence

Evidence is observable or authoritative material that can support or challenge a claim.

In v0.2, Evidence includes:

- Reported context
- Raw source material
- Prepared evidence
- Extracted evidence

Evidence answers:

> What was observed, reported, collected, or extracted?

Evidence should be captured with enough context to be independently reviewed.

Useful metadata includes source, timestamp, component, version, collection method, extraction method, confidence in source reliability, and whether the evidence is direct, indirect, reported, or derived.

### 7.2 Information

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

### 7.3 Knowledge

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

Knowledge must also be grounded. The source of knowledge should be recorded wherever possible.

### 7.4 Insight

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

### 7.5 Challenge

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an insight.

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

Challenge answers:

> Why might this explanation be wrong?

A useful challenge stage should produce one of several outcomes:

- Insight strengthened
- Insight weakened
- Insight rejected
- Insight split into multiple hypotheses
- More evidence required
- Alternative explanation preferred

### 7.6 Wisdom

Wisdom is the current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

This stage is intentionally tentative.

Wisdom may eventually be renamed or removed.

For now, wisdom represents the transition from AI-assisted reasoning to responsible human judgment.

Wisdom answers:

> What should we believe, given the evidence and uncertainty?

Wisdom should include confidence level, remaining uncertainty, known assumptions, risk of being wrong, consequences of action, and whether more evidence is required.

### 7.7 Decision

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

### 7.8 Action

Action is the execution of the decision.

Examples include restarting a service, applying a patch, changing a timeout, running a diagnostic command, capturing a core dump, enabling additional logging, opening a pull request, updating a runbook, or communicating to stakeholders.

Action answers:

> What did we actually do?

Actions should be recorded because later outcome analysis depends on knowing what changed.

### 7.9 Outcome

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

### 7.10 Learning

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

## 8. Evidence Preparation Tools

EGATF distinguishes between several types of scripts and tools.

### Collectors

Collectors gather raw source material from live systems or external sources.

Examples:

- Collect logs
- Export metrics
- Capture configuration
- Collect Kubernetes events
- Download support bundle data

### Evidence Extractors

Evidence Extractors parse raw source material and produce extracted evidence with provenance.

Examples:

- Extract restart events
- Extract error messages
- Extract gflags
- Extract version information
- Extract metric anomalies
- Extract leader changes
- Extract process lifecycle events

### Normalizers

Normalizers convert raw or extracted data into consistent formats.

Examples:

- Normalize timestamps
- Normalize hostnames
- Normalize log severity
- Normalize node names
- Normalize component names

### Correlators

Correlators compare extracted evidence across time, nodes, components, or sources.

Examples:

- Compare restart time against memory pressure
- Compare leader changes against disk latency
- Compare customer-reported time window against log evidence
- Compare error rates across nodes

### Helpers

Helpers assist later workflow tasks after investigation.

Examples:

- Generate engineering escalation
- Draft customer update
- Create case summary
- Generate post-incident review outline
- Format a bug report

Rule:

> Extractors and correlators support evidence preparation. Helpers support communication, escalation, or follow-up.

---

## 9. Evidence Chain Requirements

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
Extracted Evidence
    ↓ prepared from
Raw Source Material
    ↓ optionally guided by
Reported Context
```

A well-formed evidence chain should show:

- Which reported context was used
- Which raw source material was available
- Which preparation methods were applied
- Which evidence was extracted
- Which information was produced
- Which knowledge sources were applied
- Which insights were generated
- Which challenges were performed
- Which uncertainty remained
- Why a decision was made
- What action was taken
- What outcome resulted

---

## 10. AI Roles in the Framework

AI may assist at multiple stages, but should not be treated as equally reliable at every stage.

| Stage | Useful AI Role | Key Risk |
|---|---|---|
| Reported Context | Decompose ticket summaries into symptoms, timeline claims, component claims, and causal claims | Treating reported cause as verified truth |
| Raw Source Material | Inspect samples, identify file types, and suggest extraction paths | Token waste or missing important files |
| Evidence Preparation | Help design extractors, filters, parsing rules, and correlation scripts | Encoding assumptions into extraction |
| Extracted Evidence | Summarize observations and identify gaps | Losing provenance or overstating reliability |
| Information | Summarize, normalize, deduplicate, cluster, and timeline observations | Over-compression or incorrect grouping |
| Knowledge | Retrieve documentation, source code, bug reports, and prior incidents | Using outdated or wrong-version sources |
| Insight | Generate hypotheses and candidate explanations | Hallucination or overconfidence |
| Challenge | Test hypotheses against supporting, missing, and contradicting evidence | Weak challenge or confirmation bias |
| Wisdom | Assist human judgment | Over-delegation |
| Decision and Action | Suggest options and consequences | Unsafe operational changes |
| Outcome and Learning | Summarize results and generate reusable artefacts | Institutionalizing a false root cause |

---

## 11. Intended Use Cases

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

## 12. Non-Goals

EGATF is not intended to be:

- A replacement for experienced engineers
- A fully automated RCA system
- A guarantee of correctness
- A generic prompt template
- A vendor-specific AIOps architecture
- A claim that AI can safely diagnose without human review
- A reason to trust customer-reported cause without verification
- A reason to trust prepared data without provenance

The framework is intended to improve reasoning discipline, not remove human responsibility.

---

## 13. Open Questions

The framework is still experimental. Current open questions include:

1. Should **Wisdom** remain as a distinct stage?
2. Should **Challenge** be renamed to Validation, Adversarial Review, or Pressure Test?
3. Should Evidence and Information remain top-level stages, with sub-stages inside Evidence?
4. How should confidence be represented?
5. How should reported context be scored?
6. How should contradictory evidence be tracked?
7. What metadata is required for a useful evidence item?
8. Can the framework be applied consistently across different technical domains?
9. Does the Challenge stage measurably improve outcomes?
10. How should case studies be anonymized and sanitized?
11. What is the smallest useful tool that could support the workflow?
12. How should extractor quality be tested?
13. How should cold and guided analysis findings be compared?
14. How should anchoring risk be represented?

---

## 14. Success Criteria

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

The most important validation question is:

> Does introducing a formal Challenge stage improve the quality and trustworthiness of AI-assisted troubleshooting?

A second important validation question is:

> Does evidence preparation improve AI-assisted diagnosis by reducing noise while preserving traceability?

---

## 15. Current Status

This document is an early draft.

It should be treated as a working hypothesis for review, criticism, and testing against real diagnostic examples.

Future revisions should be recorded in `framework/changelog.md`.
