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

### Content — Urine Ketones (Ketonuria)

Date: 2026-07-17

Status: complete.

Added `/urine-ketones/`, a deep public-reference and SEO pillar completing the measurement triad (blood / urine / breath). The page owns the blood-vs-urine distinction the category is built to preserve: a urine ketone strip measures mostly acetoacetate (AcAc) via the nitroprusside reaction, not the beta-hydroxybutyrate (BHB) measured in blood; it is time-lagged and semi-quantitative; and urine AcAc can under-represent rising blood BHB and stay positive during DKA resolution as BHB converts back to AcAc. Governing distinction: ketonemia is a blood measurement state, ketonuria is a urinary finding — same molecules, different measurement layer, different meaning.

Every claim is sourced from the existing registry only — SRC-LAB-BHB-ACAC (BHB/AcAc measure different fractions; urine lag and DKA-resolution discordance), SRC-LEHNINGER-BIOCHEM (BHB/AcAc interconversion), and SRC-NHS-DKA (public ketone guidance depends on diabetes context, symptoms, and measurement type). No new or invented source. The strip categories (negative / trace / small / moderate / large) are presented as the strip's own semi-quantitative reporting language, not as clinical severity, thresholds, or a diagnosis; clinical questions route to professional care. Structured data is WebPage with no medical claim, matching the measurement-cluster siblings.

Reconciliation moved the route count from 31 to 32: architecture/index.html and SYSTEM_ARCHITECTURE.md (`/urine-ketones/` added to the Measurement & Laboratory cluster / Cluster B, JSON-LD ItemList extended to 32, counts), blood-ketones and laboratory-context (Related Pages and AI summary linked pages), sources/index.html and data/source-registry.json (pages-using-source for the three cited sources), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-one → thirty-two), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing content-production, source-discipline, and clinical-boundary rules without changing a governance rule.

### Operations — GitHub Pages deployment

Date: 2026-07-17

Status: complete.

The default "pages build and deployment" builder was failing: GitHub Pages was configured to build from a `/docs` folder that does not exist, and it ran Jekyll against a plain static HTML site, attempting to convert a `jekyll-theme-primer` `assets/css/style.scss` the repository never had (`No such file or directory @ dir_chdir0 - /github/workspace/docs`). Ketonemia.com is a static HTML site served from the repository root — no `_config.yml`, no Gemfile, no `.scss`. Resolution: added `.github/workflows/deploy-pages.yml` (uploads the repository root and deploys it verbatim via `actions/upload-pages-artifact` + `actions/deploy-pages`, no Jekyll build) and `.nojekyll` (bypass Jekyll). The custom domain `ketonemia.com` was verified at the account level and attached; a root `CNAME` file pins it across Actions deploys. This required setting Settings → Pages → Source to "GitHub Actions". No DEC was created because this is a deployment-configuration fix, not a governance rule.

### Content — Breath Ketones (Breath Acetone)

Date: 2026-07-17

Status: complete.

Added `/breath-ketones/`, completing the measurement triad (blood / urine / breath). A breath ketone analyzer measures exhaled acetone — formed largely by spontaneous decarboxylation of acetoacetate and exhaled because it is volatile — as a non-invasive proxy for ketone state, not the beta-hydroxybutyrate (BHB) measured in blood. The page anchors the third ketone body to its measurement layer and preserves the governing distinction: blood measures BHB as a number, urine measures AcAc as a category, breath measures acetone as a proxy. It presents a three-layer comparison table, sensor-proxy measurement, why breath correlates with but does not equal a blood value, a context table, limits, audience notes, source IDs, and an AI-readable summary.

Every claim is sourced from the existing registry only — SRC-LEHNINGER-BIOCHEM (acetone as a ketone body from spontaneous decarboxylation of acetoacetate, and its volatility) and SRC-LAB-BHB-ACAC (measurement across fractions and methods; primacy of blood BHB for clinical monitoring). No new or invented source, no numeric thresholds, and no clinical-decision use: the page routes acute concern to blood measurement and professional care. Structured data is WebPage with no medical claim, matching the measurement-cluster siblings.

