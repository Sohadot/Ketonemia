# Ketonemia Signal Ontology

The **Ketonemia Signal Ontology (KSO)** classifies blood ketone signals by context, not by diagnosis.

KSO is a language system for education, reference pages, interface outputs, AI summaries, and future licensing.

## Ontology Classes

### 1. Baseline Signal

A low or non-prominent ketone signal.

Use for educational explanations of normal or low ketone presence when no strong contextual interpretation is being made.

### 2. Nutritional Signal

A signal associated with low-carbohydrate nutrition or nutritional ketosis contexts.

Must not imply that a reading is beneficial or safe without context.

### 3. Fasting Signal

A signal associated with fasting or reduced intake.

Must distinguish educational physiology from individualized medical interpretation.

### 4. Exercise / Performance Signal

A signal associated with exercise, endurance, energy metabolism, or performance contexts.

Must avoid performance claims unless sourced.

### 5. Illness / Stress Signal

A signal associated with illness, vomiting, infection, dehydration, stress physiology, or reduced intake during illness.

Must preserve caution and route to clinical-boundary content where appropriate.

### 6. Diabetes-Associated Signal

A signal associated with diabetes, insulin deficiency risk, glucose status, or diabetes safety education.

Must not diagnose DKA or tell users they are safe.

### 7. Medication-Context Signal

A signal associated with medication contexts, especially where ketone risk language may differ from glucose-only assumptions.

Requires careful sourcing and boundary language.

### 8. Laboratory Measurement Signal

A signal explained through specimen type, assay, reporting language, or lab interpretation boundaries.

Must separate blood, urine, and breath ketone measurement.

### 9. DKA Concern Boundary

Not a diagnosis. A boundary class used when ketone information belongs in a clinical concern frame.

Must link to clinical care guidance and cited sources.

### 10. Emergency Referral Boundary

Not treatment advice. A boundary class for language that points toward urgent or emergency medical evaluation where source guidance supports it.

Must not ask users to self-triage.

## Ontology Rule

KSO may classify context. It must not declare a patient state.
