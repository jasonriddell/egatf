# EGATF Case Study Template

**Document type:** Case study template  
**Status:** Draft v0.5  
**Repository path:** `cases/001-template.md`

---

## Purpose

This template is used to apply the Evidence-Grounded AI Troubleshooting Framework (EGATF) to a real, synthetic, or sanitized technical investigation.

The template is intended to help analysts preserve a traceable evidence chain from reported problem through collection context, raw source material, prepared evidence, information, knowledge, insight, challenge, decision, action, outcome, and learning.

The goal is not only to find an answer.

The goal is to show why the answer should be trusted.

---

## Case Metadata

| Field | Value |
|---|---|
| Case ID | |
| Case title | |
| Case type | Real / Synthetic / Sanitized / Public incident |
| Product or system | |
| Environment | |
| Date opened | |
| Date investigated | |
| Analyst | |
| Reviewers | |
| EGATF version used | v0.5 |
| Status | Draft / In review / Complete |
| Sensitivity | Public / Internal / Confidential / Sanitized |

---

## Operating Model for This Case

This case should be worked through the three EGATF loops.

| Loop | Question | Gate |
|---|---|---|
| Evidence Loop | Can we trust what we are reasoning from? | Evidence Sufficiency Gate |
| Reasoning Loop | Can we trust what we believe? | Challenge Confidence Gate |
| Action Loop | Can we trust what happened next? | Outcome Validation Gate |

The case should not move from one loop to the next until the relevant gate has been satisfied or the remaining uncertainty has been explicitly accepted.

---

## 1. Case Summary

### Short summary

```text
Briefly describe the issue in 3 to 5 sentences.
```

### What makes this case useful?

```text
Explain why this case is useful for validating EGATF.

Examples:
- It tests Collection Context.
- It tests cold versus guided analysis.
- It tests whether Challenge rejects a plausible but unsupported insight.
- It tests Evidence Preparation.
- It tests AI-assisted analysis of support bundles.
```

### Primary validation focus

Select one or more:

- [ ] Reported Context handling
- [ ] Collection Context handling
- [ ] Evidence Package Manifest usefulness
- [ ] Evidence Preparation
- [ ] Source Transformation
- [ ] Evidence Extraction
- [ ] Derived Evidence
- [ ] Correlation
- [ ] Cold analysis
- [ ] Guided analysis
- [ ] Anchoring risk
- [ ] Challenge stage
- [ ] Decision traceability
- [ ] Outcome and learning loop

---

## 2. Reported Context

Reported Context is the unvalidated description of the problem.

It is useful guidance, but it is not ground truth.

### Original reported problem

```text
Paste or summarize the original ticket description, customer statement, alert description, or first responder note.
```

### Reported symptoms

| Symptom | Source | Initial confidence | Notes |
|---|---|---|---|
| | | Low / Medium / High | |

### Reported error messages

| Error message | Source | Verified in raw source material? | Notes |
|---|---|---|---|
| | | Yes / No / Unknown | |

### Reported timeline claims

| Claim | Source | Verified? | Notes |
|---|---|---|---|
| | | Yes / No / Unknown | |

### Reported causal claims

| Claim | Source | Initial treatment | Notes |
|---|---|---|---|
| | | Hypothesis only | |

### Initial handling rule

```text
State how reported context will be used.

Example:
The reported context will be used to guide search, but all causal claims will be treated as hypotheses until verified against source material.
```

---

## 3. Collection Context

Collection Context describes how the evidence package was created and how its contents should be interpreted.

### Evidence package

| Field | Value |
|---|---|
| Evidence package type | Support bundle / Live collection / Manual archive / Other |
| Bundle UUID | |
| Support bundle version | |
| Support bundle schema version | |
| Support bundle collector version | |
| Created at | |
| Created by | |
| Scope UUID | |
| Path or source | |

### Environment identity

| Field | Value |
|---|---|
| Universe UUID | |
| Universe name | |
| YBDB version at collection time | |
| YBA instance | |
| YBA version at collection time | |
| Replication factor | |
| Master count | |
| TServer count | |
| Provider | |
| Deployment type | VM / K8s / Unknown |
| Infrastructure type | Cloud / On prem / Unknown |
| Node Agent enabled | Yes / No / Unknown |

