# Classification Protocol

The Classification Protocol organizes blood ketone signal context into reference
categories. It does not diagnose, triage, treat, score risk, declare safety,
declare danger, or interpret an individual reading.

Governing sentence:

**Classify the context. Preserve the clinical boundary.**

Guiding rule for the entire protocol:

**The protocol classifies the interpretive frame, not the person.**

This is a reference classification protocol for organizing blood ketone signal
context. It is not a medical tool, not a diagnostic protocol, and not a triage
flow. It is the governed bridge between the Ketonemia Signal Ontology (KSO), the
Ketonemia State Standard (KSS), source discipline, and any future engine output.

---

## 1. Purpose

The purpose of this protocol is to define how Ketonemia.com converts structured
context inputs into governed reference outputs:

Observed context → KSO class → KSS zone language → boundary statement → canonical references → source requirements.

The protocol is the operational layer that sits between knowledge and tool:

- KSO defines *what the context classes are* ([KETONEMIA_SIGNAL_ONTOLOGY.md](KETONEMIA_SIGNAL_ONTOLOGY.md)).
- KSS defines *what the signal-zone language is* ([KETONEMIA_STATE_STANDARD.md](KETONEMIA_STATE_STANDARD.md)).
- This protocol defines *how KSO and KSS are used together under governance*.
- A future engine (build phase F4) would *run* this protocol in an interface.

The protocol does not replace the clinical boundary
([CLINICAL_BOUNDARY.md](CLINICAL_BOUNDARY.md)); it operationalizes it.

---

## 2. Non-Clinical Boundary

This protocol must never output:

- diagnosis;
- triage;
- treatment guidance;
- emergency status;
- safety status;
- danger status;
- individualized interpretation;
- risk, severity, or probability scoring;
- device endorsement;
- product recommendation.

If any input pushes toward one of these, the protocol responds with boundary
language and canonical references, not with a verdict. The clinical boundary does
not change across audiences, inputs, or context combinations.

---

## 3. Inputs

The protocol accepts context inputs only. It does not accept, request, or require
numeric readings, and it must not publish or infer numeric thresholds.

| Input | Allowed values |
| --- | --- |
| Measurement type | blood / urine / breath / laboratory / not specified |
| Measured compound | BHB / AcAc / acetone / not specified |
| Sample type | blood / urine / breath / not specified |
| Context | fasting / nutritional ketosis / diabetes / illness-stress / medication / laboratory / research / media / AI reference / not specified |
| Audience | public / student / clinician-educator / laboratory / researcher / media / AI system / strategic reviewer |
| Medication context | present / not present / not specified |
| Clinical concern boundary | present / not present |
| Source class | clinical guideline / institutional / regulatory / peer-reviewed / textbook / manufacturer (labeled) / media (labeled) / not specified |
| Interpretation need | definition / comparison / measurement / classification / boundary |

No personal identity, no health history beyond non-personal context selection, and
no individual reading is collected (consistent with [INTERFACE_THESIS.md](INTERFACE_THESIS.md)).

---

## 4. Output

Every classification produces a governed output only:

- KSO class (from the ten classes in [KETONEMIA_SIGNAL_ONTOLOGY.md](KETONEMIA_SIGNAL_ONTOLOGY.md));
- KSS zone language (K0–K5 reference labels from [KETONEMIA_STATE_STANDARD.md](KETONEMIA_STATE_STANDARD.md));
- boundary statement;
- canonical page links;
- source ID or source-class requirement;
- allowed language;
- prohibited inference.

The output must never contain the following as a verdict about a person or a
reading: *safe, dangerous, urgent, normal, abnormal, you should, diagnosis likely,
has DKA, no DKA, treatment needed.* The term *ketoacidosis* or *DKA* may appear only
as a named clinical-syndrome context that this site does not evaluate — never as a
determination applied to the reader.

