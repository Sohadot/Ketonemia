# Quality Gate

No page, tool, brief, or monetization surface should ship unless it passes this gate.

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
