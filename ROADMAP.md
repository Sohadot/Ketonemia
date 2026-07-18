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

## F3 — System Architecture / Reference Map

Goal: build the single artifact that shows the asset as one governed system — the reference map a strategic buyer and an AI agent read first. Build phase F3 of the Asset Intelligence Factory Plan (Gap 4).

Governing sentence: The architecture makes the system legible. It does not add clinical content.

Deliverables:

- SYSTEM_ARCHITECTURE.md — internal canonical map: layer stack, route-map clusters, build order, and the architecture rule;
- `/architecture/` — public reference-grade page: the asset as a system, layer-stack table, reference map with all 16 routes clustered on one page, how-to-read-the-system audience block, governance spine, and machine/agent layer;
- SEO: unique title, meta description, canonical, CollectionPage + BreadcrumbList JSON-LD with no medical claims;
- built with existing CSS only — no new CSS, no JS beyond JSON-LD, no external assets;
- wire-in: homepage card and footer, `/ai-reference/`, `/reference-pack/`, sitemap, llms.txt, page-index.json, reference-pack.json;
- reconcile stale "Nine interconnected reference pages" on `/strategic-availability/` and add a System Architecture value-stack row;
- README governance index and F3 section, DECISION_LOG record, and QUALITY_GATE System Architecture Gate.

Prohibited: any new clinical content, thresholds, diagnosis, triage, or verdicts; new CSS; orphan or broken routes.

Status: complete.

## F4 — Governed Classification Engine

Goal: build the first operational tool on Ketonemia.com — a deterministic reference engine that runs the Classification Protocol. Build phase F4 of the Asset Intelligence Factory Plan (layer 6, Engine / Tool).

Governing sentence: The engine classifies the interpretive frame around a blood ketone signal. It does not classify a person, diagnose a condition, triage urgency, recommend treatment, or declare safety or danger.

Deliverables:

- `/classification-engine/` — boundary notice, engine thesis, context-only input form, nine-field governed output template, protocol explanation, AI-readable summary;
- `/data/classification-rules.json` — 15 deterministic rules, first-match priority order, unconditional catch-all, using only real KSO classes and KSS labels;
- `/assets/js/classification-engine.js` — vanilla JS, no backend, no external API, no tracking, no storage, output rendered via `textContent`;
- `<noscript>` static fallback explaining the engine and linking to `/signal-map/` and `/clinical-boundary/`;
- sensitive-context routing (diabetes + illness/stress, diabetes + medication) to explicit clinical-concern-boundary language, never a verdict;
- SEO: unique title, meta description, canonical, `WebPage` + `BreadcrumbList` JSON-LD (deliberately not `MedicalWebPage`, `MedicalRiskCalculator`, or `MedicalTest`);
- wire-in: homepage, `/architecture/` and `SYSTEM_ARCHITECTURE.md` (Engine/Tool layer, route-count correction 16→17), `/signal-map/`, `/ai-reference/`, `/reference-pack/`, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- `QUALITY_GATE.md` Governed Classification Engine Gate;
- README and DECISION_LOG entries.

Prohibited: numeric inputs, thresholds, symptom fields, personal data, diagnosis/triage/treatment/risk-score language, invented KSO/KSS names, backend or external API calls.

Status: complete.

## F5 — Deep KSO Ontology Class Pages

Goal: turn the ten-class Ketonemia Signal Ontology from a governance spec into a citable reference structure. Build phase F5 of the Asset Intelligence Factory Plan (deepens layer 3).

Governing sentence: KSO may classify context. It must not declare a patient state.

Deliverables:

- `/ontology/` hub + ten `/ontology/<slug>/` class pages, one per KSO class, each deep and distinct: governing rule, definition, context map, "what it is not" distinction, KSS relationship, boundary language, audience notes, source IDs, AI-readable summary;
- boundary classes (DKA Concern, Emergency Referral) carry the strongest restraint — not diagnoses, no self-triage;
- engine integration: `kso_class_page` added to every rule in `data/classification-rules.json`; the Classification Engine renders the KSO-class result as a link to the matching class page; inline rules stay byte-identical;
- `data/kso-ontology.json` — `ontology_page` per class;
- built with existing CSS only; `DefinedTerm` / `DefinedTermSet` + `BreadcrumbList` JSON-LD, no medical claims in structured data;
- wire-in and route-count reconciliation 17 → 28: `/architecture/` + `SYSTEM_ARCHITECTURE.md` (Ontology layer Owned, new Ontology cluster, ItemList), `/signal-map/`, `/ai-reference/`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- `QUALITY_GATE.md` KSO Class Pages Gate; README and DECISION_LOG entries.

