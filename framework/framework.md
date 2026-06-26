# Evidence-Grounded AI Troubleshooting Framework

**Working acronym:** EGATF  
**Status:** Draft v0.6  
**Document type:** Canonical framework definition  
**Repository path:** `framework/framework.md`

---

## 1. Purpose

The Evidence-Grounded AI Troubleshooting Framework is a proposed methodology for using AI to assist with technical diagnosis while preserving a clear evidence chain from raw observations to final decisions.

The framework is intended for situations where engineers need to reason across support bundles, logs, metrics, traces, dumps, source code, documentation, bug reports, ticket summaries, customer observations, and historical incidents.

The purpose is not to make AI the final decision maker.

The purpose is to make AI useful while keeping its reasoning auditable, challengeable, and grounded in evidence.

---

## 2. Problem Statement

AI systems are increasingly capable of reading large volumes of technical material and producing plausible explanations.

However, plausible explanations are not enough in technical diagnosis. In support engineering, incident response, reliability engineering, and distributed systems troubleshooting, a conclusion must be supported by evidence.

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
- Outcomes should be checked against the judgment that led to the action.

In short:

> Without evidence, an insight is speculation.  
> Without traceability, an insight cannot be trusted.  
> Without challenge, an insight should not become judgment.

Collection-context principle:

> Evidence packages should describe their own collection context. AI should not be asked to infer timing, scope, source meaning, or collection limitations from raw files alone.

---

## 5. Chain and Operating Model

The framework can be introduced as a chain:

```text
Evidence -> Information -> Knowledge -> Insight -> Challenge -> Judgment -> Decision -> Action -> Outcome -> Learning
```

This chain is useful as a vocabulary and teaching model.

However, the operating model is not a straight line. EGATF is intended to operate as three related gated loops. Each loop has a gate that can stop progression, require rework, or return the investigation to an earlier loop.

```text
Loop 1: Evidence Loop
Can we trust what we are reasoning from?

Loop 2: Reasoning Loop
Can we trust what we believe?

Loop 3: Action Loop
Can we trust what happened next?
```

| Loop | Contains | Gate | Gate question |
|---|---|---|---|
| Evidence Loop | Reported Context, Collection Context, Raw Source Material, Evidence Preparation, Prepared Evidence Base, Information | Evidence Sufficiency Gate | Do we understand the evidence well enough to reason from it? |
| Reasoning Loop | Information, Knowledge, Insight, Challenge, Judgment | Challenge Confidence Gate | Has the insight survived enough challenge to become responsible judgment? |
| Action Loop | Decision, Action, Outcome, Learning | Outcome Validation Gate | Did the action produce the expected outcome, and what should be learned or revisited? |

Information intentionally appears at the boundary between the Evidence Loop and the Reasoning Loop. It is the point where prepared evidence becomes meaningful enough to support reasoning, but it should still stop short of diagnosis.

## 6. Loop 1: Evidence Loop

The Evidence Loop turns reported context and raw source material into a prepared evidence base and information.

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

Purpose:

> Build a trustworthy evidence base before reasoning begins.

The Evidence Loop includes:

- Separating reported symptoms from reported causal claims.
- Understanding the evidence package manifest.
- Identifying collection windows and collection-time snapshots.
- Inventorying raw source material.
- Preparing evidence through transformation, parsing, normalization, indexing, extraction, derivation, and correlation.
- Producing information in the form of timelines, observations, comparisons, and relationships.

Gate:

> Evidence Sufficiency Gate: Do we understand the evidence well enough to reason from it?

If the answer is no, the investigation loops back to collection context, raw source material, or evidence preparation.

---

## 7. Loop 2: Reasoning Loop

The Reasoning Loop turns information and knowledge into challenged judgment.

```text
Information
    ↓
Knowledge
    ↓
Insight
    ↓
Challenge
    ↓
Judgment
```

Purpose:

> Build a trustworthy judgment from evidence, information, and knowledge.

The Reasoning Loop includes:

- Validating reference knowledge sources before they are used to support an insight.
- Applying documentation, source code, bug reports, runbooks, prior incidents, and domain knowledge.
- Running cold analysis and guided analysis in isolated analysis sandboxes where useful.
- Comparing the cold and guided outputs before creating or accepting insights.
- Generating candidate insights as hypotheses.
- Challenging each insight against evidence, contradictions, missing evidence, assumptions, alternatives, timeline order, time-window compatibility, version fit, and preparation quality.
- Producing a human judgment only after the insight survives challenge.

Gate:

> Challenge Confidence Gate: Has the insight survived enough challenge to become responsible judgment?

