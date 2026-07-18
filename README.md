# Ketonemia.com

## Blood Ketone Intelligence Infrastructure

Ketonemia.com is being developed as a governed category asset for blood ketone intelligence.

It is not a generic health blog, keto content site, diagnostic tool, medical advice platform, supplement funnel, or thin dictionary page.

Ketonemia.com exists to define, organize, classify, and explain blood ketone signals across metabolic health, fasting, diabetes risk, laboratory measurement, clinical literacy, product education, investment intelligence, and AI-readable reference systems.

Core doctrine:

**Ketonemia is a blood signal before it is a clinical verdict.**

Operational rule:

**Classify the signal. Preserve the clinical boundary.**

Final asset statement:

**Ketonemia.com turns blood ketones from isolated readings into governed intelligence - readable by people, institutions, and AI systems, without crossing into clinical verdicts.**

## Sprint 0 Foundation

This repository contains the doctrine and governance layer for the asset. Sprint 0 locked the category thesis before public pages or tools were built.

Governance documents:

- [FOUNDATION_DOCTRINE.md](FOUNDATION_DOCTRINE.md)
- [ASSET_THESIS.md](ASSET_THESIS.md)
- [CATEGORY_LANGUAGE.md](CATEGORY_LANGUAGE.md)
- [KETONEMIA_SIGNAL_ONTOLOGY.md](KETONEMIA_SIGNAL_ONTOLOGY.md)
- [KETONEMIA_STATE_STANDARD.md](KETONEMIA_STATE_STANDARD.md)
- [CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md)
- [CLAIM_POLICY.md](CLAIM_POLICY.md)
- [SOURCE_POLICY.md](SOURCE_POLICY.md)
- [CONTENT_PRODUCTION_POLICY.md](CONTENT_PRODUCTION_POLICY.md)
- [INTERFACE_THESIS.md](INTERFACE_THESIS.md)
- [BUYER_LOGIC.md](BUYER_LOGIC.md)
- [MONETIZATION_BOUNDARY.md](MONETIZATION_BOUNDARY.md)
- [AI_REFERENCE_POLICY.md](AI_REFERENCE_POLICY.md)
- [SEO_GOVERNANCE.md](SEO_GOVERNANCE.md)
- [INTERNAL_LINKING_POLICY.md](INTERNAL_LINKING_POLICY.md)
- [QUALITY_GATE.md](QUALITY_GATE.md)
- [DECISION_LOG.md](DECISION_LOG.md)
- [ASSET_INTELLIGENCE_FACTORY_PLAN.md](ASSET_INTELLIGENCE_FACTORY_PLAN.md)
- [CLASSIFICATION_PROTOCOL.md](CLASSIFICATION_PROTOCOL.md)
- [SYSTEM_ARCHITECTURE.md](SYSTEM_ARCHITECTURE.md)
- [EDITORIAL_TRUST_STANDARD.md](EDITORIAL_TRUST_STANDARD.md)
- [MONETIZATION_SPEC.md](MONETIZATION_SPEC.md)
- [ACQUISITION_DOSSIER.md](ACQUISITION_DOSSIER.md)
- [ROADMAP.md](ROADMAP.md)

Status: complete.

## Sprint 0A Integrity Gate

