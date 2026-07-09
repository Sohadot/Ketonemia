# System Architecture

This document is the canonical map of Ketonemia.com as a single system. It shows
how every governance document, reference page, standard, protocol, and machine file
fits into one governed category-intelligence architecture.

Governing sentence:

**The architecture makes the system legible. It does not add clinical content.**

The sovereign chain this asset moves along:

**Domain → Category Artifact → Category Intelligence Source → Strategic Acquisition Asset**

The public expression of this document is [`/architecture/`](architecture/index.html).
Where the two differ in detail, this document governs; where either conflicts with
[FOUNDATION_DOCTRINE.md](FOUNDATION_DOCTRINE.md) or [CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md),
the doctrine and the clinical boundary win.

---

## The Layer Stack

The asset is built from layers, each answering one question and living in a specific
place. This table mirrors the eleven-layer model in
[ASSET_INTELLIGENCE_FACTORY_PLAN.md](ASSET_INTELLIGENCE_FACTORY_PLAN.md) §2 and must
be kept in sync with it.

| # | Layer | Question it answers | Where it lives | Status |
| --- | --- | --- | --- | --- |
| 1 | Domain thesis | What sentence makes the name necessary? | [ASSET_THESIS.md](ASSET_THESIS.md), [FOUNDATION_DOCTRINE.md](FOUNDATION_DOCTRINE.md) | Owned |
| 2 | Category language | What vocabulary does the asset own? | [CATEGORY_LANGUAGE.md](CATEGORY_LANGUAGE.md) | Owned |
| 3 | Ontology | How do we classify the category? | [KETONEMIA_SIGNAL_ONTOLOGY.md](KETONEMIA_SIGNAL_ONTOLOGY.md), `/data/kso-ontology.json` | Owned (spec); class pages pending |
| 4 | Standard | What is good / complete / trusted? | [KETONEMIA_STATE_STANDARD.md](KETONEMIA_STATE_STANDARD.md), `/data/kss-standard.json` | Owned |
| 5 | Protocol | How is context classified under governance? | [CLASSIFICATION_PROTOCOL.md](CLASSIFICATION_PROTOCOL.md) | Owned (F2) |
| 6 | Engine / Tool | How does the system produce operational output? | `/signal-map/` (conceptual); engine pending | Partial |
| 7 | Reference layer | Is the site archivable, searchable, citable? | 16 canonical routes (see Route Map) | Owned |
| 8 | Governance | How are stability, versioning, and trust ensured? | [QUALITY_GATE.md](QUALITY_GATE.md), [DECISION_LOG.md](DECISION_LOG.md), policy docs | Owned |
| 9 | Interface thesis | Does the interface embody the asset's meaning? | [INTERFACE_THESIS.md](INTERFACE_THESIS.md), `/signal-map/`, `/architecture/` | Owned |
| 10 | Monetization | How does it earn without lowering trust? | [MONETIZATION_BOUNDARY.md](MONETIZATION_BOUNDARY.md) | Boundary owned; proof pending |
| 11 | Buyer logic | Who is the buyer and why is not-buying a loss? | [BUYER_LOGIC.md](BUYER_LOGIC.md), `/strategic-availability/` | Owned (thesis); dossier pending |
| + | Machine / agent layer | Can machines read and trust it, not just humans? | `/llms.txt`, `/robots.txt`, `/sitemap.xml`, `/data/*.json`, `/reference-pack/` | Owned (F1) |

---

## Route Map

Every public route belongs to exactly one cluster. No route may exist without a
cluster and a declared layer. The public Reference Map at `/architecture/` renders
this graph so every route is reachable from one page.

### Cluster A — Definition & Comparison
- `/` — category identity and reference map
- `/definition/` — governed definition of ketonemia as a blood state
- `/ketonemia-vs-ketosis/` — blood measurement state vs. metabolic state
- `/ketonemia-vs-ketoacidosis/` — signal vs. clinical syndrome, clinically bounded

### Cluster B — Measurement & Laboratory
- `/blood-ketones/` — signal layer and measurement context
- `/beta-hydroxybutyrate/` — primary blood ketone marker, biochemistry depth
- `/laboratory-context/` — measurement methods, substrates, report-language limits

### Cluster C — Audience Layers
- `/student-guide/` — learning pathway across disciplines
- `/research/` — research-facing context variables and comparability
- `/media-brief/` — public-language guidance that preserves layer distinctions
- `/clinical-literacy/` — responsible communication language patterns

### Cluster D — Boundary & Sources
- `/clinical-boundary/` — formal trust and safety boundary
- `/sources/` — source discipline policy and claim source registry
- `/signal-map/` — conceptual interface: signal zones, context dimensions, boundaries

### Cluster E — Machine & Agent Layer
- `/ai-reference/` — allowed uses, prohibited inferences, boundary rules for AI
- `/reference-pack/` — human-readable index of the machine-readable JSON files

### Cluster F — Strategic
- `/strategic-availability/` — partnership, licensing, and acquisition context
- `/architecture/` — this system map (Reference System layer)

---

## Dependency and Build Order

The asset is built in the phased order defined in
[ASSET_INTELLIGENCE_FACTORY_PLAN.md](ASSET_INTELLIGENCE_FACTORY_PLAN.md) §5:

- **F1** — Agent-readable machine layer (complete).
- **F2** — Classification Protocol (complete).
- **F3** — System Architecture / Reference Map (this layer).
- **F4** — Deterministic reference engine (runs the F2 protocol; layer 6).
- **F5** — Ten deep ontology class pages (deepens layer 3).
- **F6** — First governed product spec + inquiry surface (layer 10 proof).
- **F7** — Acquisition dossier (layer 11 proof).

Each layer depends on the ones above it in the stack, not below: the engine (F4) is
bound by the protocol (F2), which is bound by the ontology (layer 3) and standard
(layer 4), which are bound by the language (layer 2) and thesis (layer 1).

---

## Architecture Rule

- No route may exist without a declared layer and a place in a Route Map cluster.
- Every new page must name its layer, join a cluster, and link back into the graph
  (this extends [INTERNAL_LINKING_POLICY.md](INTERNAL_LINKING_POLICY.md)).
- When a route is added or removed, this document, `/architecture/`, `/sitemap.xml`,
  `/llms.txt`, and `/data/page-index.json` must be updated together.
- The architecture describes the system. It never introduces clinical content,
  thresholds, diagnosis, triage, or verdicts.
- This document and `ASSET_INTELLIGENCE_FACTORY_PLAN.md` §2 must never drift; a change
  to one is a change to both.
