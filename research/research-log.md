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

### Notes

This principle should appear consistently in:

- README
- Framework definition
- Articles
- Whitepaper
- Diagrams
- Case study templates

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

This may be the key difference between:

```text
AI-assisted troubleshooting
```

and

```text
Evidence-grounded AI-assisted troubleshooting
```

### Notes

Challenge questions include:

- What evidence supports this insight?
- What evidence contradicts this insight?
- What evidence is missing?
- What assumptions does this depend on?
- What alternative explanations exist?
- Did the timeline happen in the required order?
- Does source code support this interpretation?
- Is the documentation relevant to the correct version?

### Follow-up

Collect examples where Challenge rejects or weakens an initially plausible AI-generated hypothesis.

---

## 2026-06-22 - Initial Artefacts Created

**Type:** Artefact tracking  
**Status:** Recorded

### Summary

Created initial repository artefacts:

- `README.md`
- `framework/framework.md`
- `framework/terminology.md`
- `framework/changelog.md`
- `research/prior-art.md`

### Why It Matters

These files form the foundation of the project.

They establish:

- Project purpose
- Canonical framework definition
- Working terminology
- Framework change history
- Initial prior-art mapping

### Notes

Current recommended next artefacts:

1. `research/research-log.md`
2. `research/bibliography.md`
3. `cases/001-example.md`
4. `articles/01-introduction.md`

### Follow-up

Create bibliography and first case study template.

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

### Follow-up

Create `research/bibliography.md` with proper references and links.

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

### Notes

Recommended sequence:

1. Develop framework privately.
2. Apply to 3-5 case studies.
3. Get trusted peer feedback.
4. Publish practitioner article.
5. Iterate.
6. Produce whitepaper.
7. Consider tooling only after validation.

### Follow-up

Draft article outline once the foundational repository files are complete.

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

### Notes

Possible future tools:

- Markdown case study template
- YAML evidence-chain schema
- CLI for investigation notes
- Local evidence indexer
- RAG-based case study assistant
- Hypothesis challenge assistant
- Evidence graph visualizer

### Follow-up

After case studies, identify the smallest useful tool.

---

## 2026-06-22 - Employment and Publication Concern

**Type:** Risk note  
**Status:** Open

### Summary

Recognized a need to consider employment agreement, intellectual property, and publication policies before making the repository public.

### Why It Matters

The project is currently being developed personally, but the subject matter overlaps with professional experience in technical diagnosis and support engineering.

Before public release, it is sensible to review:

- Employment contract
- IP agreement
- Invention assignment language
- Publication policy
- Use of company resources
- Confidentiality obligations

### Notes

Current safe practice:

- Use personal repository
- Keep repository private initially
- Do not include customer data
- Do not include proprietary internal information
- Use sanitized, synthetic, or public case studies
- Avoid using company-owned material unless explicitly permitted

### Follow-up

Review relevant agreements before public release.

---

## 2026-06-22 - Case Study Direction

**Type:** Validation planning  
**Status:** Open

### Summary

Identified case studies as the most important next validation mechanism.

Potential case study sources:

- Sanitized support cases
- Public incident reports
- Synthetic distributed systems examples
- Public bug reports
- Public source code issues
- Reconstructed troubleshooting scenarios

### Why It Matters

The framework will only become credible if it can be applied to real or realistic investigations.

The most valuable examples will show where Challenge changes the result.

### Notes

Ideal case study structure:

```text
Evidence
Information
Knowledge
Insight
Challenge
Wisdom / Judgment
Decision
Action
Outcome
Learning
```

Important case study types:

1. AI insight accepted after challenge
2. AI insight rejected after challenge
3. Competing insights compared
4. Missing evidence prevents conclusion
5. Contradicting evidence changes decision

### Follow-up

Create `cases/001-example.md` as a reusable template.

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

---

## Candidate Article Ideas

Potential article sequence:

1. Why AI Troubleshooting Needs Evidence Grounding
2. From Logs to Evidence: The First Step in Safe AI Diagnosis
3. Information Is Not Insight: Structuring Observations for AI
4. Knowledge Sources: Documentation, Source Code, Bugs, and History
5. Why AI Insights Must Be Treated as Hypotheses
6. The Challenge Stage: Making AI Argue Against Itself
7. Human Judgment After AI Analysis
8. From Decision to Action Without Losing the Evidence Chain
9. Learning Loops: Turning Incidents into Future Diagnostic Memory
10. Evidence-Grounded AI Troubleshooting: A Worked Example

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

---

## Revision Notes

This research log begins on 2026-06-22.

Future entries should be added as the framework evolves, references are discovered, case studies are tested, and publication decisions are made.