Before Sprint 1 pages were built, the foundation integrity gate was run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\foundation_integrity_gate.ps1
```

The gate checks required governance files, README links, the Sprint 0 decision, clinical boundary references, high-risk phrase context, and broken internal Markdown links.

Status: complete.

## Sprint 1 — Public Reference Surface v1

Sprint 1 built nine public reference pages. All pages comply with [CONTENT_PRODUCTION_POLICY.md](CONTENT_PRODUCTION_POLICY.md) — layered by audience, clinically bounded, AI-readable, and source-disciplined. The Sprint 1 Review Gate passed before merge.

Pages:

- `/` — category identity and reference map
- `/definition/` — governed definition of ketonemia as a blood state
- `/ketonemia-vs-ketosis/` — blood measurement state vs. metabolic state
- `/ketonemia-vs-ketoacidosis/` — signal vs. clinical syndrome, clinically bounded
- `/blood-ketones/` — signal layer and measurement context
- `/beta-hydroxybutyrate/` — primary blood ketone marker, biochemistry depth
- `/clinical-boundary/` — formal trust and safety boundary
- `/sources/` — source discipline policy and reference index
- `/strategic-availability/` — category intelligence for strategic buyers

Status: complete.

## Sprint 2 — Blood Ketone Signal Map

Sprint 2 built the Signal Map — the conceptual interface showing how context transforms blood ketone signal interpretation. Passed Sprint 2 Review Gate.

Pages:

- `/signal-map/` — six signal zones (KSS K0–K5), eight context dimensions, four interpretation boundaries, accessible text fallback, AI-readable summary

Status: complete. Patch: 227c218. Merged to main.

## Sprint 3A — AI Reference Layer

Sprint 3A built the AI reference layer — structured governance for how AI systems may and may not use Ketonemia.com content. Passed Sprint 3A Review Gate.

Pages:

- `/ai-reference/` — allowed uses, prohibited inferences, allowed and prohibited claim patterns, Signal Map as conceptual interface, canonical reference pages, audience note, AI-readable summary

Status: complete. Commit: 7a508fa8. Merged to main.

## Sprint 3B — Clinical Literacy Layer

Sprint 3B built the clinical literacy layer — responsible language patterns for communicating blood ketone signals without diagnostic overreach. Passed Sprint 3B Review Gate.

Pages:

- `/clinical-literacy/` — governing rule, responsible language table (8 patterns), three-layer clinical communication framework (measurement state / metabolic context / clinical concern boundary), reference pathways, audience notes, AI-readable summary

Status: complete. Commit: b6f65244. Merged to main.

## Sprint 3C — Laboratory Context

Sprint 3C built the laboratory context layer — the measurement science reference for blood ketone signals. Passed Sprint 3C Review Gate.

Pages:

- `/laboratory-context/` — governing rule, three-substrate table (BHB/AcAc/acetone across blood/urine/breath), BHB as primary blood measurement anchor with enzymatic mechanism, report language limits table (Detected/Elevated/Normal/numeric value/units), device and method variation (at-home vs. lab precision gap, hematocrit effects, strip lot variation, sample timing, urine-blood discordance in DKA resolution), reference pathways, audience notes, AI-readable summary

Patches:

- `/blood-ketones/` — Related Pages and AI summary Linked pages updated with /laboratory-context/
- `/beta-hydroxybutyrate/` — Related Pages and AI summary Linked pages updated with /laboratory-context/
- `/signal-map/` — Context 6 ctx-links, Reference Pages grid, and AI summary Related pages updated with /laboratory-context/
- `/` — homepage card grid updated (Laboratory Context as card 7)

Status: complete. Commit: 9f044714. Merged to main.

## Sprint 3D — Student Guide

Sprint 3D built the student guide — a structured learning pathway for blood ketone terminology across academic disciplines. Passed Sprint 3D Review Gate.

Pages:

- `/student-guide/` — governing rule, terminology ladder (9 terms: ketone body through ketoacidosis), measurement layer (three technologies), comparison layer (ketonemia vs. ketosis / ketonemia vs. ketoacidosis), signal context layer (8 dimensions), boundary layer (5-row can/cannot table), ordered study pathway (8 pages), student mistakes to avoid (7 items), audience notes for 5 disciplines (medicine, pharmacy, nursing, biochemistry/laboratory science, nutrition), reference pathways (9 cards), AI-readable summary

Patches:

- `/definition/` — Related Pages and AI summary Linked pages updated with /student-guide/
- `/ketonemia-vs-ketosis/` — Related Pages and AI summary Linked pages updated with /student-guide/
- `/ketonemia-vs-ketoacidosis/` — Related Pages and AI summary Linked pages updated with /student-guide/
- `/laboratory-context/` — Reference Pathways and AI summary Linked pages updated with /student-guide/
- `/` — homepage card grid updated (Student Guide as card 8, total 13 cards)

Status: complete. Commit: d6427f88. Merged to main.

## Sprint 3F - Research Reference Layer

Sprint 3F built the research reference layer - a source-bound framework for interpreting ketonemia as a measurable blood signal in research contexts.

Pages:

- `/research/` - research use of ketonemia, measurement variables, adjacent research terms, claim boundaries, source pathways, audience notes, AI-readable summary

Status: complete. Commit: 8421c8c. Merged to main.

## Sprint 3G - Deep Media Brief Layer

Sprint 3G built the media brief layer - a public-language guidance system for describing ketonemia without collapsing measurement, metabolic, urinary, or clinical layers.

Pages:

- `/media-brief/` - media layer map, search-intent explanation blocks, headline-risk framework, allowed/avoid/because wording guidance, quote-ready lines with boundary language, source-class logic, audience layering, reference pathways, source IDs, and AI-readable summary

Patches:

- `/` - homepage card grid updated with Media Brief
- `/ai-reference/` - Canonical Reference Pages and AI summary updated with /media-brief/
- `/research/` - Source Pathways and AI summary updated with /media-brief/
- `/clinical-boundary/` - Related Pages and AI summary updated with media route
- `QUALITY_GATE.md` - Deep Media Brief Gate added

Status: complete. Commit: ce3f718. Merged to main.

## Sprint 4A / F1 - Agent-Readable Reference Layer

Sprint 4A (build phase F1 of the Asset Intelligence Factory Plan) made Ketonemia.com readable, citeable, and retrievable by AI systems, agents, and structured consumers - without adding clinical interpretation, diagnosis, triage, or treatment logic. This is the transition from *category asset* to machine-readable *category intelligence source*.

Files:

- `/llms.txt` - public AI index: positioning, allowed and prohibited AI uses, canonical pages, machine-readable files
- `/robots.txt` - crawl policy pointing to the sitemap
- `/sitemap.xml` - all canonical public routes
- `/data/reference-pack.json` - central manifest of the machine-readable layer
- `/data/glossary.json` - governed term definitions with clinical-boundary notes
- `/data/kso-ontology.json` - Ketonemia Signal Ontology (KSO), ten context classes
- `/data/kss-standard.json` - Ketonemia State Standard (KSS), K0-K5 reference labels
- `/data/source-registry.json` - claim source registry mirroring `/sources/`
- `/data/page-index.json` - canonical page index for retrieval
- `/reference-pack/` - human-readable index of the machine-readable layer

Patches:

- `/` - homepage card grid and footer updated with Reference Pack
- `/ai-reference/` - Machine-Readable Reference Files section, AI summary, and footer updated
- `QUALITY_GATE.md` - Agent-Readable Reference Layer Gate added
- Governing rule: the machine-readable layer is never looser than the human-facing site; prohibited claims stay prohibited in every format; every claim traces to a canonical page and, where medical, to a source ID (see [AI_REFERENCE_POLICY.md](AI_REFERENCE_POLICY.md)).

Status: complete.

## F2 - Classification Protocol

F2 added [CLASSIFICATION_PROTOCOL.md](CLASSIFICATION_PROTOCOL.md) as the governed bridge between KSO, KSS, source discipline, and future engine outputs. The protocol defines allowed context inputs, prohibited outputs, deterministic classification rules, reference mapping patterns, an output template, and engine-readiness boundaries. It converts observed context into a KSO class, KSS zone language, a boundary statement, canonical references, and source requirements - without diagnosis, triage, treatment, individualized interpretation, safety or danger verdicts, or risk scoring.

Governing sentence: The protocol classifies the interpretive frame, not the person.

This is the operational bridge between knowledge and tool: KSO says what the context classes are, KSS says what the signal-zone language is, F2 says how they are used together under governance, and a future engine (F4) would run F2 in an interface. Any engine built on the asset must produce outputs no broader than this protocol allows.

Status: complete.

## F3 - System Architecture / Reference Map

F3 added [SYSTEM_ARCHITECTURE.md](SYSTEM_ARCHITECTURE.md) and the public `/architecture/` page - the single artifact that shows Ketonemia.com as one governed system rather than a set of pages. This is the layer that converts a set of good pages into one legible category machine, and the page a strategic buyer and an AI agent read first.

Governing sentence: The architecture makes the system legible. It does not add clinical content.

Pages:

- `/architecture/` - the asset as a system, the layer stack (10 layers plus the machine layer), the reference map (all 16 routes clustered on one page with no orphans), a how-to-read-the-system audience block, the governance spine, and the machine and agent layer, with CollectionPage and BreadcrumbList structured data carrying no medical claims

Files and patches:

- `SYSTEM_ARCHITECTURE.md` - internal canonical map: layer stack (kept in sync with the Asset Intelligence Factory Plan), route-map clusters, build order, and the architecture rule that no route may exist without a declared layer and a place in the map
- `/` - homepage card grid and footer updated with System Architecture
- `/ai-reference/` - System map paragraph and AI summary updated with `/architecture/`
- `/strategic-availability/` - reconciled the stale "Nine interconnected reference pages" description, added a System Architecture value-stack row, and linked `/architecture/`
- `/reference-pack/` - Related Pages updated with `/architecture/`
- `/sitemap.xml`, `/llms.txt`, `/data/page-index.json`, `/data/reference-pack.json` - `/architecture/` route registered
- `QUALITY_GATE.md` - System Architecture Gate added

Status: complete.

## F4 - Governed Classification Engine

F4 added `/classification-engine/` - the first operational tool on Ketonemia.com, and the first concrete evidence the asset is a Category Intelligence Source, not just a Category Artifact. The engine runs [CLASSIFICATION_PROTOCOL.md](CLASSIFICATION_PROTOCOL.md) as a deterministic, reviewable rule set: it maps structured context selections to governed reference output, using only the real KSO classes and KSS labels already defined in the repository.

Governing sentence: The engine classifies the interpretive frame around a blood ketone signal. It does not classify a person, diagnose a condition, triage urgency, recommend treatment, or declare safety or danger.

Files:

- `/classification-engine/` - boundary notice, engine thesis, context-only input form (measurement type, measured compound, context, audience - no numeric values, no symptoms, no personal data), a nine-field governed output template, protocol explanation, and AI-readable summary
- `/data/classification-rules.json` - 15 deterministic rules (first-match wins, unconditional catch-all) mapping context inputs to KSO class, KSS language, boundary statement, allowed language, prohibited inference, canonical references, and source requirements; embedded inline in the page (byte-identical to the standalone file) so the engine has no fetch/backend dependency
- `/assets/js/classification-engine.js` - vanilla JavaScript, no dependencies, no network calls, no storage; renders output via `textContent` only
- `assets/css/style.css` - scoped `.engine-*` classes extending the existing visual language, no new design system

Sensitive combinations (diabetes + illness/stress, diabetes + medication) route to explicit clinical-concern-boundary language rather than a verdict; the boundary statement and prohibited-inference language never soften across any input combination or audience.

Patches:

- `/` - homepage card grid and footer updated with the Classification Engine
- `/architecture/` and `SYSTEM_ARCHITECTURE.md` - Engine / Tool layer marked Owned, engine added to the Boundary & Sources cluster, all stale route counts corrected from 16 to 17
- `/signal-map/` - Reference Pages and AI summary updated with the engine
- `/ai-reference/` - AI-systems warning paragraph, canonical pages, and AI summary updated
- `/reference-pack/` and `/data/reference-pack.json` - classification-rules.json added to the machine-readable file set
- `/data/page-index.json`, `/llms.txt`, `/sitemap.xml` - new route registered
- `QUALITY_GATE.md` - Governed Classification Engine Gate added

Status: complete.

## F5 - Deep KSO Ontology Class Pages

F5 turned the Ketonemia Signal Ontology from a governance spec into a citable reference structure the category owns: an `/ontology/` hub and ten deep class pages, one per KSO class. Each page is a governed reference artifact - definition, context map, an explicit "what it is not" distinction from adjacent classes, the KSS relationship, boundary language, audience notes, source IDs, and an AI-readable summary - not a thin glossary entry.

Governing sentence: KSO may classify context. It must not declare a patient state.

Pages:

- `/ontology/` - the Signal Ontology hub: the ontology rule, a table of all ten classes, and links to each class page, the Signal Map, the Classification Engine, and AI Reference
- `/ontology/baseline-signal/`, `/ontology/nutritional-signal/`, `/ontology/fasting-signal/`, `/ontology/exercise-performance-signal/`, `/ontology/illness-stress-signal/`, `/ontology/diabetes-associated-signal/`, `/ontology/medication-context-signal/`, `/ontology/laboratory-measurement-signal/` - the eight signal-context class pages
- `/ontology/dka-concern-boundary/`, `/ontology/emergency-referral-boundary/` - the two boundary class pages, carrying the strongest restraint: not diagnoses, no self-triage

Engine integration:

- Each rule in `/data/classification-rules.json` now carries a `kso_class_page`, and the Classification Engine renders the KSO-class result as a link directly to the matching class page - closing the loop from the operational tool into the reference structure. The inline rules block in the engine page stays byte-identical to the JSON file.

Patches and reconciliation (route count 17 to 28):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` - Ontology layer marked Owned pointing to `/ontology/`; new Ontology (KSO Classes) cluster added to the Reference Map / Route Map; JSON-LD ItemList extended; route counts corrected
- `/signal-map/`, `/ai-reference/` - Reference Pages and AI summaries updated with the ontology
- `/` - homepage card and footer; `/data/kso-ontology.json` - `ontology_page` added to each class; `/data/reference-pack.json`, `/data/page-index.json`, `/llms.txt`, `/sitemap.xml` - new routes registered
- `QUALITY_GATE.md` - KSO Class Pages Gate added