If the answer is no, the investigation loops back to insight, knowledge, evidence preparation, or raw source material.

---

## 8. Loop 3: Action Loop

The Action Loop turns judgment into controlled action, measured outcome, and reusable learning.

```text
Decision
    ↓
Action
    ↓
Outcome
    ↓
Learning
```

Purpose:

> Act safely, measure the result, and learn from what happened.

The Action Loop includes:

- Choosing a decision based on challenged judgment.
- Checking that the decision is safe and authorized.
- Executing the action.
- Measuring the outcome.
- Checking whether the outcome supports or contradicts the judgment.
- Capturing reusable learning.

Gate:

> Outcome Validation Gate: Did the action produce the expected outcome, and what should be learned or revisited?

If the answer is no or partial, the investigation loops back to Challenge or Evidence.

---

## Primary Gates

### Gate 1: Evidence Sufficiency Gate

Question:

> Do we understand the evidence well enough to reason from it?

This gate prevents progression when evidence is missing, misunderstood, poorly prepared, not traceable, or not time-compatible.

The gate should check:

- Reported Context has been separated into symptoms, timeline claims, component claims, and causal claims.
- Collection Context is understood, including support bundle schema, collector version, collection windows, and file index.
- Raw Source Material is sufficient for the question being asked.
- Evidence Preparation preserved provenance.
- Structured Source Material is not being confused with Extracted Evidence.
- Derived Evidence is not being treated as direct evidence.
- Collection-time snapshots are not being treated as duration-based evidence.
- A basic timeline or set of information statements can be created.

Gate outcomes:

```text
Proceed to Reasoning Loop
More collection required
More preparation required
Collection context unclear
Evidence insufficient
Evidence unsuitable for the question being asked
```

### Gate 2: Challenge Confidence Gate

Question:

> Has the insight survived enough challenge to become responsible judgment?

This gate prevents plausible but unsupported explanations from becoming decisions.

The gate should check:

- Supporting evidence exists.
- Contradicting evidence has been considered.
- Missing evidence is recorded.
- Assumptions are explicit.
- Alternative explanations were considered.
- Timeline order supports the insight.
- Evidence sources are time-window compatible.
- Knowledge sources apply to the relevant version.
- Cold and guided analysis have been compared where useful.
- Anchoring risk has been considered.

Gate outcomes:

```text
Strengthened: proceed to Judgment
Weakened: revise the insight
Rejected: return to alternatives
Split: break into smaller hypotheses
More evidence required: return to Evidence Loop
```

### Gate 3: Outcome Validation Gate

Question:

> Did the action produce the expected outcome, and what should be learned or revisited?

This gate prevents a wrong diagnosis from being preserved simply because an action was taken.

The gate should check:

- The action was performed as intended.
- The expected outcome occurred or did not occur.
- The outcome supports, weakens, or contradicts the judgment.
- New evidence was created by the action.
- The case should be closed, monitored, or returned to Challenge.
- Reusable learning has been captured.

Gate outcomes:

```text
Close case
Continue monitoring
Capture learning
Return to Challenge
Return to Evidence Loop
Open follow-up work
```
---

## 9. Evidence Stage Detail

The Evidence stage is not a single simple thing. At the beginning of a support investigation there may be a customer ticket summary, an alert title, a support bundle, logs, metrics, command output, and observations from engineers.

These inputs have different reliability levels.

The Evidence Loop therefore uses this sub-sequence:

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

## 10. Collection Context

Collection Context describes how an evidence package was created and how its contents should be interpreted.

In support-bundle analysis, the support bundle is not just a bag of files. It is a time-bounded evidence package created by a particular collector version, from a particular environment, with different data sources captured from different effective times.

Collection Context answers:

> What was collected, when was it collected, from what environment, using which collector, and what does each source represent?

Collection Context should distinguish between:

- Data representing the requested support bundle duration.
- Data representing bundle creation time.
- Data using a metrics-specific duration.
- Mixed data sources.

Rule:

> Collection Context is part of the evidence chain. It is not diagnosis, but it constrains how evidence may safely be interpreted.

---

## 11. Evidence Preparation

Evidence Preparation makes raw source material easier to inspect, query, compare, and reason about while preserving provenance.

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

Boundary rules:

```text
Transformation changes shape.
Extraction selects observations.
Derivation computes observations.
Correlation compares observations.
Information explains relationships.
```

Example:

A tool such as `wtl`, which converts tserver, master, and YBA logs into parquet columns without filtering or consolidation, is a Source Transformer or Log Structuring Tool. It produces Structured Source Material.

A tablet report parser that identifies leaderless, over-replicated, or under-replicated tables is also acting as a Derived Evidence Generator.

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

