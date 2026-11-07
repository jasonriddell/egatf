# EGATF Validation Design

**Document type:** Research design  
**Status:** Draft v0.8  
**Repository path:** `research/validation-design.md`

---

## Purpose

EGATF claims that requiring traceability and deliberate challenge makes AI-assisted troubleshooting more reliable. This document specifies how that claim could fail. Until it has been tested, the three-loop model is a hypothesis.

---

## What Would Count as Evidence

| Claim | Measure | Failure looks like |
|---|---|---|
| The Evidence Loop produces a more trustworthy evidence base. | Rate of timing and provenance errors in conclusions, with and without Collection Context. | No difference in false correlations across incompatible windows. |
| The Reasoning Loop reduces unsupported diagnosis. | Share of stated causal claims with no supporting evidence trace, and the false-accept rate at the Challenge Confidence Gate. | Challenge passes wrong hypotheses as often as an unstructured review does. |
| The Action Loop stops contradicted judgments from being institutionalized. | Share of contradicted judgments returned to Challenge. | Outcomes are recorded as supporting the judgment whenever any improvement occurs. |
| Cold analysis reduces anchoring. | Findings present in cold output and absent in guided output, verified against evidence. | Cold and guided outputs are identical in substance. |
| The framework is usable. | Time to diagnosis and analyst effort by risk profile, and whether analysts skip stages. | Lite profile is not lighter in practice. |

---

## Study Shape: Time-Sliced Replay

Replay closed historical cases with known resolutions.

1. **Select cases** with a documented final cause and a support bundle. Prefer cases where the first hypothesis was wrong or the report contained a misleading causal claim.
2. **Slice the evidence** to what existed at first diagnosis (`case.evidence_cutoff` in the case record). Exclude later tickets, comments, fixes and resolution text.
3. **Control for leakage.** A model may have seen similar public material. Use sanitized or synthetic variants, record the model and version, and include cases from after the model's knowledge cutoff where possible.
4. **Conditions.** Compare at least: (a) unstructured AI-assisted analysis, (b) EGATF Lite, (c) EGATF Standard. Same analyst pool, same time limit, randomized order.
5. **Score against the known cause** using pre-registered criteria, and score separately whether each claim is traceable to evidence.
6. **Record every gate outcome** and every place the framework was bent or skipped. Report framework failures alongside successes.

---

## Preparation Quality Tests

Evidence Preparation is a dependency of every later claim, so it needs its own tests:

- **Golden fixtures**: a small bundle with known observations, run through each preparation tool, with expected output checked in.
- **Sampling audit**: draw random raw records and confirm each is represented, classified correctly, or deliberately dropped with a reason.
- **Drop accounting**: every filter or consolidation reports what it removed.
- **AI-assisted extraction** is treated as derived evidence of unknown reliability until a human has reviewed a sample and the miss rate is recorded.

---

## Minimum Viable First Case

One real or sanitized case, run end to end, with a short "where the framework failed" section. A case where a gate caught an error a normal investigation would have missed is the most useful single artefact, and a case where it did not is nearly as informative. Use `schemas/case-record.schema.yaml` so the evidence chain is machine-checked.

---

## Threats to Validity

- Authors evaluating their own framework.
- Hindsight and model memorization.
- Selection of cases that suit the framework.
- Gate outcomes judged by the same model that generated the hypothesis.
- Learning from supported cases only (see survivorship in `framework/diagnostic-knowledge-patterns.md`).
