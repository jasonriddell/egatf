# EGATF Bibliography

**Document type:** Working bibliography  
**Status:** Draft v0.1  
**Repository path:** `research/bibliography.md`

---

## Purpose

This document captures references relevant to the Evidence-Grounded AI Troubleshooting Framework (EGATF).

The bibliography is intentionally broad at this stage. Some references are foundational. Others are adjacent and require deeper review.

This file should evolve from a loose working bibliography into a properly curated reference list for articles, whitepapers, and any future formal paper.

---

## Citation Status Key

| Status | Meaning |
|---|---|
| Core | Likely foundational to EGATF |
| Relevant | Useful context or adjacent work |
| Investigate | Needs deeper review before relying on it heavily |
| Optional | May be useful for articles but not central |

---

# 1. DIKW and Knowledge Hierarchies

## 1.1 Russell Ackoff and DIKW

**Status:** Core  
**Topic:** Data, Information, Knowledge, Wisdom

Classic DIKW-style models describe a progression from data to information to knowledge to wisdom. EGATF borrows the idea of progressive transformation but adapts it for evidence-grounded AI-assisted troubleshooting.

Reference to investigate:

- Ackoff, R. L. (1989). "From Data to Wisdom." Journal of Applied Systems Analysis.

Notes:

- Need to locate the most reliable accessible copy or citation.
- Important because many later DIKW discussions attribute the hierarchy to Ackoff.
- EGATF should cite DIKW as an influence, not as something it invented.

Useful public references:

- Ontotext. "What Is the DIKW Pyramid?"
  - https://www.ontotext.com/knowledgehub/fundamentals/dikw-pyramid/

- University of Nebraska-Lincoln. "The DIKW Pyramid and the Process of Conducting an Advanced Review."
  - https://researchmoment.unl.edu/the-dikw-pyramid-and-the-process-of-conducting-an-advanced-review/

- DIKW Pyramid overview.
  - https://en.wikipedia.org/wiki/DIKW_pyramid

---

## 1.2 DIKW Critiques and Origins

**Status:** Relevant  
**Topic:** Limitations of DIKW

DIKW is widely used but also criticized as oversimplified. EGATF should acknowledge those critiques, especially because EGATF is not simply trying to create another hierarchy.

References to investigate:

- Frické, M. "The Knowledge Pyramid: A Critique of the DIKW Hierarchy."
- Rowley, J. "The Wisdom Hierarchy: Representations of the DIKW Hierarchy."
- Sharma, N. "The Origin of Data Information Knowledge Wisdom (DIKW) Hierarchy."

Useful public reference:

- Sharma, N. "The Origin of Data Information Knowledge Wisdom (DIKW) Hierarchy."
  - https://www.researchgate.net/publication/292335202_The_Origin_of_Data_Information_Knowledge_Wisdom_DIKW_Hierarchy

Notes:

- Important for avoiding overconfidence in DIKW as a perfect model.
- EGATF should probably position itself as a practical workflow, not a universal hierarchy of human cognition.

---

# 2. Evidence in Knowledge Hierarchies

## 2.1 Data, Information, Evidence, and Knowledge

**Status:** Core  
**Topic:** Evidence as an explicit stage

Dammann proposes modifying Ackoff's DIKW hierarchy by de-emphasizing wisdom and making room for evidence.

Reference:

- Dammann, O. (2019). "Data, Information, Evidence, and Knowledge: A Proposal for Health Informatics and Data Science." Online Journal of Public Health Informatics, 10(3). DOI: 10.5210/ojphi.v10i3.9631

Useful public references:

- PubMed:
  - https://pubmed.ncbi.nlm.nih.gov/30931086/

- PMC full text:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC6435353/

- Journal page:
  - https://ojphi.jmir.org/2018/3/e62348

Notes:

- Very relevant because it explicitly introduces evidence into the DIKW discussion.
- EGATF differs by placing evidence at the beginning of the workflow, because troubleshooting begins with logs, metrics, observations, documentation, source code, and other evidence-like artefacts.
- This reference is important for the question of whether "Evidence" is a novel addition. It is not novel by itself, so EGATF should focus on how it operationalizes evidence for AI-assisted diagnosis.

---

# 3. Retrieval-Augmented Generation and Grounding

## 3.1 Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Status:** Core  
**Topic:** RAG, source grounding, provenance

Foundational RAG paper.

Reference:

- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Kuttler, H., Lewis, M., Yih, W., Rocktaschel, T., Riedel, S., & Kiela, D. (2020). "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." NeurIPS 2020.

Useful public references:

- arXiv:
  - https://arxiv.org/abs/2005.11401

- NeurIPS PDF:
  - https://proceedings.neurips.cc/paper_files/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf

- Meta AI publication page:
  - https://ai.meta.com/research/publications/retrieval-augmented-generation-for-knowledge-intensive-nlp-tasks/

Notes:

- RAG is a core technical influence for EGATF.
- EGATF should make clear that retrieval is not enough. Retrieved sources still need to be interpreted, linked into an evidence chain, challenged, and connected to decisions and outcomes.

