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

## H3 rate-based re-test (Option 1) — DONE → **second null** (`H3_arrhenius.md`)
Executed with full discipline: digitized 4 curve-only studies (QC point-error ~1.5%), Arrhenius fits
under an R²≥0.90 gate (dropped rin2021 R²=0.846 and ho2016 unreadable/confounded — no forced fits),
provenance recorded. `liquid_metal_activated` grew 1→4 Eₐ.
- **A1 REFUTED:** with the honest 4-study liquid_metal Eₐ (spread **8.5–58 kJ/mol**), η² fell 0.47→0.36;
  permutation p=0.13 (≥3-study, 4 classes) / 0.22 (all). system_class does **not** significantly explain
  the Eₐ spread; within-regime spread ≈ between-regime spread.
- **A2 REFUTED:** ML↔physics convergence undefined without a rate-target model (honesty clause, not
  redefined to pass); yield-proxy ρ=−0.20.

## FINAL DECISION (per the pre-committed binding rule) — single venue
**A1 refuted ∧ A2 refuted → H3 NOT clean support → STOP. No third attempt.**

➡️ **Venue: *Energy and AI*** — a **leakage-controlled methodology + curated open-data** paper.
Confirmed robust contributions:
1. **Naive pooling overstates generalization** (optimism gap 0.62–0.85, robust to dropping the
   dominant study; within-regime ML signal is porciuncula-weighted — TEST 1 + H2 null).
2. **The literature does not reduce to a tidy per-regime physics signal** — apparent Eₐ does not
   organize by system_class (within-regime spread ≈ between-regime spread). An honest, substantive
   negative result against the "regimes resolve the contradictions" expectation.
3. **Curated, QC'd open datasets** — 315-row yield table (0% double-extraction value error) + 76-row
   kinetic table (Eₐ/rate, provenance + heterogeneity, 13/13 Eₐ QC-exact).

Retired for good: H1 (particle-size), the ML-prediction headline, and the IJHE physics-validated claim.
ML/SHAP remain descriptive only.

**Pipeline STOPPED for user sign-off on this framing — no WP5 figures, no paper drafting yet.**
