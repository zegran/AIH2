# CLI Command — Insert Zenodo DOI + remove ALL GitHub links from the manuscript

> Paste into Claude Code at the AIH2 repo root. The dataset is published:
> DOI **10.5281/zenodo.20750297** (https://doi.org/10.5281/zenodo.20750297;
> record https://zenodo.org/records/20750297). Insert it; remove every GitHub reference from the
> manuscript and citation metadata. No content/conclusion changes otherwise. Recompile, regenerate
> the cited DOCX, keep all gates PASS, commit + push, present, stop.

## 1. Insert the DOI
- Replace `\todo{Zenodo DOI}` (conclusion.tex Data Availability) with:
  "The curated dataset is openly available at Zenodo, https://doi.org/10.5281/zenodo.20750297
  (CC-BY-4.0)." Cite the DOI, not a repo.
- Update `submission_package/zenodo/CITATION.cff` + `paper/`-side CITATION (if any): set
  `doi: 10.5281/zenodo.20750297`.

## 2. Remove ALL GitHub links/references from the manuscript + metadata
- Grep the whole `paper/` tree (and `submission_package/manuscript/`) for `github.com`, `zegran/AIH2`,
  `github`, and remove/replace every occurrence:
  - Data Availability: data → the Zenodo DOI (above).
  - **Code availability:** replace any GitHub URL with: "Analysis code is available from the
    corresponding author on reasonable request." (No GitHub link. A clean public code release may be
    added at acceptance.)
  - Remove the GitHub link from `CITATION.cff` (`repository-code:` field) — delete it; keep only the
    Zenodo `doi`.
  - Remove any stale GitHub URLs in `main.tex` comments / footnotes / `.zenodo.json`.
- After editing, grep again to confirm **zero** `github` / `zegran` occurrences remain in
  `paper/` and `submission_package/manuscript/`.

## 3. Rebuild + verify
- Recompile via CI; regenerate `submission_package/manuscript/main_review.docx` (cited, all refs [n]).
- Re-run `tools/lint_paper.py` + `citation_coverage.py --check` + `compliance_gate.py`
  + `paper-self-review` → all PASS. Confirm no `\todo` placeholders remain (the Zenodo one is now resolved).
- Commit (`docs(paper): insert Zenodo DOI 10.5281/zenodo.20750297; remove all GitHub links`) + push.

## 4. Report (for the user — these are user actions, not CLI)
- Confirm: 0 GitHub references remain; DOI inserted; gates PASS; updated DOCX path.
- Remind the user (do not perform): (a) **make the GitHub repo private during review** (it holds the
  unpublished manuscript + AI command-history); CI still runs on private repos. (b) **Remove the
  GitHub "Related works" link on the Zenodo record** (it points to that repo). (c) A clean code-only
  public release can be created at acceptance for code availability.

## Definition of done
- DOI inserted (conclusion + CITATION.cff); **zero** GitHub references in manuscript/metadata;
  code availability reworded; gates PASS; CI compiles; cited DOCX regenerated; committed + pushed;
  user reminded about repo privacy + Zenodo related-work link. Stop for user.