Prohibited: new sources (registry reused), invented class or KSS names, thresholds, diagnosis/triage/self-triage language, thin pages.

Status: complete.

## F6 — Monetization Proof

Goal: turn the monetization layer from boundary-only into a governed, demonstrable revenue path — the first governed product spec plus an inquiry surface. Build phase F6 of the Asset Intelligence Factory Plan (layer 10 proof).

Governing sentence: Revenue must extend trust, not replace it.

Deliverables:

- `MONETIZATION_SPEC.md` — internal spec operationalizing MONETIZATION_BOUNDARY.md: product catalog mapped to permitted lines, flagship spec, inquiry mechanism, and hard rules;
- `/briefs/` — public product catalog and inquiry surface: what these are, the catalog table, the flagship AI Reference Pack License spec, sponsorship rule, "what this is not," and a plain inquiry surface;
- static-only: no store, checkout, payment, ads, or data-collection form (no new security surface);
- SEO: unique title, meta, canonical, CollectionPage + BreadcrumbList JSON-LD with no Offer/price markup;
- wire-in and route-count reconciliation 28 → 29: `/architecture/` + `SYSTEM_ARCHITECTURE.md` (Monetization layer Owned, Strategic cluster, ItemList), `/strategic-availability/`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- `QUALITY_GATE.md` Monetization Proof Gate; README and DECISION_LOG entries.

Prohibited: on-site prices, checkout, payment processing, data-collection forms, ads, affiliate content, paid rankings, lead generation, restricted/prohibited monetization categories, Offer/price structured data.

Status: complete.

## F7 — Acquisition Dossier

Goal: build the final layer of the Asset Intelligence Factory — the acquisition dossier that inventories the asset as a strategic acquisition (layer 11 buyer-logic proof).

Governing sentence: Owning Ketonemia.com means owning a reference layer around an emerging metabolic signal category.

Deliverables:

- `ACQUISITION_DOSSIER.md` — private-facing, public-safe dossier: what is owned, the moat, machine and reference footprints, governance record, per-buyer-class cost of not owning it, and the constraints an acquirer inherits;
- `/acquisition/` — the public dossier surface (owned-asset table, moat table, footprints, per-buyer-class cost table), distinct in role from `/strategic-availability/`;
- neutral and boundary-safe: no price, valuation, financial projection, medical claim, or data-collection form; CollectionPage + BreadcrumbList JSON-LD with no Offer/price;
- wire-in and route-count reconciliation 29 → 30: `/architecture/` + `SYSTEM_ARCHITECTURE.md` (Buyer logic layer Owned, Strategic cluster, ItemList, build order complete), `ASSET_INTELLIGENCE_FACTORY_PLAN.md` (sequence complete), `/strategic-availability/`, `/briefs/`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- `QUALITY_GATE.md` Acquisition Dossier Gate; README and DECISION_LOG entries.

Prohibited: prices, valuations, forward-looking financial figures, new clinical claims, data-collection forms, raw-domain-listing tone.

Status: complete. With F7 the F1–F7 build sequence is complete.

## F8 — Editorial Trust & Transparency Layer

Goal: turn the source discipline the asset already practices into a visible, citable trust surface, deepening layer 8 (Governance) the way F5 deepened layer 3 (Ontology). Post-factory reinforcement, not a new layer in the stack.

Governing sentence: Trust is a standard the asset holds to, not a badge it awards itself.

Deliverables:

- `EDITORIAL_TRUST_STANDARD.md` — internal standard operationalizing SOURCE_POLICY.md, CLAIM_POLICY.md, CLINICAL_BOUNDARY.md, and AI_REFERENCE_POLICY.md, with an explicit list of what may and may not be claimed;
- `/trust/` — public trust page: the trust contract (seven disciplines tied to proving artifacts), a "claims / does not claim" table, how content is produced, the correction and change policy, independence and funding, and privacy by architecture;
- honesty rule enforced: no claim of individual clinician review, unheld credential, endorsement, or unmeasured accuracy metric;
- static-only: no new script, form, third-party dependency, or data-collection surface; CollectionPage + BreadcrumbList JSON-LD with no Offer/price/medical claim;
- wire-in and route-count reconciliation 30 → 31: `/architecture/` + `SYSTEM_ARCHITECTURE.md` (Governance layer points to `/trust/`, Boundary & Sources cluster, ItemList, counts), `/ai-reference/`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- `QUALITY_GATE.md` Editorial Trust Gate; README and DECISION_LOG entries.

Prohibited: fabricated reviewers, credentials, endorsements, or reviews; unmeasured accuracy or trust metrics; any new clinical content, threshold, or interpretation; new data-collection surface.

Status: complete.

## Content — Urine Ketones (Ketonuria)

Goal: complete the measurement triad (blood / urine / breath) with a deep public-reference and SEO pillar for "urine ketones," owning the blood-vs-urine distinction that the category is built to preserve.

Governing distinction: Ketonemia is a blood measurement state; ketonuria is a urinary finding — same molecules, different measurement layer, different meaning.

Deliverables:

