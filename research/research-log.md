# EGATF Research Log

**Document type:** Chronological research journal  
**Status:** Active  
**Repository path:** `research/research-log.md`

---

## Purpose

This document records the chronological development of the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The research log is intended to capture research questions, prior-art discoveries, design decisions, terminology changes, open concerns, validation ideas, case study candidates, publication planning, tooling ideas, and important unresolved questions.

This document is different from `framework/changelog.md`.

The changelog records formal changes to the framework.

The research log records the thinking, investigation, and discovery process around the framework.

---

## 2026-06-24 - Evidence Stage Refinement

**Type:** Framework refinement  
**Status:** Recorded

### Summary

Refined the early part of EGATF after identifying that support investigations rarely begin with clean evidence.

They usually begin with a mixture of:

- Customer problem description
- Ticket summary
- Alert title
- Reported error message
- Support bundle
- Live metrics
- Logs
- Command output
- Observations from first responders

The framework now distinguishes between:

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

### Why It Matters

The original v0.1 flow moved directly from Evidence to Information.

That was too coarse.

A customer or ticket creator may provide a useful description, but that description is unvalidated. It may contain symptoms, timeline claims, component claims, and causal claims. Those claims should guide investigation, but should not be treated as verified truth.

A support bundle or live environment snapshot is raw source material. It is not yet information.

Scripts, commands, and filters that extract useful observations from raw source material are part of evidence preparation. Their output should be extracted evidence with provenance, not unsupported diagnosis.

### Notes

Added this rule:

> Reported context is guidance, not ground truth.

Added this rule:

> Evidence preparation should reduce noise without adding unsupported meaning.

Added preferred naming:

> Evidence Extractor

This term is preferred for scripts that parse raw source material and produce structured evidence with provenance.

Other tooling categories:

- Collector
- Evidence Extractor
- Normalizer
- Correlator
- Helper

The term **Helper** should be reserved for later workflow assistance, such as generating an engineering escalation, customer update, or post-incident review outline.

### Follow-up

- Update framework document.
- Update terminology document.
- Update changelog.
- Update README.
- Update case study template to include the refined Evidence sub-stages.
- Create a synthetic case showing cold analysis, guided analysis, and anchoring risk.

---

## 2026-06-24 - Cold and Guided Analysis

**Type:** Analysis model  
**Status:** Recorded

### Summary

Introduced two analysis modes:

```text
Cold Analysis
Guided Analysis
```

Cold analysis reviews raw source material without assuming that the reported problem or reported cause is correct.

Guided analysis uses reported context to guide search and extraction, but treats causal claims as hypotheses only.

Recommended workflow:

```text
Cold pass
    ↓
Guided pass
    ↓
Compare findings
```

### Why It Matters

Guided statements can be useful, especially when a support bundle is large and noisy.

However, they can also create anchoring bias.

If the ticket says "the upgrade caused latency", AI may focus on upgrade-related evidence and miss an unrelated disk, network, load, or configuration event.

Cold analysis creates an independent baseline.

Guided analysis tests the reported context.

Comparing the two helps identify where the report was correct, incomplete, misleading, or wrong.

### Notes

This creates a possible future validation pattern:

1. Run AI cold against prepared evidence.
2. Run AI guided by ticket summary.
3. Compare findings.
4. Identify whether guidance improved focus or created bias.
5. Record where guided analysis changed confidence.

### Follow-up

Create a case study template section for:

- Cold analysis findings
- Guided analysis findings
- Differences
- Anchoring risks
- Claims verified
- Claims rejected

---

## 2026-06-24 - Evidence Extractors Naming

**Type:** Terminology decision  
**Status:** Recorded

### Summary

Chose **Evidence Extractor** as the preferred term for scripts, commands, or tools that extract useful observations from raw diagnostic material.

Rejected or deprioritized alternatives:

- Helpers
- Fact finders
- Data cooking scripts

### Why It Matters

"Helpers" is too broad and better fits later workflow scripts, such as generating engineering escalations or summaries.

"Fact finders" is friendly, but may overstate what the scripts do. A script may extract observations, but those observations still need context, provenance, and sometimes verification.

"Data cooking scripts" is risky because "cooking data" can imply altering or massaging data to fit a theory.

"Evidence Extractor" fits the framework language and keeps provenance central.

### Notes

Current tooling taxonomy:

```text
Collectors
    Gather raw source material.

Evidence Extractors
    Extract structured observations with provenance.

Normalizers
    Convert data into consistent formats.

Correlators
    Compare extracted evidence across time, nodes, components, or sources.

Helpers
    Support communication, escalation, reporting, or follow-up.
```

### Follow-up

Consider whether these categories should become a dedicated document later, possibly:

```text
framework/tooling-taxonomy.md
```

Do not create this file yet unless the tooling concepts continue to expand.

---

## 2026-06-22 - Initial Project Formation

**Type:** Project formation  
**Status:** Recorded

### Summary

Started formalizing a research project around a proposed framework called the Evidence-Grounded AI Troubleshooting Framework, abbreviated as EGATF.

The initial motivation is to understand how AI can be used safely and effectively in technical diagnosis without allowing plausible but unsupported explanations to drive decisions.

The project is currently being developed in a personal GitHub repository named `egatf`.

### Why It Matters

The repository provides a place to track artefacts, research notes, framework revisions, and future case studies.

Using GitHub also preserves version history and supports provenance if the framework later becomes public.

