# Mitigation, Risk Profiles, and Stop Rules

**Document type:** Framework detail  
**Status:** Draft v0.8  
**Repository path:** `framework/mitigation-and-stop-rules.md`

---

## Purpose

EGATF requires a challenged Judgment before Decision. Real incidents often require mitigation before diagnosis is settled. This document defines how EGATF permits action under uncertainty without weakening the gates, and when a loop must stop rather than cycle.

It adds no gate. EGATF still has exactly three.

---

## Two Kinds of Action

| Kind | Purpose | Requires |
|---|---|---|
| Diagnostic or mitigating action | Reduce harm or discriminate between hypotheses while diagnosis is incomplete. | The mitigation checklist below. A passed Challenge Confidence Gate is not required. |
| Corrective action | Fix the believed cause. | A Judgment that passed the Challenge Confidence Gate. |

A mitigation is recorded as a mitigation (`M-` node in a case record), not as a corrective Decision. It must not be described later as evidence that the diagnosis was right (see Outcome confounding in `challenge-evaluation.md`).

---

## Mitigation Checklist

A mitigation may proceed under Low or Medium confidence only if all are recorded:

1. **Reversible**, or the irreversible part is explicitly accepted by the authorizer.
2. **Blast radius** is stated and smaller than the harm being mitigated.
3. **Authorizer** is a named person with authority over the system.
4. **Time-box**: when the mitigation is reviewed or rolled back.
5. **Confidence at time** is stated. Mitigations taken at Low confidence are labelled as such.
6. **Diagnostic value**: whether the action also helps discriminate between hypotheses, and what result would favour which.

If any item is unknown, treat the action as a corrective action and return to Challenge.

---

## Risk Profiles

Rigor should be proportional to risk. Choose a profile at the start and record it.

| Profile | Use when | Required |
|---|---|---|
| Lite | Low severity, reversible actions, or exploratory triage. | Reported context separated from evidence. Collection context noted. Supporting and contradicting evidence for each hypothesis. At least one alternative. Stated confidence. |
| Standard | Customer-impacting or recurring issues. | Everything in Lite, plus cold and guided comparison where anchoring risk exists, knowledge version validation, the hypothesis matrix, and all three gate outcomes recorded. |
| High-assurance | Irreversible or high blast-radius actions, data-loss risk, or findings that will be published. | Everything in Standard, plus an independent challenger, a time-sliced review of the evidence, and a named Judgment owner who is not the analyst who generated the hypothesis. |

A profile may be raised during an investigation. It should not be lowered to pass a gate.

---

## Stop Rules

Loops must terminate. Each investigation records:

- **Time-box per loop.** When it expires the investigator chooses one of: continue with a new explicit time-box, escalate, mitigate, or close as unresolved.
- **Maximum returns to the Evidence Loop** (default two) before the question is re-scoped or escalated.
- **Closure as unresolved** is a valid outcome. An unresolved case still produces Learning: what evidence was missing and what collection change would have resolved it.

---

## Judgment Ownership

Judgment is a human assessment. Each Judgment record names:

- **Owner**: the person accountable for it.
- **Claim level**: `consistent_with`, `supported_cause`, or `established_cause` (see the Causal Claim Standard in `challenge-evaluation.md`).
- **Confidence** and **remaining uncertainty**.

For the High-assurance profile the owner must differ from the person or model that generated the leading hypothesis.

---

## Decision Checklist

Before a corrective Decision:

- Options listed, including doing nothing and the mitigation already in place.
- Reversibility and blast radius stated.
- Authorizer named.
- Rollback or abort condition stated.
- Expected outcome stated in a form that could contradict the Judgment.

The last item matters most: an expected outcome that no result could contradict cannot validate anything at the Outcome Validation Gate.
