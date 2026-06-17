# CLI Command — Pre-submission PREVIEW PACK (review before anything goes out)

> Paste into Claude Code at the AIH2 repo root. Single author is confirmed: **Dogukan Unal** (lock
> it; drop the "co-authors can be added" note). Produce three review artifacts the user wants to see
> BEFORE depositing/submitting: (1) the exact Zenodo bundle, (2) the manuscript in MD + DOCX + PDF,
> (3) a Q1/IJHE compliance report. Build everything, present it, commit + push, then STOP. No
> fabrication; the LaTeX source remains authoritative.

## Step 0 — Lock single author
Confirm `main.tex` + `.zenodo.json` show exactly one author (Dogukan Unal); remove the co-author note.

## Step 1 — Zenodo bundle preview (so the user sees exactly what will be uploaded)
- Ensure the **Route A dataset-only** bundle exists: `release/aih2_dataset_v1/`
  (`aih2_v1.csv`, `rate_extraction.csv`, `data_dictionary.md`, `README.md`, `LICENSE_CC-BY-4.0.txt`,
  `CITATION.cff`) + zip + `release/ZENODO_METADATA.md`.
- Write `release/ZENODO_PREVIEW.md`: a manifest = file tree + each file's size + row counts for the
  CSVs + the full README and the exact metadata block inline. This is the "what goes to Zenodo" sheet.
- Confirm NO manuscript / internal files are in the bundle.

## Step 2 — Manuscript in three formats
- **PDF (authoritative):** use the green CI build artifact `main.pdf` (download via `gh run download`
  if `gh` is available; else point the user to Actions). If a local TeX toolchain can be installed
  cheaply, compile locally too — otherwise CI PDF is the reference.
- **DOCX + MD (review/preview):** convert with **pandoc** (resolve `\input` sections; embed figures
  from `paper/figures/`): `main.docx` and `main.md` in `paper/preview/`. Install pandoc if missing.
- State clearly in `paper/preview/README.md`: the **PDF is the authoritative typeset version**;
  DOCX/MD are convenience previews (LaTeX-specific formatting/equations may render imperfectly).
- Verify figures appear in-place, captions present, references resolved, Turkish characters correct.

## Step 3 — Q1 / IJHE compliance report (`paper/submission/COMPLIANCE_REPORT.md`)
Measure from the LaTeX source and report a table for **IJHE** and **Energy and AI**:
- **Counts:** abstract word count; total word count; per-section word counts; # figures; # tables;
  # equations; # references; # highlights (+ each ≤85 chars incl. spaces?); # keywords.
- **Structure:** required sections present (Intro, Methods/Data, Results, Discussion, Conclusion);
  declarations present (AI-use, CRediT, Data Availability, Competing Interests, Funding).
- **Artwork:** figures vector PDF, Elsevier sizing/fonts/colorblind-safe — pass/flag each.
- **Journal fit:** **fetch the current "Guide for Authors" for IJHE and Energy and AI** (web) and
  compare against their actual limits (abstract length, highlights rules, structure, reference
  style, article-type fit). Do NOT hardcode limits you cannot verify — cite the fetched guide and
  flag anything that exceeds/misses, with a per-journal verdict: **fit / needs-trim / missing-item**.
- End with a short prioritized fix list (if any) before submission.

## Step 4 — Present + push + stop
- Present to the user: `release/ZENODO_PREVIEW.md` (+ the zip), `paper/preview/main.pdf`,
  `paper/preview/main.docx`, `paper/preview/main.md`, and `paper/submission/COMPLIANCE_REPORT.md`.
- Commit (`docs(paper): pre-submission preview pack — zenodo bundle, multi-format manuscript,
  compliance report`) + push. Stop for user review. Change no scientific content.

## Definition of done
- Zenodo bundle + `ZENODO_PREVIEW.md` (dataset-only, manuscript excluded) ready and shown.
- Manuscript available as PDF (CI), DOCX, MD — figures in place, refs resolved, presented.
- `COMPLIANCE_REPORT.md` with verified IJHE + Energy and AI checks and a per-journal verdict.
- Committed + pushed; pipeline stopped for review; no content changes.