Sources are reused from the existing registry, never invented; boundary classes carry no self-triage language. Status: complete.

## F6 - Monetization Proof

F6 turned the monetization layer from "boundary owned, proof pending" into a governed, demonstrable revenue path. It added [MONETIZATION_SPEC.md](MONETIZATION_SPEC.md) and the public `/briefs/` page - a product catalog and inquiry surface that earns by licensing and briefing the governed intelligence the asset already produces, without touching neutrality, source discipline, or the clinical boundary.

Governing sentence: Revenue must extend trust, not replace it.

Pages:

- `/briefs/` - governing sentence, "what these are," a product catalog table (each product traceable to a permitted-monetization line), the flagship AI Reference Pack License spec, how sponsorship works ("Supported by," never "recommended by"), a "what this is not" section, a plain inquiry surface, related pages, and an AI-readable summary

Files:

- `MONETIZATION_SPEC.md` - internal spec operationalizing MONETIZATION_BOUNDARY.md: the product catalog mapped to permitted lines, the flagship spec, the inquiry mechanism, and the hard rules (no on-site prices, no payment, no data-collection form, "Supported by" not "recommended by," no restricted/prohibited categories, no Offer/price in structured data)

Discipline:

- Every product is drawn only from the Permitted Monetization list; restricted categories are explicitly deferred and prohibited categories explicitly excluded. The page is static - no store, no checkout, no payment integration, no data-collection form, no ads - so there is no new security or personal-data surface. Structured data is CollectionPage / BreadcrumbList with no Offer or price markup, so the asset is not misrepresented as an e-commerce store.

