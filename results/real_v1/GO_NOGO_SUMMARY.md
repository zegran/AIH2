# GO/NO-GO SUMMARY (2026-06-16)

Two pre-stated tests run before any further figures/SHAP/narrative. Honest reporting; no rescue.

## TEST 1 — flagship within-pure_al_alkali signal: **FAILS**
The within-regime +0.58 is **not** a genuine per-study cross-study signal — it is porciuncula-weighted.
- porciuncula = 120/162 = 74% of the class; it is an easy narrow cluster (yield 93 ± 6.8, no
  particle-size variation) predicted at LOSO skill **+0.93**.
- **study-macro LOSO skill = −0.31** (each study weight 1) vs row-weighted **+0.83** — a ~1.1 gap.
- Only **4/9 studies** beat the class mean (median skill +0.07; large negatives wen −3.3, wanghq −2.4).
- porc-out 5-fold R² stays +0.45 but MAE nearly doubles (9.3→17.2); that positive R² is
  variance-driven, not replication. → SURVIVES bar (study-macro > 0) is not met.
Detail: `TEST1_porciuncula_robustness.md`.

## TEST 2 — physics pillar recoverability: **PILLAR RECOVERABLE** (strongly)
20/31 studies ARRHENIUS-READY across all 5 classes (≥3 in 4 of 5 classes); ~15 report Eₐ directly
(~10–70 kJ/mol, in-band). A literature-Eₐ-per-`system_class` analysis is buildable mostly by direct
extraction. Detail: `data/wp1/RATE_FEASIBILITY.md`.

## Implied paper framing
The two verdicts together **invert the original story**:
- The **ML-predictive headline is dead** (TEST 1). The model does *not* "resolve the contradiction by
  predicting held-out studies within a regime." ML/SHAP must be **demoted to a descriptive lens**.
- The **physics pillar is the real asset** (TEST 2). The defensible contribution is now:
  1. **Leakage demonstration** — naive pooling / random-CV overstates generalization (robust, intact).
  2. **Literature-Eₐ-per-regime physics analysis** — does apparent-Eₐ organize by `system_class` and
     sit in the 3.5–102.6 kJ/mol band? (directly extractable; the "physics-validated" core).
  3. **Rigorous test of the contradiction** via **mixed-effects meta-regression** (study random effect),
     NOT the failed ML CV.
- **Target stays IJHE** (physics-validated), *contingent* on the mixed-effects H2 test + the Arrhenius
  pillar delivering. If the mixed-effects H2 also comes out null, fall back to the
  **leakage-methodology + open-dataset** paper (Energy and AI). The next gate is the mixed-effects model.

## Decision required from user (pipeline stopped here, per brief)
1. Approve the frozen analysis protocol (`plan/analysis-protocol.md`).
2. Approve the **rate-focused second extraction pass** (harvest ~15 reported Eₐ + digitize 5 curve-only
   studies) — this unblocks WP4/H3 and the physics pillar.
3. Only then: run the mixed-effects meta-regression (primary H2 test) + Arrhenius-per-regime.
