# EGATF

**Evidence-Grounded AI Troubleshooting Framework**

Researching how AI and humans can transform evidence into trustworthy decisions.

---

## Status

**Research Project - Early Development**

This repository contains the ongoing development of the Evidence-Grounded AI Troubleshooting Framework (EGATF), a proposed methodology for using AI to assist with troubleshooting, diagnosis, and decision-making while maintaining a verifiable chain of evidence from source observations to final conclusions.

The framework is currently under active development and should be considered a working hypothesis rather than a finished model.

---

## The Problem

Modern systems generate vast amounts of diagnostic material: logs, metrics, traces, dumps, support bundles, source code, documentation, bug reports, customer observations, ticket summaries, alert descriptions, and historical incidents.

AI systems are increasingly capable of analysing these sources and generating explanations.

However, a recurring challenge remains:

> AI is often better at generating explanations than demonstrating why those explanations should be trusted.

Many AI-generated conclusions are plausible, but lack a clear chain of evidence connecting observations to reasoning and ultimately to action.

---

## Research Question

Can AI-assisted troubleshooting be made more reliable by requiring every conclusion to be traceable back to evidence and every insight to survive deliberate challenge before influencing decisions?

---

## Current Framework

The framework can be introduced as a chain:

```text
Evidence -> Information -> Knowledge -> Insight -> Challenge -> Judgment -> Decision -> Action -> Outcome -> Learning
```

But the operating model is now three gated loops:

```text
Loop 1: Evidence Loop
Can we trust what we are reasoning from?

Loop 2: Reasoning Loop
Can we trust what we believe?

Loop 3: Action Loop
Can we trust what happened next?
```

The loops are intended to prevent a straight-line march from weak evidence to wrong diagnosis.

---

## Evidence Loop

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

Gate:

> Do we understand the evidence well enough to reason from it?

The Evidence Loop helps prevent:

- Customer reports being treated as verified cause
- Collection-time evidence being confused with duration-based evidence
- Missing files being interpreted as absence of a problem
- Structured source material being mistaken for extracted evidence
- Derived evidence being mistaken for direct evidence

---

## Reasoning Loop

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

Gate:

> Has the insight survived enough challenge to become responsible judgment?

The Reasoning Loop helps prevent:

- Plausible AI-generated explanations becoming conclusions too early
- Wrong-version documentation or source code being used as knowledge
- Anchoring on the original ticket summary
- Alternative explanations being ignored
- Missing or contradicting evidence being hidden

Cold analysis and guided analysis should be run in isolated analysis sandboxes, then compared. Cold analysis reviews the evidence without being guided by the reported problem. Guided analysis uses reported context as search guidance only. The comparison helps expose anchoring risk and unexpected findings.

Reference knowledge sources should be validated before they are used to support insights. This includes checking product version, deployment context, source authority, and relevance to the evidence being evaluated.

---

## Action Loop

The Action Loop turns judgment into decision, action, measured outcome, and learning.

```text
Decision
    ↓
Action
    ↓
Outcome
    ↓
Learning
```

Gate:

> Did the action produce the expected outcome, and what should be learned or revisited?

The Action Loop helps prevent:

- Acting on low-confidence judgment
- Taking unsafe or unauthorized actions
- Ignoring outcomes that contradict the diagnosis
- Failing to capture lessons for future investigations

If the outcome does not support the judgment, the process should loop back to Challenge, Insight, Evidence Preparation, or additional evidence collection as needed.

---

## Diagnostic Knowledge Patterns

EGATF includes an experimental Diagnostic Knowledge Pattern format for recording reusable knowledge from previous investigations.

A Diagnostic Knowledge Pattern describes a known issue or diagnostic scenario in abstract evidence terms rather than as brittle command-line searches or raw text matches.

Patterns should describe:

- Applicable product, component, version, and deployment context
- Reported-context clues
- Required evidence
- Optional evidence
- Contradicting evidence
- Missing evidence
- Time relationships
- Knowledge-source validation requirements
- Challenge questions
- Confidence impact
- Possible insights
- Conclusions that are not allowed without further evidence