Patches and reconciliation (route count 28 to 29):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` - Monetization layer marked Owned pointing to `/briefs/`; `/briefs/` added to the Strategic cluster; JSON-LD ItemList and route counts updated
- `/strategic-availability/` - governed-revenue value-stack row and a Related Pages link to `/briefs/`
- `/` - homepage card and footer; `/data/reference-pack.json`, `/data/page-index.json`, `/llms.txt`, `/sitemap.xml` - new route registered
- `QUALITY_GATE.md` - Monetization Proof Gate added

Status: complete.

## F7 - Acquisition Dossier

F7 built the final layer of the Asset Intelligence Factory: the acquisition dossier that turns "the asset is valuable" into a structured, neutral account a corporate-development team can read. It added [ACQUISITION_DOSSIER.md](ACQUISITION_DOSSIER.md) and the public `/acquisition/` page.

Governing sentence: Owning Ketonemia.com means owning a reference layer around an emerging metabolic signal category.

Pages:

- `/acquisition/` - what is owned (the full layer stack), the moat (each line tied to the shipped artifact that proves it), the machine and reference footprints, the governance record, a cost-of-not-owning table for each of the eight priority buyer classes, and the constraints an acquirer inherits

Files:

- `ACQUISITION_DOSSIER.md` - the private-facing but public-safe dossier that governs the public page

Discipline:

- The dossier is an inventory of what exists - no price, no valuation, no forward-looking financial figure, no medical claim, and no data-collection form. It stays neutral (never a raw domain listing) and inside every existing boundary. Structured data is CollectionPage / BreadcrumbList with no Offer or price.

Patches and reconciliation (route count 29 to 30):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` - Buyer logic layer marked Owned pointing to `/acquisition/`; `/acquisition/` added to the Strategic cluster; JSON-LD ItemList and route counts updated; build order marked complete
- `ASSET_INTELLIGENCE_FACTORY_PLAN.md` - the F1-F7 build sequence marked complete
- `/strategic-availability/` and `/briefs/` - value-stack row and Related Pages links to `/acquisition/`
- `/` - homepage card and footer; `/data/reference-pack.json`, `/data/page-index.json`, `/llms.txt`, `/sitemap.xml` - new route registered
- `QUALITY_GATE.md` - Acquisition Dossier Gate added

