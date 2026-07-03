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
