# EGATF Changelog

**Document type:** Framework change history  
**Status:** Active  
**Repository path:** `framework/changelog.md`

---

## Purpose

This changelog records the evolution of the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is to preserve a clear history of how the framework changes over time, including stage names, stage ordering, terminology changes, major design decisions, open questions, removed ideas, and validation findings.

This document should help maintain provenance and make the development of the framework auditable.

---

## Versioning Approach

EGATF will use simple research-stage versioning.

Example:

```text
v0.1 - Initial draft
v0.2 - Evidence stage refinement
v0.3 - Case study validation changes
v1.0 - First stable public framework
```

A version does not imply software compatibility. It represents the maturity of the framework definition.

---

## v0.2 - Evidence Stage Refinement

**Date:** 2026-06-24  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Refined the early part of the framework to better represent how support investigations actually begin.

The original v0.1 model moved directly from:

```text
Evidence
    ↓
Information
```

v0.2 expands the Evidence stage into a set of sub-stages:

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

This change recognizes that customer ticket summaries, alert descriptions, support bundles, logs, metrics, and extracted observations have different reliability levels and should not be treated as the same type of input.

### Added

Added the following concepts:

- Reported Context
- Raw Source Material
- Evidence Preparation
- Extracted Evidence
- Cold Analysis
- Guided Analysis
- Anchoring Risk
- Collector
- Evidence Extractor
- Normalizer
- Correlator
- Helper

### Changed

Updated `framework/framework.md` to:

- Add a new Evidence Stage Refinement section.
- Explain how reported context should be treated.
- Define cold and guided analysis.
- Define evidence preparation.
- Define extracted evidence.
- Add evidence preparation tooling categories.
- Update evidence chain requirements.
- Update AI roles in the framework.
- Add new open questions around evidence preparation and anchoring risk.

Updated `framework/terminology.md` to:

- Add terms for reported context, raw source material, evidence preparation, and extracted evidence.
- Add tooling terms for collectors, extractors, normalizers, correlators, and helpers.
- Add cold analysis, guided analysis, and anchoring risk.
- Update the definitions of Evidence and Information.
- Clarify that reported context is guidance, not ground truth.

Updated `README.md` to:

- Add a short Evidence Stage Refinement section.
- Include ticket summaries, alert descriptions, and support bundles in the problem framing.
- Add evidence preparation and anchoring risk to the current focus areas.

Updated `research/research-log.md` to:

- Record the v0.2 refinement and rationale.

### Rationale

Support investigations usually do not start with clean evidence.

They often start with a mixture of:

- Unvalidated problem description
- Customer-reported symptoms
- Customer-reported cause
- Alert wording
- Error message
- Support bundle snapshot
- Live telemetry
- Logs
- Metrics
- Command output

The framework needs to distinguish between:

1. What someone reported.
2. What raw material is available.
3. How that material was prepared.
4. What evidence was extracted.
5. What information was inferred from that evidence.

This reduces the risk that AI treats a ticket summary or guided statement as verified truth.

### Design Decision: Reported Context

Reported context is useful but unvalidated.

Rule added:

> Reported context is guidance, not ground truth.

Example:

> The database became slow after the upgrade.

This may include a reported symptom, a timeline claim, a component claim, and a causal claim. Each must be verified separately.

### Design Decision: Cold and Guided Analysis

Added two analysis modes.

Cold analysis:

```text
Review raw source material without assuming the reported problem or cause is correct.
```

Guided analysis:

```text
Use reported context as search guidance only. Treat causal claims as hypotheses until verified.
```

Recommended workflow:

```text
Cold pass
    ↓
Guided pass
    ↓
Compare findings
```

Reason:

This helps reduce anchoring bias while still allowing ticket summaries and reported errors to guide investigation.

### Design Decision: Evidence Preparation

Evidence preparation is now the term for mechanical extraction, filtering, parsing, normalizing, indexing, and correlating of raw source material.

Rule added:

> Evidence preparation should reduce noise without adding unsupported meaning.

This creates a clearer boundary between preparing evidence and diagnosing cause.

### Design Decision: Evidence Extractors

The preferred name for scripts that parse raw material into structured observations is now:

> Evidence Extractors

Reason:

- More precise than "helpers"
- Less problematic than "data cooking scripts"
- Keeps the focus on evidence and provenance
- Avoids implying final diagnosis

Related categories:

- Collectors
- Evidence Extractors
- Normalizers
- Correlators
- Helpers

### Current Framework Sequence

The top-level framework remains:

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

The Evidence stage now contains internal sub-stages:

