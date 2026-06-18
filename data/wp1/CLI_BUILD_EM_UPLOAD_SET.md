# CLI Command — Build the Editorial Manager upload set (one file per required item type)

> Paste into Claude Code at the AIH2 repo root. Produce every file the Energy and AI Editorial
> Manager asks for, one per item type, in `submission_package/upload_ready/`, with an explicit
> upload map. Two required items are currently MISSING (Graphical Abstract; standalone Declaration
> of Interest) — create them. No fabrication; author = Dogukan Unal; conclusions unchanged.
> Commit + push + report paths. Stop for user review.

## Produce these into `submission_package/upload_ready/`

1. **Graphical Abstract** (`graphical_abstract.pdf` + `.png`) — **REQUIRED, missing.**
   Single landscape panel, **1328×531 px (w×h), ≥300 dpi**, fonts ≥7 pt, colorblind-safe (reuse
   `pubstyle.py`). Content = the headline, self-explanatory: between-study yield variance explained
   — **physical regime ≈2% vs methodological covariates ≈55% (temperature-control ≈33%)** — with a
   one-line takeaway "Apparent contradictions are predominantly methodological." Derive from the
   committed numbers (`results/real_v1/metrics`); no new data, no overclaim. Generate via a new
   `src/analysis/figures/graphical_abstract.py` (deterministic, traceable).

2. **Declaration of Interest Statement** (`declaration_of_interest.pdf` + `.docx`) — **REQUIRED, missing.**
   Standalone, standard wording: "The author declares that he has no known competing financial
   interests or personal relationships that could have appeared to influence the work reported in
   this paper." Flag `% AUTHOR: confirm` (in case of any IPEC-related interest to disclose).

3. **Highlights** (`highlights.docx`) — 5 bullets, each ≤85 chars incl. spaces (from `highlights.md`).
   Editable Word file as Elsevier expects.

4. **Cover Letter** (`cover_letter.pdf` + `.docx`) — finalize the existing draft: addressed to the
   Energy and AI editors, corresponding author block (Dogukan Unal, IPEC, dunal@ipec.com.tr, ORCID),
   `[DATE]` placeholder; state the gap, the finding, fit for Energy and AI (AI + energy), open data
   (Zenodo), and the honest AI-assistance disclosure. No overclaim.

5. **LaTeX Source Files** (`latex_source.zip`) — zip `main.tex` + `sections/` + `references.bib` +
   `figures/` (the 6 PDFs) so it compiles standalone.

6. **Supplementary Material** (`supplementary.pdf`) — make `supplementary.tex` a standalone document
   (own preamble) and compile it: add a `supplementary` target to the CI LaTeX workflow (since no
   local pdflatex), or render via tectonic/pandoc if available. If it can only build in CI, note that
   and point to the artifact.

7. **Figures** — copy the 6 vector `figures/fig1–fig6.pdf` into `upload_ready/figures/` (the "Figure"
   item; one file each).

8. **Manuscript** — point to the CI `main.pdf` (download instruction already in
   `manuscript/DOWNLOAD_PDF_FROM_CI.txt`); it is the `*Manuscript` item.

## Upload map → `submission_package/upload_ready/EM_UPLOAD_MAP.md`
A table: EM item type → exact file → status. Cover it for every required (*) item:
`*Cover Letter→cover_letter.pdf · *Declaration of Interest→declaration_of_interest.pdf ·
*Manuscript→main.pdf (CI) · *Highlights→highlights.docx · *Graphical Abstract→graphical_abstract.pdf`;
plus optional: `Figure→figures/fig1–6.pdf · LaTeX Source Files→latex_source.zip · Supplementary
Material→supplementary.pdf · Research Data→Zenodo DOI (stated in cover letter / Data Availability)`.
Flag the 2 author confirmations (DOI statement wording; Zenodo DOI pending).

## Optional (only if user opted in) — Data in Brief co-submission stub
Create `submission_package/data_in_brief/` with a short data-article skeleton (title, dataset
description, value-of-data bullets, methods pointer) referencing the Zenodo dataset. Mark as
OPTIONAL / not required for the Energy and AI submission.

## Rules / Definition of done
- `upload_ready/` contains one file per required EM item type; Graphical Abstract + standalone
  Declaration of Interest created; Highlights/Cover Letter in editable+PDF form; LaTeX zip;
  Supplementary PDF (or CI note).
- `EM_UPLOAD_MAP.md` maps every item type → file → status, with the 2 author-confirm flags.
- Graphical Abstract traces to committed numbers; no fabrication; conclusions unchanged.
- Committed + pushed; exact paths reported; stop for user review.
