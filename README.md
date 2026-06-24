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

Modern systems generate vast amounts of diagnostic material:

- Logs
- Metrics
- Traces
- Core dumps
- Support bundles
- Source code
- Documentation
- Bug reports
- Customer observations
- Historical incidents
- Ticket summaries
- Alert descriptions

AI systems are increasingly capable of analysing these sources and generating explanations.

However, a recurring challenge remains:

> AI is often better at generating explanations than demonstrating why those explanations should be trusted.

Many AI-generated conclusions are plausible, but lack a clear chain of evidence connecting observations to reasoning and ultimately to action.

This repository explores whether a structured framework can improve the trustworthiness, explainability, and auditability of AI-assisted troubleshooting.

---

## Research Question

Can AI-assisted troubleshooting be made more reliable by requiring every conclusion to be traceable back to evidence and every insight to survive deliberate challenge before influencing decisions?

---

## Current Framework (Draft)

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

The framework remains experimental and individual stages may evolve as research progresses.

---

## Evidence Stage Refinement

The Evidence stage contains several distinct sub-stages:

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

This distinction is important because ticket summaries, customer descriptions, alerts, logs, metrics, and support bundles have different reliability levels.

A ticket summary or customer report should guide the investigation, but should not be treated as verified cause.

A support bundle or live telemetry snapshot is raw source material.

Scripts and commands that parse, filter, normalize, and correlate this material are Evidence Extractors, Normalizers, or Correlators.

The output should be extracted evidence with provenance, not unsupported diagnosis.

---

## Core Principle

Every insight must be traceable to evidence, and every piece of evidence must be traceable to the insight it supports.

Without evidence, an insight is speculation.

Without traceability, an insight cannot be trusted.

Without challenge, an insight cannot become wisdom.

---

## Repository Structure

- `framework/` - Framework definitions, terminology, change history
- `research/` - Prior art, research notes, references
- `cases/` - Worked examples and validation exercises
- `articles/` - Draft articles and publications
- `paper/` - Whitepaper and formal publication drafts
- `diagrams/` - Visual models and supporting graphics

---

## Current Focus Areas

- AI-assisted troubleshooting
- Evidence-grounded reasoning
- Root cause analysis
- Retrieval-augmented diagnosis
- Evidence preparation
- Cold and guided analysis
- Anchoring risk in AI-assisted diagnosis
- Decision intelligence
- Human-in-the-loop systems
- Reducing AI hallucination in operational workflows

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
- Examples where guided analysis caused anchoring bias

---

## License

License to be determined.