```text
Reported Context
    ↓
Raw Source Material
    ↓
Evidence Preparation
    ↓
Extracted Evidence
```

### Open Questions Added

1. Should Evidence Preparation become a top-level framework stage?
2. How should reported context be scored?
3. How should cold and guided analysis be compared?
4. How should anchoring risk be represented?
5. How should extractor quality be tested?
6. Should evidence have formal classes such as reported, direct, indirect, derived, extracted, and authoritative?
7. What metadata is required for extracted evidence?
8. Should Confidence include agreement or disagreement between cold and guided analysis?
9. What naming will feel natural to support engineers?
10. How should scripts distinguish extraction from interpretation?

### Current Hypothesis

The v0.2 hypothesis is:

> Evidence preparation improves AI-assisted diagnosis by reducing noise while preserving traceability, but it must avoid embedding unsupported assumptions into the prepared evidence.

### Next Planned Work

1. Update or create a case study template that includes:
   - Reported Context
   - Raw Source Material
   - Evidence Preparation
   - Extracted Evidence
   - Information
   - Knowledge
   - Insight
   - Challenge
   - Wisdom / Judgment
   - Decision
   - Action
   - Outcome
   - Learning

2. Create a synthetic worked example showing:
   - Cold analysis
   - Guided analysis
   - A guided claim that turns out to be wrong or incomplete

3. Add future research into:
   - Evidence quality
   - Claim reliability
   - Anchoring bias
   - AI-assisted evidence extraction
   - Tool validation

---

## v0.1 - Initial Framework Definition

**Date:** 2026-06-22  
**Status:** Draft  
**Stage:** Early research and validation

### Summary

Created the initial working definition of the Evidence-Grounded AI Troubleshooting Framework.

The framework is intended to explore how AI and humans can work together to transform technical evidence into trustworthy decisions while reducing unsupported reasoning and hallucination.

### Initial Framework Sequence

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

### Core Principle Added

> Every insight must be traceable to evidence, and every piece of evidence must be traceable to the insight it supports.

Supporting statements:

> Without evidence, an insight is speculation.  
> Without traceability, an insight cannot be trusted.  
> Without challenge, an insight cannot become wisdom.

### Initial Problem Statement

AI systems are increasingly capable of analysing logs, metrics, support bundles, documentation, source code, bug reports, and operational observations.

However, AI-generated explanations are often plausible without being sufficiently grounded.

The framework begins from the observation that:

> AI is often better at generating explanations than demonstrating why those explanations should be trusted.

### Initial Research Question

Can AI-assisted troubleshooting be made more reliable by requiring every conclusion to be traceable back to evidence and every insight to survive deliberate challenge before influencing decisions?

### Initial Design Decisions

#### Evidence-first framing

The framework begins with **Evidence** rather than **Data**.

Reason:

In technical troubleshooting, the raw material is not just data. It includes logs, metrics, dumps, source code, documentation, bug reports, observations, and historical context. The term **Evidence** better captures the need for traceability and source reliability.

#### Challenge as a required stage

The framework includes **Challenge** between Insight and Wisdom.

Reason:

AI can generate plausible hypotheses quickly. The framework should require those hypotheses to be tested, weakened, contradicted, or rejected before they influence human judgment and decisions.

#### Human judgment retained

The framework does not position AI as the final decision maker.

Reason:

AI can assist with extraction, summarization, retrieval, hypothesis generation, and challenge, but humans remain accountable for judgment, decisions, and actions.

### Provisional Terms at v0.1

The following terms required further testing:

| Term | Reason Under Review |
|---|---|
| Wisdom | May be too abstract or difficult to distinguish from judgment |
| Challenge | May be renamed to Pressure Test, Validation, or Adversarial Review |
| Insight | May need clearer separation from Hypothesis |
| Knowledge | May need clearer separation between retrieved knowledge and human domain knowledge |
| Evidence | May need subtypes such as direct, indirect, derived, and authoritative evidence |

### Current Hypothesis

The strongest potential contribution of EGATF is the formal introduction of a **Challenge** stage into AI-assisted troubleshooting.

The key hypothesis is:

> A formal Challenge stage improves the quality and trustworthiness of AI-assisted troubleshooting by forcing insights to be tested against supporting, missing, and contradicting evidence before they influence human decisions.

---

## Future Version Notes

Use the following format for future entries:

```text
## vX.Y - Short Title

Date:
Status:
Stage:

### Summary

### Added

### Changed

### Removed

### Rationale

### Open Questions

### Next Planned Work
```

---

## Revision Notes

This changelog begins with v0.1 and should be updated whenever the framework definition, terminology, or major research direction changes.
