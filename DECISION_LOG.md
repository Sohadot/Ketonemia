# Decision Log

## DEC-001 - Ketonemia.com positioned as Blood Ketone Intelligence Infrastructure

Decision:

**Ketonemia.com is not a keto content site, diagnostic tool, or generic medical blog. It is governed as a blood ketone intelligence infrastructure that classifies blood ketone signals across context layers while preserving the clinical boundary.**

The asset will use KSO and KSS as internal reference systems, but will not diagnose, prescribe, triage, or replace clinical care.

Date: 2026-06-27

Rationale:

- The domain matches the category term.
- Blood ketone measurement spans public, clinical, laboratory, product, market, and AI contexts.
- The strongest asset position is governed intelligence, not generic keto content.
- Clinical boundary discipline protects trust and strategic value.

Consequences:

- All pages must serve the category thesis.
- Medical claims require sources.
- Signal tools must be educational, not diagnostic.
- Monetization must not damage neutrality.
- Interface design must express signal -> context -> boundary.

Integrity:

- Sprint 0A adds a foundation integrity gate before Sprint 1.
- Governance documents must remain linked, internally consistent, and clinically bounded.

## DEC-002 - Sprint 1 content must be layered reference infrastructure

Decision:

**Sprint 1 content is not page filling. It is layered reference infrastructure by audience.**

Every public page must be useful to a human, legible to an AI system, credible to a specialist, and strategically meaningful to a buyer.

Date: 2026-06-27

Rationale:

- Ketonemia.com must not produce generic articles.
- A single page can serve multiple audiences only if it has a governed reference core and explicit depth layers.
- The public surface must prove category authority without content inflation.
- Source discipline, clinical boundary language, internal linking, and AI-readable summaries must be part of page production from the beginning.

Consequences:

- Sprint 1 is renamed "Public Reference Surface v1 with Layered Content Depth."
- Every Sprint 1 page must answer the five content production questions before being built.
- Every Sprint 1 page must include definition, category role, nearby-concept distinctions, context, interpretation limits, internal links, source support or placeholders, AI-readable summary, and audience notes.
- Shallow "What is X?" pages, repeated ideas, unsupported medical claims, keto hype, and pages without reference or buyer logic are prohibited.

## Implementation Record

This section records completed sprint implementations that did not require a new governance decision. Every completed sprint leaves one of two traces: a DEC entry if production friction created a new governance rule, or an Implementation Record entry if production completed without requiring one.

### Sprint 1B — Public Reference Surface v1

Status: complete.
Merged to main.

Sprint 1B created the first public reference surface for Ketonemia.com, including the homepage and eight reference pages: /, /definition/, /ketonemia-vs-ketosis/, /ketonemia-vs-ketoacidosis/, /blood-ketones/, /beta-hydroxybutyrate/, /clinical-boundary/, /sources/, /strategic-availability/.

The Sprint 1 Review Gate passed without requiring a new governance decision. No DEC was created because no production friction required a new rule.

### Sprint 2 — Blood Ketone Signal Map

Status: complete.
Patch: 227c218. Merged to main.

Sprint 2 added /signal-map/ as a conceptual interface showing that blood ketone signal meaning depends on context, not clinical judgment. The review identified one production gap: context cards needed specific reference links. The gap was patched in the same branch. No DEC was created because the fix was an implementation correction, not a new governance rule.

### Sprint 3A — AI Reference Layer

Status: complete.
Merge commit: 7a508fa8. Docs: fb41b05e.

Sprint 3A added /ai-reference/ as a visible AI-readable reference layer. The page defines allowed AI uses, prohibited inferences, allowed and prohibited claim patterns, Signal Map interpretation boundaries, canonical reference pages, and AI-readable summary structure. No DEC was created because no new friction emerged around KSS classification, prohibited-phrase scope, or JSON-LD structure.

### Sprint 3B — Clinical Literacy Layer

Status: complete.
Merge commit: b6f65244. Docs: 0de43976.

Sprint 3B added /clinical-literacy/ as the responsible language layer for clinicians, educators, care teams, students, and product teams. The page includes the Responsible Language Patterns table (8 rows), the three-layer clinical communication framework (measurement state / metabolic context / clinical concern boundary), reference pathways to all adjacent pages, and full AI-readable summary. Patches updated /clinical-boundary/, /ai-reference/, /signal-map/ (Context 7 ctx-links and Reference Pages grid), and the homepage card grid. No DEC was created because no production friction required a new governance rule.