### Notes

Current repository positioning:

> Researching how AI and humans can transform evidence into trustworthy decisions.

Current recommended repository visibility:

- Private during early formation
- Potentially public once terminology, examples, and prior art are stronger

---

## 2026-06-22 - Initial Framework Shape

**Type:** Framework design  
**Status:** Draft

### Summary

Defined the initial EGATF sequence:

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

### Why It Matters

This sequence reframes traditional DIKW-style thinking for AI-assisted technical diagnosis.

The framework begins with **Evidence** rather than **Data** because technical troubleshooting depends on source reliability, traceability, and interpretation of observed material.

### Notes

The framework is currently a working hypothesis.

Stable-looking stages:

- Evidence
- Information
- Knowledge
- Insight
- Challenge
- Decision
- Action
- Outcome
- Learning

Stages under review:

- Wisdom

The term **Wisdom** may be too abstract. It currently represents human judgment after challenge, but may be renamed or removed later.

---

## 2026-06-22 - Core Principle Identified

**Type:** Design principle  
**Status:** Draft

### Summary

Defined the current core principle:

> Every insight must be traceable to evidence, and every piece of evidence must be traceable to the insight it supports.

Supporting language:

> Without evidence, an insight is speculation.  
> Without traceability, an insight cannot be trusted.  
> Without challenge, an insight cannot become wisdom.

### Why It Matters

This principle separates EGATF from generic AI troubleshooting.

The framework is not only about generating explanations. It is about preserving an auditable path from source material to decision.

---

## 2026-06-22 - Challenge Stage Identified as Potential Contribution

**Type:** Research hypothesis  
**Status:** Important

### Summary

Identified **Challenge** as the potentially most distinctive stage of EGATF.

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an AI-generated insight before it influences human judgment.

### Why It Matters

AI can generate convincing explanations quickly. The Challenge stage creates a formal checkpoint where those explanations must survive pressure testing.

This may be the key difference between:

```text
AI-assisted troubleshooting
```

and

```text
Evidence-grounded AI-assisted troubleshooting
```

---

## 2026-06-22 - Prior Art Areas Identified

**Type:** Prior-art research  
**Status:** Initial

### Summary

Identified initial areas of related work:

- DIKW
- DIEK
- Root Cause Analysis
- Retrieval-Augmented Generation
- Grounded generation
- Claim verification
- LLM-based root cause analysis
- AIOps
- Decision intelligence
- Scientific method
- Evidence-based reasoning
- Post-incident review and learning loops

### Why It Matters

EGATF should not be positioned as an idea created in isolation.

It should be positioned as a practical synthesis of existing ideas applied to AI-assisted technical diagnosis.

### Notes

Safe positioning:

> EGATF is a proposed practitioner framework that synthesizes DIKW, evidence-based reasoning, RAG, root cause analysis, and decision intelligence for AI-assisted technical diagnosis.

Avoid overclaiming:

> EGATF is the first framework for AI troubleshooting.

---

## Open Research Questions

Current open questions:

1. Does a formal Challenge stage improve AI-assisted troubleshooting?
2. Should Wisdom remain as a distinct framework stage?
3. What is the best name for Challenge?
4. How should confidence be represented?
5. How should contradicting evidence be represented?
6. How should missing evidence affect confidence?
7. What evidence metadata is required?
8. Can the framework work across different technical domains?
9. How much structure is useful before it becomes too heavy?
10. What is the minimum useful tooling?
11. How should the framework avoid becoming just another RCA checklist?
12. How should AI-generated intermediate outputs be cited or recorded?
13. How should source authority be ranked?
14. How should version-specific documentation and source code be handled?
15. How should private or customer-sensitive evidence be sanitized?
16. Should Evidence Preparation become a top-level stage?
17. How should cold and guided analysis be compared?
18. How should anchoring risk be measured?
19. How should Evidence Extractors be validated?
20. Should extractor outputs have a standard schema?

---

## Candidate Article Ideas

Potential article sequence:

1. Why AI Troubleshooting Needs Evidence Grounding
2. From Ticket Summary to Evidence: Avoiding Anchoring Bias
3. From Raw Source Material to Extracted Evidence
4. Information Is Not Insight: Structuring Observations for AI
5. Knowledge Sources: Documentation, Source Code, Bugs, and History
6. Why AI Insights Must Be Treated as Hypotheses
7. The Challenge Stage: Making AI Argue Against Itself
8. Human Judgment After AI Analysis
9. From Decision to Action Without Losing the Evidence Chain
10. Learning Loops: Turning Incidents into Future Diagnostic Memory
11. Evidence-Grounded AI Troubleshooting: A Worked Example

---

## Candidate Validation Metrics

Possible ways to evaluate EGATF:

- Number of unsupported insights detected
- Number of contradicted hypotheses rejected
- Time to identify missing evidence
- Quality of evidence traceability
- Reduction in speculative conclusions
- Human reviewer confidence
- Reproducibility of diagnosis
- Agreement between independent reviewers
- Corrective action quality
- Reuse of learning in future cases
- Agreement between cold and guided analysis
- Number of guided claims verified
- Number of guided claims rejected
- Number of unexpected cold analysis findings
- Evidence extractor precision and recall

---

## Revision Notes

This research log begins on 2026-06-22.

Future entries should be added as the framework evolves, references are discovered, case studies are tested, and publication decisions are made.
