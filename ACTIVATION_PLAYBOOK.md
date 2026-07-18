# Activation Playbook

This document governs the phase after the build. The reference asset is complete,
self-governing, and hardened; its remaining value is not in more pages but in being
**discovered, cited, contacted, and — on the owner's terms — licensed or acquired**.

Governing sentence:

**A reference that no one can find, cite, or contact is not yet an asset; activation
turns a built thing into a used one.**

This playbook is operational and neutral. It never turns the site into a sales funnel,
never fabricates adoption, and never relaxes the clinical boundary. Where it touches
buyers it defers to [BUYER_LOGIC.md](BUYER_LOGIC.md) and [ACQUISITION_DOSSIER.md](ACQUISITION_DOSSIER.md);
where either conflicts with [CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md), the boundary wins.

---

## Where We Are

- 43 canonical routes across eight clusters; every layer of the Asset Intelligence
  Factory built and merged.
- Governance is self-enforcing: `scripts/verify_governance.py` runs 12 invariants on
  every push and pull request and blocks a merge on any drift.
- Edges hardened: custom 404, RFC 9116 `security.txt`.
- Discovery layer shipped: OpenGraph/Twitter cards, favicon, sitemap, robots, `llms.txt`,
  deep JSON-LD — all boundary-safe.

Nothing above is worth anything until the asset is indexed, reachable, and measured.

---

## The Shift: Build → Activation

Three value paths, in dependency order. Later paths depend on earlier ones.

1. **Authority / citation** — search engines and AI assistants find, trust, and cite
   the asset for blood-ketone terminology. This is the foundation and the moat's proof.
2. **Licensing** — governed products at `/briefs/` (AI reference pack, measurement
   briefs, taxonomy licensing) generate recurring income without lowering trust.
3. **Acquisition** — the dossier at `/acquisition/` converts a strategic buyer, on the
   owner's terms.

You cannot license or sell what no one can find. So indexing and reachability come first.

---

## Division of Labor

| The AI owner/PM does (autonomously) | The human owner does (external) |
| --- | --- |
| Build, govern, verify, document; keep all invariants green | Merge pull requests |
| Prepare governed materials (verification guides, outreach drafts, adoption-check design) | Create/verify accounts (Search Console, Bing, mailboxes) |
| Draft honest, boundary-safe copy for any outreach | Send outreach from a real inbox; hold buyer conversations |
| Design a repeatable adoption/citation measurement | Provide resources, accounts, and real-world signals |
| Flag what only the owner can unblock | Decide direction; approve or reject recommendations |

The rule that has governed this project stands: the owner intervenes externally
(merging, accounts, resources) or to flag an observation the PM accepts or rejects with
reasoning.

---

## Phase A — Indexing & Discovery (do first)

Without this, every SEO/GEO signal already shipped is invisible. Owner actions:

1. **Confirm the site is live.** Visit `https://ketonemia.com/` and confirm it loads over
   HTTPS with the custom domain. Confirm the latest GitHub Actions "Deploy" run is green.
2. **Google Search Console** (uses the existing Google account):
   - Add the property `ketonemia.com` (Domain property; the Cloudflare DNS TXT verification
     is the same mechanism already used for the domain).
   - Submit `https://ketonemia.com/sitemap.xml`.
   - Use "URL Inspection → Request indexing" on `/`, `/definition/`, and `/glossary/` to seed.
3. **Bing Webmaster Tools:** add the site and submit the same sitemap (Bing feeds other
   engines and some AI retrieval).
4. **Verify the link-preview card** with any link-preview/OpenGraph debugger on two or
   three URLs, confirming the branded card and description render.

Success signal: pages begin appearing in Search Console's Coverage/Pages report as indexed.

---

## Phase B — Contact Channels (do first, in parallel with A)

The whole activation dead-ends if an interested party's email bounces. The asset publicly
commits to `inquiry@ketonemia.com` (strategic), `corrections@ketonemia.com` (governance),
and `security.txt` points to corrections@. Owner actions:

1. In Cloudflare Email Routing, confirm routes exist for `inquiry@` and `corrections@`
   forwarding to a monitored inbox.
2. Send a test message to each from an outside address; confirm delivery.
3. Optional upgrade: add `security@ketonemia.com` and I will switch `security.txt` to it.

Success signal: a test to each published address arrives in your inbox.

---

## Phase C — Adoption & Citation Proof (ongoing)

"Reference gravity" is a claim until measured. This is how we prove the moat honestly —
no fabricated metrics, ever.

- I will maintain a fixed list of category queries (e.g. "what is ketonemia", "ketonemia
  vs ketoacidosis", "is blood, urine, breath ketone the same") to test whether search and
  AI assistants cite or reflect the asset's governed distinctions.
- On a periodic cadence, the owner (or I, given access) runs the list and records what cites
  ketonemia.com. Results feed a truthful adoption record — cited, not-yet-cited, misquoted.
- A misquote that collapses a governed distinction is a signal to strengthen that page's
  clarity, not to make a louder claim.

Success signal: at least one independent search or AI surface reflects a governed
distinction traceable to the asset.

---

## Phase D — Licensing & Acquisition (owner-gated)

Only after A and B are live, and once C shows any traction. Governed by
[BUYER_LOGIC.md](BUYER_LOGIC.md) and [ACQUISITION_DOSSIER.md](ACQUISITION_DOSSIER.md).

- **Inbound first.** With contact channels live and the dossier public, the lowest-cost
  path is a well-handled inbound inquiry. I will prepare a neutral, honest response
  template that qualifies intent and preserves the "must remain" constraints.
- **Measured outbound, if the owner chooses.** I will draft governed, non-spam outreach for
  the buyer *classes* already public in BUYER_LOGIC — each message honest about what the
  asset is and is not, and explicit that its value is conditional on preserving neutrality
  and the clinical boundary. The owner sends from a real inbox and holds the conversation.
- **No price, no funnel, no pressure.** Inquiries route to the neutral contact; the asset
  stays a reference, not a store.

Success signal: a qualified inbound or outbound conversation with an organization in a
priority buyer class.

---

## Guardrails for Activation

Activation must not damage what makes the asset valuable:

- **No fabricated adoption.** Every citation, metric, or reference claimed is real and
  verifiable, or it is not claimed.
- **Neutral, not a funnel.** No ads, affiliates, pop-ups, price tags, or data-collection
  forms enter the site.
- **Boundary intact.** Nothing in outreach or copy converts the reference into diagnosis,
  triage, or a safety verdict.
- **Machine-human parity holds.** Link previews, structured data, and any pitch stay
  consistent with the pages and never looser.

---

## Inputs Needed From the Owner Now

To move, I need four confirmations. Answer any subset; each unblocks a step.

1. Is `https://ketonemia.com/` live and is the latest Deploy run green?
2. Confirm access to the Google account for Search Console (yes/no).
3. Are `inquiry@` and `corrections@` currently receiving mail (tested)?
4. What resource or subscription do you now have available (so I tailor Phase C/D)?

I will proceed on Phases A and B guidance immediately; C and D are staged behind them.
