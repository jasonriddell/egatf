# EGATF Prior Art Register

**Document type:** Research register  
**Status:** Draft v0.1  
**Repository path:** `research/prior-art.md`

---

## Purpose

This document tracks existing ideas, models, research areas, and practices related to the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The goal is not to prove that EGATF is entirely new.

The goal is to understand what EGATF inherits, what it adapts, what it combines, and where it may make a useful contribution.

EGATF should be positioned as a practical synthesis of existing ideas rather than as an invention created in isolation.

---

## Positioning Statement

EGATF is currently best understood as a practitioner-focused synthesis of:

- DIKW and related knowledge hierarchies
- Evidence-based reasoning
- Root cause analysis
- Retrieval-augmented generation
- Grounded AI generation
- LLM-assisted incident diagnosis
- Decision intelligence
- Human-in-the-loop systems
- Post-incident learning loops

The proposed contribution is not simply that AI can assist troubleshooting.

The proposed contribution is a structured workflow requiring AI-generated insights to remain traceable to evidence and to survive deliberate challenge before influencing human decisions.

---

## Summary Table

| Area | What It Contributes | What EGATF Adds or Changes |
|---|---|---|
| DIKW | Data to information to knowledge to wisdom | Replaces generic data with evidence and adds challenge, decision, action, outcome, and learning |
| DIEK | Adds evidence into the data-information-knowledge chain | Extends toward operational troubleshooting and human decision-making |
| Root Cause Analysis | Hypothesis testing and cause identification | Adds AI-specific grounding, traceability, and challenge discipline |
| RAG | Grounding AI answers in retrieved sources | Applies grounding to diagnostic workflows, not just answer generation |
| Grounded generation | Reduces unsupported claims | Connects grounding to decisions, actions, outcomes, and learning |
| LLM RCA / AIOps | Uses AI for incident and failure diagnosis | Provides a general practitioner framework rather than a tool-specific architecture |
| Decision Intelligence | Links analysis to decisions and outcomes | Starts earlier with evidence extraction and hypothesis challenge |
| Scientific method | Hypothesis, test, revise | Adapts the pattern for AI-assisted troubleshooting |
| Post-incident review | Captures learning after action | Makes learning part of the reasoning loop |

---

## 1. DIKW

### Description

DIKW stands for:

```text
Data → Information → Knowledge → Wisdom
```

It is widely used in knowledge management and information science to describe increasing levels of meaning and judgment.

### What EGATF Borrows

EGATF borrows the idea that raw material can be transformed through increasingly meaningful stages.

The EGATF sequence includes similar concepts:

```text
Evidence → Information → Knowledge → Insight → Challenge → Judgment
```

### What EGATF Changes

EGATF differs from classic DIKW in several ways:

1. It begins with **Evidence** rather than generic **Data**.
2. It adds **Insight** as a hypothesis-generating stage.
3. It adds **Challenge** as a formal pressure-testing stage.
4. It extends beyond judgment into **Decision**, **Action**, **Outcome**, and **Learning**.
5. It is designed for AI-assisted troubleshooting rather than general knowledge management.

### Why This Matters

DIKW is useful as background, but it does not directly solve the problem of AI-generated plausible but unsupported diagnostic conclusions.

EGATF attempts to make the hierarchy operational for technical diagnosis.

### References to Investigate

- Russell Ackoff's original knowledge hierarchy work
- Later DIKW critiques and variants
- DIKW usage in data science and knowledge management

---

## 2. DIEK

### Description

DIEK stands for:

```text
Data → Information → Evidence → Knowledge
```

DIEK modifies DIKW by introducing **Evidence** between information and knowledge.

### What EGATF Borrows

EGATF shares the view that evidence deserves explicit treatment.

This is important because diagnosis is not only about turning data into meaning. It is about deciding which observations are strong enough to support a conclusion.

### What EGATF Changes

EGATF places **Evidence** at the beginning rather than between information and knowledge.

Reason:

In troubleshooting, the starting material is already evidence-like:

- Logs
- Metrics
- Dumps
- Source code
- Documentation
- Bug reports
- Customer observations

EGATF treats these as evidence sources from the start.

### Why This Matters

DIEK is a useful prior-art reference because it shows that others have already identified evidence as a missing concept in DIKW-style hierarchies.

EGATF extends that concern into AI-assisted operational diagnosis.

### References to Investigate

- Dammann O. "Data, Information, Evidence, and Knowledge: A Proposal for Health Informatics and Data Science"

---

## 3. Root Cause Analysis

### Description

Root Cause Analysis (RCA) is a family of practices used to identify underlying causes of problems or incidents.

Common RCA practices include:

- Timeline construction
- Five Whys
- Fault tree analysis
- Fishbone diagrams
- Causal chain analysis
- Corrective and preventive actions

### What EGATF Borrows

EGATF borrows the idea that troubleshooting should move beyond symptoms to plausible causes.

It also borrows the need to test explanations against facts.

