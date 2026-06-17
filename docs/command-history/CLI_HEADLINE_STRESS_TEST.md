# CLI Command — Two go/no-go tests before any further analysis (senior brief)

> Paste into Claude Code at the AIH2 repo root. **Do NOT produce new figures, SHAP, or narrative
> until both tests below are run and reported.** Purpose: decide whether the headline result is
> real and whether the physics pillar is recoverable — before sinking more effort. Report results
> flat, with the pre-stated decision rules. **No rescue narratives**: if a test fails, say it fails.

Context (do not re-derive): dataset `data/curated/aih2_v1.csv` (315 rows / 31 studies, QC'd).
Primary model `random_forest`. Prior run: global grouped R² = −0.058; within-`pure_al_alkali`
grouped R² = +0.581 (9 studies, 162 rows) — **but `porciuncula2012` = 120/162 = 74% of that
class.** That single fact is why the headline is currently unverified.

---

## TEST 1 — Is the flagship within-`pure_al_alkali` signal real or porciuncula-driven?

Run all of the following on `pure_al_alkali` rows only, `random_forest`, study = CV group.
Use **5 seeds** (0,1,2,7,42); report mean ± sd, never a single seed.

1. **Baseline (reproduce):** within-class grouped CV, FULL pure_al_alkali (9 studies). Report
   grouped R², MAE, and a **skill score vs class-mean baseline** (1 − MSE_model/MSE_meanpredictor).
2. **Porciuncula-out:** repeat with `porciuncula2012` removed (8 studies, ~42 rows). Report same
   metrics.
3. **Leave-one-study-out (LOSO):** within pure_al_alkali, hold out each study in turn; report
   per-study held-out MAE and skill score. Surface explicitly:
   - how well porciuncula is predicted when trained on the other 8 (rows-weighted view);
   - how well the 8 small studies are predicted when porciuncula IS in train (is their accuracy
     inflated by porciuncula spanning the feature space?).
4. **Study-macro vs row-weighted:** report both the pooled (row-weighted) R² and the
   **mean of per-study skill scores (study-macro, each study weight 1)**. A large gap = the
   pooled +0.58 is porciuncula-weighted, not a per-study replication signal.
5. **Distribution check:** yield mean/sd/range and (T, alkali_conc, particle_size) coverage for
   porciuncula vs the rest of pure_al_alkali — is porciuncula an easy narrow cluster?

**Decision rule (state the verdict explicitly):**
- **SURVIVES** ⇔ porciuncula-out grouped R² stays clearly positive (≳0.2) AND study-macro skill
  score is positive (not just porciuncula self-prediction). → headline is a genuine within-regime
  cross-study signal; keep H2 as primary.
- **FAILS** ⇔ porciuncula-out collapses to ≤0, OR the positive pooled R² is essentially
  porciuncula-held-out while the 8 small studies are individually ≤0. → headline is a
  porciuncula artifact; it must be reframed/killed, not salvaged.

Output → `results/real_v1/TEST1_porciuncula_robustness.md` (tables + one-line VERDICT: SURVIVES/FAILS).

---

## TEST 2 — Is the physics pillar (Arrhenius/SCM) recoverable from studies in hand?

The dataset is **yield**-based; Arrhenius Eₐ needs a **rate** metric. Determine, without new
literature, how much kinetic data the 31 archived studies actually contain.

1. Scan `data/raw/literature/md/<citekey>.md` (and PDFs where text is thin) for each in-hand study
   for kinetic indicators: reported **Eₐ (kJ/mol)**, rate constant **k**, **max H₂ rate**
   (mL·min⁻¹·g⁻¹ / mL·s⁻¹·g⁻¹), **t50/t80/time-to-completion**, **H₂-volume-vs-time curves**
   (digitizable), and **number of distinct temperatures** reported.
2. Classify each study: **ARRHENIUS-READY** (reported Eₐ, or rate/k at ≥3 temperatures) ·
   **RATE-READY** (a rate metric or digitizable V(t) at ≥1 T, but <3 T) · **YIELD-ONLY**.
3. Tabulate counts **per `system_class`** (Arrhenius-ready / rate-ready / yield-only).

**Decision rule:**
- **PILLAR RECOVERABLE** ⇔ ≥3 ARRHENIUS-READY studies in ≥2 classes (enough for a per-class Eₐ
  with the 3.5–102.6 kJ/mol band check). → schedule a second, rate-focused extraction pass; keep
  the "physics-validated" framing (IJHE target).
- **PILLAR NOT RECOVERABLE** ⇔ below that. → drop the physics-validation claim; reframe as a
  leakage-controlled methodology paper (Energy and AI fallback). State this plainly.

Output → `data/wp1/RATE_FEASIBILITY.md` (per-study table + per-class counts + one-line VERDICT).

---

## After both verdicts (do this, then STOP for user decision)

Write `results/real_v1/GO_NOGO_SUMMARY.md` with: TEST1 verdict, TEST2 verdict, and the implied
paper framing (mechanism/IJHE vs methodology/Energy-and-AI). Then **freeze the analysis protocol**
in `plan/analysis-protocol.md` (pre-registration): primary hypothesis **H2** (regime moderation
of literature contradiction), confound = `study_id` random effect, planned primary test =
**mixed-effects meta-regression** (ML/SHAP demoted to descriptive secondary), H1/particle-size
declared **exploratory**, multi-seed + study-bootstrap CIs mandatory for any headline number.
Do not run the mixed-effects model yet — stop after the protocol is written and await user sign-off.

## Rules
- Honest reporting only; if TEST1 FAILS, the summary says FAILS — no reframing to hide it.
- Multi-seed for every headline number; report dispersion.
- Prefer MAE + skill-score vs mean-baseline over R² for tiny folds (R² is unstable at n_study≈8).
- Touch no data rows; this is analysis-only. Conventional Commits; durable artifacts English.

## Definition of done
- `TEST1_porciuncula_robustness.md`, `RATE_FEASIBILITY.md`, `GO_NOGO_SUMMARY.md`, and
  `plan/analysis-protocol.md` written and committed; both VERDICT lines explicit; pipeline stopped
  for user decision before mixed-effects modeling.
