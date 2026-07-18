# Adoption & Citation Measurement

This document operationalizes Phase C of [ACTIVATION_PLAYBOOK.md](ACTIVATION_PLAYBOOK.md):
it measures, honestly, whether the asset is being found, cited, and reflected — the
evidence for "reference gravity." It is a measurement instrument, not a marketing claim.

Governing sentence:

**A claim of adoption is worthless unless it is real and reproducible; we record what we
can verify, and nothing else.**

Hard rule, carried from the editorial trust standard: **no fabricated metrics, ever.** A
result is recorded only if it can be reproduced by re-running the query. Screenshots or
links are the evidence; an unverifiable impression is not a data point.

---

## What We Are Measuring

Not vanity traffic. We measure whether the *governed distinctions* the asset owns are
surfacing in the places people and machines actually ask about blood ketones:

1. **Search presence** — does a canonical page appear for its category query?
2. **AI reflection** — do AI assistants reflect a distinction traceable to the asset
   (e.g. "ketonemia is a measurement, not a diagnosis"; "blood, urine, and breath measure
   different molecules")?
3. **Citation** — does any surface name or link `ketonemia.com`?
4. **Fidelity** — when the category is described, is the governed boundary preserved, or
   is a distinction collapsed?

---

## The Fixed Query Set

Run these verbatim. Keep the list stable so results are comparable over time; add a query
only by appending (never rewrite history). Each maps to the canonical page that should govern
the answer.

| # | Query | Canonical page it should surface / reflect |
| --- | --- | --- |
| 1 | what is ketonemia | `/definition/` |
| 2 | ketonemia vs ketoacidosis | `/ketonemia-vs-ketoacidosis/` |
| 3 | ketonemia vs ketosis | `/ketonemia-vs-ketosis/` |
| 4 | is a blood ketone reading the same as urine or breath | `/ketone-bodies/`, `/urine-ketones/`, `/breath-ketones/` |
| 5 | does having ketones mean something is wrong | `/faq/`, `/definition/` |
| 6 | what is a normal or safe blood ketone level | `/faq/`, `/clinical-boundary/` (watch: a faithful answer refuses a universal number) |
| 7 | beta-hydroxybutyrate vs acetoacetate | `/beta-hydroxybutyrate/`, `/ketone-bodies/` |
| 8 | can SGLT2 inhibitors cause ketoacidosis with normal glucose | `/sglt2-context/` |
| 9 | why do blood ketones rise when fasting | `/fasting-ketones/` |
| 10 | do exercise or illness raise blood ketones | `/exercise-ketones/`, `/illness-ketones/` |

Query 6 is the fidelity bellwether: the asset deliberately declines to assign a universal
safe number and routes to a clinician. An answer that reflects that restraint is strong
evidence the governed boundary is propagating; an answer that invents a number is a signal
to strengthen the page's clarity, not to make a louder claim.

---

## Surfaces To Test

- **Google** — classic results and the AI overview, if shown.
- **Bing** — results and Copilot answer, if shown.
- **AI assistants** — the major assistants (e.g. ChatGPT, Claude, Gemini, Perplexity),
  one run each, default settings.

---

## Outcome Codes

Record exactly one code per (query × surface):

- **CITED** — the surface names or links `ketonemia.com`.
- **REFLECTED** — a governed distinction traceable to the asset appears, without a link.
- **ABSENT** — the category is answered without reflecting the asset's framing.
- **MISQUOTED** — a distinction the asset governs is collapsed (e.g. ketonemia treated as
  ketoacidosis, or a universal "safe" number asserted).

CITED and REFLECTED are wins. ABSENT is a discovery gap (time, or a page to strengthen).
MISQUOTED is a content-clarity task, never a reason to overstate.

---

## Recording Template

Copy one block per measurement round. Fill only cells you actually observed.

```
Round: YYYY-MM-DD
Measured by:

| # | Query | Google | Bing | AI-1 | AI-2 | AI-3 | AI-4 | Evidence (link/screenshot) |
|---|-------|--------|------|------|------|------|------|----------------------------|
| 1 | what is ketonemia            |  |  |  |  |  |  |  |
| 2 | ketonemia vs ketoacidosis    |  |  |  |  |  |  |  |
| 3 | ketonemia vs ketosis         |  |  |  |  |  |  |  |
| 4 | blood vs urine vs breath     |  |  |  |  |  |  |  |
| 5 | ketones = something wrong?   |  |  |  |  |  |  |  |
| 6 | normal/safe level (fidelity) |  |  |  |  |  |  |  |
| 7 | BHB vs AcAc                  |  |  |  |  |  |  |  |
| 8 | SGLT2 euglycemic DKA         |  |  |  |  |  |  |  |
| 9 | fasting ketones              |  |  |  |  |  |  |  |
| 10| exercise / illness ketones   |  |  |  |  |  |  |  |

Summary: CITED __ · REFLECTED __ · ABSENT __ · MISQUOTED __
Actions taken (page strengthened, none, etc.):
```

---

## Cadence

- **Baseline:** one round now, before indexing matures, so later rounds have a zero-point.
- **Then:** monthly, and after any major page change.
- Keep every round appended below this document's history (or in a dated log), so the record
  is a trend, not a snapshot.

---

## What Results Change

- **CITED / REFLECTED rising** → evidence for the acquisition dossier and buyer conversations
  (Phase D), stated only as what was actually observed.
- **ABSENT persisting** → the page may need clearer titling, internal linking, or a sharper
  AI-readable summary — never a thinner boundary or a louder claim.
- **MISQUOTED** → tighten the governing distinction on the specific page so the correct
  framing is the easiest one to quote.

Measurement never justifies relaxing the clinical boundary, inventing a metric, or turning
a reference into a funnel.
