# Quality Gate

No page, tool, brief, or monetization surface should ship unless it passes this gate.

The structural gates below — route-count reconciliation across the four route
lists, the source-of-truth count, JSON and inline JSON-LD validity, the
Classification Engine inline-rules byte-identity, the internal link graph, and
FAQ machine-human parity — are enforced automatically by
`scripts/verify_governance.py`, which runs on every push and pull request via
the **Verify governance invariants** workflow (`.github/workflows/verify-governance.yml`).
A regression fails the check and blocks the merge. The judgment gates (doctrine,
clinical boundary, source discipline, and the content-production gates) remain a
human responsibility; the machine check cannot read intent, only structure.

## Doctrine Gate

- Does it strengthen Blood Ketone Intelligence Infrastructure?
- Does it preserve "Ketonemia is a blood signal before it is a clinical verdict"?
- Does it classify signal context rather than diagnose?

## Clinical Boundary Gate

- Does it avoid diagnosis?
- Does it avoid treatment instruction?
- Does it avoid emergency triage?
- Does it avoid saying the reader is safe?
- Does high-risk language link to boundary pages?

## Source Gate

- Are medical claims sourced?
- Are thresholds sourced?
- Are source contexts preserved?
- Are manufacturer claims labeled?
- Are market claims dated and sourced?

## SEO Gate

- Is the page reference-grade?
- Does it avoid thinness?
- Does it have a unique strategic purpose?
- Does it link into the category graph?

## Deep Media Brief Gate

- Does the page have search-intent blocks, not only a generic article?
- Does it include a layer map separating molecule, measurement, metabolic state, urinary finding, and clinical syndrome?
- Does it include headline-risk analysis?
- Does it explain why wording choices are safer, not only which words to use?
- Does it have source-class logic, not only source IDs?
- Is it quote-ready without being clinically directive?
- Does it serve journalists, editors, health writers, AI systems, and strategic reviewers?
- Does it strengthen internal linking across definition, lab, student, research, boundary, sources, and AI layers?

## Agent-Readable Reference Layer Gate

- Do `/llms.txt`, `/robots.txt`, and `/sitemap.xml` exist?
- Do all `/data/*.json` files exist and parse as valid JSON?
- Does `/robots.txt` point to the sitemap, and does the sitemap include every canonical public page?
- Does `llms.txt` state both allowed and prohibited AI uses?
- Do the JSON files exclude diagnosis, triage, treatment guidance, safety or danger verdicts, and individualized interpretation?
- Do KSO and KSS JSON files match `KETONEMIA_SIGNAL_ONTOLOGY.md` and `KETONEMIA_STATE_STANDARD.md` exactly, without invented classes or thresholds?
- Does `source-registry.json` match the visible registry on `/sources/`?
- Is the machine-readable layer no looser than the human-facing site (`AI_REFERENCE_POLICY.md`)?
- Does `/ai-reference/` link to the machine-readable files, and does `/reference-pack/` document them?

## System Architecture Gate

- Does `/architecture/` present the asset as one system: layer stack, reference map, and audience paths?
- Does every public route appear on `/architecture/` exactly once, with no orphan and no broken link?
- Is the page built with existing CSS only, with no new CSS, no JS beyond JSON-LD, and no external assets?
- Does the structured data (CollectionPage, BreadcrumbList, ItemList) carry no medical claim, threshold, or verdict?
- Does the page preserve the clinical boundary — reference structure only, no diagnosis, triage, or interpretation?
- Do SYSTEM_ARCHITECTURE.md and ASSET_INTELLIGENCE_FACTORY_PLAN.md §2 agree on the layer stack?
- Are stale page counts and route lists reconciled across `/strategic-availability/`, sitemap, llms.txt, and page-index.json?

## Governed Classification Engine Gate

- Does `/classification-engine/` exist and is it deterministic (same inputs always produce the same output)?
- Is there no backend, no external API, and no tracking of any kind?
- Are there zero personal-medical input fields, zero numeric ketone values or thresholds, and zero symptom fields?
- Does every output avoid diagnosis, triage, treatment guidance, risk scoring, and safety/danger verdicts?
- Do outputs include KSO class, KSS language, boundary statement, canonical references, and source requirements?
- Do all KSO/KSS names in `data/classification-rules.json` match `data/kso-ontology.json` and `data/kss-standard.json` exactly, with no invented classes or labels?
- Do sensitive context combinations (diabetes + illness/stress, diabetes + medication) route to explicit clinical-concern-boundary language rather than a verdict?
- Does the page work meaningfully without JavaScript (a readable static explanation, not a broken form)?
- Does the mobile layout pass, do internal links pass, and does all JSON validate?
- Is the inline rules JSON in the page byte-identical to `data/classification-rules.json`?
- Are `llms.txt`, `sitemap.xml`, `data/page-index.json`, and `data/reference-pack.json` updated with the new route and file?
- Do `/architecture/`, `/ai-reference/`, and `/signal-map/` link to the engine, and are stale route counts corrected everywhere they appear?

