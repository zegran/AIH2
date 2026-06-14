# Concept Foundation (summary)

> Entry note for the immutable scientific core. Full document:
> `../../plan/2026-06-14-aih2-concept-foundation.md`. Linked from [[00-Hub]].

## Central thesis
The aluminum–water hydrolysis literature is internally contradictory about how parameters
control H2 yield. The contradiction is **structural** — it comes from each study reporting an
isolated, non-standardized window of conditions. This is framed as an **unsolved scientific
problem (significance)**, not a "missing combination" (novelty).

## The four documented contradictions (evidence)
1. Direction-changing particle-size effect (inverted-U within single studies).
2. Activation energies spanning ~3.5–102.6 kJ/mol for the same reaction family.
3. Inconsistently characterized rate–yield trade-off.
4. Cross-study disagreement on which parameter dominates.

## Research question
Are these contradictions real physical interactions or artifacts of isolated study windows?
Can interpretable ML on a unified dataset separate the two and recover the true parameter
hierarchy?

## Hypotheses
- **H1:** particle-size sign flip = shrinking-core regime switch → SHAP
  `particle_size × {temperature, alkalinity}` interaction.
- **H2:** contradiction largely explained by `system_class` + data-quality covariates.
- **H3:** ML temperature sensitivity → Arrhenius-consistent Ea per `system_class` in the
  3.5–102.6 kJ/mol band.

## Why Q1
Open reproducible dataset + leakage-controlled methodology (optimism gap) + physical validation
+ interaction-based significance. Novelty = (contradiction-resolution + physical validation +
open data), **not** "SHAP on a new system".

## Scope lock
Aqueous Al hydrolysis only (pure Al-alkali, Al-alloy, mechanically/liquid-metal activated,
waste Al). Mg and others = background citation only, never in the dataset. Al–NaBH4, acid
hydrolysis, non-aqueous = out.
