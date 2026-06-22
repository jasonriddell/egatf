# Evidence-Grounded AI Troubleshooting Framework

**Working acronym:** EGATF  
**Status:** Draft v0.1  
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
- Customer observations
- Historical incidents

The purpose is not to make AI the final decision maker.

The purpose is to make AI useful while keeping its reasoning auditable, challengeable, and grounded in evidence.

---

## 2. Problem Statement

AI systems are increasingly capable of reading large volumes of technical data and producing plausible explanations.

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

## 6. Stage Definitions

### 6.1 Evidence

Evidence is raw material from authoritative or observable sources.

Examples:

- A log line
- A metric sample
- A stack trace
- A configuration value
- A source code branch
- A product documentation statement
- A bug report
- A customer observation
- A command output
- A timestamped event

Evidence should be captured with enough context to be independently reviewed.

Useful metadata includes:

- Source
- Timestamp
- System or component
- Collection method
- Confidence in source reliability
- Whether the evidence is direct or indirect

Evidence answers:

> What was observed?

---

### 6.2 Information

Information is evidence that has been structured, normalized, summarized, or placed into context.

Examples:

- Error count increased after deployment.
- Memory usage reached 98 percent before the service restarted.
- Leader movement began 17 seconds after disk latency increased.
- The same error appears on three nodes, but not on the fourth.
- The failing code path is only used when a specific feature flag is enabled.

Information answers:

> What happened?

AI can be highly effective at this stage because it can extract, group, summarize, and normalize large volumes of raw material.

However, every information item should remain linked to the evidence it was derived from.

---

### 6.3 Knowledge

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

Examples:

- A specific log message is emitted when a retry loop exhausts.
- A specific metric increases when request queueing occurs.
- A source code path is only reached during tablet leader election.
- A documented configuration value controls timeout behavior.

Knowledge answers:

> How does this system behave?

Knowledge must also be grounded. The source of knowledge should be recorded wherever possible.

---

### 6.4 Insight

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

---

### 6.5 Challenge

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
- What would we expect to see if this insight were true?
- What would we expect to see if this insight were false?

Challenge exists because AI-generated insights can sound convincing while being incomplete or unsupported.

Challenge answers:

> Why might this explanation be wrong?

A useful challenge stage should produce one of several outcomes:

- Insight strengthened
- Insight weakened
- Insight rejected
- Insight split into multiple hypotheses
- More evidence required
- Alternative explanation preferred

---

### 6.6 Wisdom

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

---

### 6.7 Decision

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

---

### 6.8 Action

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

---

### 6.9 Outcome

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

---

### 6.10 Learning

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

## 7. Evidence Chain Requirements

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
Evidence
```

A well-formed evidence chain should show:

- Which evidence was used
- Which information was extracted
- Which knowledge sources were applied
- Which insights were generated
- Which challenges were performed
- Which uncertainty remained
- Why a decision was made
- What action was taken
- What outcome resulted

---

## 8. AI Roles in the Framework

AI may assist at multiple stages, but should not be treated as equally reliable at every stage.

### Evidence

AI can help index, classify, and retrieve evidence.

Risk:

- Missing relevant evidence
- Misreading source context
- Treating weak evidence as strong evidence

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

## 9. Intended Use Cases

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

## 10. Non-Goals

EGATF is not intended to be:

- A replacement for experienced engineers
- A fully automated RCA system
- A guarantee of correctness
- A generic prompt template
- A vendor-specific AIOps architecture
- A claim that AI can safely diagnose without human review

The framework is intended to improve reasoning discipline, not remove human responsibility.

---

## 11. Open Questions

The framework is still experimental. Current open questions include:

1. Should **Wisdom** remain as a distinct stage?
2. Should **Challenge** be renamed to Validation, Adversarial Review, or Pressure Test?
3. Should Evidence and Information be separated more formally?
4. How should confidence be represented?
5. How should contradictory evidence be tracked?
6. What metadata is required for a useful evidence item?
7. Can the framework be applied consistently across different technical domains?
8. Does the Challenge stage measurably improve outcomes?
9. How should case studies be anonymized and sanitized?
10. What is the smallest useful tool that could support the workflow?

---

## 12. Success Criteria

The framework will be considered useful if it helps practitioners:

- Find unsupported AI conclusions earlier
- Preserve evidence chains
- Improve diagnostic confidence
- Reduce hallucination-driven troubleshooting errors
- Compare competing hypotheses more clearly
- Record uncertainty explicitly
- Convert investigations into reusable learning
- Improve collaboration between humans and AI during diagnosis

The most important validation question is:

> Does introducing a formal Challenge stage improve the quality and trustworthiness of AI-assisted troubleshooting?

---

## 13. Current Status

This document is an early draft.

It should be treated as a working hypothesis for review, criticism, and testing against real diagnostic examples.

Future revisions should be recorded in `framework/changelog.md`.
