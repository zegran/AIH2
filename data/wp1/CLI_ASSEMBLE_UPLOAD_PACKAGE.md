# CLI Command — Assemble the final upload package (one folder) + manuscript PDF/DOCX + separate Zenodo subfolder

> Paste into Claude Code at the AIH2 repo root. Consolidate EVERYTHING to be uploaded into a single
> `submission_package/`. Produce the manuscript as **PDF (figures embedded) and DOCX (figures
> embedded)** for the user to review. Put the **Zenodo files in their own subfolder**, isolated from
> the journal manuscript. Packaging only — change no content. Commit + push + report exact paths.

## Target structure
```
submission_package/
├── MANIFEST.md                 # index: every file + 1-line desc + status + JOURNAL vs ZENODO tag
├── manuscript/                 # → goes to Energy and AI (Editorial Manager)
│   ├── main.pdf                # compiled, figures embedded (authoritative — from CI)
│   ├── main.docx               # figures embedded (review/preview copy)
│   ├── main.tex  + sections/   # LaTeX source
│   ├── references.bib
│   └── figures/                # the 6 figure PDFs (+ PNG previews)
├── paperwork/                  # → journal submission forms
│   ├── cover_letter.md
│   ├── highlights.md
│   ├── suggested_reviewers.md
│   ├── ai_disclosure.md
│   ├── COMPLIANCE_REPORT.md
│   └── energy_and_ai_checklist.md
└── zenodo/                     # → goes to Zenodo ONLY (dataset, no manuscript)
    ├── aih2_v1.csv
    ├── rate_extraction.csv
    ├── data_dictionary.md
    ├── README.md
    ├── LICENSE_CC-BY-4.0.txt
    ├── CITATION.cff
    ├── ZENODO_METADATA.md       # ready-to-paste title/description/creators/keywords/license
    ├── ZENODO_STEPS.md          # click-path
    └── aih2_dataset_v1.zip      # zipped bundle for one-shot upload
```

## Steps
1. **PDF:** take the latest **green CI** `main.pdf` — fetch with `gh run download <run-id> -n <artifact>`
   into `manuscript/main.pdf`. If `gh` is unavailable/unauth, do NOT fake it: leave a note in
   MANIFEST + the Actions URL so the user downloads it manually and drops it in.
2. **DOCX:** `pandoc` `paper/main.tex` → `manuscript/main.docx` with figures embedded
   (`--resource-path=paper/figures`, extract/embed media; resolve `\input` sections). Keep a `main.md`
   too. State in MANIFEST that the **PDF is authoritative**; DOCX is a review/preview copy.
3. **Assemble** the tree above by copying (not moving) from `paper/`, `paper/figures/`,
   `paper/submission/`, and the existing Zenodo bundle. Renumber nothing; change no text.
4. **Verify:** `main.pdf` and `main.docx` both show all 6 figures in place; `zenodo/` contains ONLY
   dataset files (no manuscript, no internal/command-history files); all journal paperwork present;
   `MANIFEST.md` tags each file JOURNAL or ZENODO and flags the 3 open user gates (Zenodo DOI,
   AI-disclosure confirm, reviewers/COI confirm).
5. **Commit** (`docs(submission): assemble final upload package — manuscript PDF/DOCX + isolated
   Zenodo subfolder`) + push. **Report the exact paths** of `submission_package/manuscript/main.pdf`
   and `main.docx` for the user to open, and list `submission_package/zenodo/` contents.

## Rules / Definition of done
- `submission_package/` complete; manuscript present as PDF + DOCX with figures embedded.
- `zenodo/` = dataset-only (verified: no manuscript / internal files inside).
- `MANIFEST.md` indexes everything with JOURNAL/ZENODO tags + the open user gates.
- No content changed; committed + pushed; exact review paths reported. Stop for user review.