With F7 the build sequence F1-F7 is complete: every layer of the Asset Intelligence Factory is owned and in production, and the asset has moved the full distance from domain to strategic acquisition asset.

Status: complete.

## F8 - Editorial Trust & Transparency Layer

F8 deepened the governance layer (layer 8) the way F5 deepened the ontology layer: it turned the source discipline the asset already practices into a visible, citable trust surface. It added [EDITORIAL_TRUST_STANDARD.md](EDITORIAL_TRUST_STANDARD.md) and the public `/trust/` page.

Governing sentence: Trust is a standard the asset holds to, not a badge it awards itself.

The honesty rule is the point of the layer: it documents the standard and the mechanism, and never asserts a review, endorsement, credential, or accuracy metric that did not occur. The page states, in the same table, what it claims and what it does not — most importantly, that no page is claimed to have been individually reviewed or approved by a named clinician.

Pages:

- `/trust/` - the trust contract (seven disciplines, each tied to the artifact that proves it), a "what this page claims and does not" table, how content is produced, the correction and change policy (neutral `corrections@ketonemia.com`, no form, no data collection), independence and funding, and privacy by architecture

Files:

- `EDITORIAL_TRUST_STANDARD.md` - the internal standard operationalizing SOURCE_POLICY.md, CLAIM_POLICY.md, CLINICAL_BOUNDARY.md, and AI_REFERENCE_POLICY.md into one trust contract, with an explicit list of what may and may not be claimed

Discipline:

- The page is static - no new script, form, third-party dependency, or data-collection surface. It adds no clinical content, threshold, or interpretation. Structured data is CollectionPage / BreadcrumbList with no Offer, price, or medical claim.

