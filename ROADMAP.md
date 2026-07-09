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
- report language limits table: Detected / Elevated / Normal / numeric value / mmol L vs mg dL;
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

## Sprint 3D — Student Guide

Goal: build the learning pathway reference layer for blood ketone terminology across academic disciplines.

Governing sentence: The student guide organizes ketonemia as terminology, measurement, context, and boundary — not as a shortcut to clinical judgment.

Deliverables:

- Student Guide page (`/student-guide/`);
- governing rule;
- terminology ladder: 9 terms from ketone body (biochemical) through BHB/AcAc/acetone/ketogenesis/ketonemia/ketosis/ketonuria to ketoacidosis (clinical syndrome);
- measurement layer: three technologies (blood meter, urine strip, breath analyzer) with links to /blood-ketones/, /beta-hydroxybutyrate/, /laboratory-context/;
- comparison layer: ketonemia vs. ketosis / ketonemia vs. ketoacidosis;
- signal context layer: 8 context dimensions linking to /signal-map/;
- boundary layer: 5-row can/cannot table linking to /clinical-boundary/;
- study pathway: 8 pages in order (/definition/ through /clinical-boundary/);
- student mistakes to avoid: 7 items;
- audience notes: medicine, pharmacy, nursing, biochemistry/laboratory science, nutrition;
- reference pathways: 9 cards;
- AI-readable summary;
- homepage grid card (card 8, total 13 cards);
- /definition/ Related Pages and AI summary Linked pages updated;
- /ketonemia-vs-ketosis/ Related Pages and AI summary Linked pages updated;
- /ketonemia-vs-ketoacidosis/ Related Pages and AI summary Linked pages updated;
- /laboratory-context/ Reference Pathways and AI summary Linked pages updated;
- DECISION_LOG Implementation Record: Sprint 3D entry added.

Status: complete. Passed Sprint 3D Review Gate. Commit: d6427f88. Merged to main.

## Sprint 3F - Research Reference Layer

Goal: build the research-facing reference layer for ketonemia as a measurable, contextual, source-bound blood signal.

Deliverables:

- Research Reference page (`/research/`);
- governing rule: research reference organizes ketonemia as a measurable, contextual, source-bound blood signal, not as a single clinical meaning;
- research use of ketonemia terms: ketonemia, blood BHB, AcAc, acetone, ketosis, ketoacidosis;
- research contexts table: fasting metabolism, nutritional ketosis, diabetes and DKA contexts, SGLT2 inhibitor contexts, illness and metabolic stress, exercise and substrate use, laboratory measurement studies, device and monitoring studies, AI and retrieval terminology contexts;
- measurement variables researchers must preserve: measured compound, sample type, method, units, timing, population, medication context, clinical condition, source class;
- adjacent research terms and internal links;
- research claim boundaries table;
- source pathways and Source IDs Used;
- audience notes for metabolism researchers, diabetes researchers, nutrition researchers, laboratory medicine, device teams, and AI systems;
- AI-readable summary;
- homepage grid card;
- related-page links from /beta-hydroxybutyrate/, /laboratory-context/, /ai-reference/, and /signal-map/;
- /sources/ Claim Source Registry pages-using-source updated.

Status: complete. Commit: 8421c8c. Merged to main.

## Sprint 3G - Deep Media Brief Layer

Goal: build the media-facing public-language layer for ketonemia without turning it into marketing copy, clinical advice, or a thin press reference.

Governing sentence: Media language must preserve the layer of meaning: ketonemia is a blood measurement state; ketosis is a metabolic process; ketonuria is a urinary finding; ketoacidosis is a clinical syndrome; and none of them should be collapsed into diet culture, panic language, or individual medical advice.

Deliverables:

- Media Brief page (`/media-brief/`);
- SEO title and meta description;
- media layer map separating molecule, measurement, metabolic state, urinary finding, clinical syndrome, DKA, BHB, and AcAc;
- search-intent explanation blocks for ketonemia, ketosis, ketoacidosis, blood vs. urine ketones, and BHB;
- headline-risk framework with better public framing and reference pages;
- allowed / avoid / because wording table;
- quote-ready public-language lines with explicit boundary language;
- source-class logic for biochemistry, measurement, DKA, medication-risk, and media-safe wording;
- audience notes for journalists, editors, health writers, medical communicators, AI systems, and strategic reviewers;
- reference pathways to definition, comparison, measurement, student, research, boundary, sources, AI, and Signal Map layers;
- AI-readable summary;
- homepage grid card;
- /ai-reference/ Canonical Reference Pages and AI summary updated;
- /research/ Source Pathways and AI summary updated;
- /clinical-boundary/ Related Pages and AI summary updated;
- Deep Media Brief Gate added to QUALITY_GATE.md;
- DECISION_LOG Implementation Record: Sprint 3G entry added.

Status: complete. Commit: ce3f718. Merged to main.

## Sprint 4A / F1 — Agent-Readable Reference Layer

Goal: make Ketonemia.com readable, citeable, and retrievable by AI systems, agents, and structured consumers without adding clinical interpretation. Build phase F1 of the Asset Intelligence Factory Plan — the transition from category asset to machine-readable category intelligence source.

Governing sentence: The machine-readable layer is never looser than the human-facing site; if a claim is prohibited on the pages, it is prohibited in the data.

Deliverables:

- `/llms.txt` — public AI index with allowed and prohibited AI uses, canonical pages, and machine-readable files;
- `/robots.txt` — crawl policy pointing to the sitemap;
- `/sitemap.xml` — all canonical public routes;
- `/data/reference-pack.json` — central manifest;
- `/data/glossary.json` — governed term definitions with clinical-boundary notes;
- `/data/kso-ontology.json` — Ketonemia Signal Ontology, ten context classes;
- `/data/kss-standard.json` — Ketonemia State Standard, K0–K5 reference labels;
- `/data/source-registry.json` — claim source registry mirroring `/sources/`;
- `/data/page-index.json` — canonical page index for retrieval;
- `/reference-pack/` — human-readable index of the machine-readable layer with Dataset JSON-LD;
- homepage card and footer updated;
- `/ai-reference/` Machine-Readable Reference Files section, AI summary, and footer updated;
- Agent-Readable Reference Layer Gate added to QUALITY_GATE.md;
- DECISION_LOG Implementation Record: Sprint 4A entry added.

Status: complete.

## F2 — Classification Protocol

Goal: build the governed protocol layer that connects observed context to a KSO class, KSS zone language, boundary statement, canonical references, and source requirements. Build phase F2 of the Asset Intelligence Factory Plan — the bridge between the reference knowledge (KSO, KSS) and any future classification engine (F4).

Governing sentence: The protocol classifies the interpretive frame, not the person.

Deliverables:

- CLASSIFICATION_PROTOCOL.md;
- purpose and non-clinical boundary;
- context-only inputs (no numeric thresholds);
- governed outputs (KSO class, KSS language, boundary statement, canonical links, source requirements, allowed and prohibited language);
- seven deterministic classification rules;
- reference mapping table using real KSO classes and KSS labels;
- output template and worked reference example;
- engine-readiness clause binding any future engine to this protocol;
- strategic / licensing note;
- README, ROADMAP, and DECISION_LOG updated;
- /ai-reference/ note that the protocol governs future machine outputs.

Prohibited: diagnosis, triage, treatment guidance, individualized interpretation, safety verdicts, danger verdicts, risk scoring, device or product endorsement, invented thresholds, clinical algorithms.

Status: complete.

## Sprint 3 — Remaining Audience Layers

Goal: expand beyond public pages into institutional reference layers.

Remaining pages:

- market intelligence.

## Sprint 4 — Monetization Without Trust Damage

Goal: create revenue paths that strengthen authority.

Deliverables:

- premium brief framework;
- licensing language;
- sponsorship boundary;
- strategic inquiry page;
- acquisition readiness language.
