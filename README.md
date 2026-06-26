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
Evidence -> Information -> Knowledge -> Insight -> Challenge -> Wisdom -> Decision -> Action -> Outcome -> Learning
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
Wisdom / Judgment
```

Gate:

> Has the insight survived enough challenge to become responsible judgment?

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

---

## Core Principle

Every insight must be traceable to evidence, and every piece of evidence must be traceable to the insight it supports.

Without evidence, an insight is speculation.

Without traceability, an insight cannot be trusted.

Without challenge, an insight cannot become wisdom.

Additional principles:

> Evidence packages should describe their own collection context. AI should not be asked to infer timing, scope, source meaning, or collection limitations from raw files alone.

> Use deterministic preparation tools where possible to reduce noise, preserve provenance, and give AI cleaner evidence to reason over.

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
- Cold and guided analysis
- Anchoring risk in AI-assisted diagnosis
- Reducing AI hallucination in operational workflows

---

## Repository Structure

- `framework/` - Framework definitions, terminology, process flow, stage details, and change history
- `research/` - Prior art, research notes, and references
- `cases/` - Worked examples and validation exercises
- `articles/` - Draft articles and publications
- `paper/` - Whitepaper and formal publication drafts
- `diagrams/` - Visual models and supporting graphics
- `engineering/` - Engineering feature requests and implementation notes

---

## License

License to be determined.
