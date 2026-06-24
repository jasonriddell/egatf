# EGATF Research Log

**Document type:** Chronological research journal  
**Status:** Active  
**Repository path:** `research/research-log.md`

---

## Purpose

This document records the chronological development of the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The research log captures research questions, prior-art discoveries, design decisions, terminology changes, validation ideas, case study candidates, publication planning, tooling ideas, and important unresolved questions.

This document is different from `framework/changelog.md`.

The changelog records formal changes to the framework.

The research log records the thinking, investigation, and discovery process around the framework.

---

## 2026-06-24 - Collection Context Added

**Type:** Framework refinement  
**Status:** Recorded

### Summary

Added Collection Context as a distinct concept inside the Evidence stage.

Collection Context describes how an evidence package was created, what it contains, what time periods its contents represent, and how those contents should be interpreted.

This emerged from support bundle analysis.

A support bundle may have a requested duration, but not every file inside the bundle represents that duration.

Example:

```text
Support bundle created at:
T

Logs collected for:
T - 7 days to T - 5 days

Tablet metadata collected at:
T

Tablet report collected at:
T
```

### Why It Matters

Without explicit Collection Context, AI can make false correlations.

For example, it may use tablet state collected at T to explain log events from T - 7 to T - 5.

This is unsafe because tablet metadata, consensus metadata, and tablet reports may be collection-time snapshots rather than evidence of state during the requested log window.

### Notes

Updated Evidence stage model:

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

New principle:

> Evidence packages should describe their own collection context. AI should not be asked to infer timing, scope, source meaning, or collection limitations from raw files alone.

New formal term:

```text
Evidence Package Manifest
```

For support bundles, this may be implemented as:

```text
manifest.json
```

or as:

```text
manifest.json
bundle_context.json
file_index.json
```

### Follow-up

- Create `framework/collection-context.md`.
- Update framework document.
- Update terminology.
- Update changelog.
- Draft engineering feature request for support bundle manifest improvements.
- Update review deck.

---

## 2026-06-24 - Support Bundle Manifest Improvement Idea

**Type:** Engineering feature idea  
**Status:** Drafted

### Summary

Identified improvements to support bundle manifests to make support bundles more self-describing for humans, deterministic tools, and AI-assisted analysis.

Proposed additions include:

- Support bundle version
- Support bundle schema version
- Created time
- Universe identity
- Universe YBDB version
- YBA instance identity
- YBA version
- Replication factor
- TServer and master counts
- Provider
- Deployment type
- Infrastructure type
- Node Agent enabled state
- Metric collection level
- Metric duration, retention, and resolution
- Per-component collection windows
- AI-friendly component descriptions
- File index

### Why It Matters

YBA may move toward a release model where YBA is kept current while universes may run different YBDB versions.

This creates an opportunity to improve support bundle formats iteratively, as long as the support bundle schema and collector versions are explicit.

Automated analysis tools can select parsers based on support bundle schema version and fail safely when they encounter unknown versions.

### Notes

The feature request should emphasize that the manifest is not expected to diagnose the issue.

It should describe collection context.

---

## 2026-06-24 - Evidence Preparation Taxonomy

**Type:** Framework refinement  
**Status:** Recorded

### Summary

Refined the difference between preparation and extraction.

Evidence Preparation is now treated as a broad category that includes:

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

Example:

`wtl` converts tserver, master, and YBA logs into parquet files with structured columns. It does not consolidate, filter, or diagnose. Its output is still source material, but in a more queryable form.

Therefore, `wtl` is better classified as:

```text
Source Transformer / Log Structuring Tool
```

---

## 2026-06-24 - Tablet Report Parser Classification

**Type:** Tool classification  
**Status:** Recorded

### Summary

Classified the tablet report parser as a hybrid tool.

It performs at least two conceptual roles:

1. It transforms a raw tablet report into SQLite or parquet tables.
2. It derives meaningful observations such as leaderless tablets, under-replicated tables, and over-replicated tables.

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

---

## 2026-06-22 - Initial Project Formation

**Type:** Project formation  
**Status:** Recorded

### Summary

Started formalizing a research project around a proposed framework called the Evidence-Grounded AI Troubleshooting Framework, abbreviated as EGATF.

The initial motivation is to understand how AI can be used safely and effectively in technical diagnosis without allowing plausible but unsupported explanations to drive decisions.

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

---

## 2026-06-22 - Challenge Stage Identified as Potential Contribution

**Type:** Research hypothesis  
**Status:** Important

### Summary

Identified **Challenge** as the potentially most distinctive stage of EGATF.

Challenge is the deliberate attempt to test, weaken, disprove, or qualify an AI-generated insight before it influences human judgment.

---

## Open Research Questions

1. Does a formal Challenge stage improve AI-assisted troubleshooting?
2. Should Wisdom remain as a distinct framework stage?
3. What is the best name for Challenge?
4. Should Collection Context become a top-level stage?
5. How should confidence be represented?
6. How should contradicting evidence be represented?
7. How should missing evidence affect confidence?
8. What evidence metadata is required?
9. Can the framework work across different technical domains?
10. How much structure is useful before it becomes too heavy?
11. What is the minimum useful tooling?
12. How should AI-generated intermediate outputs be cited or recorded?
13. How should source authority be ranked?
14. How should version-specific documentation and source code be handled?
15. How should private or customer-sensitive evidence be sanitized?
16. Should Evidence Preparation become a top-level stage?
17. How should cold and guided analysis be compared?
18. How should anchoring risk be measured?
19. How should Evidence Extractors be validated?
20. Should extractor outputs have a standard schema?
21. Should Source Transformers and Evidence Extractors have distinct output schemas?
22. How should hybrid tools label structured, extracted, derived, and correlated outputs?
23. What should be included in a minimal Evidence Package Manifest?
24. Should AI-friendly component descriptions be embedded in support bundles?

---

## Candidate Article Ideas

Potential article sequence:

1. Why AI Troubleshooting Needs Evidence Grounding
2. From Ticket Summary to Evidence: Avoiding Anchoring Bias
3. Collection Context: Why Support Bundles Must Explain Themselves
4. From Raw Source Material to Prepared Evidence
5. Source Transformation Is Not Evidence Extraction
6. Information Is Not Insight: Structuring Observations for AI
7. Knowledge Sources: Documentation, Source Code, Bugs, and History
8. Why AI Insights Must Be Treated as Hypotheses
9. The Challenge Stage: Making AI Argue Against Itself
10. Human Judgment After AI Analysis
11. From Decision to Action Without Losing the Evidence Chain
12. Learning Loops: Turning Incidents into Future Diagnostic Memory
13. Evidence-Grounded AI Troubleshooting: A Worked Example
