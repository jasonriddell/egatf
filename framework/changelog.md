# EGATF Changelog

**Document type:** Framework change history  
**Status:** Active  
**Repository path:** `framework/changelog.md`

---

## Purpose

This changelog records the evolution of the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is to preserve a clear history of how the framework changes over time, including:

- Stage names
- Stage ordering
- Terminology changes
- Major design decisions
- Open questions
- Removed ideas
- Validation findings

This document should help maintain provenance and make the development of the framework auditable.

---

## Versioning Approach

EGATF will use simple research-stage versioning.

Example:

```text
v0.1 - Initial draft
v0.2 - Terminology refinement
v0.3 - Case study validation changes
v1.0 - First stable public framework
```

A version does not imply software compatibility. It represents the maturity of the framework definition.

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

### Initial Repository Artefacts

Created or planned the following foundational artefacts:

- `README.md`
- `framework/framework.md`
- `framework/terminology.md`
- `framework/changelog.md`
- `research/prior-art.md`
- `research/research-log.md`
- `research/bibliography.md`
- `cases/001-example.md`
- `articles/01-introduction.md`
- `paper/whitepaper.md`
- `diagrams/`

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

### Stable Terms at v0.1

The following terms currently appear stable:

- Evidence
- Information
- Knowledge
- Insight
- Challenge
- Decision
- Action
- Outcome
- Learning
- Evidence chain
- Traceability
- Unsupported insight
- Contradicting evidence
- Missing evidence

### Provisional Terms at v0.1

The following terms require further testing:

| Term | Reason Under Review |
|---|---|
| Wisdom | May be too abstract or difficult to distinguish from judgment |
| Challenge | May be renamed to Pressure Test, Validation, or Adversarial Review |
| Insight | May need clearer separation from Hypothesis |
| Knowledge | May need clearer separation between retrieved knowledge and human domain knowledge |
| Evidence | May need subtypes such as direct, indirect, derived, and authoritative evidence |

### Open Questions Added

1. Should **Wisdom** remain as a distinct stage?
2. Should **Challenge** be renamed to Validation, Pressure Test, or Adversarial Review?
3. Should Evidence and Information be separated more formally?
4. How should confidence be represented?
5. How should contradictory evidence be tracked?
6. What metadata is required for a useful evidence item?
7. Can the framework be applied consistently across different technical domains?
8. Does the Challenge stage measurably improve outcomes?
9. How should case studies be anonymized and sanitized?
10. What is the smallest useful tool that could support the workflow?

### Current Hypothesis

The strongest potential contribution of EGATF is the formal introduction of a **Challenge** stage into AI-assisted troubleshooting.

The key hypothesis is:

> A formal Challenge stage improves the quality and trustworthiness of AI-assisted troubleshooting by forcing insights to be tested against supporting, missing, and contradicting evidence before they influence human decisions.

### Next Planned Work

The next planned artefacts are:

1. `research/prior-art.md`
2. `research/research-log.md`
3. `cases/001-example.md`
4. `articles/01-introduction.md`

The next research task is to compare EGATF against related concepts, including:

- DIKW
- Root Cause Analysis
- Retrieval-Augmented Generation
- Grounded generation
- AIOps
- Decision Intelligence
- Scientific method
- Evidence-based reasoning
- Post-incident review and learning loops

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