The goal is to make previous issues reusable as Knowledge sources while preserving evidence traceability and avoiding direct dependence on support bundle layout, parser version, or `rg` command matches.

Diagnostic Knowledge Patterns live in:

```text
knowledge-patterns/
```

The pattern schema lives in:

```text
schemas/
```

The framework explanation lives in:

```text
framework/diagnostic-knowledge-patterns.md
```

Diagnostic Knowledge Patterns should not directly declare root cause. They should identify when a known diagnostic pattern is consistent with the available evidence, what evidence is still required, and what challenge questions must be answered before an insight can become judgment.

---

## Core Principle

Every insight must be traceable to evidence, and every piece of evidence must be traceable to the insight it supports.

Without evidence, an insight is speculation.

Without traceability, an insight cannot be trusted.

Without challenge, an insight should not become judgment.

Additional principles:

> Evidence packages should describe their own collection context. AI should not be asked to infer timing, scope, source meaning, or collection limitations from raw files alone.

> Use deterministic preparation tools where possible to reduce noise, preserve provenance, and give AI cleaner evidence to reason over.

> Reusable diagnostic knowledge should describe semantic evidence requirements, not brittle text searches.

---

## Current Focus Areas

- AI-assisted troubleshooting
- Evidence-grounded reasoning
- Three-loop diagnostic process design
- Evidence Sufficiency Gate
- Challenge Confidence Gate
- Outcome Validation Gate
- Collection context
- Evidence package manifests
- Support bundle metadata
- Evidence preparation
- Source transformation
- Evidence extraction
- Derived evidence generation
- Diagnostic Knowledge Patterns
- Semantic observation vocabulary
- Knowledge-source validation
- Version-independent diagnostic patterns
- Cold and guided analysis
- Isolated cold and guided analysis sandboxes
- Reference knowledge validation
- Anchoring risk in AI-assisted diagnosis
- Reducing AI hallucination in operational workflows

---

## Repository Structure

- `framework/` - Framework definitions, terminology, process flow, stage details, and change history
- `schemas/` - Machine-readable schemas for framework artefacts
- `knowledge-patterns/` - Reusable diagnostic knowledge patterns
- `research/` - Prior art, research notes, investigation threads, and references
- `cases/` - Worked examples and validation exercises
- `articles/` - Draft articles and publications
- `paper/` - Whitepaper and formal publication drafts
- `diagrams/` - Visual models and supporting graphics
- `engineering/` - Engineering feature requests and implementation notes
- `presentations/` - Optional slide decks and review presentations

---

## Current Repository Artefacts

Current core framework artefacts include:

```text
framework/framework.md
framework/terminology.md
framework/process-flow.md
framework/stage-deep-dives.md
framework/challenge-evaluation.md
framework/evidence-preparation.md
framework/collection-context.md
framework/diagnostic-knowledge-patterns.md
framework/changelog.md
```

Current validation and research artefacts include:

```text
cases/001-template.md
research/research-log.md
research/prior-art.md
research/bibliography.md
research/investigation-thread-tracker.md
```

Current diagnostic knowledge artefacts include:

```text
schemas/diagnostic-knowledge-pattern.schema.yaml
knowledge-patterns/
```

---

## Contributing

The framework is currently in the research and validation phase.

Feedback, criticism, alternative viewpoints, and references to related work are welcome.

Particular interest exists in:

- Prior art
- Similar frameworks
- Case studies
- Failure modes
- Validation approaches
- Evidence extraction approaches
- Evidence preparation tooling
- Collection context models
- Diagnostic Knowledge Patterns
- Semantic observation vocabularies
- Knowledge-source validation models
- Examples where missing collection context caused incorrect analysis
- Examples where guided analysis caused anchoring bias
- Examples where previous issue knowledge helped or misled an investigation

---

## License

License to be determined.