- `/urine-ketones/` — urine-vs-blood comparison, nitroprusside / AcAc measurement, urine lag and DKA-resolution discordance, context table, limits, audience notes, source IDs, AI-readable summary;
- sources reused only (SRC-LAB-BHB-ACAC, SRC-LEHNINGER-BIOCHEM, SRC-NHS-DKA); strip categories framed as reporting language, not severity or thresholds;
- wire-in and route-count reconciliation 31 → 32: `/architecture/` + `SYSTEM_ARCHITECTURE.md` (Measurement & Laboratory cluster, ItemList, counts), `/blood-ketones/`, `/laboratory-context/`, `/sources/` + `data/source-registry.json` (pages-using-source), `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: new or invented sources; numeric or clinical thresholds; diagnosis, triage, or interpretation of an individual reading; treating urine AcAc and blood BHB as interchangeable.

Status: complete.

## Content — Breath Ketones (Breath Acetone)

Goal: complete the measurement triad (blood / urine / breath) with a deep public-reference and SEO pillar for "breath ketones," anchoring the third ketone body (acetone) to its measurement layer.

Governing distinction: Blood measures BHB as a number; urine measures acetoacetate as a category; breath measures acetone as a proxy — three windows onto the same metabolism.

Deliverables:

- `/breath-ketones/` — three-layer comparison, sensor-proxy measurement, why breath is a proxy not a blood value, context table, limits, audience notes, source IDs, AI-readable summary;
- sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-LAB-BHB-ACAC); breath framed as a trend proxy, never a clinical decision tool;
- wire-in and route-count reconciliation 32 → 33: `/architecture/` + `SYSTEM_ARCHITECTURE.md` (Measurement & Laboratory cluster, ItemList, counts), `/blood-ketones/`, `/urine-ketones/`, `/laboratory-context/`, `/sources/` + `data/source-registry.json`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: new or invented sources; numeric or clinical thresholds; using breath output for acute clinical decisions; treating breath acetone, urine AcAc, and blood BHB as interchangeable.

Status: complete.

## Content — Ketone Bodies

Goal: build the foundational biochemistry hub that anchors the measurement triad, capturing high-volume "ketone bodies" search intent while strengthening the internal link graph.

Governing idea: There is no single "ketone." There are three ketone bodies (BHB, AcAc, acetone), related but distinct — and which one you measure depends on how you measure.

Deliverables:

- `/ketone-bodies/` — the three-compound table mapped to blood/urine/breath, ketogenesis and interconversion, a naming note, what "ketone bodies present" does not mean, limits, audience notes, source IDs, AI-readable summary;
- sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-STRYER-BIOCHEM); no thresholds; states ketone bodies are normal fuel and not equal to ketoacidosis;
- wire-in and route-count reconciliation 33 → 34: `/architecture/` + `SYSTEM_ARCHITECTURE.md` (Measurement & Laboratory cluster, ItemList, counts), `/beta-hydroxybutyrate/`, `/blood-ketones/`, `/laboratory-context/`, `/sources/` + `data/source-registry.json`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: new or invented sources; numeric or clinical thresholds; presenting ketone-body presence as a disease or as ketoacidosis.

Status: complete.

## Content — Fasting Ketones (Cluster H)

Goal: open the Metabolic & Clinical Context cluster — the public/SEO-facing counterparts to the KSO context classes — with the highest-intent context page, fasting.

Governing distinction: Fasting is a driver of the signal; ketonemia is the blood measurement. A fasting rise is usually expected, but "expected" is about context, not clinical clearance.

Deliverables:

- `/fasting-ketones/` — fasting physiology and ketogenesis, what changes as a fast continues (direction, no thresholds), distinctions from nutritional ketosis / ketoacidosis / a single number, where context still matters, limits, audience notes, source IDs, AI-readable summary;
- new Route Map cluster **Metabolic & Clinical Context** (Cluster H), seeded to grow (future: nutritional, exercise, medication/SGLT2, diabetes context pages);
- sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-STRYER-BIOCHEM); no thresholds, no fasting-duration advice; fasting ketosis never equated with ketoacidosis;
- wire-in and reconciliation 34 → 35 routes, 7 → 8 clusters: `/architecture/` + `SYSTEM_ARCHITECTURE.md`, `/ketonemia-vs-ketosis/`, `/ontology/fasting-signal/`, `/sources/` + `data/source-registry.json`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: new or invented sources; numeric thresholds; recommending a fast; declaring an individual reading safe; equating fasting ketosis with ketoacidosis.

Status: complete.

## Content — Nutritional Ketosis (Cluster H)

Goal: own the highest-volume term in the category ("nutritional ketosis") as a governed reference — the second page of the Metabolic & Clinical Context cluster.

Governing distinction: Nutritional ketosis is a metabolic state; ketonemia is the blood measurement that can accompany it; neither is a diagnosis, and neither is ketoacidosis.

Deliverables:

- `/nutritional-ketosis/` — the state defined, state vs. measurement, nutritional/fasting/ketoacidosis comparison, measurement across the triad without thresholds, what it is not, context, limits, audience notes, source IDs, AI-readable summary;
- strictest keto-hype guardrails: no diet advice, no macros/food guidance, no health-benefit or weight-loss claims, no supplement/exogenous-ketone promotion, no numeric thresholds;
- sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-STRYER-BIOCHEM, SRC-NHS-DKA);
- wire-in and reconciliation 35 → 36 routes (cluster count stays eight): `/architecture/` + `SYSTEM_ARCHITECTURE.md`, `/ketonemia-vs-ketosis/`, `/fasting-ketones/`, `/ontology/nutritional-signal/`, `/sources/` + `data/source-registry.json`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: diet advice; macro/food guidance; health-benefit, weight-loss, or supplement claims; numeric thresholds; equating nutritional ketosis with ketoacidosis.

Status: complete.

## Content — SGLT2 Inhibitors & Ketones (Cluster H)

Goal: own the highest-authority safety topic in the category — how SGLT2-inhibitor medication changes ketone-signal interpretation — as a strictly bounded reference, opening the clinical/medication dimension of the Metabolic & Clinical Context cluster.

Governing distinction: On an SGLT2 inhibitor, ketoacidosis can occur without markedly elevated glucose, so a normal glucose reading does not by itself rule out concern.

Deliverables:

- `/sglt2-context/` — what the medication class is, why it changes interpretation, a common-assumption table, an explicit "what this page does not do," a strong boundary block, audience notes, source IDs, AI-readable summary;
- strongest sourcing on the site: SRC-FDA-SGLT2 (regulatory warning) + SRC-ADA-2026 + SRC-NHS-DKA, reused only;
- strictest boundary: no medication/dosing/start-stop advice, no diagnosis or triage, no sick-day rules, no thresholds, no product naming;
- wire-in and reconciliation 37 → 38 (cluster count stays eight; all four route lists kept identical): `/architecture/` + `SYSTEM_ARCHITECTURE.md`, `/ketonemia-vs-ketoacidosis/`, `/ontology/medication-context-signal/`, `/fasting-ketones/`, `/nutritional-ketosis/`, `/sources/` + `data/source-registry.json`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: medication advice; dosing or start/stop guidance; diagnosis or triage; sick-day rules; numeric thresholds; naming, ranking, or recommending products.

Status: complete.

## Content — Diabetes & Blood Ketones (Cluster H)

Goal: build the diabetes ketone context — how the diabetes context changes ketone-signal interpretation — as a strictly bounded reference. Deliberately scoped as the *diabetes ketone context*, not a generic diabetes page, to keep depth aligned with the asset's name.

Governing distinction: Diabetes changes what a ketone signal may mean, not what a ketone is; ketone presence is still not a diagnosis, but the context raises the stakes of interpretation and timing.

Deliverables:

- `/diabetes-ketone-context/` — why diabetes changes the reading (insulin, DKA pathway), type 1 / type 2 note, compounding contexts (illness, missed insulin, SGLT2), held boundary, "what this page does not do," emergency-aware boundary block, audience notes, source IDs, AI-readable summary;
- highest clinical sensitivity, strictest boundary: no diagnosis/triage, no safety verdicts, no thresholds, no sick-day rules (defers to the reader's care team), no insulin/medication advice; DKA framed as a medical emergency with urgent-care routing;
- sources reused only (SRC-ADA-2026, SRC-DUK-DKA, SRC-NHS-DKA);
- wire-in and reconciliation 38 → 39 (cluster count stays eight; all four route lists kept identical): `/architecture/` + `SYSTEM_ARCHITECTURE.md`, `/ketonemia-vs-ketoacidosis/`, `/sglt2-context/`, `/ontology/diabetes-associated-signal/`, `/sources/` + `data/source-registry.json`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: generic diabetes-management content; diagnosis or triage; safety/danger verdicts; thresholds; sick-day rules; insulin or medication advice.

Status: complete.

## Content — Exercise & Blood Ketones (Cluster H)

Goal: complete the metabolic side of the Metabolic & Clinical Context cluster with the exercise/performance context, refusing the performance-claim and supplement hype the topic attracts.

Governing distinction: Exercise is a context that shapes the signal, not a claim about it; a ketone reading around exercise reflects fuel metabolism, not benefit, a performance metric, or a diagnosis.

Deliverables:

- `/exercise-ketones/` — fuel-substrate physiology, context-dependence (timing, feeding state, intensity/duration, diet background), "what exercise ketones are not," a neutral no-endorsement note on ketone supplements, measurement across the triad without thresholds, limits, audience notes, source IDs, AI-readable summary;
- no performance claim (either direction), no supplement endorsement, no thresholds; diabetes/medication context preserved;
- sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-STRYER-BIOCHEM);
- wire-in and reconciliation 39 → 40 (cluster count stays eight; all four route lists kept identical): `/architecture/` + `SYSTEM_ARCHITECTURE.md`, `/fasting-ketones/`, `/nutritional-ketosis/`, `/ontology/exercise-performance-signal/`, `/sources/` + `data/source-registry.json`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- README and DECISION_LOG entries.

Prohibited: performance-benefit or performance-harm claims; treating a reading as a fitness metric; endorsing or assessing ketone supplements; numeric thresholds.

Status: complete.

## Tool — Interactive Glossary

Goal: add a governed retention tool ("reference gravity," not an engagement loop) — a searchable glossary people and AI return to for terminology — while staying entirely inside privacy-by-architecture and the clinical boundary.

Owner decision: reject engagement/tracking/personalization tools (they break the moat); build reference tools that make the site the default place to look terminology up.

Deliverables:

- `/glossary/` — searchable, client-side glossary mirroring `data/glossary.json` (14 terms; layer, non-equivalents, boundary note, canonical page each);
- `/assets/js/glossary.js` — vanilla JS filter, no network/storage/tracking; content static and crawlable without JS;
- scoped `.glossary-*` CSS using existing variables;
- static-only, no personal or numeric-value inputs, definitions only (no diagnosis or reading interpretation); `DefinedTermSet` JSON-LD;
- wire-in and reconciliation 40 → 41 (cluster count stays eight; all four route lists kept identical): `/architecture/` + `SYSTEM_ARCHITECTURE.md`, `/reference-pack/`, `/student-guide/`, `/acquisition/` + `ACQUISITION_DOSSIER.md`, homepage, `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml`;
- `QUALITY_GATE.md` Glossary Tool Gate; README and DECISION_LOG entries.

Prohibited: accounts, tracking, personalization, saved state; personal or numeric-value inputs; interpreting an individual reading; any definition looser than glossary.json.

Status: complete.

## Engine Upgrade — Context Reference as a Formal Output

Goal: close four review-identified gaps so the engine ↔ context-page link is complete and formalized.

Deliverables:

- exercise context added to the engine form + `RULE-EXERCISE-BLOOD` (rule set 15 → 16), routing to Exercise / Performance Signal and `/exercise-ketones/`;
- `context_reference_page` promoted to a dedicated output field (mirroring `kso_class_page`) on the five context rules, removed from `canonical_references`, and rendered by the engine JS as its own "Context reference" link;
- `CLASSIFICATION_PROTOCOL.md` lists the context reference as a formal governed output that must match `data/kso-ontology.json` `context_page`;
- `QUALITY_GATE.md` Context Reference Linkage Gate;
- inline rules JSON re-verified byte-identical; no boundary/label/source change; sensitive combinations unchanged; no new route (lists stay 41);
- engine prose and AI summary updated; README and DECISION_LOG entries.

Prohibited: changing boundary or prohibited-inference language; softening sensitive-combination handling; duplicating the context page in canonical_references; any inline/standalone JSON drift.

Status: complete.

## Content — Illness & Blood Ketones (Cluster H)

Goal: complete public-page coverage of every non-boundary KSO context class by building the illness / metabolic-stress context page, and extend the engine loop to it.

Governing distinction: Illness can drive the signal by a stress response, not a nutritional choice; ketone presence during illness is still not a diagnosis.

Deliverables:

- `/illness-ketones/` — illness ketogenesis (reduced intake + stress response, vomiting/dehydration), context-changes-the-reading table, held boundary, "what this page does not do," emergency-aware boundary block, audience notes, source IDs, AI-readable summary;
- engine loop: KSO-5 `context_page` + `RULE-ILLNESS-ALONE` `context_reference_page` = `/illness-ketones/` (matching), inline byte-identical;
- highest-sensitivity boundary: no diagnosis/triage, no safety verdicts, no sick-day rules, no thresholds, no treatment advice; sources reused only (LEHNINGER, NHS, DUK);
- wire-in and reconciliation 41 → 42 (cluster count stays eight; four route lists identical): architecture + SYSTEM_ARCHITECTURE, signal-map, ontology/illness-stress-signal, sources + source-registry, acquisition + ACQUISITION_DOSSIER, homepage, reference-pack.json, page-index.json, llms.txt, sitemap.xml;
- README and DECISION_LOG entries.

Prohibited: sick-day rules; thresholds; diagnosis/triage; treatment advice; changing the constant boundary statement or sensitive-combination handling.

Status: complete.

## Content — Blood Ketone FAQ (Cluster A, GEO surface)

Goal: add a governed FAQ answer layer that captures the highest-intent natural-language questions about blood ketones and answers each within the clinical boundary, routing every answer to its canonical page — a generative-engine-optimization surface for humans and AI systems alike.

Governing distinction: An answer is a routing decision, not a verdict; the FAQ names the governed distinction and hands off to the page that owns it, and it never assigns a safe/normal number.

Deliverables:

- `/faq/` — eight boundary-safe Q&A (what ketonemia is; vs. ketoacidosis; whether ketones mean something is wrong; the "normal/safe level" question, answered by refusing a universal number and routing to a clinician; what raises ketones; blood/urine/breath differences; vs. ketosis; whether the site can interpret a personal reading), each answer linking to its canonical page;
- `FAQPage` JSON-LD whose `acceptedAnswer` text is byte-identical to the visible answers (machine-human parity verified programmatically);
- wire-in and reconciliation 42 → 43 (cluster count stays eight; four route lists identical): architecture + SYSTEM_ARCHITECTURE, homepage, acquisition + ACQUISITION_DOSSIER, reciprocal links from `/definition/` and `/glossary/`, reference-pack.json, page-index.json, llms.txt, sitemap.xml;
- README and DECISION_LOG entries.

Prohibited: numeric thresholds; safe/danger verdicts; diagnosis, triage, or individual interpretation; any structured-data claim looser than the visible answer; new unsourced claims.

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
