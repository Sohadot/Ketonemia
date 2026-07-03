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

## Implementation Records

### Sprint 3E - Source Registry and Accuracy Hardening

Date: 2026-07-03

Scope:

- Added a visible Claim Source Registry to `/sources/` with source IDs, titles, organizations/publications, source classes, URLs or citations, access dates, supported claims, population/context notes, and pages using each source.
- Added page-level source ID references to existing high-risk pages: `/ketonemia-vs-ketoacidosis/`, `/clinical-boundary/`, `/beta-hydroxybutyrate/`, and `/blood-ketones/`.
- Confirmed `/laboratory-context/` and `/student-guide/` are not present as public pages in this repository snapshot; no new pages were created during this source-hardening sprint.
- Patched BHB page NAD markup from superscript-plus glyph usage to `NAD<sup>+</sup>` markup where embedded in HTML text.
- Patched the AcAc/BHB discordance explanation on `/blood-ketones/` because `/laboratory-context/` is not present in this repository snapshot.
- Preserved clinical-boundary language: no diagnosis, triage, individualized safety claim, or treatment instruction was added.

No new DEC was created. The sprint did not establish a new governance rule; it implemented existing source and claim discipline.

Closed stale open decisions:

- "Which sources become the first official source index?" Closed by the Sprint 3E Claim Source Registry on `/sources/`.
- "Which source placeholders should be accepted for Sprint 1 before full citations are collected?" Closed by replacing high-risk placeholders with source IDs and visible registry entries.
- "What exact fields belong in the first AI Reference Pack?" Closed for current scope by `AI_REFERENCE_POLICY.md`, which records definitions, term relationships, KSO ontology classes, KSS state language, allowed claims, prohibited claims, citation requirements, emergency boundary language, and page-to-page internal link map.
- "What is the minimum viable Blood Ketone Signal Map interaction?" Closed by the Sprint 2 `/signal-map/` implementation.

## Open Decisions

- None at this time.
