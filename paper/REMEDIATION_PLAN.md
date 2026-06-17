# Remediation plan — the Q1 blueprint (for approval; not yet executed)

Goal: lift the manuscript from ≈2,960 words / 18 refs to the Q1/IJHE range (≈5,500–6,500 words /
≈46–58 refs, ≤8,000-word cap) by **adding committed evidence and verified-DOI attributions only**.
**No conclusion changes.** Every addition below names the committed artifact or verified DOI that
feeds it — nothing invented.

## Section-by-section blueprint

### Abstract — 196 → **≤150 words** (IJHE fix, not growth)
Trim to the IJHE 150-word cap. Keep problem → dataset → leakage gap → variance result (55/2/33) →
particle-size 5/5 → "predominantly methodological". Cut the second methods clause and one hedge.
*Feeds:* existing content only.

### Introduction — 383 → **~650**
Add: concrete statement of the contradiction with **cited examples** (a study reporting smaller→higher
yield vs one reporting the opposite across size ranges; the Eₐ spread 3.5–102.6); sharpen the gap
(single-study in-sample fits + no cross-study leakage control); expand the contribution list to 4
bullets (dataset, leakage benchmark, methodological-variance finding, reporting standard).
*Feeds:* `musicco2025`, `dupreez2021review`, `das2023fuel`, and 3–4 Tier-A studies for the examples.

### Related work — 243 → **~750**
Reorganize methodologically into: (a) Al–water hydrolysis parameter studies, engaged **by regime**
with the data-source studies named (pure-Al/alkali, alloy, mechanically activated, liquid-metal,
waste) — this is where most Tier-A and ~12 Tier-B citations land; (b) leakage / reproducibility
precedent (already cited); (c) round-robin / measurement-standardization analogues from neighbouring
fields. *Feeds:* Tier-A (28), Tier-B (~12), Tier-C (`bernett2024, john2025, suvarna2024, pomerantsev2021,
noble2022, wulf2021, hoque2018`).

### Data and methods — 494 → **~1,150** (+ Table 1 data-sources, Table 2 QC)
Add: the **screening funnel** (N ingested → 31 extracted, with the Tier-B pool cited); full **schema**
(30 columns, the missing-as-0 vs unreported-as-missing rule); **double-extraction QC** detail
(52/52 exact on 16.5%; the `dudoladov2016` reclassification, class counts 162/19; ≈1.5% digitization
error; 13/13 Eₐ re-read) ; **leakage-CV** spec (6 models, grouped vs random k-fold, imputation);
**variance decomposition** formula and cluster-bootstrap; **mixed-effects** spec (REML, random
intercept per study, Holm); **Arrhenius gate** (R²≥0.90, ≥3 T, fits dropped not forced).
*Feeds:* `QC_DOUBLE_EXTRACTION.md`, `RATE_FEASIBILITY.md`, `method.tex` artifacts, `canonical_studies.csv`.

