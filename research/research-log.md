# EGATF Research Log

**Document type:** Chronological research journal  
**Status:** Active  
**Repository path:** `research/research-log.md`

---

## Purpose

This document records the chronological development of the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The research log is intended to capture:

- Research questions
- Prior-art discoveries
- Design decisions
- Terminology changes
- Open concerns
- Validation ideas
- Case study candidates
- Publication planning
- Tooling ideas
- Important unresolved questions

This document is different from `framework/changelog.md`.

The changelog records formal changes to the framework.

The research log records the thinking, investigation, and discovery process around the framework.

---

## How to Use This Log

Add entries whenever meaningful progress is made.

Useful entry types:

- Research note
- Design decision
- Open question
- Reference discovered
- Case study idea
- Validation result
- Terminology concern
- Publication idea
- Tool idea

Suggested entry format:

```text
## YYYY-MM-DD - Short Title

Type:
Status:

### Summary

### Why It Matters

### Notes

### Follow-up
```

---

## 2026-06-24 - Evidence Preparation Taxonomy

**Type:** Framework refinement  
**Status:** Recorded

### Summary

Refined the difference between preparation and extraction.

The term Evidence Preparation is now treated as a broad category that includes:

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

This was needed because some tools used during support bundle analysis do not extract evidence. They transform or structure raw source material so it can be queried more effectively.

### Why It Matters

The framework needs to distinguish between tools that change the shape of source material and tools that select or compute notable observations.

Without this distinction, everything becomes an "extractor", which is inaccurate.

Example:

`wtl` converts tserver, master, and YBA logs into parquet files with structured columns. It does not consolidate, filter, or diagnose. Its output is still source material, but in a more queryable form.

Therefore, `wtl` is better classified as:

```text
Source Transformer / Log Structuring Tool
```

It produces:

```text
Structured Source Material
```

not:

```text
Extracted Evidence
```

unless another step selects notable observations from it.

### Notes

Boundary rules added:

```text
Transformation changes shape.
Extraction selects observations.
Derivation computes observations.
Correlation compares observations.
Information explains relationships.
```

This improves the Evidence stage by making it clearer which outputs are direct, structured, extracted, derived, or correlated.

### Follow-up

- Update framework document.
- Update terminology document.
- Create dedicated evidence preparation document.
- Update changelog.
- Update README.
- Update case study template later.

---

## 2026-06-24 - wtl Classification

**Type:** Tool classification  
**Status:** Recorded

### Summary

Classified `wtl` as a Source Transformer or Log Structuring Tool.

`wtl` takes tserver, master, and YBA logs, extracts each line into columns, and writes the result to parquet files.

It does not consolidate or filter at this layer.

It exists so that DuckDB can query logs more effectively than direct text search with tools such as ripgrep.

### Why It Matters

This is an important example because it shows the distinction between transformation and extraction.

`wtl` prepares source material, but it does not necessarily identify which observations matter.

### Notes

Classification:

```text
Tool type:
Source Transformer / Log Structuring Tool

Input:
Raw log files

Output:
Structured Source Material

Not:
Evidence Extractor, unless it also identifies notable observations.
```

Possible evidence chain:

```text
Raw log files
    ↓ wtl
Structured parquet logs
    ↓ DuckDB query
Extracted restart events
    ↓ timeline
Information
```

### Follow-up

Use this example in the first case study template or synthetic worked example.

---

## 2026-06-24 - Tablet Report Parser Classification

**Type:** Tool classification  
**Status:** Recorded

### Summary

Classified the tablet report parser as a hybrid tool.

It performs at least two conceptual roles:

1. It transforms a raw tablet report into SQLite or parquet tables.
2. It derives meaningful observations such as leaderless tablets, under-replicated tables, and over-replicated tables.

### Why It Matters

This shows that tools do not always fit into a single category.

The same binary can perform multiple roles, but its outputs should distinguish which layer they belong to.

### Notes

Classification:

```text
Tool type:
Hybrid

Roles:
Source Transformer
Derived Evidence Generator

Input:
Raw tablet report

Outputs:
Structured Source Material
Derived Evidence
```

Recommended conceptual output separation:

```text
source_tables/
    tablet_raw
    tablet_peer_raw
    tablet_replica_raw

derived_evidence/
    tablet_leader_status
    table_replication_status
    tablet_placement_status

findings/
    leaderless_tablets
    under_replicated_tables
    over_replicated_tables
```