### Requested support bundle window

| Field | Value |
|---|---|
| Requested start | |
| Requested end | |
| Duration | |
| Timezone handling | UTC / Local / Unknown |

### Component collection windows

| Component | Window type | Start | End | Collected at | Notes |
|---|---|---|---|---|---|
| UniverseLogs | requested_duration | | | | |
| ApplicationLogs | requested_duration | | | | |
| Metrics | metrics_duration | | | | |
| TabletMeta | collection_time_snapshot | | | | |
| ConsensusMeta | collection_time_snapshot | | | | |
| TabletReport | collection_time_snapshot | | | | |
| YbaMetadata | mixed | | | | |
| GFlags | collection_time_snapshot | | | | |
| K8sInfo | collection_time_snapshot | | | | |
| NodeAgent | requested_duration / collection_time_snapshot / unknown | | | | |

Recommended `windowType` values:

```text
requested_duration
metrics_duration
collection_time_snapshot
mixed
unknown
not_applicable
```

### Metric collection context

| Field | Value |
|---|---|
| Configured metric collection level | |
| Requested metric types | |
| Metric start | |
| Metric end | |
| Metric resolution | |
| Metric retention | |
| Known limitations | |

### Included components

| Component | Included? | Notes |
|---|---|---|
| UniverseLogs | Yes / No / Unknown | |
| OutputFiles | Yes / No / Unknown | |
| ErrorFiles | Yes / No / Unknown | |
| CoreFiles | Yes / No / Unknown | |
| GFlags | Yes / No / Unknown | |
| Instance | Yes / No / Unknown | |
| ConsensusMeta | Yes / No / Unknown | |
| TabletMeta | Yes / No / Unknown | |
| YbcLogs | Yes / No / Unknown | |
| K8sInfo | Yes / No / Unknown | |
| NodeAgent | Yes / No / Unknown | |
| YbaMetadata | Yes / No / Unknown | |
| ApplicationLogs | Yes / No / Unknown | |

### File index summary

| File group | Expected | Present | Missing | Notes |
|---|---:|---:|---:|---|
| Master directories | | | | |
| TServer directories | | | | |
| Controller directories | | | | |
| Node Agent directories | | | | |
| YBA log directories | | | | |
| Metrics files | | | | |
| Core files | | | | |
| GFlags files | | | | |
| Tablet metadata files | | | | |
| Consensus metadata files | | | | |
| Tablet report files | | | | |

### Collection context warnings

List any collection context issues that may constrain interpretation.

Examples:

- Tablet metadata was collected after the requested log window.
- Metrics duration differs from requested bundle duration.
- Metric collection level may explain missing metrics.
- Some nodes are missing logs.
- YBA version differs significantly from universe YBDB version.
- Bundle schema version is unknown.

| Warning | Impact | Follow-up |
|---|---|---|
| | | |

---

## 4. Raw Source Material

Raw Source Material is the untouched diagnostic material available to the investigation.

### Source inventory

| Source | Path or location | Type | Time semantics | Notes |
|---|---|---|---|---|
| | | Logs / Metrics / Metadata / Dump / Other | | |

### Source reliability

| Source | Reliability | Reason |
|---|---|---|
| | Low / Medium / High | |

### Missing or incomplete source material

| Missing source | Expected? | Why it matters | Impact |
|---|---|---|---|
| | Yes / No / Unknown | | |

---

## 5. Evidence Preparation

Evidence Preparation is the process of making raw source material easier to inspect, query, compare, and reason about while preserving provenance.

### Preparation tools used

| Tool | Tool type | Input | Output | Version | Notes |
|---|---|---|---|---|---|
| | Collector | | | | |
| | Source Transformer | | | | |
| | Parser | | | | |
| | Normalizer | | | | |
| | Indexer | | | | |
| | Evidence Extractor | | | | |
| | Derived Evidence Generator | | | | |
| | Correlator | | | | |

Tool type definitions:

```text
Collector:
Gathers raw source material.

Source Transformer:
Converts raw material into a structured or queryable form without selecting meaning.

Parser:
Reads a specific format and exposes fields.

Normalizer:
Converts values into consistent forms.

Indexer:
Makes material searchable or queryable.

Evidence Extractor:
Selects notable observations.

Derived Evidence Generator:
Computes higher-level observations.

Correlator:
Compares observations across time, nodes, components, or sources.
```

### Source Transformation

Use this section for tools such as `wtl` that convert source material into queryable structure without selecting meaning.

| Transformer | Input | Output | Output classification | Notes |
|---|---|---|---|---|
| | | | Structured Source Material | |

Example:

```text
wtl:
Raw tserver, master, and YBA logs to parquet logs.
Classification:
Source Transformer / Log Structuring Tool.
Output:
Structured Source Material.
```

### Extraction

Use this section for selected notable observations.

| Extractor | Observation type | Source | Output | Provenance preserved? |
|---|---|---|---|---|
| | | | Extracted Evidence | Yes / No |

### Derivation

Use this section for computed observations.

| Generator | Derived observation | Inputs | Logic | Output | Limitations |
|---|---|---|---|---|---|
| | | | | Derived Evidence | |

Example:

```text
Tablet report parser:
If it computes leaderless tablets, under-replicated tables, or over-replicated tables, this is Derived Evidence.
```

### Correlation

Use this section for relationships across observations.

| Correlator | Relationship | Inputs | Output | Notes |
|---|---|---|---|---|
| | | | Correlated Evidence | |

### Preparation quality checks

| Check | Result | Notes |
|---|---|---|
| Timestamps normalized? | Yes / No / Unknown | |
| Source provenance preserved? | Yes / No / Unknown | |
| Tool versions recorded? | Yes / No / Unknown | |
| Derived evidence logic recorded? | Yes / No / Unknown | |
| Collection windows preserved? | Yes / No / Unknown | |
| Missing files recorded? | Yes / No / Unknown | |

---

## 6. Prepared Evidence Base

The Prepared Evidence Base is the body of prepared material available for analysis.

### Structured Source Material

| Output | Source | Tool | Description | Notes |
|---|---|---|---|---|
| | | | | |

### Extracted Evidence

| Evidence ID | Observation | Source | Time or window | Component | Provenance | Confidence |
|---|---|---|---|---|---|---|
| E-001 | | | | | | Low / Medium / High |

### Derived Evidence

| Evidence ID | Derived observation | Inputs | Logic | Time semantics | Confidence |
|---|---|---|---|---|---|
| D-001 | | | | | Low / Medium / High |

### Correlated Evidence

| Evidence ID | Relationship | Inputs | Time compatibility checked? | Confidence |
|---|---|---|---|---|
| C-001 | | | Yes / No / Unknown | Low / Medium / High |

### Evidence limitations

| Limitation | Affected evidence | Impact |
|---|---|---|
| | | |

---

## 7. Information

Information is evidence structured into meaningful observations, timelines, comparisons, or relationships.

It answers:

> What happened?

### Timeline

| Time | Event | Evidence IDs | Notes |
|---|---|---|---|
| | | | |

### Observations

| Information ID | Observation | Evidence IDs | Confidence | Notes |
|---|---|---|---|---|
| I-001 | | | Low / Medium / High | |

### Comparisons

| Comparison | Evidence IDs | Result | Notes |
|---|---|---|---|
| | | | |

### Time-window compatibility notes

Use this section to explicitly record whether evidence sources can safely be compared.

| Evidence A | Evidence B | Compatible? | Reason |
|---|---|---|---|
| | | Yes / No / Unknown | |

---

## 8. Knowledge

Knowledge is contextual understanding from trusted sources.

It answers:

> How does this system behave?

### Knowledge sources used

| Knowledge ID | Source | Version or date | Claim | Relevance |
|---|---|---|---|---|
| K-001 | Documentation / Source code / Bug / Runbook / Prior incident | | | |

### Version checks

| Knowledge source | Applies to this environment? | Reason |
|---|---|---|
| | Yes / No / Unknown | |

