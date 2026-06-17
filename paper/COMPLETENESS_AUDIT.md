# Completeness audit — draft (2026-06-17, post-polish)

Honest pass over the five reviewer-kill checks. Fixed where possible; remaining items flagged.

## 1. Reporting-standard contribution — does it exist? → **FIXED**
The abstract/intro/conclusion promise "a minimum-information reporting standard." It previously
existed only as prose. **Now a concrete artifact:** `Table~\ref{tab:mireport}` in Discussion §5.3 — an
11-row checklist ordered by the between-study variance each field carried (temperature control 0.33,
measurement method 0.07, water type 0.04, …). A claimed contribution is now in the text.

## 2. Traceability — every number → committed artifact → **PASS**
All quantitative claims trace (full table in `SELF_REVIEW.md` §1): 315/31 (`aih2_v1.csv`); 76
(`rate_extraction.csv`); optimism gap 0.62–0.85 and 0.48–0.73 porc-out (`RQ_FINDINGS.md`);
method 0.55 / regime 0.02 / temperature_control 0.33 / incremental +0.47 [0.04,0.77]
(`TB_method_variance.md`, `TB_confound_check.md`); particle-size 5/5 (`TA_within_study.md`); Eₐ
η²=0.36, p=0.13, 8.5–58 (`H3_arrhenius.md`); QC 52/52 and ~1.5% (`QC_*`, `H3_*`). The Table~1
$R^2$ values (0.33/0.07/0.04/0.04/0.02) match `TB_method_variance.md`. **No orphan numbers.**

## 3. Open flags — **zero `\todocite`; no fabricated numbers**
- `grep todocite` over `sections/` + `main.tex`: **0**.
- `das2023fuel`: text reads "near-perfect in-sample fit" (no fabricated $R^2$); `references.bib`
  carries `% verified: metadata (exact R^2 NEEDS-FULLTEXT)` — the only NEEDS-FULLTEXT flag.
- `saceleanu2019`: softened to the verified title scope (nano/micro tunable kinetics).
- No `\todo`. One residual omission (xiao 2021 review) documented in `SELF_REVIEW.md` §5.

## 4. Abstract ↔ body consistency — **PASS**
Every abstract claim appears in the body: dataset sizes (Methods §3.1), optimism gap (Results §3.1),
method 55% vs regime 2% + temperature 33% (Results §3.2, Fig.~\ref{fig:variance}), particle-size 5/5
(Results §3.3, Fig.~\ref{fig:particle}), "predominantly methodological" (Results/Discussion),
reporting standard (now Table~1). No headline claim is body-only or abstract-only.

## 5. Figures/tables — **PASS**
5 figures, all `\ref`-erenced in Results; captions self-contained; values match `results/real_v1/`.
Table~1 (reporting standard) added and referenced. `booktabs` loaded. (Compile unverified — no local
TeX; see SUBMISSION_PLAN WP-COMPILE.)

## Polish applied (WP-POLISH)
- Causal→associational: "driver/drives" → "largest single source / accounts for" (3 sites).
- AI-tell scan: clean (no moreover/crucial/delve/landscape/testament/filler found).
- Limitations made complete + prominent: power-limited nulls, associational + study-level-confound
  caveat, Saceleanu finer-physics caveat, thin exploratory classes, T_A predictive null.
- Terminology/units consistent (kJ mol$^{-1}$, mL g$^{-1}$, $R^2$, system\_class).

## Verdict
Content is **complete and internally consistent**; the one prior gap (reporting standard as a real
artifact) is fixed. Remaining work is packaging + user gates (compile, frontmatter, Zenodo) —
see `SUBMISSION_PLAN.md`.