Patches and reconciliation (route count 30 to 31):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` - Governance layer "Where it lives" now points to `/trust/`; `/trust/` added to the Boundary & Sources cluster; JSON-LD ItemList extended to 31; route counts and build order updated (layer 8 marked deepened F8)
- `/ai-reference/` - Canonical Reference Pages and AI summary updated with `/trust/`
- `/acquisition/` and `ACQUISITION_DOSSIER.md` - Governance and moat rows point to the published trust standard; route counts reconciled to thirty-one
- `/` - homepage card grid and footer; `/data/reference-pack.json` (canonical page + governance document), `/data/page-index.json`, `/llms.txt`, `/sitemap.xml` - new route registered
- `QUALITY_GATE.md` - Editorial Trust Gate added

Status: complete.

## Content — Urine Ketones (Ketonuria)

A deep public-reference and SEO pillar completing the measurement triad (blood / urine / breath). It captures high-intent search around "urine ketones" and "ketones in urine" and routes it correctly: a urine strip measures mostly acetoacetate (AcAc), not the beta-hydroxybutyrate (BHB) measured in blood, on a time lag, and the two are not interchangeable.

Governing distinction: Ketonemia is a blood measurement state; ketonuria is a urinary finding — same family of molecules, different measurement layer, and different meaning.

Pages:

- `/urine-ketones/` — what urine ketones are, a urine-vs-blood comparison table, how urine strips measure (nitroprusside / AcAc), why urine lags and can disagree with blood (DKA-resolution discordance), context that changes meaning, what urine ketones cannot tell you alone, interpretation limits, audience notes, source IDs, and an AI-readable summary

Discipline:

- Every claim is sourced from the existing registry only (SRC-LAB-BHB-ACAC, SRC-LEHNINGER-BIOCHEM, SRC-NHS-DKA) — no new or invented source. Strip categories (negative / trace / small / moderate / large) are presented as the strip's semi-quantitative reporting language, never as clinical severity, thresholds, or a diagnosis. Clinical questions route to professional care. `WebPage` JSON-LD with no medical claim, matching the measurement-cluster siblings.

Patches and reconciliation (route count 31 to 32):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` — `/urine-ketones/` added to the Measurement & Laboratory cluster; JSON-LD ItemList extended to 32; route counts updated
- `/blood-ketones/` and `/laboratory-context/` — Related Pages and AI summary linked pages updated with `/urine-ketones/`
- `/sources/` and `data/source-registry.json` — pages-using-source updated for the three cited sources
- `/acquisition/` and `ACQUISITION_DOSSIER.md` — route counts reconciled to thirty-two
- `/` — homepage card grid; `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml` — new route registered

Status: complete.

## Content — Breath Ketones (Breath Acetone)

The page that completes the measurement triad (blood / urine / breath). A breath ketone analyzer measures exhaled acetone — a volatile by-product of ketone metabolism — as a non-invasive proxy for ketone state, not the beta-hydroxybutyrate (BHB) measured in blood. It is best read as a trend, not as a blood number.

Governing distinction: Blood measures BHB as a number; urine measures acetoacetate as a category; breath measures acetone as a proxy — three windows onto the same metabolism, not three versions of one number.

Pages:

- `/breath-ketones/` — what breath ketones are, a three-layer (blood / urine / breath) comparison table, how breath acetone is measured (sensor proxy), why breath is a proxy and not a blood value, context that changes meaning, what it cannot tell you alone, interpretation limits, audience notes, source IDs, and an AI-readable summary

Discipline:

- Sources reused only (SRC-LEHNINGER-BIOCHEM for acetone from spontaneous decarboxylation of acetoacetate, SRC-LAB-BHB-ACAC for measurement across fractions and the primacy of blood BHB). No invented source, no numeric thresholds, no clinical decision use — the page explicitly routes acute concern to blood measurement and professional care. `WebPage` JSON-LD with no medical claim.

Patches and reconciliation (route count 32 to 33):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` — `/breath-ketones/` added to the Measurement & Laboratory cluster; JSON-LD ItemList extended to 33; route counts updated
- `/blood-ketones/`, `/urine-ketones/`, and `/laboratory-context/` — Related Pages and AI summary linked pages updated with `/breath-ketones/`
- `/sources/` and `data/source-registry.json` — pages-using-source updated for the two cited sources
- `/acquisition/` and `ACQUISITION_DOSSIER.md` — route counts reconciled to thirty-three
- `/` — homepage card grid; `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml` — new route registered

Status: complete. With this the measurement triad (blood / urine / breath) is fully owned, each ketone body anchored to its measurement layer.

## Content — Ketone Bodies

The foundational biochemistry hub that anchors the measurement triad: `/ketone-bodies/` defines the three ketone bodies — beta-hydroxybutyrate (BHB), acetoacetate (AcAc), and acetone — and maps each to the measurement layer that reads it (blood / urine / breath). High-intent, high-volume, and purely foundational, it is the parent concept the compound and measurement pages hang from.

Governing idea: There is no single "ketone." There are three ketone bodies, related but distinct — and which one you are measuring depends on how you measure.

Pages:

- `/ketone-bodies/` — what ketone bodies are (hepatic ketogenesis as fuel), the three-compound table mapped to blood/urine/breath, how BHB and AcAc interconvert and acetone forms, a naming note (BHB is a hydroxy acid grouped with ketones by convention), what "ketone bodies present" does not mean, interpretation limits, audience notes, source IDs, and an AI-readable summary

Discipline:

- Sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-STRYER-BIOCHEM) — textbook biochemistry, no invented source, no thresholds, no clinical claim. Explicitly states ketone-body presence is normal fuel, is not a disease, and does not equal ketoacidosis. `WebPage` JSON-LD with no medical claim.

Patches and reconciliation (route count 33 to 34):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` — `/ketone-bodies/` added to the Measurement & Laboratory cluster; JSON-LD ItemList extended to 34; route counts updated
- `/beta-hydroxybutyrate/`, `/blood-ketones/`, and `/laboratory-context/` — Related Pages and AI summary linked pages updated with `/ketone-bodies/`
- `/sources/` and `data/source-registry.json` — pages-using-source updated for the two cited sources
- `/acquisition/` and `ACQUISITION_DOSSIER.md` — route counts reconciled to thirty-four
- `/` — homepage card grid; `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml` — new route registered

