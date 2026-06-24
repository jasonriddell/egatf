# EGATF Terminology

**Document type:** Working glossary  
**Status:** Draft v0.2  
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

The process of extracting, filtering, parsing, normalizing, indexing, and correlating raw source material without adding unsupported diagnosis.

Examples:

- Extract all restart events
- Extract all ERROR and FATAL log lines
- Parse version and build information
- Extract configuration values
- Build node inventory
- Normalize timestamps
- Group repeated stack traces
- Identify gaps in logs or metrics
- Compare events across nodes

Evidence preparation answers:

> How do we turn raw source material into usable extracted evidence?

Rule:

> Evidence preparation should reduce noise without adding unsupported meaning.

---

### Extracted Evidence

A clean observation produced from raw source material with provenance.

Examples:

```text
At 2026-06-21 10:14:22 UTC, tserver-3 restarted.
Source: tserver.log line 18422.
```

```text
CPU usage on node-2 exceeded 95 percent for 11 minutes.
Source: metrics.csv.
```

```text
The flag ysql_output_buffer_size was set to 262144.
Source: gflags.json.
```

Extracted evidence answers:

> What verified observation can be traced back to source material?

Extracted evidence should include observation, source, timestamp or time range, component, extraction method, confidence in source reliability, and limitations.

---

### Evidence

Observable, reported, collected, or extracted material that can support or challenge a claim.

In EGATF v0.2, Evidence includes:

- Reported context
- Raw source material
- Evidence preparation output
- Extracted evidence

Evidence answers:

> What was observed, reported, collected, or extracted?

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
- Did cold analysis find anomalies that guided analysis missed?

Challenge answers:

> Why might this explanation be wrong?

Challenge is currently considered one of the most important and distinctive stages of EGATF.

---

### Wisdom

The current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

Wisdom answers:

> What should we believe, given the evidence and uncertainty?

Wisdom should include confidence level, remaining uncertainty, known assumptions, risk of being wrong, consequences of action, and whether more evidence is required.

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

## Analysis Modes

### Cold Analysis

Analysis of raw source material without using reported context as the primary guide.

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

Example:

A customer reports that an upgrade caused latency. AI then focuses only on upgrade-related evidence and misses a disk event that started earlier.

Anchoring risk should be considered whenever guided analysis is used.

---

## Tooling Terms

### Collector

A script, command, or tool that gathers raw source material.

Examples:

- Collect logs
- Export metrics
- Capture configuration
- Collect Kubernetes events
- Package support bundle data

Collectors answer:

> What raw material can we collect?

---

### Evidence Extractor

A script, command, or tool that extracts structured observations from raw source material while preserving provenance.

Examples:

- Extract restart events
- Extract error messages
- Extract gflags
- Extract version information
- Extract metric anomalies
- Extract process lifecycle events

Evidence Extractors answer:

> What evidence can we extract from the raw material?

Preferred generic name:

> Evidence Extractor

This is preferred over "helper" because the purpose is evidence preparation, not later workflow assistance.

---

### Normalizer

A script, command, or tool that converts raw or extracted data into consistent forms.

Examples:

- Normalize timestamps to UTC
- Normalize hostnames
- Normalize node names
- Normalize log severity
- Normalize component names

Normalizers answer:

> How do we make evidence comparable?

---

### Correlator

A script, command, or tool that compares extracted evidence across time, nodes, components, or sources.

Examples:

- Compare restart time against memory pressure
- Compare leader changes against disk latency
- Compare reported time window against log evidence
- Compare error rates across nodes

Correlators answer:

> What relationships exist between extracted evidence items?

---

### Helper

A script, command, or tool that assists later workflow tasks after investigation or during communication.

Examples:

- Generate engineering escalation
- Draft customer update
- Create case summary
- Generate post-incident review outline
- Format a bug report

Helpers answer:

> How do we turn the investigation into a useful follow-up artefact?

Rule:

> Extractors and correlators prepare evidence. Helpers support communication, escalation, or follow-up.

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
Extracted Evidence
    ↓ prepared from
