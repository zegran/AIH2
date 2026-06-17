# submission_package/

One consolidated place to see and stage everything for submission. Start with **`MANIFEST.md`** — it
indexes every asset (manuscript, figures, paperwork, dataset, plans, tooling) with its canonical path
and status.

## What's physically here vs indexed
- **Here as copies (final/stable):** `dataset/` (the Zenodo Route-A bundle + zip) and `paperwork/`
  (cover letter, highlights, suggested reviewers, IJHE checklist, AI disclosure, compliance report).
- **Indexed by path (will change in the Q1 rewrite):** the manuscript sources (`paper/main.tex`,
  `paper/sections/`, `paper/references.bib`), figures (`paper/figures/`), and build outputs
  (`paper/preview/main.pdf|docx|md`).

This avoids a second, diverging copy of the manuscript source — `paper/` stays the single source of
truth. After the approved rewrite, the final manuscript build will be materialized here as a flat
upload bundle.

## Status
The Q1 remediation is **planned, not executed**. See `paper/REMEDIATION_PLAN.md` (blueprint),
`paper/DIAGNOSIS.md` (why), and `paper/CITATION_COVERAGE.md` (the 28 missing data-source citations).
Approve the plan to proceed with the rewrite.