### Sprint 3C — Laboratory Context

Status: complete.
Merged to main.

Sprint 3C added /laboratory-context/ as the measurement reference layer for blood ketone signals. The page covers three substrates (BHB, AcAc, acetone) and three measurement technologies (electrochemical blood meters, colorimetric urine strips, breath analyzers), BHB as the primary blood measurement anchor, report language limits, and device and method variation including hematocrit effects, strip lot variation, and urine-blood discordance in DKA resolution. Patches updated /blood-ketones/, /beta-hydroxybutyrate/, /signal-map/ (Context 6 ctx-links, Reference Pages grid, AI summary), and the homepage card grid. No DEC was created because no production friction required a new governance rule.

### Sprint 3D — Student Guide

Status: complete.
Merged to main.

Sprint 3D added /student-guide/ as the learning pathway reference layer for blood ketone terminology. The page organizes ketonemia as a layered concept (term → molecule → measurement → context → boundary) with a terminology ladder covering nine terms from ketone body to ketoacidosis, measurement layer, comparison layer, signal context layer, boundary layer, ordered study pathway (eight pages), and seven student mistakes to avoid. Audience notes cover five disciplines: medicine, pharmacy, nursing, biochemistry/laboratory science, and nutrition. Patches updated /definition/, /ketonemia-vs-ketosis/, /ketonemia-vs-ketoacidosis/ (Related Pages with Student Guide card and AI summary Linked pages), /laboratory-context/ (Reference Pathways with Student Guide card and AI summary Linked pages), and the homepage card grid (Student Guide as card 8, total 13 cards). No DEC was created because no production friction required a new governance rule.

### Sprint 3E - Source Registry and Accuracy Hardening

Date: 2026-07-03

Scope:

- Added a visible Claim Source Registry to `/sources/` with source IDs, titles, organizations/publications, source classes, URLs or citations, access dates, supported claims, population/context notes, and pages using each source.
- Added page-level source ID references to existing high-risk pages: `/ketonemia-vs-ketoacidosis/`, `/clinical-boundary/`, `/beta-hydroxybutyrate/`, `/blood-ketones/`, `/laboratory-context/`, and `/student-guide/`.
- Sprint 3E was initially executed from a local snapshot that was behind GitHub main. After reconciliation, `/laboratory-context/` and `/student-guide/` are confirmed as active public pages and remain part of the source-mapping scope.
- Patched NAD markup from superscript-plus glyph usage to `NAD<sup>+</sup>` markup where embedded in HTML text.
- Patched the AcAc/BHB discordance explanation on `/blood-ketones/` and `/laboratory-context/` to preserve consistent urine AcAc vs blood BHB DKA-resolution wording.
- Preserved clinical-boundary language: no diagnosis, triage, individualized safety claim, or treatment instruction was added.

No new DEC was created. The sprint did not establish a new governance rule; it implemented existing source and claim discipline.

### Sprint 3F - Research Reference

Status: complete.
Commit: 8421c8c. Merged to main.

Sprint 3F added /research/ as the research-facing reference layer for ketonemia. The page organizes blood ketone research variables across measured compound, method, population, fasting state, metabolic context, medication context, clinical condition, and source class. It links research-facing interpretation back to /sources/, /laboratory-context/, /beta-hydroxybutyrate/, /signal-map/, /clinical-boundary/, and /ai-reference/. No DEC was created because no production friction required a new governance rule.

### Sprint 3D-R1 - Student Guide Depth Upgrade

Status: complete. Commit: 0fe9409. Merged to main.

Sprint 3D-R1 deepened /student-guide/ from a basic learning pathway into an academic student reference layer. The upgrade added learning objectives, a conceptual layer map, strengthened terminology reading guidance, student reasoning errors, educational reasoning patterns, source ID mapping, a link to /research/, and a stronger AI-readable summary. No DEC was created because the sprint extended existing educational and source-discipline rules without creating a new governance rule.

### Sprint 3G - Deep Media Brief Layer

Status: complete. Commit: ce3f718. Merged to main.