Reconciliation moved the route count from 32 to 33: architecture/index.html and SYSTEM_ARCHITECTURE.md (`/breath-ketones/` added to the Measurement & Laboratory cluster / Cluster B, JSON-LD ItemList extended to 33, counts), blood-ketones, urine-ketones, and laboratory-context (Related Pages and AI summary linked pages), sources/index.html and data/source-registry.json (pages-using-source for the two cited sources), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-two → thirty-three), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing content-production, source-discipline, and clinical-boundary rules without changing a governance rule. With this the measurement triad is fully owned.

### Content — Ketone Bodies

Date: 2026-07-17

Status: complete.

Added `/ketone-bodies/`, the foundational biochemistry hub anchoring the measurement triad. It defines the three ketone bodies — beta-hydroxybutyrate (BHB), acetoacetate (AcAc), and acetone — describes hepatic ketogenesis and their role as fuel, and maps each compound to the measurement layer that reads it (blood → BHB, urine → AcAc, breath → acetone), tying the blood/urine/breath pages together under one parent concept. Governing idea: there is no single "ketone"; there are three ketone bodies, and which one you measure depends on how you measure. It includes a naming note (BHB is chemically a hydroxy acid grouped with ketones by biochemical convention) and states plainly that ketone-body presence is a normal fuel, is not a disease, and does not equal ketoacidosis.

Every claim is sourced from the existing registry only — SRC-LEHNINGER-BIOCHEM (ketogenesis, the three ketone bodies, BHB/AcAc interconversion, acetone from decarboxylation, and the convention that BHB is a ketone body) and SRC-STRYER-BIOCHEM (ketone-body synthesis and utilization, BHB as a peripheral energy substrate). No new or invented source, no thresholds, no clinical claim; structured data is WebPage with no medical claim.

Reconciliation moved the route count from 33 to 34: architecture/index.html and SYSTEM_ARCHITECTURE.md (`/ketone-bodies/` added to the Measurement & Laboratory cluster / Cluster B, JSON-LD ItemList extended to 34, counts), beta-hydroxybutyrate, blood-ketones, and laboratory-context (Related Pages and AI summary linked pages), sources/index.html and data/source-registry.json (pages-using-source for the two cited sources), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-three → thirty-four), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing content-production, source-discipline, and clinical-boundary rules without changing a governance rule.

### Content — Fasting Ketones (new Cluster H)

Date: 2026-07-17

Status: complete.

Added `/fasting-ketones/`, the first page of a new Route Map cluster, **Metabolic & Clinical Context** (Cluster H) — the public-facing, SEO-facing counterparts to the KSO context classes. The page explains why blood ketones rise during fasting: as glucose and insulin fall, the liver shifts to hepatic ketogenesis and BHB rises as an alternative fuel for the brain and peripheral tissues. Governing distinction: fasting is a driver of the signal, ketonemia is the blood measurement; a fasting rise is usually expected, but "expected" describes context, not a clinical clearance. It distinguishes fasting ketones from nutritional ketosis, from ketoacidosis, and from a single interchangeable number, and it preserves the boundary for people with diabetes, on medications such as SGLT2 inhibitors, who are ill or pregnant, or undertaking prolonged fasts.

Every claim is sourced from the existing registry only — SRC-LEHNINGER-BIOCHEM (hepatic ketogenesis and the fasting metabolic shift) and SRC-STRYER-BIOCHEM (ketone bodies as an energy substrate during fasting and starvation). No new or invented source, deliberately no numeric thresholds and no fasting-duration advice; fasting ketosis is never equated with ketoacidosis and no individual reading is declared safe. Structured data is WebPage with no medical claim.

This is the first cluster added since F5 introduced the Ontology cluster (Cluster G). Reconciliation moved the route count from 34 to 35 and the cluster count from seven to eight: architecture/index.html and SYSTEM_ARCHITECTURE.md (new Cluster H "Metabolic & Clinical Context" seeded with `/fasting-ketones/`, JSON-LD ItemList extended to 35, route and cluster counts, Route clusters list), ketonemia-vs-ketosis and ontology/fasting-signal (Related Pages and AI summary linked pages), sources/index.html and data/source-registry.json (pages-using-source for the two cited sources), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-four → thirty-five routes, seven → eight clusters), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page and the new cluster applied existing content-production, source-discipline, internal-linking, and clinical-boundary rules without changing a governance rule.