Status: complete.

## Content — Fasting Ketones (new Cluster H)

The first page of a new Route Map cluster, **Metabolic & Clinical Context** — the public-facing, SEO-facing counterparts to the KSO context classes. `/fasting-ketones/` captures the highest-intent "ketones" search context (fasting) and routes it correctly: blood ketones rise during fasting because falling glucose and insulin shift the liver to ketogenesis, an expected physiological rise whose meaning still depends on context.

Governing distinction: Fasting is a driver of the signal; ketonemia is the blood measurement. A rise in fasting ketones is usually expected — but "expected" is a statement about context, not a clinical clearance.

Pages:

- `/fasting-ketones/` — why ketones rise during fasting (glycogen depletion, falling insulin, hepatic ketogenesis, BHB as fuel), what changes as a fast continues (direction, no numeric thresholds), what fasting ketones are not (nutritional ketosis / ketoacidosis / one interchangeable number), where context still matters (diabetes, SGLT2 and other medications, illness, pregnancy, prolonged fasting), interpretation limits, audience notes, source IDs, AI-readable summary

Discipline:

- Sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-STRYER-BIOCHEM) — textbook fasting physiology, none invented, and deliberately no numeric thresholds or fasting-duration advice. States plainly that fasting ketosis is not ketoacidosis and never declares an individual reading safe. `WebPage` JSON-LD with no medical claim.

Patches and reconciliation (route count 34 to 35; clusters 7 to 8):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` — new **Metabolic & Clinical Context** cluster (Cluster H) added, seeded with `/fasting-ketones/`; JSON-LD ItemList extended to 35; route counts and cluster count updated
- `/ketonemia-vs-ketosis/` and `/ontology/fasting-signal/` — Related Pages and AI summary linked pages updated with `/fasting-ketones/`
- `/sources/` and `data/source-registry.json` — pages-using-source updated for the two cited sources
- `/acquisition/` and `ACQUISITION_DOSSIER.md` — route counts reconciled to thirty-five, cluster count to eight
- `/` — homepage card grid; `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml` — new route registered

Status: complete.

## Content — Nutritional Ketosis (Cluster H)

The second page in the Metabolic & Clinical Context cluster, and the highest-volume search term in the category. `/nutritional-ketosis/` defines nutritional ketosis as a diet-driven metabolic state and holds the line the category is built on: the state is not the measurement, and neither is ketoacidosis.

Governing distinction: Nutritional ketosis is a metabolic state; ketonemia is the blood measurement that can accompany it. A diet can produce the state; only a measurement reports the signal — and neither is a diagnosis.

Pages:

- `/nutritional-ketosis/` — what the state is (sustained low-carbohydrate intake, low insulin, hepatic ketogenesis, BHB as fuel), state vs. measurement, a nutritional/fasting/ketoacidosis comparison, how it is measured (across the triad, no thresholds), what it is not, where context still matters, interpretation limits, audience notes, source IDs, AI-readable summary

Discipline:

- The highest keto-hype-risk topic on the site, handled with the strictest framing: no diet advice, no "how to get into ketosis," no macro or food guidance, no health-benefit or weight-loss claims, no exogenous-ketone or supplement promotion, and no numeric thresholds. Sources reused only (SRC-LEHNINGER-BIOCHEM, SRC-STRYER-BIOCHEM, SRC-NHS-DKA). `WebPage` JSON-LD with no medical claim. Nutritional ketosis is never equated with ketoacidosis.

Patches and reconciliation (route count 35 to 36; cluster count stays eight):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` — `/nutritional-ketosis/` added to the Metabolic & Clinical Context cluster (now two pages); JSON-LD ItemList extended to 36; route counts updated
- `/ketonemia-vs-ketosis/`, `/fasting-ketones/`, and `/ontology/nutritional-signal/` — Related Pages and AI summary linked pages updated with `/nutritional-ketosis/`
- `/sources/` and `data/source-registry.json` — pages-using-source updated for the three cited sources
- `/acquisition/` and `ACQUISITION_DOSSIER.md` — route counts reconciled to thirty-six
- `/` — homepage card grid; `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml` — new route registered

