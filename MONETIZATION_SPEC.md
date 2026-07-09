# Monetization Spec

This document operationalizes [MONETIZATION_BOUNDARY.md](MONETIZATION_BOUNDARY.md).
The boundary says what revenue is permitted; this spec defines the actual products,
how each one extends the reference layer, and the hard rules that keep revenue from
touching trust.

Governing sentence:

**Revenue must extend trust, not replace it.**

The public expression of this spec is [`/briefs/`](briefs/index.html). Where the two
differ in detail, this document governs; where either conflicts with
[MONETIZATION_BOUNDARY.md](MONETIZATION_BOUNDARY.md) or
[CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md), the boundary and the clinical boundary win.

---

## What a Governed Product Is

A governed product is an **output of the reference layer**, sold or licensed without
lowering the neutrality, source discipline, or clinical boundary that make the asset
trustworthy. It is not advertising, not lead generation, and not a store.

Every product must answer yes to all of:

- Does it come from the Permitted Monetization list in `MONETIZATION_BOUNDARY.md`?
- Does it extend the reference layer rather than dilute it?
- Does it preserve the clinical boundary (no diagnosis, triage, endorsement, or ranking)?
- Does it keep source discipline (claims sourced or framed as concept language)?
- Would a clinical, institutional, or AI buyer still trust the asset after seeing it?

If any answer is no, it is not built.

---

## Product Catalog

Each product maps to a line in the Permitted Monetization list.

| Product | Permitted-list basis | What it contains | Who it serves | Boundary preserved |
| --- | --- | --- | --- | --- |
| **AI Reference Pack License** (flagship) | AI reference packs; licensed glossary or taxonomy data | The governed machine layer: glossary, KSO ontology, KSS standard, source registry, page index, classification rules | Health-AI systems, agent platforms, medical-reference tools | Licensee may not present it as diagnosis, endorsement, or ranking; output stays no looser than the human site |
| **Blood Ketone Measurement Landscape Brief** | blood ketone measurement landscape reports | A neutral reference on measurement methods, substrates, and device/method variation, with manufacturer material clearly labeled | Diagnostics, monitoring, and metabolic-health teams; analysts | No device ranking, no endorsement; manufacturer sources labeled, not treated as neutral guidance |
| **Category Brief** | premium category briefs; educational briefs | A governed explainer of a category topic (e.g. ketonemia vs. ketoacidosis language) for institutional education | Clinical educators, publishers, communicators | Educational framing only; no individualized advice |
| **Signal Map / Taxonomy Licensing** | embeddable signal map licensing; licensed glossary or taxonomy data | Embeddable Signal Map or licensed KSO/KSS terminology for a partner surface | Platforms, education providers | The clinical boundary and prohibited inferences travel with the license |
| **Institutional Education Partnership** | institutional education partnerships; clearly disclosed sponsored reference sections | Co-developed or supported educational layers, disclosed with "Supported by" | Institutions, education providers | Sponsorship never touches the clinical boundary or source discipline |

Restricted categories (directories, lead generation, sponsored tools, device
comparisons, provider listings, product landscape pages) are **not** offered here;
they require the explicit review named in `MONETIZATION_BOUNDARY.md` before any use.

---

## Flagship Spec: AI Reference Pack License

The strongest first product, because it already exists and is boundary-safe by
construction.

- **What it is.** A license to use the governed machine-readable reference layer built
  in the agent-readable sprint: `/data/glossary.json`, `/data/kso-ontology.json`,
  `/data/kss-standard.json`, `/data/source-registry.json`, `/data/page-index.json`,
  and `/data/classification-rules.json`, documented at `/reference-pack/`.
- **What the licensee gets.** A versioned, agent-readable taxonomy and standard for
  blood ketone signal language, with allowed and prohibited claim patterns, source
  IDs, and the clinical boundary encoded in the data.
- **Governance it inherits.** The pack is never looser than the human-facing site
  (`AI_REFERENCE_POLICY.md`): if a claim is prohibited on the pages, it is prohibited
  in the license. Every claim traces to a canonical page and, where medical, to a
  source ID.
- **Versioning.** Each file carries a version and update date; changes are additive and
  reviewable, so a licensee can pin a version and track changes.
- **The boundary the licensee must keep.** The pack may be used to define, compare, and
  bound terminology. It may not be presented as a diagnosis tool, a risk score, a
  device endorsement, or a ranking, and it may not be made looser than the source.

---

## Inquiry Mechanism

Product, licensing, and sponsorship inquiries use the same neutral contact as
`/strategic-availability/`: **inquiry at ketonemia.com**. An inquiry describes the
organization, the intended use, and the engagement model. There is no on-site store,
no checkout, no payment processing, and no data-collection form; the inquiry surface
is a plain contact, not a lead-generation funnel.

---

## Hard Rules

- **No prices on-site.** Pricing is handled in inquiry, not published, so the asset
  reads as category infrastructure, not a store.
- **No payment processing** and **no data-collection forms** on the asset (no PCI or
  personal-data surface).
- **No ads, affiliate content, or paid rankings presented as neutral.**
- **Sponsorship uses "Supported by," never "recommended by"** unless a formal
  endorsement framework exists (Sponsorship Rule).
- **Sponsorship never touches** the clinical boundary, source discipline, or the
  neutrality of reference content.
- **No restricted or prohibited category** is offered without the review named in
  `MONETIZATION_BOUNDARY.md`.
- **Structured data carries no `Offer` or price**, so the asset is not misrepresented
  as an e-commerce store.