## 12. Challenge as the Central Safety Mechanism

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an insight.

Challenge questions include:

- What evidence supports this insight?
- What evidence contradicts this insight?
- What evidence is missing?
- What assumptions does this insight depend on?
- Are there alternative explanations?
- Did the timeline happen in the required order?
- Are all evidence sources time-window compatible?
- Did guided analysis anchor the investigation too strongly?
- Did cold analysis find anomalies guided analysis missed?
- Did evidence preparation hide, drop, or misclassify relevant material?
- Did analysis confuse collection-time evidence with duration-based evidence?
- Does the knowledge source apply to the relevant product version?
- What would we expect to see if this insight were true?
- What would we expect to see if this insight were false?

Challenge outcomes:

```text
Strengthened
Weakened
Rejected
Split
More evidence required
```

Only a strengthened or appropriately qualified insight should move toward Judgment.

---

## 13. Cold and Guided Analysis Sandboxes

Cold analysis and guided analysis are Reasoning Loop techniques for reducing anchoring risk.

Cold analysis reviews prepared evidence without using the reported problem statement as the primary guide. Guided analysis uses the reported context to focus search and verification.

For stronger validation, these two passes should be run in isolated analysis sandboxes.

An isolated analysis sandbox means:

- The cold pass does not receive the customer theory, reported cause, or guided prompt.
- The guided pass receives the reported context as guidance, not proof.
- The outputs are recorded separately.
- The comparison is performed after both outputs exist.
- Agreement increases confidence only when both passes are evidence-grounded.
- Disagreement becomes an input to Challenge.

The comparison should ask:

- What did both passes find?
- What did only the cold pass find?
- What did only the guided pass find?
- Did guided analysis overfit to the reported context?
- Did cold analysis miss a reported symptom that was later verified?
- Which differences affect confidence?

## 14. Reference Knowledge Validation

Knowledge sources should be validated before they are used to support an insight.

Examples of reference knowledge sources include:

- Product documentation
- Source code
- Release notes
- Known bug reports
- Runbooks
- Architecture diagrams
- Previous incidents
- Domain expertise

Validation should check:

- Version applicability
- Product or component applicability
- Source authority
- Date or freshness
- Whether the source is normative, historical, advisory, or anecdotal
- Whether the source directly supports the claim being made

A knowledge source that is plausible but version-mismatched should lower confidence or force further validation.

## 15. Evidence Chain Requirements

A well-formed EGATF investigation should allow a reviewer to trace backward from any decision to the evidence that supported it.

```text
Decision
    ↓ supported by
Judgment
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

The evidence chain must show not only what supported the decision, but also what gates were passed and what uncertainty remained.

---

## 16. Non-Goals

EGATF is not intended to be:

- A replacement for experienced engineers.
- A fully automated RCA system.
- A guarantee of correctness.
- A generic prompt template.
- A reason to trust customer-reported cause without verification.
- A reason to trust prepared data without provenance.
- A reason to treat derived evidence as direct evidence.
- A reason to ignore collection windows or component-specific timing.
- A reason to move from insight to action without challenge.

The framework is intended to improve reasoning discipline, not remove human responsibility.

---

## 17. Success Criteria

The framework will be considered useful if it helps practitioners:

- Find unsupported AI conclusions earlier.
- Preserve evidence chains.
- Improve diagnostic confidence.
- Reduce hallucination-driven troubleshooting errors.
- Compare competing hypotheses more clearly.
- Record uncertainty explicitly.
- Separate reported context from verified evidence.
- Separate collection context from raw source material.
- Distinguish transformation from extraction.
- Distinguish extracted evidence from derived evidence.
- Avoid false correlations across incompatible collection windows.
- Stop progression at the Evidence Sufficiency Gate when evidence is not good enough.
- Stop progression at the Challenge Confidence Gate when reasoning is not good enough.
- Reopen reasoning at the Outcome Validation Gate when results contradict judgment.

Important validation questions:

1. Does the Evidence Loop produce a more trustworthy evidence base?
2. Does the Reasoning Loop reduce unsupported or hallucinated diagnosis?
3. Does the Action Loop prevent contradicted judgments from being institutionalized?
4. Does the three-loop model make EGATF easier to apply than a straight chain?

---

## 18. Current Status

This document is an early draft.

The current position is:

```text
v0.1: Core framework chain
v0.2: Evidence stage refinement
v0.3: Evidence preparation taxonomy
v0.4: Collection context and evidence package manifests
v0.5: Three-loop operating model and gates
v0.6: Rename Wisdom to Judgment
```

Future revisions should be recorded in `framework/changelog.md`.