## KSO Class Pages Gate

- Do the `/ontology/` hub and all ten class pages exist, one per KSO class?
- Is each class page deep, not thin: governing rule, definition, context map, a "what it is not" distinction, KSS relationship, boundary language, audience notes, and an AI-readable summary?
- Does every class page have at least three outgoing internal links and an incoming link from the `/ontology/` hub (no orphans)?
- Do all class names and KSS labels match `KETONEMIA_SIGNAL_ONTOLOGY.md` and `KETONEMIA_STATE_STANDARD.md` exactly, with no invented names?
- Do the boundary classes (DKA Concern, Emergency Referral) carry no diagnosis and no self-triage language, and route to professional care?
- Are all source IDs reused from the existing registry, never invented, with physiological classes using concept language where no source applies?
- Does the Classification Engine link each result to its class page, and does the inline rules JSON stay byte-identical to `data/classification-rules.json`?
- Is the route count reconciled to 28 everywhere it appears (architecture Layer Stack and AI summary, SYSTEM_ARCHITECTURE.md, JSON-LD ItemList), with every route in the Reference Map exactly once?
- Do all JSON files validate and does the sitemap contain the eleven new routes?

## Monetization Proof Gate

- Does every product on `/briefs/` come from the Permitted Monetization list in `MONETIZATION_BOUNDARY.md`, with no restricted or prohibited category offered?
- Is the page static with no store, checkout, payment processing, or data-collection form (no new security or personal-data surface)?
- Are there no on-site prices, and no "buy now" / cart / checkout language?
- Is there no advertising, affiliate content, paid ranking presented as neutral, or lead-generation funnel?
- Does any sponsorship language use "Supported by," never "recommended by," and never touch the clinical boundary or source discipline?
- Does the inquiry surface route to the existing neutral contact with no data collection?
- Does the structured data carry no `Product`, `Offer`, or price markup?
- Does the page preserve the clinical boundary (no diagnosis, triage, or device ranking)?
- Are route counts reconciled to 29 everywhere they appear, and do all JSON files validate?

## Acquisition Dossier Gate

- Does `/acquisition/` inventory what is owned, the moat, the footprints, the governance record, and the per-buyer-class cost of not owning the asset?
- Do the buyer classes match the priority list in `BUYER_LOGIC.md` exactly?
- Is there no price, valuation, or forward-looking financial figure anywhere on the page or in `ACQUISITION_DOSSIER.md`?
- Does the structured data carry no `Product`, `Offer`, or price markup?
- Is the tone neutral (not a raw domain listing), and does it carry no medical claim used as a determination?
- Is there no data-collection form, with inquiry routed to the existing neutral contact?
- Does the page state its distinct role from `/strategic-availability/` so the two do not read as duplicates?
- Are the route count (30) and the "Owned" status for layers 10 and 11 reconciled everywhere (architecture, SYSTEM_ARCHITECTURE.md, ASSET_INTELLIGENCE_FACTORY_PLAN.md), with no remaining "pending" language?
- Do all JSON files validate and does the sitemap contain `/acquisition/`?

## Editorial Trust Gate

- Does `/trust/` state the trust disciplines (sourcing, clinical boundary, independence, machine parity, corrections, privacy by architecture, governance record), each tied to the artifact that proves it?
- Is every claim on the page true and verifiable from the site or the public governance record — with nothing overstated?
- Does the page explicitly refrain from claiming individual clinician review, unheld credentials, endorsements, or any unmeasured accuracy metric?
- Does it preserve the clinical boundary: no diagnosis, threshold, triage, or interpretation of any individual reading?
- Is the correction path stated (neutral contact, no form, no data collection), with a defined triage → correct → record → version flow?
- Does the page add no new script, form, third-party dependency, or data-collection surface (static only)?
- Does `EDITORIAL_TRUST_STANDARD.md` govern the page, and do the two agree without drift?
- Is the route count reconciled to 31 everywhere it appears (architecture Layer Stack, AI summary, and JSON-LD ItemList; SYSTEM_ARCHITECTURE.md; `/acquisition/` and `ACQUISITION_DOSSIER.md`), with `/trust/` in the Boundary & Sources cluster exactly once?
- Are `sitemap.xml`, `llms.txt`, `data/page-index.json`, and `data/reference-pack.json` updated with the new route, and do all JSON files validate?

