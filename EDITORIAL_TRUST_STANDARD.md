# Editorial Trust Standard

This document is the governed standard for how content on Ketonemia.com is
produced, sourced, corrected, and kept trustworthy over time. It operationalizes
[SOURCE_POLICY.md](SOURCE_POLICY.md), [CLAIM_POLICY.md](CLAIM_POLICY.md),
[CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md), and [AI_REFERENCE_POLICY.md](AI_REFERENCE_POLICY.md)
into a single visible trust contract. Its public expression is [`/trust/`](trust/index.html).

Governing sentence:

**Trust is a standard the asset holds to, not a badge it awards itself.**

Where this document and `/trust/` differ in detail, this document governs; where
either conflicts with [FOUNDATION_DOCTRINE.md](FOUNDATION_DOCTRINE.md) or
[CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md), the doctrine and the clinical boundary win.

---

## Why This Layer Exists

The asset already practices source discipline, clinical-boundary preservation, and
machine-human parity. What it lacked was a single place that states, honestly and
verifiably, *how* it earns trust — without overstating it. A trust page that claims
more than the asset does would itself be the first breach of trust. This standard
exists to make the real discipline legible, and to bound what may and may not be
claimed about it.

The honesty rule is absolute: this layer documents the standard and the mechanism.
It never asserts a review, an endorsement, a credential, or an outcome that did not
occur.

---

## What May Be Claimed

Only statements that are true and verifiable from the repository or the live site:

- Every medical claim traces to a source in the claim source registry (`/sources/`,
  mirrored in `/data/source-registry.json`), identified by a source ID.
- The clinical boundary in [CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md) is applied on
  every page; no page diagnoses, triages, treats, scores risk, or declares a reader
  safe or in danger.
- The machine-readable layer is never looser than the human-facing site
  ([AI_REFERENCE_POLICY.md](AI_REFERENCE_POLICY.md)).
- Every surface passes [QUALITY_GATE.md](QUALITY_GATE.md) before it ships.
- Build phases and governance decisions are recorded in [DECISION_LOG.md](DECISION_LOG.md).
- The site is static: no accounts, no tracking, no advertising, no affiliate links,
  and no on-site collection of personal or health data.

## What May Not Be Claimed

- That any page has been individually reviewed or approved by a named clinician,
  unless that review actually happened and the reviewer, credential, and date are
  published.
- That the content is a substitute for professional medical judgment.
- That a reading, a KSS zone, or a KSO class is safe, dangerous, or a diagnosis.
- Any credential, affiliation, certification, or endorsement the asset does not hold.
- Any accuracy, ranking, or trust metric that is not measured and dated.

If independent expert review is added in the future, it is published by name,
credential, scope, and date on the reviewed page — never implied in the aggregate,
and never retroactively claimed for pages it did not cover.

---

## The Trust Contract

The public trust page must present, at minimum, these disciplines, each tied to the
artifact that proves it:

| Discipline | What it means | Where it is proven |
| --- | --- | --- |
| Sourcing | Every medical claim carries a source ID from the registry | `/sources/`, `/data/source-registry.json` |
| Clinical boundary | No diagnosis, triage, treatment, risk score, or safety verdict | `/clinical-boundary/`, [CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md) |
| Independence | No ads, affiliates, paid rankings, or trust-for-pay; sponsorship is "Supported by," never "recommended by" | [MONETIZATION_BOUNDARY.md](MONETIZATION_BOUNDARY.md), `/briefs/` |
| Machine parity | JSON, summaries, and any future API are held to the same rules as the pages | [AI_REFERENCE_POLICY.md](AI_REFERENCE_POLICY.md), `/reference-pack/` |
| Corrections | A stated way to report an inaccuracy and how it is handled | `/trust/`, this document |
| Privacy by architecture | Static site; no personal or health data is collected or stored | The site itself |
| Governance record | Quality gate per surface, decision log per phase | [QUALITY_GATE.md](QUALITY_GATE.md), [DECISION_LOG.md](DECISION_LOG.md) |

---

## Correction and Change Policy

- **Reporting.** Inaccuracies are reported to the neutral contact
  **corrections at ketonemia.com**. There is no form and no data collection.
- **Triage.** A report that identifies a sourcing error, a boundary breach, or a
  factual mistake is treated as a defect against [QUALITY_GATE.md](QUALITY_GATE.md).
- **Correction.** Substantive corrections to a medical claim are made against a
  source, and the source registry is updated if the underlying reference changed.
- **Record.** Material corrections are recorded in [DECISION_LOG.md](DECISION_LOG.md)
  (as an Implementation Record or a DEC entry if a new rule results).
- **Versioning.** The machine-readable files carry an `updated` date; when a claim
  changes, the relevant file's date advances so retrieval systems can see freshness.
- **No silent loosening.** A correction may tighten the boundary or improve a source.
  It may never quietly widen what the asset claims beyond this standard.

---

## Boundaries of This Layer

- This is a transparency and standards layer. It adds no clinical content, no
  thresholds, no diagnosis, and no interpretation of any individual reading.
- It introduces no new data collection, script, form, or third-party dependency.
- It does not certify the site as medically reviewed; it documents the governance
  the site actually runs on.
- It is bound by every layer above it in [SYSTEM_ARCHITECTURE.md](SYSTEM_ARCHITECTURE.md):
  the doctrine, the clinical boundary, the source policy, and the AI-reference policy.

---

## Relationship to the Layer Stack

This layer deepens **Layer 8 (Governance)** of the Asset Intelligence Factory, the way
the ten `/ontology/` class pages (F5) deepened Layer 3 (Ontology). It adds no new layer
to the stack; it makes an owned layer visible and citable. `/trust/` is registered in
the Boundary & Sources cluster of the Route Map.