### Content — Nutritional Ketosis (Cluster H)

Date: 2026-07-17

Status: complete.

Added `/nutritional-ketosis/`, the second page of the Metabolic & Clinical Context cluster (Cluster H) and the highest-volume search term in the category. It defines nutritional ketosis as a diet-driven metabolic state — sustained low-carbohydrate intake keeps insulin low and maintains hepatic ketogenesis, elevating ketone bodies (primarily BHB) as fuel — and holds three distinctions the category depends on: the state is not the blood measurement (ketonemia), it is the same physiology as fasting ketosis driven by diet rather than absence of food, and it is emphatically not ketoacidosis (a clinical syndrome, not a diet state).

This is the highest keto-hype-risk topic on the site, so it was handled with the strictest framing: no diet advice, no "how to get into ketosis," no macro or food-list guidance, no health-benefit or weight-loss claims, no exogenous-ketone or supplement promotion, and no numeric thresholds (consistent with the fasting-ketones precedent). Sources are reused from the registry only — SRC-LEHNINGER-BIOCHEM and SRC-STRYER-BIOCHEM (ketogenesis and ketone bodies as fuel) and SRC-NHS-DKA (public framing that interpretation is context-dependent and that ketoacidosis is a clinical emergency, not a diet state). Structured data is WebPage with no medical claim.

Reconciliation moved the route count from 35 to 36 (cluster count unchanged at eight): architecture/index.html and SYSTEM_ARCHITECTURE.md (`/nutritional-ketosis/` added to Cluster H, now two pages; JSON-LD ItemList extended to 36; counts), ketonemia-vs-ketosis, fasting-ketones, and ontology/nutritional-signal (Related Pages and AI summary linked pages), sources/index.html and data/source-registry.json (pages-using-source for the three cited sources), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-five → thirty-six), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing content-production, source-discipline, and clinical-boundary rules without changing a governance rule.

### Consistency — Route-Set Symmetry Hardening

Date: 2026-07-17

Status: complete.

Resolved two internal-consistency observations in the machine layer (non-blocking; no deploy, SEO, or Search Console impact) by making the canonical route set identical across every surface.

Before: three route lists each silently excluded a different page. `data/reference-pack.json` `canonical_pages` (36) omitted `/reference-pack/`; the `/architecture/` JSON-LD `hasPart` ItemList (36) omitted `/architecture/` itself; `/sitemap.xml` and `data/page-index.json` listed all 37. The stated route count (36) therefore undercounted the true total (37) and the two "36" lists held different members.

After: the canonical route set is a single 37-route source of truth (every page except home `/`), and all four lists — `sitemap.xml` (minus home), `data/page-index.json` (minus home), `data/reference-pack.json` `canonical_pages`, and the `/architecture/` `hasPart` ItemList — are now byte-verified as the identical 37-member set. Changes: added `/reference-pack/` to `canonical_pages`; added `/architecture/` to its own Reference Map (a card in the Strategic cluster, matching SYSTEM_ARCHITECTURE Cluster F, which already listed it) and to the `hasPart` ItemList (position 37) and AI summary; corrected the count from 36 to 37 on `/architecture/` (layer stack), `SYSTEM_ARCHITECTURE.md` (layer 7), and the acquisition surfaces. `SYSTEM_ARCHITECTURE.md` now records the architecture rule that the 37-route count is the single source of truth and that no canonical route — including `/architecture/` and `/reference-pack/` — may be silently excluded from any list.

The second observation (whether `/architecture/` should appear in its own map) is resolved by inclusion: it is now carded as "the container page that renders every route on one page," so the map is complete and self-consistent rather than relying on an undocumented exception.

No DEC was created because this hardened existing internal-linking and machine-parity discipline without changing a governance rule; it makes the "machine layer is never looser than the human site" guarantee exact.

### Content — SGLT2 Inhibitors & Ketones (Cluster H)

