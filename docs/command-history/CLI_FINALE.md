# CLI Command — FINALE: wire figures, self-contained build, auto-compile, submission packaging

> Paste into Claude Code at the AIH2 repo root. Figures are approved. Do all CLI-doable finalization,
> set up automatic compilation (removes the local-TeX blocker), and prepare the submission package.
> Leave only the genuine user gates (real author info, Zenodo deposit, final venue sign-off).
> No fabrication; placeholders clearly marked. Commit + push + present, then stop.

## Step 0 — Commit the approved figure work
Commit script + `pubstyle.py` + `FIGURE_PLAN_v2.md` + catalog
(`feat(figures): Q1 re-plan — publication style, accuracy-first encodings, justified 3D`).

## Step 1 — Make the paper self-contained + wire in the figures
1. Copy the 6 final figure **PDFs** into a tracked `paper/figures/` (un-gitignore this folder only)
   so the paper compiles anywhere (Overleaf/CI/local). Set `\graphicspath{{figures/}}`.
2. Wire all 6 into the `.tex` with `\begin{figure}` + `\includegraphics[width=\columnwidth]{...}` +
   captions (from the catalog, `writing-anti-ai` style) + `\label{}` and in-text `\ref{}` at the
   right places (fig2 = headline in Results; fig1 leakage in Results; fig3 particle-size; fig4 Eₐ;
   fig5 dataset; fig6 within-study surface). **No figure left unreferenced.**

## Step 2 — elsarticle frontmatter
Switch `main.tex` to `\documentclass[preprint,12pt]{elsarticle}` with a `frontmatter` block:
`\author{[AUTHOR NAMES — USER INPUT]}`, `\affiliation{[AFFILIATIONS — USER INPUT]}` (clearly
placeholdered), abstract, **Highlights** (3–5 bullets ≤85 chars each), and **Keywords**. Keep an
`article`-class fallback note for local builds.

## Step 3 — Automatic compilation (removes the no-local-pdflatex blocker)
1. Add `.github/workflows/latex.yml`: on push, set up TeX Live, compile `paper/main.tex`
   (latexmk -pdf, with bibtex/natbib), and upload `main.pdf` as a build artifact.
2. Run a local **structural lint** first and fix issues: every `\cite{}` key exists in
   `references.bib`; every `\ref{}`/`\label{}` resolves; every `\includegraphics` path exists; no
   stray `\todocite`. Report the lint result.
   (User can also use Overleaf; the CI is the zero-setup path — PDF downloads from the Actions tab.)

## Step 4 — Data-release prep (Zenodo-ready; user does the deposit)
- Add `.zenodo.json` (title, creators=[AUTHOR PLACEHOLDER], license: data **CC-BY-4.0**, code
  **MIT**, keywords) and `data/README_dataset.md` (a dataset card: files `aih2_v1.csv` (315 yield)
  + `rate_extraction.csv` (76 kinetic), schema, provenance, QC summary, scope lock).
- Add a **Data Availability** statement to the paper with `\todo{Zenodo DOI}` placeholder.

## Step 5 — Submission packaging
- `paper/submission/cover_letter.md` (draft: the gap, the finding, fit for IJHE, integrity/open-data).
- `paper/submission/suggested_reviewers.md` (template; candidates from the cited authors —
  Saceleanu/Wen/Testa/du Preez — with a note to verify no conflicts; user finalizes).
- `paper/submission/IJHE_checklist.md` (artwork specs, sections, declarations, ORCID).
- Venue note: IJHE primary; Energy and AI honest floor.

## Step 6 — Final self-review, status, push, STOP
- `paper-self-review` end-to-end; confirm every number traces, nulls power-framed, associational
  language, abstract↔body, all figures referenced. Update `paper/SELF_REVIEW.md`.
- Update `paper/SUBMISSION_PLAN.md` with a true overall readiness %, and the **only remaining user
  gates**: (1) real author/affiliation/ORCID, (2) Zenodo deposit to mint the dataset DOI,
  (3) final venue sign-off + submit.
- Commit + push. In the final message: report the GitHub Actions compile status + where to download
  `main.pdf`, the lint result, and the remaining-gates list. Present, then stop.

## Rules / Definition of done
- Paper self-contained (figures in `paper/figures/`), all figures wired + referenced, zero
  `\todocite`, structural lint clean, CI compiles `main.pdf`.
- Author/affiliation/Zenodo-DOI left as clearly-marked placeholders — never invented.
- `.zenodo.json`, dataset card, cover letter, suggested reviewers, checklist committed + pushed.
- Final readiness % + 3 user gates reported; pipeline stopped for user.