---

## 3.2 RAG Hallucination and Citation Verification

**Status:** Relevant  
**Topic:** Grounding is necessary but insufficient

RAG can reduce hallucination, but cited or retrieved context does not guarantee correct reasoning.

References to investigate:

- CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text.
  - https://arxiv.org/abs/2605.27700

- Attribution Techniques for Mitigating Hallucinated Citations in Retrieval-Augmented Generation.
  - https://arxiv.org/html/2601.19927v1

- Pawlik, L. "Reducing Hallucinations in Medical AI Through Citation..." Applied Sciences, 2026.
  - https://www.mdpi.com/2076-3417/16/6/3013

Notes:

- These are useful for the EGATF argument that citation alone is not the same as trustworthy diagnosis.
- Need deeper review to identify the best references for hallucination and citation grounding.

---

# 4. LLM-Assisted Root Cause Analysis and AIOps

## 4.1 RCACopilot

**Status:** Core  
**Topic:** LLM-assisted root cause analysis for cloud incidents

Reference:

- Chen, Y., Xie, H., Ma, M., Kang, Y., Gao, X., Shi, L., Cao, Y., Gao, X., Fan, H., Wen, M., Zeng, J., Ghosh, S., Zhang, X., Zhang, C., Lin, Q., Rajmohan, S., Zhang, D., & Xu, T. (2023/2024). "Automatic Root Cause Analysis via Large Language Models for Cloud Incidents."

Useful public references:

- arXiv:
  - https://arxiv.org/abs/2305.15778

- arXiv PDF:
  - https://arxiv.org/pdf/2305.15778

- ACM page:
  - https://dl.acm.org/doi/10.1145/3627703.3629553

Notes:

- Highly relevant because it uses LLMs for cloud incident RCA.
- RCACopilot aggregates diagnostic information, predicts root cause category, and provides explanatory narrative.
- EGATF differs by being a practitioner reasoning framework rather than a specific RCA system.
- EGATF should cite this as key adjacent work, not a competitor to dismiss.

---

## 4.2 OpenRCA

**Status:** Core  
**Topic:** Benchmarking LLM root cause analysis

Reference:

- Xu, J. et al. "OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?"

Useful public references:

- OpenReview:
  - https://openreview.net/forum?id=M4qNIzQYpd

- GitHub:
  - https://github.com/microsoft/OpenRCA

- PDF mirror:
  - https://netman.aiops.org/wp-content/uploads/2025/05/13411_OpenRCA_Can_Large_Langua.pdf

Notes:

- OpenRCA is relevant because it benchmarks LLM ability to identify root causes using telemetry data.
- The dataset includes failures, logs, metrics, and traces.
- EGATF can use OpenRCA as evidence that LLM RCA is a live research area and that evaluation matters.
- Need deeper review of benchmark design and reported model performance.

---

## 4.3 Recent LLM RCA Work

**Status:** Investigate  
**Topic:** Multi-source telemetry, microservices, network RCA, domain-specific RCA

References to investigate:

- Zhou, L., Liu, A., Liu, H., He, M., & Zhang, H. (2026). "Root Cause Analysis Method Based on Large Language Models with Residual Connection Structures."
  - https://arxiv.org/abs/2602.08804

- Shan, A., Kaur, J., Singh, R., Banka, T., Yavatkar, R., & Sridhar, T. (2025). "RCA Copilot: Transforming Network Data into Actionable Insights via Large Language Models."
  - https://arxiv.org/abs/2507.03224

- Wang, Y. et al. (2025). "Root Cause Analysis of Radiation Oncology Incidents Using Large Language Models."
  - https://arxiv.org/abs/2508.17201

Notes:

- These references show the field is expanding quickly.
- Need careful review before citing heavily.
- They may help position EGATF as a general framework across operational and safety-critical domains.

---

# 5. Root Cause Analysis and Incident Review

## 5.1 Google SRE Postmortem Culture

**Status:** Core  
**Topic:** Post-incident learning, blameless review, action items

References:

- Google SRE Book. "Blameless Postmortem Culture."
  - https://sre.google/sre-book/postmortem-culture/

- Google SRE Workbook. "Postmortem Practices for Incident Management."
  - https://sre.google/workbook/postmortem-culture/

Notes:

- Useful for EGATF's Outcome and Learning stages.
- SRE postmortems emphasize documenting incidents, understanding contributing causes, and creating preventive actions.
- EGATF can borrow the idea that learning is an operational requirement, not an optional afterthought.

---

## 5.2 External and Shared Postmortems

**Status:** Relevant  
**Topic:** Communicating incident analysis externally

Reference:

- Google Cloud Blog. "Google's tips on how to hold a fearless shared postmortem."
  - https://cloud.google.com/blog/products/gcp/fearless-shared-postmortems-cre-life-lessons

Notes:

- Useful later if EGATF discusses customer-facing support communication.
- Relevant to safe public case study creation and sanitized incident narratives.

---

# 6. Decision Intelligence

## 6.1 Decision Intelligence Overview