Date: 2026-07-17

Status: complete.

Added `/sglt2-context/`, the clinical/medication dimension of the Metabolic & Clinical Context cluster (Cluster H) and the site's highest-authority safety topic. It explains why one class of diabetes medication changes ketone-signal interpretation: regulatory safety communication warns that SGLT2 inhibitors are associated with ketoacidosis, including presentations where blood glucose is not markedly elevated ("euglycemic"). Governing distinction: on an SGLT2 inhibitor, a normal glucose reading does not by itself rule out a ketone-related concern, so the medication context must stay attached to the reading.

This is the highest clinical-sensitivity page on the site, so it carries the strictest boundary of any content page: it gives no medication advice, no dosing or start/stop/adjust guidance, no diagnosis or triage, no sick-day rules, no numeric thresholds, and no product naming or ranking. It opens and closes with an explicit instruction never to change a prescribed medication on one's own, and routes every individual question to professional care or urgent care. Sources are reused from the registry only — SRC-FDA-SGLT2 (the regulatory warning about ketoacidosis risk without marked hyperglycemia), SRC-ADA-2026 (standards of care), and SRC-NHS-DKA (public emergency framing). Structured data is WebPage with no medical claim, and deliberately not MedicalWebPage or any calculator/risk type.

Reconciliation moved the route count from 37 to 38 (cluster count unchanged at eight), keeping all four route lists identical per the source-of-truth rule: architecture/index.html and SYSTEM_ARCHITECTURE.md (`/sglt2-context/` added to Cluster H, now three pages; JSON-LD ItemList extended to 38; counts and the source-of-truth line updated to 38), ketonemia-vs-ketoacidosis, ontology/medication-context-signal, fasting-ketones, and nutritional-ketosis (Related Pages, AI summaries, and inline SGLT2 links), sources/index.html and data/source-registry.json (pages-using-source for the three cited sources), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-seven → thirty-eight), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing source-discipline, clinical-boundary, and medication-context rules without changing a governance rule.

### Content — Diabetes & Blood Ketones (Cluster H)

Date: 2026-07-17

Status: complete.

Added `/diabetes-ketone-context/`, the fourth Metabolic & Clinical Context page. A deliberate scope decision drove it: rather than a generic `/diabetes/` page, the page is the *diabetes ketone context* — how the diabetes context changes interpretation of a blood ketone signal — keeping depth aligned with the asset's name (blood ketone intelligence) instead of drifting into a general diabetes site. It explains why the diabetes context is the strongest modifier of ketone interpretation: insulin insufficiency can drive rapid ketone production even with high glucose, the pathway toward diabetic ketoacidosis (DKA), a medical emergency. Governing distinction: diabetes changes what a ketone signal may mean, not what a ketone is; ketone presence is still not a diagnosis, but the context raises the stakes of interpretation and timing.

This is the most clinically sensitive context page on the site, so it carries the strictest boundary: no diagnosis or triage, no safety/danger verdicts, no ketone or glucose thresholds, no sick-day rules (it defers explicitly to the reader's own diabetes care team's plan), and no insulin or medication advice. It routes warning symptoms to the sick-day plan and urgent care, states plainly that DKA is a medical emergency, and holds the core boundary that a home reading cannot confirm or exclude DKA. Sources are reused from the registry only — SRC-ADA-2026, SRC-DUK-DKA, and SRC-NHS-DKA. Structured data is WebPage with no medical claim.

Reconciliation moved the route count from 38 to 39 (cluster count unchanged at eight), keeping all four route lists identical per the source-of-truth rule: architecture/index.html and SYSTEM_ARCHITECTURE.md (`/diabetes-ketone-context/` added to Cluster H, now four pages; JSON-LD ItemList extended to 39; counts and the source-of-truth line updated to 39), ketonemia-vs-ketoacidosis, sglt2-context, and ontology/diabetes-associated-signal (Related Pages and AI summaries), sources/index.html and data/source-registry.json (pages-using-source for ADA, Diabetes UK, and NHS), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-eight → thirty-nine), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing source-discipline, clinical-boundary, and context-scoping rules without changing a governance rule. The scope decision (diabetes ketone context, not generic diabetes) is an application of the existing doctrine that every page must serve the category thesis, recorded here for traceability.

