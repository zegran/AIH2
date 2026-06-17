# CLI Command — Ultrathink diagnosis + Q1 remediation plan + consolidated package (PLAN ONLY)

> Paste into Claude Code at the AIH2 repo root. **Ultrathink first.** Do NOT rewrite manuscript
> content in this run — diagnose the root cause, re-review everything from scratch, design the
> treatment, consolidate all assets (incl. the Zenodo dataset) into one folder, and deliver a
> detailed REPORT + PLAN for the user to approve. Invoke the relevant skills for planning:
> `ml-paper-writing`, `paper-self-review`, `citation-verification`, `results-analysis`,
> `writing-anti-ai`. No fabrication; the plan must map every proposed addition to a committed
> artifact or a verified DOI. Conclusions do not change — the paper deepens, it does not pivot.

## Problem statement (the user's concern, confirmed)
The manuscript is too thin for Q1: **≈2,960 body words and only 18 references**, while the dataset
is built from **~31 source studies**. Q1/IJHE norm is ≈5,000–8,000 words and ≈40–80 references.

## Phase 1 — ULTRATHINK root-cause diagnosis → `paper/DIAGNOSIS.md`
Reason explicitly about WHY it is thin, with evidence. Test at least these candidate root causes:
1. **Provenance–bibliography decoupling:** references.bib (18) was built from positioning refs, not
   systematically from the data sources. Check: how many `study_id` in `data/curated/aih2_v1.csv` +
   `data/wp1/rate_extraction.csv` are **absent** from `references.bib`? (Every data-source study
   must be cited — this is attribution, not optional.)
2. **Results under-reporting:** which analyses in `results/real_v1/*.md` (H2_mixed_effects,
   TB_method_variance, TB_confound_check, TEST1_porciuncula_robustness, TA_within_study,
   porciuncula_sensitivity, cv_metrics, permutation_importance) are computed but **not written into
   `results.tex`**? (e.g., bootstrap CIs, porciuncula-out sensitivity, per-class N, confound check.)
3. **Methods compression:** is the extraction protocol, double-extraction QC, schema, leakage-CV,
   variance-decomposition, and mixed-effects spec fully specified, or compressed?
4. **Discussion under-engagement:** does it engage the *specific* contradicting studies, the
   MgH₂/biohydrogen round-robin analogues, and the reporting-standard rationale?
State the diagnosis + which causes dominate.

## Phase 2 — Full re-review from scratch (evidence base for the plan)
1. **Citation-coverage matrix** → `paper/CITATION_COVERAGE.md`: for every study in the archive
   (`data/raw/literature/`) + pool + `master_dois.csv`, classify: **data-source (MUST cite)** /
   **domain-context (should cite)** / **method-precedent (cited)** / **out**. Mark cited vs missing.
   Output the concrete **target reference list** (with verified DOIs) that takes refs 18 → ~45–60.
2. **Results-coverage table:** each committed analysis → in-paper? where? what's missing.
3. **Figure/table adequacy for Q1:** are 6 figures + 1 table enough? Propose needed **tables**
   (e.g., a *data-sources table* — the ~31 studies with condition ranges, system_class, n rows; a
   *results-summary table* — CV metrics + variance components with bootstrap CIs; a *QC table*).
4. **Section depth audit:** per-section word count vs a Q1 target; flag thin sections.

## Phase 3 — Treatment plan (the Q1 blueprint) → `paper/REMEDIATION_PLAN.md`
A section-by-section rewrite blueprint (do not execute yet):
- For each section: current words → **target words**, what substance to add, **which committed
  artifact / verified DOI feeds it** (no fluff, no invented content).
- New tables + (if warranted) a **Supplementary Material** plan (extended tables, full per-study
  results, QC detail).
- The 3 IJHE fixes (abstract ≤150, keywords →6, funding statement).
- Projected end-state: ≈ target words, ≈ target references, N figures/tables — must land in Q1 range.
- **Preventive measures:** a lint rule that every dataset `study_id` has a citation; a pre-submission
  compliance gate (counts + coverage) wired into `tools/lint_paper.py` / CI so thinness can't recur.

## Phase 4 — Consolidate ALL assets into one folder + manifest
Assemble a single `submission_package/` (tracked) containing/referencing everything correctly:
- `manuscript/` (main.tex + sections, main.pdf, main.docx, main.md), `figures/` (6 PDFs),
  `references.bib`, `highlights`, `cover_letter`, `suggested_reviewers`, `IJHE_checklist`,
  `ai_disclosure`, `compliance_report`.
- `dataset/` = the Zenodo bundle (CSVs, data_dictionary, README, LICENSE, CITATION.cff) + the zip.
- `MANIFEST.md` — an indexed listing of every file with a one-line description + status
  (final / draft / pending-user). This is the "everything in one place, correctly listed" sheet.

## Phase 5 — Deliver + STOP (no content rewrite this run)
- Commit (`docs(paper): Q1 remediation diagnosis + plan + consolidated submission package`) + push.
- Present: `DIAGNOSIS.md`, `CITATION_COVERAGE.md`, `REMEDIATION_PLAN.md`, `submission_package/MANIFEST.md`.
- **Stop for user approval of the plan before executing the rewrite.**

## Rules / Definition of done
- Ultrathink diagnosis written; root cause identified with evidence.
- Citation-coverage matrix + concrete target DOI list (refs → ~45–60); results/figure/table/section
  audits done.
- Section-by-section remediation blueprint with per-item artifact/DOI backing + projected Q1 end-state
  + preventive lint/compliance gate.
- `submission_package/` assembled with `MANIFEST.md` (incl. Zenodo dataset).
- Committed + pushed; **manuscript prose NOT rewritten yet**; stopped for user review.