### What EGATF Changes

EGATF is not a generic RCA method.

It focuses specifically on AI-assisted reasoning and asks:

- What did AI extract?
- What did AI infer?
- What evidence supports the inference?
- What evidence contradicts it?
- What uncertainty remains?
- What should humans accept, reject, or investigate next?

### Why This Matters

RCA methods are strong at causal thinking, but many do not explicitly handle AI-generated hypotheses, hallucination, source grounding, or citation traceability.

EGATF attempts to bring RCA discipline into AI workflows.

### References to Investigate

- Five Whys
- Fault tree analysis
- Incident postmortem practices
- SRE post-incident review practices
- Causal analysis methods

---

## 4. Retrieval-Augmented Generation

### Description

Retrieval-Augmented Generation (RAG) improves LLM outputs by retrieving relevant external sources and using them as context during generation.

RAG is commonly used to ground AI responses in documents, knowledge bases, source code, or other external material.

### What EGATF Borrows

EGATF borrows the principle that AI-generated claims should be grounded in retrieved sources.

Relevant EGATF sources may include:

- Documentation
- Source code
- Bug reports
- Historical incidents
- Runbooks
- Logs
- Metrics
- Support bundles

### What EGATF Changes

RAG is usually framed as an answer-generation architecture.

EGATF frames grounding as part of a broader troubleshooting workflow:

```text
Evidence → Information → Knowledge → Insight → Challenge → Decision → Action → Outcome → Learning
```

In EGATF, retrieval is necessary but not sufficient.

The retrieved source must be used in an evidence chain and then challenged.

### Why This Matters

RAG can reduce hallucination, but it does not automatically ensure that conclusions are correct, complete, or safe to act on.

EGATF treats RAG as one mechanism inside a larger diagnostic discipline.

### References to Investigate

- Retrieval-augmented generation papers
- Grounded generation methods
- Citation-aware RAG
- Claim-level verification
- RAG hallucination detection

---

## 5. Grounded Generation and Claim Verification

### Description

Grounded generation focuses on ensuring that AI outputs are supported by provided or retrieved sources.

Related work includes:

- Claim verification
- Citation verification
- Evidence selection
- Faithfulness evaluation
- Hallucination detection
- Natural language inference-based checking

### What EGATF Borrows

EGATF borrows the idea that each generated claim should be checked against evidence.

This maps directly to the EGATF Challenge stage.

### What EGATF Changes

EGATF applies claim verification to technical diagnosis and operational decision-making.

Instead of only asking:

> Is this generated sentence supported by the source?

EGATF also asks:

> Is this diagnostic explanation strong enough to influence a human decision or operational action?

### Why This Matters

A claim can be individually grounded while the overall diagnosis remains incomplete.

EGATF tries to evaluate not only claim-level support, but also the reasoning chain from evidence to action.

### References to Investigate

- Evidence-grounded RAG
- Citation hallucination detection
- Claim verification systems
- Retrieval-grounded detection of hallucinations

---

## 6. LLM-Based Root Cause Analysis and AIOps

### Description

Recent research and tools use LLMs to assist with incident diagnosis and root cause analysis using:

- Logs
- Metrics
- Traces
- Alerts
- Service topology
- Historical incidents
- Runbooks
- Domain knowledge

Examples include research systems and tool architectures for LLM-assisted RCA.

### What EGATF Borrows

EGATF borrows the use case of applying AI to operational diagnosis.

It assumes AI can help with:

- Clustering evidence
- Building timelines
- Retrieving relevant context
- Suggesting hypotheses
- Comparing similar incidents
- Summarizing investigation state

### What EGATF Changes

EGATF is not primarily a tool architecture.

It is a reasoning framework that can be applied with or without a specific AIOps product.

EGATF emphasizes:

- Evidence chains
- Explicit uncertainty
- Contradicting evidence
- Missing evidence
- Human judgment
- Learning from outcomes

### Why This Matters

LLM RCA systems often aim to automate diagnosis.

EGATF is more cautious. It aims to make diagnosis more trustworthy and reviewable, not fully automatic.

### References to Investigate

- RCACopilot
- OpenRCA
- LLM-based incident diagnosis papers
- AIOps RCA frameworks
- Multi-agent RCA systems

---

## 7. Decision Intelligence

### Description

Decision Intelligence focuses on improving how organizations make, execute, and learn from decisions.

It often connects:

```text
Data → Insight → Decision → Action → Outcome → Feedback
```

### What EGATF Borrows

EGATF borrows the idea that analysis is incomplete unless it connects to decisions, actions, and outcomes.

### What EGATF Changes

Decision Intelligence usually begins around the point where insight becomes decision.

EGATF begins earlier, with evidence extraction and evidence-chain construction.

EGATF also emphasizes deliberate challenge before decision.

### Why This Matters

Troubleshooting is not just about finding a root cause.

It is about deciding what to do under uncertainty.

EGATF attempts to connect diagnostic reasoning to accountable decision-making.