### Content — Exercise & Blood Ketones (Cluster H)

Date: 2026-07-17

Status: complete.

Added `/exercise-ketones/`, the fifth Metabolic & Clinical Context page, completing the metabolic side of the cluster (fasting, nutritional, exercise) alongside the clinical side (SGLT2, diabetes). It explains why exercise changes blood ketone levels — lower carbohydrate availability during prolonged, fasted, or low-carbohydrate exercise shifts fuel toward fat and raises ketogenesis, and BHB can itself serve as fuel — and why a reading around exercise is context-dependent (timing, feeding state, intensity, duration, diet background). Governing distinction: exercise is a context that shapes the signal, not a claim about it; a reading reflects fuel metabolism, not benefit, a performance metric, or a diagnosis.

The topic's principal risks are performance hype and supplement promotion, so the page makes no claim that ketones improve or impair performance (in either direction), treats no reading as a performance or fitness metric, and includes an explicit note that exogenous ketone products are a separate topic which the page does not assess or endorse. It attaches no numeric thresholds and preserves diabetes/medication context (linking to /sglt2-context/) where relevant. This mirrors the guardrail already stated on the exercise/performance KSO class. Sources are reused from the registry only — SRC-LEHNINGER-BIOCHEM and SRC-STRYER-BIOCHEM. Structured data is WebPage with no medical claim.

Reconciliation moved the route count from 39 to 40 (cluster count unchanged at eight), keeping all four route lists identical per the source-of-truth rule: architecture/index.html and SYSTEM_ARCHITECTURE.md (`/exercise-ketones/` added to Cluster H, now five pages; JSON-LD ItemList extended to 40; counts and the source-of-truth line updated to 40), fasting-ketones, nutritional-ketosis, and ontology/exercise-performance-signal (Related Pages and AI summaries), sources/index.html and data/source-registry.json (pages-using-source for the two cited sources), acquisition/index.html and ACQUISITION_DOSSIER.md (thirty-nine → forty), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing content-production, source-discipline, and clinical-boundary rules without changing a governance rule.

### Deepening — Context Loop-Closure (structure ↔ context pages)

Date: 2026-07-17

Status: complete.

A vertical deepening rather than a new page: after the Metabolic & Clinical Context cluster reached five deep public context pages (fasting, nutritional, exercise, diabetes, SGLT2), the abstract context structures did not yet point to them. This change closes that loop on both the machine and human sides, so the ontology and the conceptual interface route into the deep public reference, and the machine layer's context representation is no looser than the human layer.

Machine side — `data/kso-ontology.json`: added a `context_page` field (mirroring the existing `ontology_page` pattern) to the five KSO classes that now have a dedicated public context page — KSO-2 Nutritional → `/nutritional-ketosis/`, KSO-3 Fasting → `/fasting-ketones/`, KSO-4 Exercise/Performance → `/exercise-ketones/`, KSO-6 Diabetes-Associated → `/diabetes-ketone-context/`, KSO-7 Medication-Context → `/sglt2-context/`. Laboratory Measurement (KSO-8) already carries `/laboratory-context/` as its `canonical_page`, and the boundary/baseline/illness classes have no dedicated public context page, so they were left unchanged. The file `updated` date advanced to 2026-07-17.

Human side — `/signal-map/`: enriched the "See also" links on the matching context-dimension cards (Fasting → fasting + exercise ketones; Nutritional Ketosis → nutritional-ketosis; Diabetes → diabetes-ketone-context; Medication → sglt2-context) and added a "Context reference pages" row to the AI-readable summary listing all five.

No routes were added, so the four-route-list source of truth is unchanged at 40 and remains byte-identical. No new source was introduced and no boundary changed. No DEC was created because this operationalized existing internal-linking and machine-parity discipline without changing a governance rule.

### Deepening — Engine Loop-Closure (classification engine ↔ context pages)

Date: 2026-07-17

Status: complete.