**Status:** Relevant  
**Topic:** Connecting insight to decision, action, outcome, and feedback

Decision intelligence connects data, analytics, AI, human expertise, decisions, actions, outcomes, and feedback loops.

Useful public references:

- Qualtrics. "The Ultimate Guide to Decision Intelligence."
  - https://www.qualtrics.com/articles/strategy-research/decision-intelligence/

- C&F. "From Data to Action: What Is Decision Intelligence?"
  - https://candf.com/our-insights/articles/what-is-decision-intelligence-from-data-to-action/

- IBM. "What Is Data-Driven Decision-Making?"
  - https://www.ibm.com/think/topics/data-driven-decision-making

Notes:

- These are mostly practitioner references, not academic foundations.
- Need stronger academic decision intelligence references later.
- Useful for early positioning of EGATF as extending beyond diagnosis into decision, action, outcome, and learning.

---

# 7. Scientific Method and Hypothesis Testing

## 7.1 Hypothesis, Test, Revise

**Status:** Core concept, references needed  
**Topic:** Treating insights as hypotheses

EGATF's Challenge stage draws heavily on the scientific habit of treating explanations as hypotheses that must be tested.

References to investigate:

- Philosophy of science references on hypothesis testing
- Falsifiability
- Scientific method
- Abductive reasoning
- Diagnostic reasoning
- Causal inference

Notes:

- This area needs better references.
- Potentially important because "Challenge" may be the most distinctive EGATF stage.
- The framework should avoid pretending that Challenge is new in human reasoning. The contribution is applying it explicitly to AI-assisted troubleshooting workflows.

---

# 8. Evidence-Based Reasoning

## 8.1 Evidence Quality and Claim Support

**Status:** Investigate  
**Topic:** Evidence strength, source authority, missing evidence, contradicting evidence

Potential adjacent fields:

- Evidence-based medicine
- Legal reasoning
- Safety engineering
- Security investigations
- Intelligence analysis
- Causal inference
- Assurance cases

Notes:

- EGATF may benefit from a formal evidence model.
- This is likely important for future versions if confidence scoring is added.
- Need to identify practical references that are not too academic for the intended audience.

---

# 9. Human-in-the-Loop AI

## 9.1 Human Judgment and Accountability

**Status:** Investigate  
**Topic:** Humans remain accountable for decisions and actions

EGATF assumes AI can assist reasoning but should not become the final accountable actor in operational diagnosis.

References to investigate:

- Human-in-the-loop AI
- Human-centered AI
- AI decision support
- Automation bias
- Human oversight
- Responsible AI

Notes:

- Important for the Wisdom / Judgment stage.
- May influence whether the stage remains named "Wisdom" or becomes "Human Judgment."

---

# 10. Candidate References for Future Deep Review

The following are not yet curated. They should be reviewed before being promoted to core references.

## DIKW and Knowledge Models

- Ackoff, R. L. "From Data to Wisdom."
- Rowley, J. "The Wisdom Hierarchy: Representations of the DIKW Hierarchy."
- Frické, M. "The Knowledge Pyramid: A Critique of the DIKW Hierarchy."
- Sharma, N. "The Origin of Data Information Knowledge Wisdom (DIKW) Hierarchy."

## Evidence and Knowledge

- Dammann, O. "Data, Information, Evidence, and Knowledge: A Proposal for Health Informatics and Data Science."

## RAG and Grounding

- Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."
- CiteCheck and citation verification papers.
- RAG hallucination surveys.

## AI RCA and AIOps

- RCACopilot.
- OpenRCA.
- RCA Copilot for network data.
- RC-LLM residual connection RCA.
- Multi-agent RCA systems.

## Decision and Learning

- Decision intelligence literature.
- Data-driven decision-making.
- SRE postmortem culture.
- Incident learning systems.

## Human Factors

- Human-in-the-loop AI.
- Automation bias.
- Human oversight of AI decision support.
- Responsible AI.

---

# Current Bibliography Gaps

The current bibliography is strongest in:

- DIKW
- DIEK
- RAG
- LLM-based RCA
- SRE postmortems

It is weaker in:

- Formal decision intelligence literature
- Evidence-based reasoning
- Safety engineering
- Human factors
- Diagnostic reasoning
- Causal inference
- Legal or medical evidence frameworks
- Assurance cases
- Claim verification literature

These gaps should be addressed before writing a formal whitepaper.

---

# Notes for Articles

When writing practitioner articles, use a small number of strong references rather than overwhelming the reader.

Possible reference strategy for Article 1:

1. DIKW as the historical background.
2. Dammann's DIEK model as evidence-aware hierarchy.
3. RAG as the current technical grounding mechanism.
4. RCACopilot or OpenRCA as evidence that AI RCA is an active field.
5. Google SRE postmortem culture as support for learning loops.

---

# Revision Notes

This is the initial bibliography draft.

The next revision should:

1. Add complete citation metadata.
2. Separate academic papers from practitioner references.
3. Mark which references have been fully read.
4. Add short annotations after deeper review.
5. Add BibTeX entries if the project moves toward a formal paper.
