# Asset Intelligence Factory Plan

Ketonemia.com — from category asset to **category intelligence source**.

This document governs the transition described in the Sovereign Asset System:

> A domain does not stay a site that explains a topic. It becomes a system that
> produces governed intelligence inside a category: definitions, classifications,
> tools, diagnosis, standards, maps, reports, and later APIs — under a governance
> layer that makes the intelligence trustworthy.

It sits above every future sprint the way `FOUNDATION_DOCTRINE.md` sits above every
page. Where the two conflict, the doctrine and `CLINICAL_BOUNDARY.md` win: the
factory produces **governed reference intelligence**, never diagnosis.

---

## 1. The inevitability thesis

The banana taped to a wall sold for millions because of a frame, a piece of tape,
and a concept — not the fruit. The interface did not decorate the object; it
embodied a thesis about the category ("art is the certificate and the idea, not
the material"). Ketonemia must reach the same structural place in its own category:

> **A blood ketone number is meaningless without governed context. Ketonemia.com
> is the governed context.**

An asset is *inevitable* when a strategic buyer concludes that not owning it means
leaving a piece of the category's future outside their control — the name, the
language, the classification, the standard, the working tool, the machine
interface, the trust layer, and the accumulated footprint. A rival can build
ketone content. It cannot cheaply rebuild the *category infrastructure* around it.

Today Ketonemia owns the upper half of that stack (name, language, ontology,
standard, reference surface, governance, interface thesis, buyer logic). It does
**not yet** own the lower half that turns a reference site into a factory: a
protocol, a working engine that emits governed output, a machine-readable /
agent-readable layer, an explicit system architecture, deep ontology class pages,
and monetization + acquisition **proof**. Those are the missing rungs. This plan
builds them without touching the clinical boundary.

---

## 2. The eleven-layer model — current status

The Sovereign Asset System defines eleven layers every tier-1 asset must own.
Ketonemia's status against each:

| # | Layer | Question it answers | Status | Evidence / Gap |
| --- | --- | --- | --- | --- |
| 1 | **Domain thesis** | What sentence makes the name necessary? | Owned | `ASSET_THESIS.md`, `FOUNDATION_DOCTRINE.md` |
| 2 | **Category language** | What vocabulary will the asset own? | Owned | `CATEGORY_LANGUAGE.md` |
| 3 | **Ontology** | How do we classify the category? | Owned (spec) / partial (pages) | `KETONEMIA_SIGNAL_ONTOLOGY.md` — 10 KSO classes exist as spec; **not yet 10 dedicated class pages** |
| 4 | **Standard** | What is good / complete / trusted? | Owned | `KETONEMIA_STATE_STANDARD.md` (KSS K0–K5) |
| 5 | **Protocol** | How is diagnosis / evaluation / classification actually performed? | **Missing** | No `CLASSIFICATION_PROTOCOL.md`; the rules that map a context selection to a KSO class + KSS zone are implicit, not published |
| 6 | **Engine / Tool** | How does the system produce operational output? | **Missing** | `/signal-map/` is a static conceptual interface — it explains, it does not emit a governed output for a chosen context |
| 7 | **Reference layer** | Is the site archivable, searchable, citable? | Owned | 16 governed pages, canonical routes, AI summaries |
| 8 | **Governance** | How is stability, versioning, trust ensured? | Owned (strong) | `QUALITY_GATE.md`, `DECISION_LOG.md`, policies, integrity gate |
| 9 | **Interface thesis** | Does the interface embody the asset's meaning? | Owned | `INTERFACE_THESIS.md`, Signal Map |
| 10 | **Monetization** | How does it earn respectably without lowering trust? | Owned (boundary) / **no proof** | `MONETIZATION_BOUNDARY.md` defines what is allowed; **no product exists** and no revenue evidence |
| 11 | **Buyer logic** | Who is the strategic buyer and why is not-buying a loss? | Owned (thesis) / **no dossier** | `BUYER_LOGIC.md`; **no acquisition dossier / valuation narrative artifact** |

Plus the AI-era rung the methodology adds on top:

| + | **Agent-readable machine layer** | Can machines, not just humans, read and trust it? | **Missing** | No `llms.txt`, `sitemap.xml`, `robots.txt`; no JSON endpoints (glossary, ontology, KSS, sources, route manifest); JSON-LD is present but shallow (mostly `WebPage`) |

---

## 3. What Ketonemia lacks to be inevitable

Seven concrete gaps, ranked by how much each raises inevitability per unit of effort.
None require crossing the clinical boundary; each is a reference/infrastructure
artifact.

### Gap 1 — Agent-readable machine layer (highest leverage, lowest risk)
The asset is legible to humans and shallowly legible to crawlers, but not yet
**structured for machines and AI agents that compare, cite, and choose**. In an
agentic-retrieval world this is the difference between being quoted and being
skipped.

Build:
- `llms.txt` — public AI index: what the asset is, canonical routes, allowed and
  prohibited claim patterns, pointer to the reference pack.
- `sitemap.xml` + `robots.txt` — crawl and archive discipline.
- A JSON reference pack under a stable route (e.g. `/ai-reference/pack/`):
  `glossary.json`, `ontology.json` (KSO), `kss.json` (KSS states), `sources.json`,
  `routes.json` (route manifest). Static files, versioned, append-only.
- Deepen JSON-LD: `DefinedTerm` / `DefinedTermSet` on every definitional page,
  `Dataset` on the reference pack, `MedicalWebPage` where clinical context applies.

Governance: `AI_REFERENCE_POLICY.md` already requires machine output to be **no
looser than** human output. Every JSON claim must trace to a page and a source ID.

### Gap 2 — Protocol layer (`CLASSIFICATION_PROTOCOL.md`)
The ontology says *what the classes are*; the standard says *what the zones are*;
nothing published says *how you get from an observed context to a class and a zone*.
That deterministic, rules-only mapping is the Protocol — and it is the specification
the Engine (Gap 3) executes. It is also independently licensable.

Build: an append-only protocol document — inputs (measurement type, context
dimension, audience), the rules-only mapping to a KSO class and a KSS reference
label, and the mandatory boundary output. No invented thresholds; every numeric
range cites a source with population and method, per `KETONEMIA_STATE_STANDARD.md`.

### Gap 3 — Engine / Tool that emits governed output
`/signal-map/` teaches the model; it does not run it. The factory needs a
**deterministic reference engine**: the visitor selects measurement type + context
+ audience, and receives a *governed reference output* — the KSO class, the KSS
reference label, what the signal can and cannot mean, the boundary language, and
the source pages to read. Rules-based, no personal data, no diagnosis, no "you are
safe" / "you have DKA" (`INTERFACE_THESIS.md` safety rules). This is the artifact a
buyer cannot get from static content — it proves the standard is operational.

### Gap 4 — System Architecture / Reference Map
There is no single page that shows the asset *as a system*: thesis → language →
ontology → standard → protocol → engine → reference surface → governance → machine
layer, and how every route connects. This is the page a strategic buyer, an
archivist, and an AI agent each read first. It converts "a set of good pages" into
"one legible category machine."

### Gap 5 — Deep ontology class pages
KSO defines ten classes but only some have dedicated canonical pages. The
methodology calls for **ten deep ontology class pages**, each a citable reference
node the engine output links into directly. This is what makes the classification
*own the language* rather than merely list it.

### Gap 6 — Monetization proof (not just boundary)
`MONETIZATION_BOUNDARY.md` says what is permitted; nothing yet earns. Inevitability
rises when there is **evidence** of respectable, trust-extending income. Build the
first governed product spec (e.g. *Blood Ketone Measurement Landscape Brief* or
*AI Reference Pack license*) and a `/briefs/` or inquiry surface — output as an
extension of the reference layer, never ad clutter or lead-gen.

### Gap 7 — Acquisition dossier
`BUYER_LOGIC.md` argues the case; it is not the artifact a buyer's corp-dev team
reads. Build an `ACQUISITION_DOSSIER.md` (private-facing tone, public-safe): what
is owned, the moat, the machine footprint, the reference footprint, the governance
record, and the explicit **cost of not owning it** per buyer class.

---

## 4. The nine questions (methodology answer sheet)

Required for every tier-1 asset:

1. **Which category does it own?**
   Blood ketone signal intelligence — the governed reference layer between a raw
   ketone reading and its interpretation, across fasting, nutrition, diabetes,
   illness, medication, laboratory, research, media, and AI contexts.

2. **What language will it create?**
   The vocabulary in `CATEGORY_LANGUAGE.md`: *blood ketone signal, ketonemia state,
   measurement context, interpretation layer, clinical concern boundary, emergency
   referral boundary*, and the KSO/KSS labels.

3. **What is the Ontology?**
   The Ketonemia Signal Ontology (KSO) — ten context classes, from Baseline Signal
   to Emergency Referral Boundary. Classifies context, never a patient state.

4. **What is the Standard?**
   The Ketonemia State Standard (KSS) — K0–K5 reference labels organizing cited
   guidance, never inventing thresholds.

5. **What is the Engine?**
   A deterministic reference engine (Gap 3) that turns a context selection into a
   governed KSO/KSS output with boundary language and source routes — educational,
   not diagnostic.

6. **What respectable income?**
   Category briefs, measurement-landscape reports, AI reference-pack licensing,
   taxonomy/standard licensing, embeddable signal-map licensing, disclosed
   sponsorship, institutional education partnerships — per `MONETIZATION_BOUNDARY.md`.
   Never affiliate spam, fear lead-gen, or diagnosis tools.

7. **Who is the strategic buyer?**
   Continuous ketone/glucose monitoring companies; ketone meter and strip makers;
   diabetes-safety and RPM platforms; metabolic-health and wearable platforms;
   diagnostics and laboratory companies; clinical-education providers; health-AI and
   medical-reference systems; health-education publishers (`BUYER_LOGIC.md`).

8. **How is not buying it a loss?**
   The buyer can build ketone content but cannot cheaply rebuild the category-matched
   name, the governed language, the KSO/KSS standard, the clinical-boundary system,
   the working engine, the machine/agent layer, the internal link graph, the search
   footprint, and the neutral trust layer — simultaneously and credibly. Leaving it
   unowned hands a rung of the category's future to a competitor or a neutral third
   party.

9. **How does the interface embody the thesis?**
   The interface makes *signal → context → boundary* visible rather than decorating
   it (`INTERFACE_THESIS.md`). The engine extends this: the user watches a number
   acquire meaning only through context, then meet a boundary. The medium **is** the
   thesis — that a ketone number is nothing without governed context.

---

## 5. Build sequence

Ordered by inevitability-per-effort, boundary-safe throughout. Each ships only
through `QUALITY_GATE.md` (add an **Asset Intelligence Factory Gate**).

| Phase | Deliverable | Gap | Layer added | Status |
| --- | --- | --- | --- | --- |
| F1 | `llms.txt`, `sitemap.xml`, `robots.txt`, JSON reference pack, deepened JSON-LD | 1 | Agent-readable machine layer | Complete |
| F2 | `CLASSIFICATION_PROTOCOL.md` | 2 | Protocol | Complete |
| F3 | System Architecture / Reference Map page (`/architecture/`) | 4 | Reference-as-system | Complete |
| F4 | Deterministic reference engine (`/classification-engine/`) | 3 | Engine | Complete |
| F5 | Ten deep KSO class pages (`/ontology/`) | 5 | Ontology depth | Complete |
| F6 | First governed product spec + inquiry surface (`/briefs/`) | 6 | Monetization proof | Complete |
| F7 | `ACQUISITION_DOSSIER.md` + `/acquisition/` | 7 | Buyer logic proof | Complete |

The build sequence F1–F7 is complete: every named gap is closed and every layer of
the factory is owned and in production.

Rules for every phase:
- Nothing ships that a page cannot back and a source cannot support.
- The machine layer is never looser than the human layer (`AI_REFERENCE_POLICY.md`).
- No personal health data, no diagnosis, no triage, no "you are safe" / "you have
  DKA" (`FOUNDATION_DOCTRINE.md`, `INTERFACE_THESIS.md`).
- Every artifact links back into the category graph; no orphan routes
  (`INTERNAL_LINKING_POLICY.md`).
- Every phase records a `DECISION_LOG.md` entry.

---

## 6. The factory rule

> Ketonemia.com does not publish content about blood ketones.
> It produces **governed intelligence** about blood ketones — for people,
> institutions, and AI agents — with a working standard, a working protocol, a
> working engine, and a machine interface, without ever crossing into a clinical
> verdict.

When that rule is fully true, the asset is no longer a name. It is the category's
reference machine — and not owning it becomes the loss.