The second half of the loop-closure: after linking the KSO ontology and Signal Map to the deep public context pages, the operational tool — the Classification Engine — did not yet route to them. This change makes the engine's output point to the matching public context reference, so a user (or agent) who classifies a context is handed the deep page for it.

For the four non-sensitive context rules whose KSO class has a dedicated public context page, the matching page was added as the first entry of the rule's existing `output.canonical_references` array — RULE-FASTING-BLOOD → `/fasting-ketones/`, RULE-NUTRITIONAL-BLOOD → `/nutritional-ketosis/`, RULE-DIABETES-ALONE → `/diabetes-ketone-context/`, RULE-MEDICATION-ALONE → `/sglt2-context/`. The two sensitive combinations (diabetes+illness, diabetes+medication) route to the DKA Concern Boundary class, which has no context page, and were left unchanged to preserve their deliberate clinical restraint; their boundary and prohibited-inference language is untouched.

Because `canonical_references` is already rendered by the engine (`assets/js/classification-engine.js`), no JavaScript logic changed — the new links appear automatically. Both `data/classification-rules.json` and the inline copy embedded in `/classification-engine/` were edited together and re-verified byte-identical, per the engine gate. No rule matching, boundary statement, KSO/KSS label, or source was changed; no route was added, so the four-route-list source of truth remains 40. No DEC was created because this operationalized existing internal-linking and machine-parity discipline without changing a governance rule.

### Tool — Interactive Glossary (retention as reference gravity)

Date: 2026-07-17

Status: complete.

Added `/glossary/`, the second operational tool on the site and a deliberate answer to the question of repeat-usage tools. Owner decision: the asset's retention model is "reference gravity" — being the default place people and AI systems return to look terminology up — not the consumer-app engagement loop. Tools that require accounts, tracking, personalization, saved state, notifications, or interpretation of a personal value are rejected, because they would break privacy-by-architecture, neutrality, and the clinical boundary, which are the source of the asset's value and acquirability. A glossary lookup drives return visits entirely inside that boundary.

The page is a searchable, client-side glossary generated to mirror `data/glossary.json` exactly (14 terms, each with measurement layer, non-equivalents, clinical-boundary note, and canonical reference), so the human page is never looser than the data. All content is static HTML (crawlable and AI-readable); the JavaScript (`assets/js/glossary.js`, vanilla, no network/storage/tracking) only filters what is already on the page, so the tool works without JS. There are no personal or numeric-value inputs — search is over terminology only — and it interprets no individual reading. Scoped `.glossary-*` CSS reuses existing variables, mirroring the F4 engine precedent. Structured data is `DefinedTermSet` with no medical claim.

Reconciliation moved the route count from 40 to 41 (cluster count unchanged at eight), keeping all four route lists identical per the source-of-truth rule: architecture/index.html and SYSTEM_ARCHITECTURE.md (`/glossary/` added to the Definition & Comparison cluster; JSON-LD ItemList extended to 41; counts and the source-of-truth line updated to 41), reference-pack (glossary.json now points to `/glossary/` as its human view), student-guide (Reference Pathways), acquisition/index.html and ACQUISITION_DOSSIER.md (forty → forty-one), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml. A Glossary Tool Gate was added to QUALITY_GATE.md.

No DEC was created because the tool operationalized existing content-production, machine-parity, privacy, and clinical-boundary rules without changing a governance rule; the retention-model decision (reference gravity, no engagement loops) is an application of the existing doctrine and monetization/interface boundaries, recorded here for traceability.

### Engine Upgrade — Context Reference as a Formal Output

Date: 2026-07-17

Status: complete.

Closed four gaps identified in review of the engine loop-closure, completing and formalizing the engine ↔ context-page link.

1. Exercise context in the engine: added an "Exercise / performance" option to the engine form and a deterministic rule `RULE-EXERCISE-BLOOD` (blood + BHB + exercise context) routing to the Exercise / Performance Signal class, `/ontology/exercise-performance-signal/`, and `/exercise-ketones/`. The rule set is now 16 rules (was 15). The rule mirrors the fasting/nutritional pattern; the boundary and prohibited-inference language is the constant boundary text plus the exercise-specific "do not infer that ketones improve or impair performance."