Raw Source Material
    ↓ optionally guided by
Reported Context
```

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

### Unsupported Insight

An insight that sounds plausible but lacks sufficient supporting evidence.

Unsupported insights should not drive decisions without further evidence.

### Contradicting Evidence

Evidence that weakens or disproves an insight.

Contradicting evidence should be explicitly recorded rather than ignored.

### Missing Evidence

Evidence required to support or reject an insight but not currently available.

Missing evidence should reduce confidence and may drive further data collection.

### Assumption

A claim used in reasoning that has not yet been proven by available evidence.

Assumptions should be made explicit.

### Confidence

The degree of trust assigned to an insight, judgment, or decision.

Confidence should be based on strength of supporting evidence, contradicting evidence, source quality, timeline completeness, assumptions, alternatives, reproducibility, whether reported context was independently verified, and whether cold and guided analysis agree.

Confidence should not be based only on how plausible an explanation sounds.

### Hypothesis

A testable candidate explanation.

In EGATF, most insights begin as hypotheses.

A hypothesis should be challenged before it influences decisions.

### Traceability

The ability to move backward and forward through the reasoning chain.

Backward traceability:

> Why did we believe this?

Forward traceability:

> What did this evidence influence?

### Auditability

The ability for another person to review the reasoning process and understand how a conclusion was reached.

An auditable investigation should preserve reported context, raw source material, preparation methods, extracted evidence, sources, reasoning steps, assumptions, challenges, decisions, actions, and outcomes.

### Human-in-the-Loop

A design principle where humans retain responsibility for judgment, decisions, and actions.

In EGATF, AI assists with reasoning, extraction, summarization, hypothesis generation, and challenge.

Humans remain accountable for accepting conclusions and taking action.

### Hallucination

A generated claim that is false, unsupported, or not grounded in the available sources.

EGATF aims to reduce the impact of hallucination by requiring evidence chains and challenge.

### Pressure Test

A possible alternative name for the Challenge stage.

Pressure testing means deliberately applying stress to an insight to see if it survives.

### Validation

A possible alternative name for the Challenge stage.

Validation suggests confirming an insight, while Challenge suggests actively trying to disprove it.

EGATF currently uses **Challenge** because it better captures the adversarial nature of the stage.

---

## Provisional Terms Under Review

| Current Term | Reason Under Review |
|---|---|
| Wisdom | May be too abstract or difficult to distinguish from judgment |
| Challenge | May be renamed to Pressure Test, Validation, or Adversarial Review |
| Knowledge | May need clearer separation between retrieved knowledge and human domain knowledge |
| Insight | May need clearer distinction from hypothesis |
| Evidence | May need subtypes such as reported, direct, indirect, derived, extracted, and authoritative evidence |
| Evidence Preparation | May need to become a named stage rather than a sub-stage |
| Evidence Extractor | May need a broader name if tools do more than extraction |

---

## Working Language Guidelines

When writing about EGATF:

- Use **reported context** for unvalidated problem descriptions.
- Use **raw source material** for untouched logs, metrics, bundles, dumps, and documents.
- Use **evidence preparation** for parsing, filtering, normalizing, and correlating.
- Use **extracted evidence** for clean observations with provenance.
- Use **evidence** for raw or extracted material that can support or challenge claims.
- Use **information** for structured observations derived from evidence.
- Use **knowledge** for contextual understanding from trusted sources.
- Use **insight** for candidate explanations.
- Use **challenge** for deliberate testing of an insight.
- Use **decision** for choosing what to do.
- Use **action** for doing it.
- Use **outcome** for measuring what happened.
- Use **learning** for reusable knowledge captured afterward.
- Use **Evidence Extractor** for scripts that extract evidence.
- Use **Helper** for scripts that create follow-up artefacts, summaries, or communications.

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

---

## Revision Notes

This draft updates the terminology to include the v0.2 evidence-stage refinement.

Future revisions should be recorded in `framework/changelog.md`.
