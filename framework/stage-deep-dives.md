# EGATF Stage Deep Dives

**Document type:** Stage detail  
**Status:** Draft v0.5  
**Repository path:** `framework/stage-deep-dives.md`

---

## Purpose

This document expands each EGATF stage into practical steps, key questions, expected outputs, and loop conditions.

It is organized around the three-loop operating model.

## Three Gated Loops

The linear chain is useful for teaching the framework, but EGATF is intended to operate as three related gated loops.

```text
Loop 1: Evidence Loop
Can we trust what we are reasoning from?

Loop 2: Reasoning Loop
Can we trust what we believe?

Loop 3: Action Loop
Can we trust what happened next?
```

The chain remains the vocabulary of the framework:

```text
Evidence -> Information -> Knowledge -> Insight -> Challenge -> Wisdom -> Decision -> Action -> Outcome -> Learning
```

The three-loop model is the operating model. Each loop has a gate that can stop progression, require rework, or return the investigation to an earlier loop.

| Loop | Contains | Gate | Gate question |
|---|---|---|---|
| Evidence Loop | Reported Context, Collection Context, Raw Source Material, Evidence Preparation, Prepared Evidence Base, Information | Evidence Sufficiency Gate | Do we understand the evidence well enough to reason from it? |
| Reasoning Loop | Information, Knowledge, Insight, Challenge, Wisdom / Judgment | Challenge Confidence Gate | Has the insight survived enough challenge to become responsible judgment? |
| Action Loop | Decision, Action, Outcome, Learning | Outcome Validation Gate | Did the action produce the expected outcome, and what should be learned or revisited? |

Information intentionally appears at the boundary between the Evidence Loop and the Reasoning Loop. It is the point where prepared evidence becomes meaningful enough to support reasoning, but it should still stop short of diagnosis.
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
| Wisdom / Judgment | The current best human judgment after evidence, insight, and challenge have been considered. |
| Decision | The selected next response based on the current best judgment. |
| Action | The execution of the selected decision. |
| Outcome | The measured result of the action. |
| Learning | Reusable knowledge captured from the investigation for future use. |
---

## Loop 1: Evidence Loop

Purpose:

> Build a trustworthy evidence base before reasoning begins.

Gate:

> Evidence Sufficiency Gate: Do we understand the evidence well enough to reason from it?

### Reported Context

Steps:

1. Capture the original wording.
2. Separate symptoms from causal claims.
3. Identify reported time windows.
4. Identify reported components.
5. Mark causal claims as hypotheses.

Output:

- Reported symptoms
- Reported timeline claims
- Reported component claims
- Reported causal claims

Loop condition:

Return here if the problem description is too ambiguous to guide collection.

### Collection Context

Steps:

1. Identify support bundle schema version.
2. Identify collector version.
3. Identify bundle creation time.
4. Identify requested collection window.
5. Identify component-specific collection windows.
6. Identify YBA and YBDB versions.
7. Identify expected and present files.
8. Record collection limitations.

Output:

- Manifest summary
- Collection windows
- Component timing semantics
- File index summary
- Collection warnings

Loop condition:

Return here if evidence timing, bundle completeness, or parser compatibility is unclear.

### Raw Source Material

Steps:

1. Inventory sources.
2. Classify source types.
3. Record paths.
4. Record source reliability.
5. Identify missing expected material.
6. Link sources to collection context.

Output:

- Source inventory
- Missing source list
- Reliability notes

Loop condition:

Return to collection if required raw material is missing.

### Evidence Preparation

Steps:

1. Transform source material into structured form where useful.
2. Parse fields.
3. Normalize timestamps and identifiers.
4. Index material for query.
5. Extract notable observations.
6. Derive computed observations.
7. Correlate related observations.
8. Preserve provenance.
9. Record tool versions and limitations.

Output:

- Structured Source Material
- Extracted Evidence
- Derived Evidence
- Correlated Evidence
- Tool usage record

Loop condition:

Return here if provenance is missing, timestamps are wrong, parsing is unreliable, or extraction logic is unclear.

### Prepared Evidence Base

Steps:

1. Classify outputs by type.
2. Assign evidence IDs.
3. Record provenance.
4. Record time semantics.
5. Record confidence.
6. Record limitations.

Output:

- Evidence table
- Derived evidence table
- Correlated evidence table
- Limitations list

Loop condition:

Return to Evidence Preparation if classification, provenance, or timing is incomplete.

### Information

Steps:

1. Build timeline.
2. Group observations.
3. Compare affected and unaffected components.
4. Identify order of events.
5. Identify anomalies.
6. Identify evidence gaps.
7. Avoid root cause claims.

Output:

- Timeline
- Observations
- Comparisons
- Information statements
- Evidence gaps

Loop condition:

Return to Evidence Preparation if the timeline or observations are incomplete.

---

## Loop 2: Reasoning Loop

Purpose:

> Build a trustworthy judgment from evidence, information, and knowledge.

Gate:

> Challenge Confidence Gate: Has the insight survived enough challenge to become responsible judgment?

### Knowledge

Steps:

1. Identify relevant knowledge sources.
2. Check version applicability.
3. Record source authority.
4. Link knowledge to information.
5. Record knowledge gaps.

Output:

- Knowledge source table
- Version applicability notes
- Knowledge claims
- Knowledge gaps

Loop condition:

Return here if a source is outdated, version-mismatched, or uncertain.

### Insight

Steps:

1. Generate candidate insights.
2. Make assumptions explicit.
3. Link each insight to evidence.
4. Record alternative explanations.
5. Assign initial confidence.

Output:

- Candidate insights
- Hypotheses
- Assumptions
- Alternatives
- Initial confidence

Loop condition:

Return to Information if no testable insight exists.

### Challenge

Steps:

1. Identify supporting evidence.
2. Identify contradicting evidence.
3. Identify missing evidence.
4. Test timeline order.
5. Test time-window compatibility.
6. Test version applicability.
7. Test assumptions.
8. Compare alternatives.
9. Evaluate cold versus guided findings.
10. Assign challenge result.
11. Assign confidence after challenge.

Output:

- Challenge checklist
- Contradicting evidence table
- Missing evidence table
- Challenge result
- Confidence after challenge
- Challenge summary

Loop condition:

Return to Insight if the insight is weakened, rejected, or split.

Return to the Evidence Loop if more evidence is required.

### Wisdom / Judgment

Steps:

1. Select current best explanation.
2. State confidence.
3. State uncertainty.
4. State risk of being wrong.
5. State whether more evidence is needed.

Output:

- Current best judgment
- Confidence rating
- Remaining uncertainty
- Risk statement

Loop condition:

Return to Challenge or the Evidence Loop if confidence is insufficient for decision.

---

## Loop 3: Action Loop

Purpose:

> Act safely, measure the result, and learn from what happened.

Gate:

> Outcome Validation Gate: Did the action produce the expected outcome, and what should be learned or revisited?

### Decision

Steps:

1. List options.
2. Evaluate risk.
3. Select action or defer.
4. Identify owner.
5. Record rationale.

Output:

- Decision record
- Rationale
- Owner
- Approval status

Loop condition:

Return to Judgment or Challenge if the decision is unsafe or confidence is insufficient.

### Action

Steps:

1. Execute action.
2. Record time.
3. Record owner.
4. Record exact change.
5. Record communication.

Output:

- Action log
- Communication log

Loop condition:

Return to Decision if action cannot be executed or requires a safer plan.

### Outcome

Steps:

1. Measure before and after.
2. Check customer impact.
3. Compare outcome to expected result.
4. Decide whether judgment was supported.
5. Record new evidence.

Output:

- Outcome measurements
- Supported or contradicted judgment
- New evidence

Loop condition:

Return to Challenge if outcome does not support the judgment.

### Learning

Steps:

1. Capture reusable lessons.
2. Update runbooks.
3. Create bug reports.
4. Improve monitoring.
5. Improve extraction tools.
6. Improve templates.
7. Improve documentation.

Output:

- Lessons learned
- Follow-up artefacts
- Framework improvements

Loop condition:

Return to framework or tooling design if the case exposes a process gap.