2. `context_reference_page` as a dedicated field: previously the context page had been added into `canonical_references`. It is now its own output field (mirroring `kso_class_page`) on the five context rules — RULE-FASTING-BLOOD, RULE-NUTRITIONAL-BLOOD, RULE-EXERCISE-BLOOD, RULE-DIABETES-ALONE, RULE-MEDICATION-ALONE — and removed from those rules' `canonical_references` to avoid duplication. The engine JS renders it as its own "Context reference" link, immediately after the KSO class row. Each rule's `context_reference_page` matches the `context_page` for the same KSO class in `data/kso-ontology.json`.

3. CLASSIFICATION_PROTOCOL.md now lists the context reference as a formal governed output, states it must match the ontology `context_page`, notes that classes without a public page (baseline, illness/stress, boundary classes) omit it, and adds it to the output chain (Observed context → KSO class → context reference → KSS zone language → boundary statement → canonical references → source requirements).

4. QUALITY_GATE.md gained a Context Reference Linkage Gate verifying the field's presence/absence rules, the ontology match, no duplication in canonical_references, the exercise rule, the protocol listing, and inline byte-identity.

Discipline: `data/classification-rules.json` and the inline copy in `/classification-engine/` were edited together and re-verified byte-identical; the constant boundary statement and sensitive-combination handling (diabetes+illness, diabetes+medication route to DKA Concern Boundary, no context reference) are unchanged; no KSO/KSS label or source was invented (KSS uses the existing "K2 — Nutritional / Fasting Range"); no route was added (four route lists stay 41). The engine page prose and AI-summary Outputs line were updated to describe the current template. No DEC was created because this operationalized the existing protocol and machine-parity discipline without changing a governance rule.

### Content — Illness & Blood Ketones (completes context-class coverage)

Date: 2026-07-17

Status: complete.

Added `/illness-ketones/`, completing the Metabolic & Clinical Context cluster and public-page coverage of every non-boundary KSO context class. The review that closed the engine-context gaps also surfaced that the illness / stress class (KSO-5) was the last selectable engine context and citable ontology class without its own public reference page. This page closes that and extends the engine loop to it. It explains why illness raises ketones (reduced intake layered on stress-driven ketogenesis, plus vomiting and dehydration), why the context changes the reading (highest-stakes in diabetes), and holds the boundary that ketone presence during illness is still not a diagnosis and does not by itself mean ketoacidosis.

Engine loop extension: `data/kso-ontology.json` KSO-5 now carries `context_page: /illness-ketones/`, and `RULE-ILLNESS-ALONE` in `data/classification-rules.json` (and the byte-identical inline copy) now carries `context_reference_page: /illness-ketones/`, matching the ontology. Six of sixteen rules now carry a context reference; the two sensitive combinations still route to the DKA Concern Boundary class with no context reference, unchanged.