### Results — 752 → **~1,600** (+ Table 3 CV/variance summary, Table 4 per-class Eₐ)
Add the committed-but-unreported quantities (each traces to an artifact):
| add | numbers | source |
|---|---|---|
| Full per-model CV table | kNN grp −1.49, elasticnet −6.08, GP −0.48, + RMSE/MAE | `metrics/cv_metrics.csv` |
| Per-model porc-out | RF −0.046, LGBM −0.221, XGB −0.145 (still <0) | `metrics/porciuncula_sensitivity.csv` |
| Permutation importance | particle_size 0.60 (#1) vs system_class 0.03 (#14), alkali_conc 0.01 (#15) | `tables/permutation_importance.csv` |
| TEST 1 negative control | row-weighted +0.83 vs study-macro **−0.31**; porc-out MAE 9.3→17.2; 4/9 beat mean | `TEST1_porciuncula_robustness.md` |
| H2 mixed-effects | joint Wald p=0.32/0.45/0.41; 0/8 Holm interactions; 34% bootstrap sig | `H2_mixed_effects.md` |
| Per-class Eₐ medians | 52.0/47.4/36.2/39.2/23.7; η² CI [0.13,0.81] | `H3_arrhenius.md` |
| Coverage / power | particle_size in 19% of rows, 0% in al_alloy & mechanically | `RQ_FINDINGS.md` |
| η²_study exact + within-study | 0.496; 5/14 positive; per-study skills (qiao 0.84, zhang 0.86) | `TA_within_study.md` |
| Method-covariate CIs + level-N | per-covariate R² CIs; level counts | `TB_method_variance.md` |
| SHAP-rank stability | cross-fold Spearman 0.66/0.68/0.70 | `RQ_FINDINGS.md` |

Add a short **"why ML prediction was demoted"** paragraph built on TEST 1 + permutation importance —
turns a deleted angle into an honest negative control. *Feeds:* the artifacts above (all committed).

### Discussion — 583 → **~1,000**
Add: name the **specific contradicting studies** anchoring each apparent contradiction (the 5
particle-size studies; the liquid-metal Eₐ-spread studies 8.5–58); the round-robin/measurement-
standardization analogues; an item-by-item rationale for each **reporting-standard** row (why it
removes a specific cross-study artifact); reinforce "predominantly, not purely" with `saceleanu2019`
within-study physics. *Feeds:* Tier-A studies, `saceleanu2019`, Table 1.

### Conclusion — 305 → **~300** (keep)
Minor: align with the deepened Results; add the funding statement nearby (IJHE fix).

## New tables (4) + Supplementary
- **T1 Data-sources** (Methods): 31 studies × {key, regime, n yield/rate rows, T/conc/size ranges,
  value_origin}. Cites all Tier-A. Full version → **Supplementary** if it crowds the main text.
- **T2 QC** (Methods): double-extraction, classification audit, digitization, Arrhenius gate.
- **T3 CV + variance summary** (Results): per-model random/grouped/gap + variance components w/ CIs.
- **T4 Per-class Eₐ** (Results): median, n, range per regime.
- Existing **Table 1 (reporting standard)** stays (renumber).
- **Supplementary Material:** full per-study within-study skills, full per-study Arrhenius fits, full
  permutation-importance ranking, full coverage tables, the complete 31-row sources table.

## The 3 IJHE compliance fixes (from `COMPLIANCE_REPORT.md`)
1. Abstract → ≤150 words. 2. Keywords 7 → 6 (drop "methodological heterogeneity", subsumed by
"reproducibility"). 3. Add a **funding statement** (e.g. "received no specific grant…", if accurate).

## Projected end-state
| | now | target |
|---|---|---|
| words (abstract+body) | ≈2,960 | **≈5,600** (≤8,000 cap) |
| references | 18 | **46–58** (28 Tier-A + ~12 Tier-B + 18) |
| figures / tables | 6 / 1 | 6 / **4–5** (+ Supplementary) |
Lands in Q1/IJHE range on every axis. Conclusions unchanged.

## Preventive measures (so thinness/attribution gaps cannot recur)
1. **Citation gate:** wire `tools/citation_coverage.py --check` into `tools/lint_paper.py` + CI —
   fails if any dataset `study_id` is uncited. (Enable **after** the Tier-A backfill.)
2. **Compliance gate:** a `tools/compliance_gate.py` (extend `paper_counts.py`) asserting abstract
   ≤150 words, keywords ≤6, references ≥40, every Tier-A cited; run in CI as a non-blocking report
   pre-submission, blocking at the submission tag.
3. **Bib discipline:** every new entry tagged full-text/metadata tier (existing convention); BibTeX
   fetched from Crossref by DOI, never written from memory.

## Execution order (when approved)
1. Backfill 28 Tier-A BibTeX from Crossref (+ ~12 Tier-B) → `references.bib`.
2. Methods + data-sources/QC tables. 3. Results expansion + CV/Eₐ tables. 4. Related work + Intro.
5. Discussion. 6. Abstract trim + keywords + funding. 7. Supplementary. 8. Enable gates; recompile (CI);
re-run self-review + compliance. **Stop after the plan is approved — none of this is executed yet.**
