# AIH2 — Concept Foundation (Immutable Scientific Core)

**Status:** Canonical. This document sits **above** the design spec and the implementation
plan. It defines the project's fixed scientific identity. If any later decision — modeling,
scoping, writing — conflicts with this document, **this document wins**, and the conflict must
be resolved here first.

**Date:** 2026-06-14
**Topic (locked):** Hydrogen production via the **aluminum–water reaction** (aqueous Al
hydrolysis).
**Primary venue:** International Journal of Hydrogen Energy (IJHE) → fallback *Energy and AI*.

---

## 1. Central thesis

The aluminum–water hydrolysis literature is **internally contradictory** about how reaction
parameters govern hydrogen yield. The same parameter is reported to act in opposite directions
across studies, and quantitative kinetic descriptors disagree by more than an order of
magnitude. These contradictions are not random noise: they arise because each study reports
results from an **isolated, non-standardized window** of conditions (temperature range,
alkalinity, particle morphology, alloying, activation route, measurement protocol), and those
windows are stitched together by the field without a unifying model.

This work treats that situation as a **specific, unsolved scientific problem**, not as a
combinatorial gap. The contribution is framed on the axis of **significance**, not novelty:

> The point is **not** "machine learning has not yet been applied to this exact system."
> The point is "**the field holds mutually inconsistent beliefs about parameter effects, and
> no one has reconciled them on a unified evidentiary basis.**"

Reframing for emphasis: a "nobody has tried combination X" framing is weak and easily
dismissed by reviewers. A "the literature contradicts itself and we resolve the contradiction
with a leakage-controlled, physics-validated, openly reproducible analysis" framing is a
significance claim that survives scrutiny.

## 2. Empirical grounding of the contradiction (fixed as evidence)

The following observations are documented across the Al–water hydrolysis literature and anchor
the problem. They are recorded here as the evidentiary basis of the thesis. Specific per-claim
citations are attached during literature extraction (WP1) and verified before submission;
they are not invented here.

1. **Direction-changing particle-size effect.** Decreasing particle size accelerates hydrogen
   generation and raises yield in some studies, yet suppresses yield in others. Within single
   studies, an **inverted-U (non-monotonic) dependence** on particle size has been observed —
   an effect that cannot be captured by a single monotonic rule and that flips sign depending
   on the operating regime.

2. **Order-of-magnitude spread in activation energy.** Reported apparent activation energies
   for nominally the same reaction family span roughly **3.5–102.6 kJ/mol**. Such a spread is
   incompatible with a single rate-controlling mechanism and signals **regime-dependent
   kinetics** (e.g., reaction-controlled vs. diffusion-controlled).

3. **Inconsistently characterized rate–yield trade-off.** Additives and activation routes that
   most increase the *initial rate* can simultaneously *reduce final yield* (and vice versa).
   The field does not agree on where the trade-off frontier lies.

4. **Cross-study disagreement on parameter dominance.** Studies disagree about which parameter
   (temperature, alkalinity, particle size, alloying, activation method) is the dominant
   control on yield. The apparent ranking changes with the (narrow) window each study samples.

Together, these four observations establish that the contradiction is **structural** — a
property of how the literature is partitioned — rather than a defect of any single experiment.

## 3. Research question (final)

> Do the apparent contradictions in the Al–water hydrolysis literature reflect **genuine
> physical parameter interactions**, or are they **artifacts of isolated, non-standardized
> per-study experimental windows**? Can interpretable machine learning, by **unifying the
> scattered literature into one provenance-tracked dataset**, separate these two cases and
> recover the **true relative hierarchy** of parameter effects on hydrogen yield?

The question is deliberately diagnostic: its value is the *separation* of "real interaction"
from "study artifact," not merely a predictive score.

## 4. Hypotheses (final — aligned with design spec H1–H3)

- **H1 (mechanism of the headline contradiction).** The direction-changing particle-size
  effect corresponds to a **shrinking-core regime switch** (diffusion-controlled vs.
  reaction/passivation-controlled). It surfaces in the model as a
  `particle_size × {temperature, alkalinity}` **interaction** in SHAP, not as a main effect.

- **H2 (artifact vs. real).** A large share of the apparent cross-study contradiction is
  explained by **`system_class`** and **data-quality** covariates. Conditioning on them
  **reduces** the contradiction; what remains after conditioning is the genuine physical
  signal.

- **H3 (physical consistency).** The model's learned **temperature sensitivity** reproduces
  Arrhenius behavior and yields, **per `system_class`**, an activation energy inside the
  literature **3.5–102.6 kJ/mol** band — tying the data-driven result back to first-principles
  kinetics.

## 5. Why this clears Q1 standards

The work meets top-tier (Q1 / IJHE) expectations through four reinforcing pillars, none of
which is "applying SHAP to a new system":

1. **Open, reproducible dataset.** A unified, provenance-tracked, quality-tiered dataset
   released openly (Zenodo DOI, CC-BY-4.0) — addressing the field's reproducibility deficit.
2. **Leakage-controlled methodology.** Study-grouped / leave-one-study-out validation, with the
   **random-vs-grouped optimism gap** reported as a first-class result that quantifies how
   study-confounded the field's apparent predictability is.
3. **Physical validation.** Data-driven sensitivities are cross-checked against **Arrhenius**
   kinetics and (in core Phase 2) **shrinking-core** regimes — the model is not trusted on fit
   alone.
4. **Interaction-based significance.** The central claim is a **mechanistic interaction**
   (H1), resolving a concrete contradiction, rather than a marginal predictive improvement.

**Novelty statement (explicit):** the novelty is the **triad of contradiction-resolution +
physical validation + open reproducible data**, not the act of fitting an interpretable model
to aluminum–water data.

## 6. Scope lock

- **In scope (dataset):** aqueous aluminum–water hydrolysis only — **pure Al–alkali, Al-alloy,
  mechanically activated, liquid-metal activated, and waste-Al** systems.
- **Background only (NOT in the dataset):** magnesium-based and other non-aluminum hydrolysis
  systems may be cited **solely** to corroborate that contradictory parameter effects are a
  general phenomenon in metal–water hydrolysis. They never enter the training data.
- **Out of scope entirely:** Al–NaBH₄ hybrids, acid hydrolysis, and non-aqueous systems.

This scope is fixed. Expanding the dataset beyond aqueous Al hydrolysis would dilute the
contradiction signal and is therefore prohibited without revising this document.

## 7. Relationship to the rest of the documentation

- `plan/2026-06-14-aih2-concept-foundation.md` (this file) — **immutable scientific core.**
- `plan/2026-06-14-aih2-design-spec.md` — research/engineering design that *implements* this
  core (dataset schema, modeling, XAI, physical validation, reproducibility).
- `plan/2026-06-14-aih2-phase1-implementation-plan.md` — task-by-task build of Phase 1.

Precedence: **concept foundation > design spec > implementation plan.** A change that
contradicts this file is not a local edit — it is a change to the project's identity and must
be argued and recorded here before propagating downward.

---

*Phase note:* Phase 1 (single-target, synthetic-fixture pipeline) demonstrates the methodology
but does **not** by itself close H1. A submission-ready manuscript requires Phase 1 + core
Phase 2 (shrinking-core regime-switch analysis + SHAP↔physics consistency metric). See design
spec §5.