Highest-sensitivity handling: no diagnosis or triage, no safety/danger verdicts, no sick-day rules (defers to the reader's own care team), no thresholds, no treatment advice; the page routes worrying symptoms to urgent care and frames DKA as a medical emergency. Sources reused only — SRC-LEHNINGER-BIOCHEM, SRC-NHS-DKA, SRC-DUK-DKA. Structured data is WebPage with no medical claim.

Reconciliation moved the route count from 41 to 42 (cluster count unchanged at eight), keeping all four route lists identical: architecture/index.html and SYSTEM_ARCHITECTURE.md (Cluster H now six pages; JSON-LD ItemList extended to 42; counts and source-of-truth line updated to 42), signal-map (Context 4 and AI summary context-reference list) and ontology/illness-stress-signal (Related Pages), sources/index.html and data/source-registry.json (pages-using-source for LEHNINGER, NHS, DUK; registry date advanced), acquisition/index.html and ACQUISITION_DOSSIER.md (forty-one → forty-two), homepage card grid, data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page and the engine-loop extension applied existing content-production, source-discipline, machine-parity, and clinical-boundary rules without changing a governance rule.

### Content — Blood Ketone FAQ (governed answer layer, GEO surface)

Date: 2026-07-18

Status: complete.

Added `/faq/`, a governed FAQ answer layer in Cluster A (Definition & Comparison). It captures the highest-intent natural-language questions people and AI assistants actually ask about blood ketones and answers each one within the clinical boundary, routing every answer to the canonical page that governs it. This is a generative-engine-optimization (GEO) surface: it makes the site's governed distinctions directly retrievable as question-answer pairs, both for humans and for AI systems that prefer FAQPage structured data.

Eight questions, each boundary-safe: what ketonemia is; ketonemia vs. ketoacidosis; whether having ketones means something is wrong; what a "normal or safe" level is (the answer refuses a universal number and routes the reader to a clinician — no threshold, no verdict); what raises blood ketones; whether blood/urine/breath ketones are the same; ketonemia vs. ketosis; and whether the site can interpret an individual reading (no). Each visible answer links to its canonical page (`/definition/`, `/ketonemia-vs-ketoacidosis/`, `/ketone-bodies/`, `/clinical-boundary/`, `/signal-map/`, `/ketonemia-vs-ketosis/`).

Machine-human parity: the page carries `FAQPage` JSON-LD whose `acceptedAnswer` text is byte-identical to the visible answer text (verified programmatically), so the structured data is never looser than — nor divergent from — the human-facing content, satisfying both the editorial trust standard and FAQPage rich-result eligibility. No new source was cited (answers are definitional and defer to already-sourced canonical pages); no numeric threshold, safe/danger verdict, diagnosis, triage, or individual interpretation appears in any answer.

Reconciliation moved the route count from 42 to 43 (cluster count unchanged at eight), keeping all four route lists identical (verified: sitemap, page-index, reference-pack canonical_pages, and the architecture JSON-LD ItemList all 43): architecture/index.html and SYSTEM_ARCHITECTURE.md (Cluster A now carries `/faq/`; JSON-LD ItemList extended to 43; counts and source-of-truth line updated to 43), homepage card, acquisition/index.html and ACQUISITION_DOSSIER.md (forty-two → forty-three), reciprocal links added from `/definition/` and `/glossary/` (Related Pages grid and AI-summary linked-pages row), data/reference-pack.json, data/page-index.json, llms.txt, and sitemap.xml.

No DEC was created because the page applied existing content-production, machine-parity, and clinical-boundary rules without changing a governance rule.

### Governance — Automated invariant enforcement (CI)

Date: 2026-07-18

Status: complete.

Converted the structural governance discipline from a manual routine into an automated, merge-blocking check. Every reconciliation and machine-parity invariant that had been verified by hand on each change is now encoded in `scripts/verify_governance.py` and run on every push and pull request by a new GitHub Actions workflow, `.github/workflows/verify-governance.yml` (**Verify governance invariants**).

The script asserts: (1) the four route lists — `sitemap.xml`, `data/page-index.json`, `data/reference-pack.json` `canonical_pages`, and the `/architecture/` JSON-LD `hasPart` ItemList — are the identical set of canonical routes; (2) that count equals the source-of-truth number declared in `SYSTEM_ARCHITECTURE.md`; (3) every canonical route is discoverable in `llms.txt`; (4) every `data/*.json` file is valid JSON; (5) every inline JSON-LD block on every page is valid; (6) the Classification Engine's inline rules are equal to `data/classification-rules.json`; (7) no internal link is broken; (8) each FAQPage `acceptedAnswer` is byte-identical to its visible answer. It exits non-zero with precise diagnostics on any violation.

Verified both directions: the script passes on the current tree, and a negative test (removing one route from `sitemap.xml` only) makes it fail with an exact diff and a source-of-truth mismatch. `QUALITY_GATE.md` now records which gates are machine-enforced versus which remain human judgment (doctrine, clinical boundary, source discipline, content production — the machine cannot read intent, only structure); `SYSTEM_ARCHITECTURE.md`'s Architecture Rule notes the automated enforcement.

No DEC was created because this operationalized existing reconciliation and machine-parity rules — it changed how they are enforced, not what they require. It adds no canonical route (the script is tooling, not a page), so the route count stays 43.

## Open Decisions

- None at this time.
