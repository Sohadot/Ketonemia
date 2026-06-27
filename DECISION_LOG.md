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
Merged to main.

Sprint 3B added /clinical-literacy/ as the responsible language layer for clinicians, educators, care teams, students, and product teams. The page includes the Responsible Language Patterns table (8 rows), the three-layer clinical communication framework (measurement state / metabolic context / clinical concern boundary), reference pathways to all adjacent pages, and full AI-readable summary. Patches updated /clinical-boundary/, /ai-reference/, /signal-map/ (Context 7 ctx-links and Reference Pages grid), and the homepage card grid. No DEC was created because no production friction required a new governance rule.

## Open Decisions

- Which sources become the first official source index?
- Which source placeholders should be accepted for Sprint 1 before full citations are collected?
- What exact fields belong in the first AI Reference Pack?
- What is the minimum viable Blood Ketone Signal Map interaction?