Sprint 3G added /media-brief/ as the public-language guidance layer for ketonemia. The page separates media wording across molecule, measurement, metabolic state, urinary finding, clinical syndrome, and boundary layers; adds search-intent explanation blocks, headline-risk analysis, allowed/avoid/because wording guidance, quote-ready lines with clinical limits, source-class logic, audience layering, internal reference pathways, source IDs, and a rich AI-readable summary. Patches updated the homepage card grid, /ai-reference/, /research/, /clinical-boundary/, and QUALITY_GATE.md. No DEC was created because the sprint applies existing source discipline and clinical-boundary rules to media-facing language without creating a new governance rule.

### Sprint 4A / F1 - Agent-Readable Reference Layer

Status: complete.

Sprint 4A (build phase F1 of the Asset Intelligence Factory Plan) added the machine-readable reference layer that begins the transition from category asset to category intelligence source. Files added: /llms.txt, /robots.txt, /sitemap.xml, /data/reference-pack.json, /data/glossary.json, /data/kso-ontology.json, /data/kss-standard.json, /data/source-registry.json, /data/page-index.json, and the human-readable /reference-pack/ index with Dataset JSON-LD. The KSO and KSS JSON files mirror KETONEMIA_SIGNAL_ONTOLOGY.md and KETONEMIA_STATE_STANDARD.md without inventing classes or thresholds; source-registry.json mirrors the visible registry on /sources/. Patches updated the homepage card grid and footer, /ai-reference/ (Machine-Readable Reference Files section, AI summary, footer), ROADMAP.md, and QUALITY_GATE.md (Agent-Readable Reference Layer Gate). No new DEC was created: the layer is a direct extension of AI_REFERENCE_POLICY.md, which already requires that machine-readable output must not be looser than human-facing content. Clinical-boundary language was preserved: the data does not diagnose, triage, declare a reader safe, or provide treatment instruction.

### F2 - Classification Protocol

Status: complete.

F2 added CLASSIFICATION_PROTOCOL.md as the governed protocol layer connecting observed context to KSO class, KSS language, boundary statement, canonical references, and source requirements. The protocol prepares the future engine layer (F4) while prohibiting diagnosis, triage, treatment guidance, individualized interpretation, safety verdicts, danger verdicts, risk scoring, and device endorsement. It accepts context-only inputs, never numeric thresholds, and keeps blood BHB, urine AcAc, and breath acetone as non-interchangeable signals. The mapping table and output template use the real KSO classes and KSS K0-K5 labels from KETONEMIA_SIGNAL_ONTOLOGY.md and KETONEMIA_STATE_STANDARD.md. Governing sentence: the protocol classifies the interpretive frame, not the person. Patches: README governance index, README F2 section, ROADMAP F2 entry, and an /ai-reference/ note that the protocol governs future machine outputs. No DEC was created because the sprint operationalized existing KSO, KSS, source-discipline, AI-reference, and clinical-boundary rules without creating a new governance rule.

### F3 - System Architecture / Reference Map

Status: complete.

F3 added SYSTEM_ARCHITECTURE.md and the public /architecture/ page, the single artifact that presents Ketonemia.com as one governed system rather than a set of pages. SYSTEM_ARCHITECTURE.md documents the layer stack (kept in sync with ASSET_INTELLIGENCE_FACTORY_PLAN.md), the route-map clusters, the build order, and the architecture rule that no route may exist without a declared layer and a place in the map. The /architecture/ page renders the layer stack, the full reference map of all 16 routes on one page with no orphans, a how-to-read-the-system audience block, the governance spine, and the machine and agent layer, using only existing CSS and CollectionPage/BreadcrumbList structured data with no medical claims. Patches: homepage card grid and footer, /ai-reference/ system-map paragraph and AI summary, /strategic-availability/ (reconciled the stale "Nine interconnected reference pages" line and added a System Architecture value-stack row and link), /reference-pack/ Related Pages, sitemap.xml, llms.txt, data/page-index.json, data/reference-pack.json, and a System Architecture Gate in QUALITY_GATE.md. The page preserves the clinical boundary: it describes reference structure only, with no diagnosis, triage, thresholds, or verdicts. No DEC was created because F3 operationalized the existing methodology and internal-linking discipline without creating a new governance rule.

### F4 - Governed Classification Engine

Status: complete.

