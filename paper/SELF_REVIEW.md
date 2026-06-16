# Self-review — methodological-heterogeneity draft (pre-sign-off)

Reviewed against the project's discipline: every quantitative claim traces to a committed artifact;
associational (not causal) language on observational findings; nulls framed as power-limited; novelty
matches the Consensus GAP; citations verified or explicitly placeholdered.

## Verdict: **complete honest FIRST DRAFT; NOT yet submission-ready** (two blocking items below)

## 1. Quantitative-claim traceability (every number → committed source)
| claim in draft | value | source artifact |
|---|---|---|
| dataset size | 315 yield rows / 31 studies | `data/curated/aih2_v1.csv` |
| kinetic table | 76 rows | `data/wp1/rate_extraction.csv` |
| Eₐ band | 3.5–102.6 kJ/mol | literature band (README/concept-foundation) |
| optimism gap | 0.62–0.85 | `results/real_v1/RQ_FINDINGS.md`, `metrics/cv_metrics.csv` |
| random-split R² (trees) | 0.56 / 0.57 / 0.55 | `metrics/cv_metrics.csv` |
| gap after dropping largest study | 0.48–0.73 | `RQ_FINDINGS.md` (porciuncula-out) |
| between-study variance share | ~50% (η²=0.496) | `temp tb_method` / TA |
| regime R² | 0.018 [0.015,0.373] | `TB_method_variance.md` |
| method covariates joint R² | 0.553 [0.361,0.999] | `TB_method_variance.md` |
| temperature_control R² | 0.332 [0.030,0.676] | `TB_method_variance.md` |
| per-level means | 86 / 75 / 32 % | `TB_method_variance.md` |
| coverage 22/7/2; spans 4–5 regimes | — | `TB_confound_check.md` |
| incremental tc\|sc | +0.467 [+0.037,+0.772] | `TB_confound_check.md` |
| incremental sc\|tc | +0.153 | `TB_confound_check.md` |
| isothermal residual range/sd | 26–100 / 18.7 | `TB_confound_check.md` |
| particle-size signs | 5/5 negative, ρ −0.29…−0.87 | `TA_within_study.md`, fig3 |
| liquid_metal Eₐ spread | 8.5–58 kJ/mol | `rate_extraction.csv`, `H3_arrhenius.md` |
| Eₐ regime η²/p | 0.36 / p=0.13 | `H3_arrhenius.md` |
| within-study median skill | −0.145 [−0.45,+0.23]; well-designed 0.84–0.86 | `TA_within_study.md` |
| QC: double-extraction | 52/52 exact | `QC_DOUBLE_EXTRACTION.md` |
| QC: digitization point error | ~1.5% | `H3_arrhenius.md` |
| Das 2023 foil | R²≈0.998 single-study | user/Consensus (cite placeholder) |
**Result: all numbers trace. No untraceable or invented figure found.**

## 2. Causal-language audit
- Headline uses **"explain / are associated with", "predominantly", "associationally"** — correct.
- ⚠️ Minor: the word **"driver/drives"** appears (variance-decomposition sense). It is statistically
  defensible but could read mechanistic; consider "largest single source" on a polish pass. Not blocking.
- "predominantly, not purely, methodological" is stated in abstract, results, discussion, conclusion. ✓

## 3. Nulls framing
H2/H3/T_A nulls are framed as **"no detectable effect at n≈31 studies / 3–9 per regime"** (results
within-study null; discussion limitations). No null stated as "no effect exists." ✓

## 4. Novelty
"to our knowledge … single-study in-sample ANN"; "first cross-study synthesis / unified open dataset /
leakage-controlled ML / reporting standard." Matches the Consensus-confirmed GAP and is hedged
("to our knowledge"). ✓

## 5. Citations — partially resolved (still blocking until complete)
**Batch 1 (7 positioning refs) RESOLVED + verified** (2026-06-17): `bernett2024`, `john2025`
(grouped/leave-group-out CV precedent); `suvarna2024`, `bozalginesta2025` (data science in
catalysis); `coelho2022`, `xue2024` (data-quality/heterogeneity in materials ML); `noble2022`
(meta-analytic nuisance heterogeneity). Verified BibTeX in `references.bib`; PDFs in the user's
downloads. Citation-verification at the general-attribution tier: all 7 titles match the framing
claims they back (no specific quantitative claim is drawn from them) → **no mismatch flags.**
- **Resolved: 7 keys (2 grouped `\citep`).** **Remaining: 15 `\todocite` placeholders** (~13 refs):
  `das2023fuel` (the Das R²≈0.998 foil), `pomerantsev2021`, `urbonavicius2023`, `testa2024`,
  `saceleanu2019` (regime caveat), `wulf2021`, `hoque2018`, `musicco2025`, `xiao2021review`,
  `dupreez2021review`, and dataset studies `wen2018`/`porciuncula2012`/`urbonav2024`.
- **Still blocking:** fetch + verify the remaining ~13 (esp. `das2023fuel` and `saceleanu2019`, which
  back specific claims) before submission.

## 6. Figures / compile
5 figures, self-contained captions, wired to `results/real_v1/figures/*.pdf` (reproducible script).
⚠️ **pdflatex is not installed in this environment → compilation is UNVERIFIED.** Structure checked
(all `\input` targets present, no stray `\end{document}`, `\todocite` defined). Compile on a TeX
machine before submission; an orphan `sections/experiments.tex` (not `\input`) can be deleted.

## Blocking issues before submission
1. **Citations**: fetch + verify all placeholdered references (in flight).
2. **Compile**: verify `main.tex` builds on a LaTeX install; check float placement + undefined refs.
## Non-blocking polish
- Soften "driver"→"largest single source"; add author block/affiliations; consider an elsarticle
  frontmatter conversion; delete orphan `experiments.tex`.

## Stop
Pipeline stopped for user sign-off on the framing and the draft before any submission step.