### References to Investigate

- Decision intelligence literature
- Decision modeling
- Outcome feedback loops
- Human-in-the-loop decision support

---

## 8. Scientific Method

### Description

The scientific method uses observation, hypothesis, testing, analysis, and revision.

### What EGATF Borrows

EGATF borrows the discipline of treating explanations as hypotheses rather than facts.

This strongly influences the Challenge stage.

### What EGATF Changes

EGATF is not a general scientific method.

It is adapted for practical technical troubleshooting where engineers may need to act under time pressure and incomplete evidence.

### Why This Matters

AI can produce confident answers quickly.

EGATF encourages a more scientific stance:

> What would prove this wrong?

This helps reduce confirmation bias and hallucination-driven reasoning.

---

## 9. Evidence-Based Reasoning

### Description

Evidence-based reasoning emphasizes conclusions supported by verifiable evidence rather than opinion or plausibility.

It is common in fields such as:

- Medicine
- Law
- Scientific research
- Safety engineering
- Security investigations

### What EGATF Borrows

EGATF borrows the idea that claims should be supported by evidence of known quality.

### What EGATF Changes

EGATF applies evidence-based reasoning to AI-assisted troubleshooting.

It asks not only whether a human can explain a conclusion, but whether an AI-assisted workflow can preserve the evidence chain clearly enough for review.

### Why This Matters

AI-generated conclusions can appear authoritative.

Evidence-based reasoning provides a discipline for resisting unsupported confidence.

---

## 10. Post-Incident Review and Learning Loops

### Description

Post-incident reviews and learning loops are used to capture lessons after incidents.

They often produce:

- Action items
- Runbook changes
- Monitoring improvements
- Documentation updates
- Process changes
- Product improvements

### What EGATF Borrows

EGATF borrows the idea that investigation should produce reusable learning.

### What EGATF Changes

EGATF makes **Learning** a formal stage in the framework.

Learning is not only a post-incident activity. It is the final step that feeds future troubleshooting.

### Why This Matters

If learning is not captured, the same incident may be diagnosed repeatedly from scratch.

EGATF treats each investigation as a chance to improve future AI-assisted diagnosis.

---

## Initial Assessment of Originality

EGATF should not claim to have invented:

- DIKW
- Evidence-based reasoning
- Root cause analysis
- RAG
- AI-assisted incident diagnosis
- Decision intelligence
- Post-incident learning

The potential originality appears to be in the combination and operational packaging:

```text
Evidence → Information → Knowledge → Insight → Challenge → Judgment → Decision → Action → Outcome → Learning
```

Especially:

1. Beginning with evidence rather than generic data.
2. Treating AI-generated insight as hypothesis rather than conclusion.
3. Requiring a formal Challenge stage.
4. Tracking missing and contradicting evidence.
5. Connecting challenged insight to human judgment, decision, action, outcome, and learning.
6. Applying the model specifically to support bundles, logs, metrics, dumps, observations, documentation, bug reports, and source code.

---

## Current Risk of Overclaiming

The main risk is presenting EGATF as entirely new.

Safer framing:

> EGATF is a proposed practitioner framework that synthesizes DIKW, evidence-based reasoning, RAG, root cause analysis, and decision intelligence for AI-assisted technical diagnosis.

Avoid claiming:

> EGATF is the first framework for AI troubleshooting.

Avoid claiming:

> EGATF solves hallucination.

Prefer claiming:

> EGATF is intended to reduce unsupported AI-assisted troubleshooting conclusions by requiring evidence traceability and deliberate challenge.

---

## References to Capture in Bibliography

Initial references to investigate and cite properly in `research/bibliography.md`:

1. Russell Ackoff and DIKW-related work
2. Dammann, "Data, Information, Evidence, and Knowledge"
3. Retrieval-Augmented Generation foundational papers
4. Evidence-grounded RAG and citation verification papers
5. RCACopilot and related LLM-based RCA papers
6. OpenRCA and similar RCA evaluation benchmarks
7. Decision Intelligence literature
8. SRE postmortem and learning review practices
9. Scientific method and hypothesis testing references
10. Evidence-based reasoning literature

---

## Open Questions

1. Are there existing frameworks that already include Evidence, Insight, Challenge, Decision, Action, Outcome, and Learning in one chain?
2. Is the term **Challenge** sufficiently clear to practitioners?
3. Does the framework need a formal evidence reliability model?
4. Should source code and documentation be treated as different evidence classes?
5. How should version-specific knowledge be handled?
6. How should the framework represent conflicting sources of truth?
7. Can EGATF be validated with public case studies?
8. Should EGATF remain a framework or become a tool-supported workflow?
9. How should EGATF cite AI-generated intermediate reasoning?
10. What related work from safety engineering, medicine, or legal reasoning should be included?

---

## Revision Notes

This is the initial prior art register.

It should be updated whenever a related model, paper, tool, or methodology is discovered.

Detailed citations should be moved into `research/bibliography.md`.