F4 added /classification-engine/ as the deterministic interface for running the Classification Protocol. The engine maps structured context selections (measurement type, measured compound, context, audience) to governed reference outputs: KSO class, KSS language, boundary statement, allowed language, prohibited inference, canonical references, and source requirements, via a first-match, unconditional-catch-all rule set of 15 rules in data/classification-rules.json (embedded inline in the page, byte-verified identical to the standalone file). It does not accept personal readings, symptoms, numeric values, or medical history, and it prohibits diagnosis, triage, treatment guidance, individualized interpretation, safety verdicts, danger verdicts, risk scoring, and device endorsement. Sensitive input combinations (diabetes + illness/stress, diabetes + medication) route to explicit clinical-concern-boundary language rather than a verdict; the boundary statement and prohibited-inference text are identical across every rule and every audience. The page is static-first (vanilla JS, no backend, no external API, no tracking, no storage, output rendered via textContent only) with a noscript fallback. All KSO/KSS names and source IDs used in the rules match data/kso-ontology.json, data/kss-standard.json, and data/source-registry.json exactly; no new taxonomy was invented. Patches: homepage, /architecture/ and SYSTEM_ARCHITECTURE.md (Engine/Tool layer marked Owned, route-count corrected 16 to 17), /signal-map/, /ai-reference/, /reference-pack/, data/reference-pack.json, data/page-index.json, llms.txt, sitemap.xml, and a Governed Classification Engine Gate in QUALITY_GATE.md. No DEC was created because the sprint operationalized the existing Classification Protocol without changing governance rules.

### F5 - Deep KSO Ontology Class Pages

Status: complete.

F5 built the `/ontology/` hub and ten deep KSO class pages (baseline, nutritional, fasting, exercise/performance, illness/stress, diabetes-associated, medication-context, laboratory-measurement, dka-concern-boundary, emergency-referral-boundary), turning the ontology from a governance spec into a citable reference structure. Each page follows the site's deep-reference pattern - governing rule (the class's own KSO constraint verbatim), definition, context map, an explicit "what it is not" distinction from adjacent classes, KSS relationship (reference labels only), boundary language, audience notes, source IDs, and an AI-readable summary - and uses DefinedTerm / DefinedTermSet plus BreadcrumbList structured data with no medical claims. The two boundary classes carry the strongest restraint: not diagnoses, no self-triage. Sources are reused from the existing registry; no new source was invented, and physiological classes without a matching registry source use concept language per SOURCE_POLICY.md. The Classification Engine now links each result to its class page: a `kso_class_page` was added to every rule in data/classification-rules.json (inline copy re-verified byte-identical), and the engine JS renders the KSO-class row as a link. Reconciliation moved the route count from 17 to 28: architecture/index.html and SYSTEM_ARCHITECTURE.md (Ontology layer marked Owned, new Ontology cluster and Cluster G, JSON-LD ItemList, counts), signal-map, ai-reference, homepage, data/kso-ontology.json (ontology_page per class), data/reference-pack.json, data/page-index.json, llms.txt, sitemap.xml, and a KSO Class Pages Gate in QUALITY_GATE.md. No DEC was created because F5 operationalized the existing ontology and internal-linking discipline without changing governance rules.

### F6 - Monetization Proof

Status: complete.

F6 added MONETIZATION_SPEC.md and the public /briefs/ page, turning the monetization layer from "boundary owned, proof pending" into a governed, demonstrable revenue path. /briefs/ presents a product catalog (each product traceable to a Permitted Monetization line in MONETIZATION_BOUNDARY.md), a deep flagship spec for the AI Reference Pack License built on the existing F1 machine layer, the "Supported by" sponsorship rule, a "what this is not" section mirroring the Prohibited list, and a plain inquiry surface routed to inquiry@ketonemia.com. The page is static: no store, checkout, payment processing, ads, or data-collection form, so it adds no security or personal-data surface; structured data is CollectionPage / BreadcrumbList with no Offer or price markup, so the asset is not misrepresented as an e-commerce store. Restricted categories (directories, lead generation, sponsored tools, device comparisons, provider listings, product-landscape pages) are explicitly deferred, and prohibited categories explicitly excluded. Reconciliation moved the route count from 28 to 29: architecture/index.html and SYSTEM_ARCHITECTURE.md (Monetization layer marked Owned, /briefs/ added to the Strategic cluster, JSON-LD ItemList, counts), strategic-availability (governed-revenue value-stack row and related link), homepage, data/reference-pack.json, data/page-index.json, llms.txt, sitemap.xml, and a Monetization Proof Gate in QUALITY_GATE.md. No DEC was created because F6 operationalized the existing monetization boundary without changing governance rules.

