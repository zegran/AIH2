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

## Modeling verdicts (2026-06-16, after GATE A+B) — both pre-registered, honest

### H2 (mixed-effects meta-regression, primary) → **NOT SUPPORTED** (`H2_mixed_effects.md`)
- system_class main effect non-significant (joint Wald p = 0.32 FULL / 0.45 porc-out / 0.41 A/B-tier).
- 0/8 parameter×system_class interactions survive Holm in any subset (best Holm 0.057).
- Cluster bootstrap: main effect significant in only 34% of resamples. → regime moderation of the
  contradiction is **not defensible** on yield data (consistent with TEST 1).

### H3 (Arrhenius, co-primary) → **NOT robustly supported (PARTIAL)** (`H3_arrhenius.md`)
- **A1** (Eₐ ~ system_class): η²≈0.47 but fragile — primary all-class permutation p=0.18 (REFUTED);
  well-powered 3-class subset p=0.049 (borderline). Descriptive finding real: mechanically_activated
  has lower apparent Eₐ (~24) than pure_al_alkali (~52) / waste_al (~47).
- **A2** (ML↔physics convergence): Spearman ρ=−0.50 (wrong direction) → REFUTED, because **yield is a
  poor temperature-sensitivity proxy** (pure_al_alkali saturates ~93%). A valid A2 needs **rate-based**
  sensitivity → requires digitizing the 5 curve-only rate studies (not yet done).

## Resulting framing (per the protocol's pre-set decision rule)
H2 refuted ∧ H3 partial → the **robust contribution is methodological**:
1. **Leakage / non-poolability** — random CV overstates; study-grouped CV collapses; regime
   conditioning does not rescue it (TEST 1 + H2). Robust.
2. **Curated open dataset** — 315 QC'd yield rows + 73-row kinetic table (CC-BY).
3. **Suggestive (not confirmed) Eₐ regime structure** — mechanically_activated lower Eₐ (A1, borderline).

- **Honest current venue: *Energy and AI*** (leakage-controlled methodology + heterogeneity + dataset).
- **Upside path to *IJHE* (physics-validated):** ONLY if a **rate-based A2** (after digitizing the 5
  curve-only studies + fitting Arrhenius from the tabulated rate-vs-T data, e.g. dudoladov) converts
  H3 from partial to clean support. H1 (particle-size) stays dead/exploratory.

## Decision required from user (pipeline STOPPED here, per brief — no figures/writing)
1. **Accept the *Energy and AI* methodology+dataset framing now** (write up the robust results), OR
2. **Invest one more round: rate-curve digitization → rate-based A2** to attempt rescuing H3 into IJHE
   territory (bounded effort: 5 studies to digitize + ~3 tabulated rate-vs-T Arrhenius fits).
3. Either way: H1 and the ML-prediction headline remain retired; ML/SHAP stays descriptive.