### Knowledge gaps

| Gap | Impact | Follow-up |
|---|---|---|
| | | |

---

## 9. Insight

Insight is a candidate explanation produced by combining evidence, information, and knowledge.

It answers:

> What might this mean?

### Candidate insights

| Insight ID | Candidate explanation | Evidence IDs | Information IDs | Knowledge IDs | Initial confidence |
|---|---|---|---|---|---|
| H-001 | | | | | Low / Medium / High |

### Assumptions

| Assumption | Related insight | Verified? | Notes |
|---|---|---|---|
| | | Yes / No / Unknown | |

### Alternative explanations

| Alternative | Supporting evidence | Contradicting evidence | Notes |
|---|---|---|---|
| | | | |

---

## 10. Challenge

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an insight.

It answers:

> Why might this explanation be wrong?

### Challenge checklist

For each candidate insight, answer:

| Challenge question | Answer |
|---|---|
| What evidence supports this insight? | |
| What evidence contradicts this insight? | |
| What evidence is missing? | |
| What assumptions does this insight depend on? | |
| Are there alternative explanations? | |
| Did the timeline happen in the required order? | |
| Are all evidence sources time-window compatible? | |
| Did guided analysis anchor the investigation too strongly? | |
| Did cold analysis find anomalies guided analysis missed? | |
| Did evidence preparation hide, drop, or misclassify relevant material? | |
| Did analysis confuse collection-time evidence with duration-based evidence? | |
| Does the knowledge source apply to the relevant product version? | |
| What would we expect to see if this insight were true? | |
| What would we expect to see if this insight were false? | |

### Insight challenge results

| Insight ID | Result | Reason | Confidence after challenge |
|---|---|---|---|
| H-001 | Strengthened / Weakened / Rejected / Split / More evidence required | | Low / Medium / High |

### Contradicting evidence

| Evidence ID | Contradicts | Explanation |
|---|---|---|
| | | |

### Missing evidence

| Missing evidence | Needed to test | Impact |
|---|---|---|
| | | |

### Challenge summary

```text
Summarize what survived challenge and what did not.
```

---

## 11. Wisdom / Judgment

Wisdom is the current best human judgment after evidence, information, knowledge, insight, and challenge have been considered.

This term is provisional in EGATF and may later be renamed.

It answers:

> What should we believe, given the evidence and uncertainty?

### Current best judgment

```text
State the current best explanation, including uncertainty.
```

### Confidence

| Area | Confidence | Reason |
|---|---|---|
| Evidence quality | Low / Medium / High | |
| Time-window compatibility | Low / Medium / High | |
| Knowledge applicability | Low / Medium / High | |
| Insight strength | Low / Medium / High | |
| Overall judgment | Low / Medium / High | |

### Remaining uncertainty

| Uncertainty | Impact | Possible resolution |
|---|---|---|
| | | |

### Risk of being wrong

```text
Describe the operational, customer, engineering, or communication risk if this judgment is wrong.
```

---

## 12. Decision

Decision is the selected response based on the current best judgment.

It answers:

> What will we do next?

### Decision record

| Decision ID | Decision | Supported by | Owner | Date |
|---|---|---|---|---|
| DEC-001 | | Insight / Judgment / Evidence IDs | | |

### Options considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| | | | Accepted / Rejected / Deferred |

### Decision rationale

```text
Explain why this decision was selected.
```

---

## 13. Action

Action is the execution of the decision.

It answers:

> What did we actually do?

### Actions taken

| Action ID | Action | Owner | Time | Result |
|---|---|---|---|---|
| A-001 | | | | |

### Communication

| Audience | Message | Time | Notes |
|---|---|---|---|
| Customer / Engineering / Support / Internal | | | |

---

## 14. Outcome

Outcome is the measured result of an action.

It answers:

> Did it work?

### Outcome measurements

| Measurement | Before | After | Evidence | Notes |
|---|---|---|---|---|
| | | | | |

### Was the judgment supported?

