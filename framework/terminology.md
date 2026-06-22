# EGATF Terminology

**Document type:** Working glossary  
**Status:** Draft v0.1  
**Repository path:** `framework/terminology.md`

---

## Purpose

This document defines the core terms used by the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is to keep the language of the framework consistent as the research evolves.

Some terms are stable. Others are provisional and may change after testing the framework against real examples.

---

## Core Terms

### Evidence

Raw material from an observable or authoritative source.

Examples:

- Log line
- Metric sample
- Trace span
- Stack trace
- Core dump
- Configuration value
- Source code reference
- Documentation statement
- Bug report
- Customer observation
- Command output
- Timestamped event

Evidence answers:

> What was observed?

Evidence should be recorded with enough context that another person can review it independently.

Useful metadata:

- Source
- Timestamp
- System or component
- Version
- Collection method
- Reliability of source
- Whether the evidence is direct or indirect

---

### Information

Evidence that has been structured, normalized, summarized, grouped, or placed into context.

Examples:

- Error rate increased after deployment.
- Memory usage reached 98 percent before restart.
- Leader movement began after disk latency increased.
- The same error occurred across three nodes.
- The failure only appeared after a configuration change.

Information answers:

> What happened?

Information must remain linked to the evidence it was derived from.

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
- What would we expect to see if this insight were true?
- What would we expect to see if this insight were false?

Challenge answers:

> Why might this explanation be wrong?

Challenge is currently considered one of the most important and distinctive stages of EGATF.

---

### Wisdom

The current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

Wisdom answers:

> What should we believe, given the evidence and uncertainty?

Wisdom should include:

- Confidence level
- Remaining uncertainty
- Known assumptions
- Risk of being wrong
- Consequences of action
- Whether more evidence is required

Status:

**Provisional term.**

Wisdom may be renamed or removed in a future version of the framework if testing shows that it is unclear, unnecessary, or too abstract.

---

### Decision

The selection of a response based on the current best judgment.

Examples:

- Collect more logs.
- Escalate to engineering.
- Apply a known workaround.
- Change configuration.
- Roll back a release.
- Open a bug.
- Communicate a suspected cause.
- Take no immediate action and continue observing.

Decision answers:

> What will we do next?

A decision should be linked to the insight or judgment that justified it.

---

### Action

The execution of a decision.

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

Actions should be recorded because outcome analysis depends on knowing what changed.

---

### Outcome

The measured result of an action.

Examples:

- Error rate decreased.
- Latency returned to baseline.
- Issue reproduced again.
- Workaround failed.
- Customer impact stopped.
- New failure mode appeared.
- Hypothesis was disproven.

Outcome answers:

> Did it work?

Outcome should feed back into the evidence base.

---

### Learning

Reusable knowledge captured from an investigation.

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
Evidence
```

A strong evidence chain shows:

- What was observed
- How observations were interpreted
- Which knowledge sources were used
- Which insights were generated
- How those insights were challenged
- Why a decision was made
- What action was taken
- What outcome resulted

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

Source code may be authoritative for implementation behavior, while documentation may be authoritative for intended behavior.

---

### Unsupported Insight

An insight that sounds plausible but lacks sufficient supporting evidence.

Example:

> The outage was caused by network failure.

This is unsupported if no network metrics, logs, packet loss data, or timeline evidence support it.

Unsupported insights should not drive decisions without further evidence.

---

### Contradicting Evidence

Evidence that weakens or disproves an insight.

Example:

Insight:

> The restart was caused by memory pressure.

Contradicting evidence:

> Memory pressure occurred after the restart, not before it.

Contradicting evidence should be explicitly recorded rather than ignored.

---

### Missing Evidence

Evidence required to support or reject an insight but not currently available.

Example:

Insight:

> Disk latency caused request timeouts.

Missing evidence:

> No disk latency metrics are available for the affected time window.

Missing evidence should reduce confidence and may drive further data collection.

---

### Assumption

A claim used in reasoning that has not yet been proven by available evidence.

Example:

> The affected node was the leader at the time of the timeout.

If this has not been confirmed through logs, metrics, or metadata, it remains an assumption.

Assumptions should be made explicit.

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

Confidence should not be based only on how plausible an explanation sounds.

---

### Hypothesis

A testable candidate explanation.

In EGATF, most insights begin as hypotheses.

A hypothesis should be challenged before it influences decisions.

---

### Traceability

The ability to move backward and forward through the reasoning chain.

Backward traceability:

> Why did we believe this?

Forward traceability:

> What did this evidence influence?

Traceability is essential for auditability and trust.

---

### Auditability

The ability for another person to review the reasoning process and understand how a conclusion was reached.

An auditable investigation should preserve:

- Evidence
- Sources
- Reasoning steps
- Assumptions
- Challenges
- Decisions
- Actions
- Outcomes

---

### Human-in-the-Loop

A design principle where humans retain responsibility for judgment, decisions, and actions.

In EGATF, AI assists with reasoning, extraction, summarization, hypothesis generation, and challenge.

Humans remain accountable for accepting conclusions and taking action.

---

### Hallucination

A generated claim that is false, unsupported, or not grounded in the available sources.

In troubleshooting, hallucination may appear as:

- Invented root cause
- Incorrect product behavior
- Misread log meaning
- False source code interpretation
- Unsupported recommendation
- Confident statement without evidence

EGATF aims to reduce the impact of hallucination by requiring evidence chains and challenge.

---

### Pressure Test

A possible alternative name for the Challenge stage.

Pressure testing means deliberately applying stress to an insight to see if it survives.

This term may be useful in practitioner-facing articles because it is more conversational than "challenge" or "validation".

---

### Validation

A possible alternative name for the Challenge stage.

Validation suggests confirming an insight, while Challenge suggests actively trying to disprove it.

EGATF currently uses **Challenge** because it better captures the adversarial nature of the stage.

---

## Provisional Terms Under Review

The following terms may change as the framework evolves:

| Current Term | Reason Under Review |
|---|---|
| Wisdom | May be too abstract or difficult to distinguish from judgment |
| Challenge | May be renamed to Pressure Test, Validation, or Adversarial Review |
| Knowledge | May need clearer separation between retrieved knowledge and human domain knowledge |
| Insight | May need clearer distinction from hypothesis |
| Evidence | May need subtypes such as direct, indirect, derived, and authoritative evidence |

---

## Working Language Guidelines

When writing about EGATF:

- Use **evidence** for raw observed or authoritative material.
- Use **information** for structured observations derived from evidence.
- Use **knowledge** for contextual understanding from trusted sources.
- Use **insight** for candidate explanations.
- Use **challenge** for deliberate testing of an insight.
- Use **decision** for choosing what to do.
- Use **action** for doing it.
- Use **outcome** for measuring what happened.
- Use **learning** for reusable knowledge captured afterward.

Avoid treating insights as conclusions until they have passed through challenge.

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

---

## Revision Notes

This is the initial terminology draft.

Future revisions should be recorded in `framework/changelog.md`.
