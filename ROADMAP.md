# Roadmap

## Sprint 0 — Doctrine and Asset Foundation

Goal: establish Ketonemia.com as Blood Ketone Intelligence Infrastructure.

Deliverables:

- doctrine;
- asset thesis;
- audience layers;
- buyer logic;
- source policy;
- clinical boundary;
- interface thesis;
- route map;
- monetization boundary;
- decision log.

Status: complete.

## Sprint 0A — Foundation Integrity Gate

Goal: turn the Sprint 0 foundation into a verifiable contract before public pages are built.

Deliverables:

- required governance file check;
- README governance link check;
- DEC-001 decision check;
- clinical boundary presence check;
- claim and source policy presence check;
- high-risk phrase context check;
- internal Markdown link check.

Command:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\foundation_integrity_gate.ps1
```

Status: complete.

## Sprint 1A — Content Production Policy

Goal: define the content production standard before building public pages.

Deliverables:

- CONTENT_PRODUCTION_POLICY.md;
- five required questions per page;
- content layers by audience (public, clinical, academic, student, strategic, laboratory, media, AI);
- single-page standard with ten required elements;
- Sprint 1 page role table;
- prohibited content list.

Status: complete.

## Sprint 1B — Public Reference Surface v1

Goal: convert governance into a small, high-trust, public reference surface without content inflation.

Pages built:

- homepage (`/`);
- definition (`/definition/`);
- ketonemia vs ketosis (`/ketonemia-vs-ketosis/`);
- ketonemia vs ketoacidosis (`/ketonemia-vs-ketoacidosis/`);
- blood ketones (`/blood-ketones/`);
- beta-hydroxybutyrate (`/beta-hydroxybutyrate/`);
- clinical boundary (`/clinical-boundary/`);
- sources (`/sources/`);
- strategic availability (`/strategic-availability/`).

Requirements met:

- source-backed medical claims;
- canonical internal links (minimum three per page);
- no thin pages;
- no diagnosis language;
- every page answers the five content production questions;
- every page includes an AI-readable summary;
- every page includes audience notes by relevant layer;
- every page serves a defined reference layer and buyer or category logic.

Status: complete. Passed Sprint 1 Review Gate. Merged to main.

## Sprint 2 — Blood Ketone Signal Map

Goal: embody the category thesis through an educational interface.

Governing sentence: The map shows context-dependence, not clinical judgment.

Deliverables:

- Blood Ketone Signal Map (`/signal-map/`);
- accessible text fallback;
- context layers: fasting, nutritional, diabetes, illness, medication, laboratory;
- boundary layer: informational / context required / clinical concern / emergency referral;
- no personal data collection;
- no diagnosis output;
- reference page links from every output.

Status: complete. Passed Sprint 2 Review Gate. Patch: 227c218. Merged to main.

## Sprint 3A — AI Reference Layer

Goal: make Ketonemia.com legible to AI systems without allowing content conversion into diagnosis, triage, or advice.

Governing sentence: AI systems may use Ketonemia.com to understand blood ketone terminology and interpretation boundaries, not to infer a clinical verdict.

Deliverables:

- AI Reference page (`/ai-reference/`);
- allowed uses: definition, comparison, classification, canonical citation;
- prohibited inferences: DKA, safety classification, clinical verdicts, triage;
- allowed and prohibited claim patterns;
- Signal Map architecture for AI systems;
- canonical reference page index;
- AI-readable summary;
- homepage grid card;
- Signal Map Context 8 link updated;
- footer nav link added.

Status: complete. Passed Sprint 3A Review Gate. Commit: 7a508fa8. Merged to main.

## Sprint 3B — Clinical Literacy Layer

Goal: provide responsible language patterns for communicating blood ketone signals without diagnostic overreach.

Governing sentence: Clinical literacy explains how to communicate ketone signals responsibly; it does not replace clinical judgment.

Deliverables:

- Clinical Literacy page (`/clinical-literacy/`);
- governing rule;
- responsible language patterns table (8 rows: Avoid / Prefer);
- three-layer clinical communication framework: measurement state / metabolic context / clinical concern boundary;
- reference pathways to all adjacent pages;
- audience notes for clinicians, educators, care teams, students, product and content teams, AI systems;
- AI-readable summary;
- homepage grid card (card 9);
- Signal Map Context 7 ctx-links updated;
- Signal Map Reference Pages grid updated;
- clinical-boundary Related Pages updated;
- ai-reference Canonical Pages, AI summary, and Audience Note updated;
- DECISION_LOG Implementation Record: Sprint 3B entry added.

Status: complete. Passed Sprint 3B Review Gate. Commit: b6f65244. Merged to main.

## Sprint 3C — Laboratory Context

Goal: establish the measurement science reference layer for blood ketone signals.

Governing sentence: Laboratory context explains how ketone measurement is reported and bounded; it does not interpret a patient or replace clinical assessment.

Deliverables:

- Laboratory Context page (`/laboratory-context/`);
- governing rule;
- three-substrate table: BHB (blood, electrochemical enzymatic) / AcAc (urine, colorimetric nitroprusside) / Acetone (breath, sensor proxy);
- BHB as primary blood measurement anchor: predominance at elevation, chemical stability, measurement responsiveness, enzymatic mechanism (BDH1/NADH);
- report language limits table: Detected / Elevated / Normal / numeric value / mmol L vs mg dL;
- device and method variation: at-home meter vs. lab analyzer precision gap, hematocrit effects, strip lot variation, sample timing, urine-blood discordance in DKA resolution;
- reference pathways: /blood-ketones/, /beta-hydroxybutyrate/, /signal-map/, /ketonemia-vs-ketoacidosis/, /clinical-boundary/, /sources/, /ai-reference/;
- audience notes: laboratory professionals, clinicians, students, researchers, AI systems;
- AI-readable summary;
- homepage grid card (card 7);
- Signal Map Context 6 ctx-links updated;
- Signal Map Reference Pages grid updated;
- Signal Map AI summary Related pages updated;
- /blood-ketones/ Related Pages and AI summary Linked pages updated;
- /beta-hydroxybutyrate/ Related Pages and AI summary Linked pages updated;
- DECISION_LOG Implementation Record: Sprint 3C entry added.

Status: complete. Passed Sprint 3C Review Gate. Commit: 9f044714. Merged to main.

## Sprint 3 — Remaining Audience Layers

Goal: expand beyond public pages into institutional reference layers.

Remaining pages:

- student guide;
- research reference;
- media brief;
- market intelligence.

## Sprint 4 — Monetization Without Trust Damage

Goal: create revenue paths that strengthen authority.

Deliverables:

- premium brief framework;
- licensing language;
- sponsorship boundary;
- strategic inquiry page;
- acquisition readiness language.