### F7 - Acquisition Dossier

Status: complete.

F7 built the final layer of the Asset Intelligence Factory. It added ACQUISITION_DOSSIER.md and the public /acquisition/ page: a structured, neutral account of the asset as a strategic acquisition - the owned-asset inventory (mirroring the layer stack), the moat with each line tied to the shipped artifact that proves it, the machine and reference footprints, the governance record, a cost-of-not-owning table for each of the eight priority buyer classes from BUYER_LOGIC.md, and the constraints an acquirer inherits. The dossier is an inventory of what exists: no price, no valuation, no forward-looking financial figure, no medical claim, and no data-collection form; it stays neutral (not a raw domain listing) and inside every existing boundary, with CollectionPage / BreadcrumbList structured data carrying no Offer or price. Reconciliation moved the route count from 29 to 30: architecture/index.html and SYSTEM_ARCHITECTURE.md (Buyer logic layer marked Owned, /acquisition/ added to the Strategic cluster, JSON-LD ItemList, counts, build order marked complete), ASSET_INTELLIGENCE_FACTORY_PLAN.md (F1-F7 sequence marked complete), strategic-availability and briefs (value-stack row and related links), homepage, data/reference-pack.json, data/page-index.json, llms.txt, sitemap.xml, and an Acquisition Dossier Gate in QUALITY_GATE.md. No DEC was created because F7 operationalized the existing buyer logic without changing governance rules. With F7 the F1-F7 build sequence is complete: every layer of the factory is owned and in production.

### F8 - Editorial Trust & Transparency Layer

Date: 2026-07-17

Status: complete.

F8 added EDITORIAL_TRUST_STANDARD.md and the public /trust/ page, deepening layer 8 (Governance) the way F5 deepened layer 3: it turned the source discipline and clinical-boundary preservation the asset already practices into a single visible, citable trust surface. /trust/ presents the trust contract (seven disciplines - sourcing, clinical boundary, independence, machine parity, corrections, privacy by architecture, governance record - each tied to the artifact that proves it), a "what this page claims and does not" table, how content is produced, the correction and change policy (neutral corrections@ketonemia.com, no form, no data collection), independence and funding, and privacy by architecture. Governing sentence: trust is a standard the asset holds to, not a badge it awards itself.

The honesty rule was the design constraint. The page and the standard document what the asset actually does and explicitly refrain from claiming what it does not: no page is claimed to have been individually reviewed or approved by a named clinician, no unheld credential or endorsement is asserted, and no unmeasured accuracy or trust metric is stated. EDITORIAL_TRUST_STANDARD.md fixes this as a governance rule: if independent expert review is ever added, it is published by name, credential, scope, and date on the reviewed page, never implied in the aggregate or claimed retroactively.

The page is static: no new script, form, third-party dependency, or data-collection surface, so it adds no security or personal-data surface. It adds no clinical content, threshold, or interpretation; structured data is CollectionPage / BreadcrumbList with no Offer, price, or medical claim. Reconciliation moved the route count from 30 to 31: architecture/index.html and SYSTEM_ARCHITECTURE.md (Governance layer "Where it lives" points to /trust/, /trust/ added to the Boundary & Sources cluster and Cluster D, JSON-LD ItemList extended to 31, counts, layer 8 marked deepened F8), ai-reference (Canonical Reference Pages and AI summary), acquisition/index.html and ACQUISITION_DOSSIER.md (Governance and moat rows point to the published trust standard; thirty → thirty-one), homepage card grid and footer, data/reference-pack.json (canonical page plus EDITORIAL_TRUST_STANDARD.md in governance documents), data/page-index.json, llms.txt, sitemap.xml, and an Editorial Trust Gate in QUALITY_GATE.md.

No DEC was created because F8 operationalized existing source, claim, clinical-boundary, and AI-reference discipline into a visible standard without changing a governance rule - with one rule made explicit for the future: expert review, if added, must be named, scoped, and dated, never implied.

## Open Decisions

- None at this time.