Status: complete.

## Content — SGLT2 Inhibitors & Ketones (Cluster H)

The clinical/medication dimension of the Metabolic & Clinical Context cluster, and the site's highest-authority safety topic. `/sglt2-context/` explains why one class of diabetes medication changes ketone-signal interpretation, using the strongest sourcing on the site (FDA regulatory warning plus ADA standards of care).

Governing distinction: Without this medication, high glucose is often part of the ketone-concern picture. On an SGLT2 inhibitor, ketoacidosis can occur without markedly elevated glucose — so a "normal glucose" reading does not, by itself, rule the concern out.

Pages:

- `/sglt2-context/` — what SGLT2 inhibitors are, why they change ketone interpretation (regulator-warned ketoacidosis risk without marked hyperglycemia), a common-assumption table, an explicit "what this page does not do," a strong boundary block, audience notes (patients, clinicians/pharmacists, AI, researchers), source IDs, and an AI-readable summary

Discipline:

- The highest clinical-sensitivity page on the site, so it carries the strictest boundary: no medication advice, no start/stop/adjust/dose guidance, no diagnosis or triage, no sick-day rules, no numeric thresholds, and no product naming or ranking. Every individual question routes to professional care, and the page opens and closes with an explicit "never change a prescribed medication on your own." Sources reused only (SRC-FDA-SGLT2, SRC-ADA-2026, SRC-NHS-DKA). `WebPage` JSON-LD with no medical claim.

Patches and reconciliation (route count 37 to 38; cluster count stays eight):

- `/architecture/` and `SYSTEM_ARCHITECTURE.md` — `/sglt2-context/` added to the Metabolic & Clinical Context cluster (now three pages); JSON-LD ItemList extended to 38; route counts updated (37-route source-of-truth rule now reads 38)
- `/ketonemia-vs-ketoacidosis/`, `/ontology/medication-context-signal/`, `/fasting-ketones/`, and `/nutritional-ketosis/` — Related Pages, AI summaries, and inline SGLT2 mentions linked to `/sglt2-context/`
- `/sources/` and `data/source-registry.json` — pages-using-source updated for the three cited sources
- `/acquisition/` and `ACQUISITION_DOSSIER.md` — route counts reconciled to thirty-eight
- `/` — homepage card grid; `data/reference-pack.json`, `data/page-index.json`, `llms.txt`, `sitemap.xml` — new route registered (all four route lists kept identical at 38)

Status: complete.

## Methodology

The asset is developed through this sequence:

Domain -> Doctrine -> Category Language -> Ontology -> Standard -> Interface -> Tooling -> Reference Surface -> Governance -> Monetization -> Buyer Logic -> Strategic Acquisition Readiness

The objective is not to publish content for its own sake. The objective is to build a category artifact that owns:

- the name;
- the language;
- the classification system;
- the standard;
- the clinical boundary;
- the visual logic;
- the internal linking structure;
- the reference layer;
- the monetization boundary;
- the buyer logic;
- and the AI-readable category map.

## Initial Route Map

Core:

- `/`
- `/definition/`
- `/ketonemia-vs-ketosis/`
- `/ketonemia-vs-ketoacidosis/`
- `/blood-ketone-intelligence/`
- `/clinical-boundary/`

Standard and ontology:

- `/standard/`
- `/ontology/`
- `/signal-map/`
- `/measurement-boundary/`
- `/claim-policy/`
- `/sources/`

Public SEO:

- `/blood-ketones/`
- `/beta-hydroxybutyrate/`
- `/urine-ketones/`
- `/breath-ketones/`
- `/fasting-ketones/`
- `/nutritional-ketosis/`

Clinical and institutional:

- `/diabetes/`
- `/dka-concern-boundary/`
- `/sglt2-context/`
- `/clinical-literacy/`
- `/laboratory-context/`
- `/patient-education/`

Strategic and AI:

- `/continuous-ketone-monitoring/`
- `/market-intelligence/`
- `/media-brief/`
- `/research/`
- `/ai-reference/`
- `/strategic-availability/`

No route may exist without a clear strategic purpose. No thin pages, empty SEO pages, duplicated explainers, or keyword farms.

## Development Rule

Every page, tool, visual, claim, source, and monetization path must answer:

- Does this strengthen the category thesis?
- Does this improve trust?
- Does this serve a real audience layer?
- Does this preserve the clinical boundary?
- Does this improve source discipline?
- Does this make the asset harder to ignore?

If the answer is no, it should not be built.