## Glossary Tool Gate

- Does `/glossary/` mirror `data/glossary.json` exactly (every term, layer, non-equivalent, clinical-boundary note, and canonical page), so the human page is never looser than the data?
- Is all glossary content present as static HTML (crawlable and AI-readable), with the client-side search only filtering what is already on the page?
- Is the tool static with no backend, no external API, no tracking, and no storage of any kind?
- Are there zero personal or numeric-value inputs (search over terminology only), and does it interpret no individual reading?
- Does every term preserve the clinical boundary (definitions only; no diagnosis, safety verdict, or treatment need)?
- Does each term link to its canonical reference page, and do all those links resolve?
- Is `/glossary/` registered in all four route lists (sitemap, page-index, reference-pack canonical_pages, architecture ItemList) and reconciled in the route count?

## Context Reference Linkage Gate

- Is `context_reference_page` a dedicated output field on every classification-engine rule whose KSO class has a dedicated public context page (fasting, nutritional, exercise, diabetes, medication), and absent on rules whose class has none (baseline, illness/stress, laboratory-only, and the boundary classes)?
- Does each rule's `context_reference_page` exactly match the `context_page` recorded for the same KSO class in `data/kso-ontology.json`, and does every such route resolve?
- Is `context_reference_page` kept out of the same rule's `canonical_references` (no duplication), and does the engine JS render it as its own labelled "Context reference" link?
- Is the exercise context selectable in the engine form and matched by a deterministic rule that routes to the Exercise / Performance Signal class and `/exercise-ketones/`?
- Does `CLASSIFICATION_PROTOCOL.md` list the context reference as a formal governed output?
- Does the inline rules JSON remain byte-identical to `data/classification-rules.json` after the change, and do all rules still validate as JSON?

## FAQ Gate

- Is every visible answer on `/faq/` boundary-safe: no numeric threshold, no safe/danger or normal-level verdict, no diagnosis, no triage, and no interpretation of an individual reading?
- Does each answer name a governed distinction and route to a canonical page that owns it, and do all those links resolve?
- Is the `FAQPage` JSON-LD `acceptedAnswer` text byte-identical to the visible answer text for every question (machine-human parity: the structured data is never looser than, nor divergent from, the human-facing answer)?
- Does the "normal or safe level" question decline to give a universal number and route the reader to a qualified professional?
- Are answers definitional and free of any new unsourced claim (they defer to already-sourced canonical pages), so the FAQ introduces no source not already governed?
- Is `/faq/` registered in all four route lists (sitemap, page-index, reference-pack canonical_pages, architecture ItemList) and reconciled in the route count, with reciprocal links from at least `/definition/` and `/glossary/`?

## Edge Hardening Gate

- Is there a custom `404.html` at the repository root that uses the site's layout and routes a lost visitor back to governed entry points, marked `noindex, follow`?
- Does the 404 page introduce no clinical content, verdict, or claim, and are all its links resolvable?
- Is `.well-known/security.txt` present and RFC 9116-shaped (Contact, Expires, Canonical at minimum), pointing only to a monitored channel the asset already publishes (no invented mailbox that could bounce)?
- Do the edge files stay out of the four route lists (they are not canonical pages) so the route count is unaffected?

## Content Production Gate

- What reference idea does this page prove?
- Which audience layer does it serve?
- What depth level is required?
- Which claims require sources?
- How does the page link back into the Ketonemia category rather than standing alone?
- Does the page include a clear definition, interpretation limits, internal links, source placeholders or citations, an AI-readable summary, and audience notes?
- Is the page useful to a human, legible to an AI system, credible to a specialist, and strategically meaningful to a buyer?

## Interface Gate

- Does the interface embody signal -> context -> boundary?
- Does it avoid decorative complexity?
- Does it provide accessible fallback?
- Does it avoid personal health data collection?

## Monetization Gate

- Does revenue preserve trust?
- Is sponsorship disclosed?
- Is the page free from hidden paid rankings?
- Does it avoid affiliate-first behavior?

## AI Gate

- Do summaries match the human-facing page?
- Are prohibited claims excluded?
- Are definitions consistent?
- Are canonical routes stable?
