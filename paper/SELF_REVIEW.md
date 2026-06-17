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

## 2. Causal-language audit — **RESOLVED (polish pass)**
- Headline uses "explain / are associated with", "predominantly", "associationally" — correct.
- "driver/drives" softened to "largest single source / accounts for" (3 sites). No "causes/proves" on
  observational findings.
- "predominantly, not purely, methodological" stated in abstract, results, discussion, conclusion. ✓
- Reporting standard now a concrete table (Table~1); Limitations complete (5/5 items incl. Saceleanu
  finer-physics caveat). See `COMPLETENESS_AUDIT.md`.

## 3. Nulls framing
H2/H3/T_A nulls are framed as **"no detectable effect at n≈31 studies / 3–9 per regime"** (results
within-study null; discussion limitations). No null stated as "no effect exists." ✓

## 4. Novelty
"to our knowledge … single-study in-sample ANN"; "first cross-study synthesis / unified open dataset /
leakage-controlled ML / reporting standard." Matches the Consensus-confirmed GAP and is hedged
("to our knowledge"). ✓

## 5. Citations — **COMPLETE; zero `\todocite` placeholders** (2026-06-17)
18 entries in `references.bib`, each tagged by tier. **full-text-verified** (archive): `wen2018`,
`urbonav2024`, `porciuncula2012`. **metadata-verified** (Crossref/Consensus): the 7 batch-1 refs +
`das2023fuel`, `saceleanu2019`, `pomerantsev2021`, `urbonavicius2023`, `wulf2021`, `hoque2018`,
`musicco2025`, `dupreez2021review` (last two resolved live via Crossref:
`10.1016/j.ijft.2025.101152`, `10.1016/j.ijhydene.2021.03.240`).

**Citation-verification (general-attribution tier) — flags handled honestly, not fixed to fit:**
- ⚠️ **`testa2024` MISMATCH → claim removed.** The only locatable Testa 2024
  (`10.1016/j.ijhydene.2024.08.152`) is an Al--NaOH kinetics study, not the intended round-robin;
  rather than mis-cite it, the round-robin/temperature-control sentence was deleted from Related Work.
- ⚠️ **`das2023fuel` specific number softened.** Metadata-only source; the exact in-sample $R^2$
  ($\approx\!0.998$) was replaced with "near-perfect in-sample fit" and flagged
  `% NEEDS-FULLTEXT` in `references.bib` (confirm against full text before submission).
- ⚠️ **`saceleanu2019` claim softened** from "kinetic$\leftrightarrow$diffusion regime transition"
  to the verified title's scope (tunable nano-/micro-aluminium kinetics).
- ⚠️ **`xiao2021review` omitted.** A 2021 IJHE Xiao review could not be resolved via Crossref; it was
  dropped (redundant with two verified reviews) rather than shipped as a placeholder.
- All other citations are general-attribution and match their cited titles → no further flags.
- **No longer blocking submission** (was item 1). Residual pre-submission task: confirm the Das exact
  $R^2$ against full text if the precise number is wanted; optionally restore a verified Xiao review.

## 6. Figures / compile — **UPDATED (2026-06-17)**
**6 figures** (Q1 re-design), self-contained captions, all referenced (fig1 gap, fig2 variance
[headline], fig3 particle, fig4 Eₐ, fig5 dataset, fig6 within-study surface). The paper is now
**self-contained**: PDFs bundled in tracked `paper/figures/` with `\graphicspath{{figures/}}`, so it
builds on Overleaf/CI/local without the analysis tree.
- **Captions match the v2 figures** — the stale fig1 "per-model bars" / fig3 "Spearman ρ bars"
  wording was corrected to the dumbbell and the points+Theil–Sen encodings.
- **`elsarticle` conversion done** (`[preprint,12pt]`, frontmatter, highlights, keywords; author/
  affiliation/ORCID clearly placeholdered). `elsarticle-num` bibliography.
- **Structural lint clean** (`tools/lint_paper.py`): 18/18 cites resolve, 7/7 refs↔labels, all
  `\includegraphics` paths exist, zero `\todocite` usage. Orphan `experiments.tex` deleted.
- ⚠️ **No local pdflatex** → the actual typeset compile runs in **GitHub Actions**
  (`.github/workflows/latex.yml`); confirm the run is green and download `main.pdf` from the Actions
  tab (Overleaf is the alternative). This is the only step the dev environment cannot self-verify.

## Blocking issues before submission
1. ~~Citations~~ **RESOLVED** — bibliography complete from verified metadata; zero placeholders.
2. ~~Compile path~~ **RESOLVED (mechanically)** — CI workflow added + structural lint clean; the
   remaining action is to confirm the CI build is green (cannot run pdflatex locally).
3. **User gates only:** (a) real author/affiliation/ORCID + CRediT roles, (b) Zenodo deposit to mint
   the dataset DOI, (c) final venue sign-off (IJHE primary / Energy and AI floor).
## Non-blocking polish
- Confirm the Das exact in-sample R² against full text if a precise number is wanted (`% NEEDS-FULLTEXT`).
- Optionally add a funding statement; consider a dedicated graphical abstract (fig2 can serve).

## Stop
Pipeline stopped for user sign-off on the framing and the draft before any submission step.