The tool does not necessarily need to be physically split into separate binaries.

However, it should ideally separate direct structured source data from derived evidence and findings.

### Follow-up

Consider whether EGATF should define output naming conventions for hybrid tools.

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
Prepared Evidence Base
    ↓
Information
```

### Why It Matters

The original v0.1 flow moved directly from Evidence to Information.

That was too coarse.

A customer or ticket creator may provide a useful description, but that description is unvalidated. It may contain symptoms, timeline claims, component claims, and causal claims. Those claims should guide investigation, but should not be treated as verified truth.

### Notes

Added this rule:

> Reported context is guidance, not ground truth.

Added this rule:

> Evidence preparation should reduce noise without adding unsupported meaning.

### Follow-up

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

Cold analysis creates an independent baseline.

Guided analysis tests the reported context.

Comparing the two helps identify where the report was correct, incomplete, misleading, or wrong.

### Follow-up

Create a case study template section for:

- Cold analysis findings
- Guided analysis findings
- Differences
- Anchoring risks
- Claims verified
- Claims rejected

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

### Follow-up

- Add initial framework definition
- Add terminology glossary
- Add changelog
- Add prior-art register
- Add bibliography
- Add first case study template

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

### Follow-up

Test whether the Wisdom stage is useful in real case studies.

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

### Follow-up

Develop examples showing backward traceability from decision to evidence.

---

## 2026-06-22 - Challenge Stage Identified as Potential Contribution

**Type:** Research hypothesis  
**Status:** Important

### Summary

Identified **Challenge** as the potentially most distinctive stage of EGATF.

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an AI-generated insight before it influences human judgment.

### Why It Matters

AI can generate convincing explanations quickly. The Challenge stage creates a formal checkpoint where those explanations must survive pressure testing.

### Follow-up

Collect examples where Challenge rejects or weakens an initially plausible AI-generated hypothesis.

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

## 2026-06-22 - Initial Publication Strategy

**Type:** Publication planning  
**Status:** Draft

### Summary

Identified a staged publication strategy:

```text
GitHub
    ↓
LinkedIn
    ↓
Medium
    ↓
Whitepaper
```

### Why It Matters

GitHub should act as the source of truth.

LinkedIn is likely best for feedback and discovery among engineers, architects, SREs, and AI practitioners.

Medium can host longer article versions.

A whitepaper should wait until the framework has examples, feedback, and revision history.

---

## 2026-06-22 - Tooling Strategy

**Type:** Tool planning  
**Status:** Deferred

### Summary

Decided not to build a tool immediately.

Recommended order:

```text
Framework
    ↓
Examples
    ↓
Validation
    ↓
Community Feedback
    ↓
Tool
```

### Why It Matters

A tool built too early may encode the wrong model.

The current priority is validating whether the framework itself is useful and understandable.

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
11. How should AI-generated intermediate outputs be cited or recorded?
12. How should source authority be ranked?
13. How should version-specific documentation and source code be handled?
14. How should private or customer-sensitive evidence be sanitized?
15. Should Evidence Preparation become a top-level stage?
16. How should cold and guided analysis be compared?
17. How should anchoring risk be measured?
18. How should Evidence Extractors be validated?
19. Should extractor outputs have a standard schema?
20. Should Source Transformers and Evidence Extractors have distinct output schemas?
21. How should hybrid tools label structured, extracted, derived, and correlated outputs?

---

## Candidate Article Ideas

Potential article sequence:

1. Why AI Troubleshooting Needs Evidence Grounding
2. From Ticket Summary to Evidence: Avoiding Anchoring Bias
3. From Raw Source Material to Prepared Evidence
4. Source Transformation Is Not Evidence Extraction
5. Information Is Not Insight: Structuring Observations for AI
6. Knowledge Sources: Documentation, Source Code, Bugs, and History
7. Why AI Insights Must Be Treated as Hypotheses
8. The Challenge Stage: Making AI Argue Against Itself
9. Human Judgment After AI Analysis
10. From Decision to Action Without Losing the Evidence Chain
11. Learning Loops: Turning Incidents into Future Diagnostic Memory
12. Evidence-Grounded AI Troubleshooting: A Worked Example

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
- Source transformer correctness
- Derived evidence correctness
- Ratio of evidence with preserved provenance

---

## Revision Notes

This research log begins on 2026-06-22.

Future entries should be added as the framework evolves, references are discovered, case studies are tested, and publication decisions are made.
