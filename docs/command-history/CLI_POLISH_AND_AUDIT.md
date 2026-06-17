# CLI Command — WP-POLISH + completeness audit (no user gate)

> Paste into Claude Code at the AIH2 repo root. Bring the draft to the most-complete state CLI can
> reach without the user gates (authors, TeX compile, Zenodo), and produce an **honest completion
> audit** so the user knows the true remaining %, not a self-report. No fabrication; no causal
> overclaim; pre-registered claims and transparent nulls preserved. Commit + push + stop.

## Step 1 — Completeness audit (write `paper/COMPLETENESS_AUDIT.md`)
Answer each explicitly, fix what you can, flag the rest:
1. **Reporting-standard contribution — does it actually exist?** The abstract promises "a
   minimum-information reporting standard." Confirm it is a concrete table/appendix in the draft.
   **If missing, write it** (Step 3). A claimed contribution that isn't in the text is a reviewer kill.
2. **Traceability:** every quantitative claim in the draft traces to a committed artifact in
   `results/real_v1/`. List any number that does not trace; fix or remove. No orphan numbers.
3. **Open flags:** list every `% NEEDS-FULLTEXT`, `\todo`, `\todocite`, and softened claim. Confirm
   `das2023` keeps abstract-supported wording (no fabricated R²); confirm zero `\todocite` remain.
4. **Abstract ↔ body consistency:** every abstract claim is supported in the body (and vice-versa
   for headline claims).
5. **Figures/tables:** all figures referenced in text; captions complete; every figure number
   matches the corresponding value in `results/real_v1/`.

## Step 2 — WP-POLISH
- `writing-anti-ai` sweep: remove AI-tells, filler hedges, repetitive scaffolding; tighten prose.
- Causal→associational softening throughout: `driver` → `largest single source` / `most associated
  with`; no "causes/drives/proves" on observational findings.
- `paper-self-review` end-to-end; update `paper/SELF_REVIEW.md`.
- Make the **Limitations** subsection prominent and honest: power-limited nulls ("no detectable
  effect at n≈31 studies / 3–9 per regime"), observational (associational) attribution, the
  Saceleanu genuine-regime caveat, thin exploratory classes, the T_A predictive null.
- Enforce consistent terminology, notation, units, and number formatting.

## Step 3 — Write the reporting standard (if Step 1 found it missing)
Add a concrete **minimum-information reporting checklist for aluminum–water hydrolysis studies**
(table/appendix), derived from the dataset schema and the covariates that carried the between-study
variance: **temperature-control method, measurement method, reaction vessel, water type, particle
size (D50), alkali type/conc, rate definition, and full provenance**. Frame it as the paper's
constructive output: standardized reporting would shrink the methodological variance the paper
quantifies. Keep it specific and checklist-form, not vague prose.

## Step 4 — Honest status + housekeeping + push, then STOP
- Update `paper/SUBMISSION_PLAN.md` with a true per-WP % and an overall submission-readiness %.
- State plainly what is now CLI-complete vs the 3 user gates (author/affiliation; a TeX-compile
  path — recommend Overleaf as fastest, optionally add a GitHub Actions LaTeX CI YAML; Zenodo
  account for the dataset DOI).
- Archive the pasted command files: move `data/wp1/CLI_*.md` into `docs/command-history/` (tracked)
  as the governance trail of this project.
- Commit (`docs(paper): polish + completeness audit + reporting-standard table`) and push. Working
  tree clean. Stop for the user.

## Rules / Definition of done
- `COMPLETENESS_AUDIT.md`, updated `SELF_REVIEW.md`, the reporting-standard table, and updated
  `SUBMISSION_PLAN.md` committed + pushed.
- Zero `\todocite`; every number traceable; no fabricated content; limitations honest and prominent.
- User gates (authors, TeX build, Zenodo) left untouched and clearly listed. Pipeline stopped.