KSS zone language is used descriptively (for example, "this falls in the language
of the Clinical Concern Boundary, K4"), never as a severity score, diagnosis scale,
or risk tier.

---

## 5. Classification Rules

These are the core of the protocol. They are deterministic reference rules, not a
clinical algorithm.

**Rule 1 — Measurement first.** If the measured compound or sample type is unclear,
the output must classify the case as *measurement-context incomplete* and direct the
reader to `/blood-ketones/` and `/laboratory-context/` before any further language.

**Rule 2 — Compound separation.** Blood BHB, urine AcAc, and breath acetone must not
be treated as interchangeable signals. The output must name which compound and sample
type the classification applies to.

**Rule 3 — Context before meaning.** A ketone signal cannot be interpreted without
context. The protocol must preserve fasting, nutritional, diabetes, illness,
medication, laboratory, research, or media context before assigning any explanatory
language.

**Rule 4 — Clinical boundary escalation without triage.** When the input includes
diabetes, illness, vomiting, medication concern, or DKA-related language, the output
must move toward clinical-boundary language and canonical sources — but must not
triage, diagnose, declare urgency, or provide instructions. It names the boundary; it
does not cross it.

**Rule 5 — Audience-specific language, constant boundary.** The protocol may adapt
wording for public, student, clinician-educator, laboratory, researcher, media, AI,
and strategic-reviewer audiences. The clinical boundary and the prohibited inferences
remain identical across all audiences.

**Rule 6 — Source discipline.** Any output involving DKA, diabetes, medication risk,
laboratory method, or measurement comparison must cite a source class or Source ID
from [SOURCE_POLICY.md](SOURCE_POLICY.md) and `/sources/`. Unsourceable claims are
rewritten as concept language or omitted.

**Rule 7 — No risk scoring.** The protocol must not produce risk scores, severity
scores, probability estimates, safety ratings, or readiness levels.

---

## 6. Mapping Table

Reference patterns using the real KSO classes and KSS labels from the repository.
These are illustrative reference mappings, not an exhaustive decision tree, and never
a determination about a person.

| Input context | Primary KSO class | KSS language | Boundary level | Canonical pages |
| --- | --- | --- | --- | --- |
| Fasting + blood BHB | Fasting Signal | Nutritional / Fasting Range (K2), context-dependent | Not a safety claim | `/blood-ketones/` · `/ketonemia-vs-ketosis/` · `/clinical-boundary/` |
| Nutritional ketosis + blood BHB | Nutritional Signal | Nutritional / Fasting Range (K2) | Not beneficial or safe without context | `/ketonemia-vs-ketosis/` · `/blood-ketones/` |
| Urine ketones + public reader | Laboratory Measurement Signal | Low Presence (K1), non-equivalent signal | Do not infer blood BHB | `/laboratory-context/` · `/blood-ketones/` |
| Illness / vomiting + reduced intake | Illness / Stress Signal | Elevated Context Signal (K3) | Route to boundary; no triage | `/clinical-boundary/` · `/blood-ketones/` · `/sources/` |
| Diabetes + DKA language | Diabetes-Associated Signal → DKA Concern Boundary | Clinical Concern Boundary (K4) | No diagnosis or triage | `/ketonemia-vs-ketoacidosis/` · `/clinical-boundary/` · `/sources/` |
| Medication (SGLT2) concern | Medication-Context Signal | Clinical Concern Boundary (K4) | Document phenomenon; no individual risk assessment | `/ketonemia-vs-ketoacidosis/` · `/clinical-boundary/` · `/sources/` |
| Emergency-referral language in source guidance | Emergency Referral Boundary | Emergency Referral Boundary (K5) | Point to professional care; no self-triage | `/clinical-boundary/` · `/sources/` |
| Laboratory method comparison | Laboratory Measurement Signal | Reference language only | Method changes description, not verdict | `/laboratory-context/` · `/beta-hydroxybutyrate/` · `/sources/` |
| Media explanation | Baseline Signal (public-language frame) | Terminology accuracy layer | Avoid panic / safety framing | `/media-brief/` · `/clinical-boundary/` |
| Research comparison | Laboratory Measurement Signal (research frame) | Source-bound measurement signal | Preserve method / population / context | `/research/` · `/sources/` |

Source IDs available for the DKA, diabetes, medication, and measurement rows include
SRC-ADA-2026, SRC-DUK-DKA, SRC-NHS-DKA, SRC-FDA-SGLT2, and SRC-LAB-BHB-ACAC
(see `/sources/` and `/data/source-registry.json`).

---

## 7. Output Template

Every classification output follows this structure. This template is the contract a
future engine must satisfy.

1. Context classification:
2. Measurement note:
3. Boundary statement:
4. Allowed language:
5. Prohibited inference:
6. Canonical references:
7. Source requirements:

Worked reference example (laboratory measurement context):

> **Context classification:** Laboratory measurement context — Laboratory Measurement Signal (KSO).
>
> **Measurement note:** Blood BHB and urine AcAc are different measurement signals and should not be treated as interchangeable.
>
> **Boundary statement:** This classification does not diagnose, triage, declare safety, or interpret an individual reading.
>
> **Allowed language:** "Measurement method changes how a ketone signal should be described."
>
> **Prohibited inference:** Do not infer DKA, safety, danger, or treatment need from method language alone.
>
> **Canonical references:** `/laboratory-context/` · `/blood-ketones/` · `/clinical-boundary/` · `/sources/`
>
> **Source requirements:** Measurement-comparison claims cite SRC-LAB-BHB-ACAC.

---

## 8. Engine Readiness

This protocol is the governing specification for any future classification engine
(build phase F4 of [ASSET_INTELLIGENCE_FACTORY_PLAN.md](ASSET_INTELLIGENCE_FACTORY_PLAN.md)).

Any engine built on Ketonemia.com must produce outputs no broader than this protocol
allows. The engine inherits every rule in Section 5, every prohibition in Section 2,
and the output contract in Section 7.

**The engine may classify reference context. It may not classify people.**

---

## 9. Strategic Use

The protocol is a licensing-ready reference layer because it defines how ketonemia
terminology, measurement context, source discipline, and clinical-boundary language
can be operationalized without becoming a clinical decision system.

A strategic buyer acquires not only terminology and pages, but a governed method for
turning blood ketone context into reference output that stays inside the clinical
boundary — the specification a compliant tool, API, or agent integration would be
built on (see [BUYER_LOGIC.md](BUYER_LOGIC.md) and [MONETIZATION_BOUNDARY.md](MONETIZATION_BOUNDARY.md)).

---

## 10. Governing Constraints Summary

- Classifies interpretive frame, not the person.
- No numeric thresholds, no invented cutoffs.
- No diagnosis, triage, treatment, safety, danger, urgency, or risk scoring.
- Blood BHB, urine AcAc, and breath acetone are never interchangeable.
- Context precedes meaning; source discipline precedes any clinical-adjacent language.
- The clinical boundary is constant across every audience and input.
- Any future engine is bound by this protocol, not the reverse.
