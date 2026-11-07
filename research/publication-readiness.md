# Publication Readiness Checklist

**Document type:** Research tracker  
**Status:** Draft v0.8  
**Repository path:** `research/publication-readiness.md`

---

## Purpose

This repository is public. Part of its content is close to the author's employer's product work. These items need a decision from the author before the repository is promoted or the framework is published. They are listed here so they are not lost; none has been decided on the author's behalf.

---

## Decisions Required

| # | Item | Why it matters | Decision needed |
|---|---|---|---|
| P-1 | Licence | `README.md` says "License to be determined". Without a licence, reuse is not permitted by default. | Choose a licence for text and a licence for code and schemas (they may differ). |
| P-2 | Employer IP and sign-off | The framework was developed in the author's employer's domain (support bundles, internal tooling). | Confirm in writing what may be public, and under what terms. |
| P-3 | `engineering/support-bundle-manifest-improvements.md` | It is a ready-to-file internal feature request for a vendor product, including a suggested ticket title. | Keep public, sanitize, or move to a private location. |
| P-4 | `presentations/` | Decks describe internal tools (`wtl`, the tablet report parser). | Confirm the tools may be named publicly, or sanitize. |
| P-5 | Git history | Removing a file from the tip does not remove it from history. | If anything must be withdrawn, decide whether to rewrite history. |
| P-6 | Case material | Real cases must be sanitized (`sensitivity` field) before they are committed. | Agree a sanitization checklist before the first real case. |

---

## Already Handled

- Duplicate `presentation collateral/` directory removed.
- Case records carry a `sensitivity` field validated by schema.