| Question | Answer |
|---|---|
| Did the action resolve or improve the issue? | Yes / No / Partial / Unknown |
| Did the outcome support the leading insight? | Yes / No / Partial / Unknown |
| Did the outcome contradict the leading insight? | Yes / No / Partial / Unknown |
| Is more evidence required? | Yes / No |

### Outcome summary

```text
Summarize what happened after action was taken.
```

---

## 15. Learning

Learning is reusable knowledge captured from the investigation.

It answers:

> What should future investigations know?

### Reusable lessons

| Lesson | Applies to | Evidence |
|---|---|---|
| | | |

### Follow-up artefacts

| Artefact | Needed? | Owner | Notes |
|---|---|---|---|
| Knowledge base article | Yes / No | | |
| Runbook update | Yes / No | | |
| Bug report | Yes / No | | |
| Test case | Yes / No | | |
| Monitoring rule | Yes / No | | |
| Alert improvement | Yes / No | | |
| Documentation correction | Yes / No | | |
| Source code comment or change | Yes / No | | |
| Case study publication | Yes / No | | |

### Learning summary

```text
Summarize what this case teaches future human and AI-assisted investigations.
```

---

## 16. Loop Gate Summary

### Evidence Sufficiency Gate

| Question | Answer |
|---|---|
| Do we understand the evidence well enough to reason from it? | Yes / No / Partially |
| What blocked or delayed progression? | |
| What rework was required? | |

### Challenge Confidence Gate

| Question | Answer |
|---|---|
| Has the insight survived enough challenge to become responsible judgment? | Yes / No / Partially |
| What was the challenge result? | Strengthened / Weakened / Rejected / Split / More evidence required |
| What confidence remained after challenge? | Low / Medium / High |

### Outcome Validation Gate

| Question | Answer |
|---|---|
| Did the action produce the expected outcome? | Yes / No / Partially / Unknown |
| Did the outcome support the judgment? | Yes / No / Partially / Unknown |
| Does the investigation need to loop back? | Yes / No |

---

## 17. Evidence Chain Summary

Use this section to summarize the final traceable chain.

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

### Final evidence chain

| Chain step | Content | References |
|---|---|---|
| Reported Context | | |
| Collection Context | | |
| Raw Source Material | | |
| Evidence Preparation | | |
| Prepared Evidence Base | | |
| Information | | |
| Knowledge | | |
| Insight | | |
| Challenge | | |
| Judgment | | |
| Decision | | |
| Action | | |
| Outcome | | |
| Learning | | |

---

## 18. AI Usage Record

Use this section to record where AI was used in the investigation.

| Stage | AI used? | How AI was used | Human review performed? |
|---|---|---|---|
| Reported Context | Yes / No | | Yes / No |
| Collection Context | Yes / No | | Yes / No |
| Raw Source Material | Yes / No | | Yes / No |
| Evidence Preparation | Yes / No | | Yes / No |
| Information | Yes / No | | Yes / No |
| Knowledge | Yes / No | | Yes / No |
| Insight | Yes / No | | Yes / No |
| Challenge | Yes / No | | Yes / No |
| Decision | Yes / No | | Yes / No |
| Communication | Yes / No | | Yes / No |

### AI prompts or methods used

```text
Record important prompts, workflows, or tools used.
```

### AI limitations observed

```text
Record hallucinations, unsupported claims, missed evidence, or useful behavior.
```

---

## 19. Review Notes

### Reviewer questions

| Question | Answer |
|---|---|
| Does the evidence chain support the final judgment? | |
| Were unsupported insights rejected? | |
| Were collection windows handled correctly? | |
| Was derived evidence clearly distinguished from direct evidence? | |
| Were assumptions made explicit? | |
| Was uncertainty recorded? | |
| Would another engineer reach the same conclusion? | |

### Reviewer comments

```text
Add reviewer comments here.
```

---

## 20. Case Status

| Field | Value |
|---|---|
| Case status | Draft / Reviewed / Complete |
| Ready for publication? | Yes / No |
| Sanitization complete? | Yes / No / Not applicable |
| Follow-up required? | Yes / No |
| Follow-up owner | |

---

## 21. Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | | | Initial case study draft |
