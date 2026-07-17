# Acquisition Dossier

This document is the structured, private-facing but public-safe account of
Ketonemia.com as a strategic acquisition asset. It inventories what is owned, the
moat, the machine and reference footprints, the governance record, and the specific
cost of not owning the asset for each priority buyer class.

It is not a valuation, a price, a forward-looking financial promise, or a domain
listing. It is an accounting of what exists.

Governing sentence:

**Owning Ketonemia.com means owning a reference layer around an emerging metabolic
signal category.**

The sovereign chain this asset has moved along is now complete:

**Domain → Category Artifact → Category Intelligence Source → Strategic Acquisition Asset**

The public expression of this dossier is [`/acquisition/`](acquisition/index.html);
the availability and engagement pitch is [`/strategic-availability/`](strategic-availability/index.html).
Where they differ in detail, this document governs; where either conflicts with
[BUYER_LOGIC.md](BUYER_LOGIC.md) or [CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md), the
buyer logic and the clinical boundary win.

---

## What Is Owned

Every layer of the Asset Intelligence Factory is built and merged. This mirrors the
Layer Stack in [SYSTEM_ARCHITECTURE.md](SYSTEM_ARCHITECTURE.md).

| Layer | What is owned | Where it lives |
| --- | --- | --- |
| Domain thesis | The category-term domain and its governing thesis | [ASSET_THESIS.md](ASSET_THESIS.md), `/definition/` |
| Category language | A governed vocabulary for blood ketone signals | [CATEGORY_LANGUAGE.md](CATEGORY_LANGUAGE.md) |
| Ontology (KSO) | Ten context classes, each a citable reference page | `/ontology/` (hub + 10 class pages) |
| Standard (KSS) | A governed K0–K5 signal-zone reference model | [KETONEMIA_STATE_STANDARD.md](KETONEMIA_STATE_STANDARD.md), `/signal-map/` |
| Protocol | A deterministic classification protocol | [CLASSIFICATION_PROTOCOL.md](CLASSIFICATION_PROTOCOL.md) |
| Engine / Tool | A working reference tool that runs the protocol | `/classification-engine/` |
| Interface | An interface that embodies signal → context → boundary | [INTERFACE_THESIS.md](INTERFACE_THESIS.md), `/signal-map/`, `/architecture/` |
| Reference layer | Thirty-three citable, archivable routes | See Reference Footprint |
| Governance | Quality gates, decision log, clinical boundary, source discipline, published editorial trust standard | [QUALITY_GATE.md](QUALITY_GATE.md), [DECISION_LOG.md](DECISION_LOG.md), [EDITORIAL_TRUST_STANDARD.md](EDITORIAL_TRUST_STANDARD.md), `/trust/` |
| Machine layer | Agent-readable index, JSON reference pack, deep JSON-LD | See Machine Footprint |
| Monetization | A governed product catalog and inquiry surface | [MONETIZATION_SPEC.md](MONETIZATION_SPEC.md), `/briefs/` |
| Buyer logic | This dossier and the availability surface | This document, `/acquisition/`, `/strategic-availability/` |

---

## The Moat

A company can build ketone content. It cannot easily rebuild the following, and each
line is now backed by a concrete, shipped artifact.

| What a rival cannot cheaply rebuild | The artifact that proves it is owned |
| --- | --- |
| The category-aligned domain | The medical term itself is the domain |
| The reference language | [CATEGORY_LANGUAGE.md](CATEGORY_LANGUAGE.md) and the definitional pages |
| The governed standard | KSS + `/signal-map/` |
| The signal ontology | `/ontology/` — hub and ten class pages |
| The clinical boundary system | [CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md), enforced on every page |
| The interface thesis | `/signal-map/` and `/architecture/` |
| The working tool | `/classification-engine/` running the classification protocol |
| The internal link graph | Thirty-three routes, no orphans, mapped on `/architecture/` |
| The neutral trust layer | Source discipline + the clinical boundary, documented, gated, and published as an editorial trust standard (`/trust/`) |
| The AI-readable reference surface | `/llms.txt`, `/data/*.json`, `/reference-pack/`, and deep JSON-LD |

The moat is not any single item; it is that all of them are governed to stay
consistent with one another. Rebuilding one is easy; rebuilding the coherent,
neutral, source-disciplined whole is not.

---

## Machine Footprint

What makes the asset legible and trustworthy to machines and AI agents, not only
people:

- `/llms.txt` — public AI index with allowed and prohibited uses and the route list.
- `/robots.txt` and `/sitemap.xml` — crawl and archive discipline.
- Seven governed JSON files under `/data/`: `reference-pack.json`, `glossary.json`,
  `kso-ontology.json`, `kss-standard.json`, `source-registry.json`, `page-index.json`,
  and `classification-rules.json`.
- `/reference-pack/` — the human-readable index of the machine layer.
- Deep JSON-LD across pages: `DefinedTerm` / `DefinedTermSet` on ontology and
  definitional pages, `CollectionPage` / `BreadcrumbList` on hubs, with no medical
  claims in structured data.

The governing constraint: the machine layer is never looser than the human-facing
site. If a claim is prohibited on the pages, it is prohibited in the data.

---

## Reference Footprint

- **Thirty-three routes** across seven clusters: Definition & Comparison, Measurement &
  Laboratory, Audience Layers, Boundary & Sources, Machine & Agent Layer, Ontology
  (KSO Classes), and Strategic.
- A complete internal link graph with **no orphan pages**, rendered on `/architecture/`.
- A **source registry of seven cited institutional, regulatory, and academic sources**,
  with every medical claim traced to a source ID.
- An **AI-readable summary on every page**, consistent with the human content.

---

## Governance Record

The trust layer is not a claim; it is a record.

- **Decision log** — DEC-001 (the positioning decision) plus implementation records for
  every build phase F1–F7 ([DECISION_LOG.md](DECISION_LOG.md)).
- **Quality gates** — a gate per surface type (doctrine, clinical boundary, source,
  SEO, interface, AI, monetization, ontology, architecture, and more) in
  [QUALITY_GATE.md](QUALITY_GATE.md).
- **Clinical boundary** — a formal, enforced scope limit ([CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md)).
- **Source discipline** — every medical claim sourced or framed as concept language
  ([SOURCE_POLICY.md](SOURCE_POLICY.md), `/sources/`).

---

## Cost of Not Owning It, per Buyer Class

For each priority buyer class in [BUYER_LOGIC.md](BUYER_LOGIC.md): what the asset gives
them, and the specific loss if a competitor or a neutral third party owns it instead.

| Buyer class | What the asset gives them | Cost of not owning it |
| --- | --- | --- |
| Continuous glucose/ketone monitoring | A governed, neutral reference layer for the ketone language their devices generate | A competitor or third party controls the category vocabulary their users learn |
| Blood ketone meter / test strip | Category-aligned reference and taxonomy for the signal they measure | Their measurement is described in someone else's governed language |
| Diabetes safety / remote patient monitoring | A clinically bounded reference for ketone concern language | The trusted neutral layer sits outside their platform |
| Metabolic health / fasting / wearable | A reference-grade ketone literacy layer as a product feature | Ketone literacy remains a gap or is owned by a rival |
| Diagnostics / laboratory | A measurement-discipline reference (BHB/AcAc/acetone separation) | The measurement-language authority is held elsewhere |
| Clinical education | A source-disciplined, boundary-safe teaching reference | No neutral partner for ketone-signal education in the category |
| Health AI / medical reference | An agent-readable, governed taxonomy and standard, safe to ingest | An AI-safe reference source in the category is unavailable or held by a competitor |
| Health media / education publishing | Public-language guidance that preserves layer distinctions | Media coverage keeps collapsing the layers the asset governs |

The recurring theme: the asset is most costly to *not* own when a competitor or a
neutral third party owns it instead, because category language, once anchored, is
expensive to dislodge.

---

## What the Asset Must Remain

The value is conditional on preserving what makes it trustworthy. An acquirer inherits
these constraints, not just the pages:

- **Clinically bounded** — never a diagnosis tool, treatment recommender, or clinical service.
- **Source-disciplined** — medical claims stay attributed, not commercial.
- **Neutral** — never an affiliate platform, brand channel, or sales funnel.
- **AI-safe** — internally consistent, free of unsourced claims that could propagate
  through AI retrieval.

These are not limitations. They are the structural conditions that create the trust
layer, and therefore the value.

---

## Inquiry

Strategic inquiries use the neutral contact on `/strategic-availability/`:
**inquiry at ketonemia.com**. There is no on-site store, price, or data-collection
form. An inquiry describes the organization, the intended use, and the engagement
model. Inquiries that reflect understanding of the reference layer and the intent to
preserve it receive priority.
