# CLI Command — Execute the approved plan: remediation + cleanup + consolidation (objective verification)

> Paste into Claude Code at the AIH2 repo root. Execute `paper/REMEDIATION_CLEANUP_PLAN.md`.
> The audit confirmed: text numbers + DOI are correct; the real issues are stale fig2 in
> `paper/figures/`, DOCX built against it, a weak consistency gate, stale derived files, and
> pre-correction duplicate bundles. Fix all, clean up, consolidate into one clean folder. Verify with
> OBJECTIVE checks (timestamps + content), not "gate passed". No fabrication; conclusions unchanged
> (method ≈72% ≫ regime ≈2%, lead = measurement apparatus). Commit per group, push, deliver, stop.

## B — Remediation (in order)
1. **Figures:** copy ALL corrected figures from `results/real_v1/figures/*.pdf` → `paper/figures/`
   (not just fig2 — verify each of the 6 matches the corrected source by mtime/size). Confirm
   `paper/figures/fig2*` is the Jun-18 corrected one.
2. **Stale derived files:** update `results/real_v1/figures/figure-catalog.md` and
   `results/real_v1/TB_method_variance.md` to the corrected numbers (0.717 joint / 0.425
   measurement_method / 0.081 temperature_control / 0.018 regime). No "0.55 method-share" / "TC 0.33"
   left anywhere in derived files.
3. **Rewrite `tools/consistency_gate.py`** to be strict: (a) require the headline numbers in the
   **abstract AND results** (not just "somewhere"); (b) parse `figure-catalog.md` and assert it
   carries 0.717/0.425, NOT 0.55; (c) assert the OLD method-share 0.55 / "temperature-control … 0.33"
   are ABSENT from all `.tex` + catalog (while leaving the fig1 optimism-gap 0.55 untouched). Wire
   into `lint_paper.py`.
4. **Regenerate the cited DOCX** (`submission_package/manuscript/main_review.docx`) AFTER step 1 so it
   embeds the corrected fig2; confirm mtime newer than the figure copy.

## C — Cleanup (delete stale/duplicate; list each deletion in the report)
- **Delete** `submission_package/dataset/` (pre-correction duplicate, wrong data).
- **Delete** `release/aih2_dataset_v1/` + its zip (old data; superseded by `release/zenodo_v1/`).
- **Fix** the old DOI in `release/aih2_code_v1/README.md`.
- **Delete** `paper/preview/` (stale pandoc preview), `temp/` scratch, and any superseded Zenodo
  planning docs identified in the plan.
- Keep exactly ONE corrected dataset bundle (`release/zenodo_v1/`, which matches
  `data/curated/aih2_v1.csv`). Verify it has 0 `uncontrolled` and equals the canonical CSV.

## D — Consolidate into ONE clean folder (per the plan's Part D tree)
- Make `submission_package/` the single clean deliverable: `manuscript/` (source + figures + CI-PDF
  pointer + corrected cited DOCX), `paperwork/` (cover letter [GitHub-free], highlights, AI
  disclosure, declaration of interest, compliance), `dataset/` = the ONE corrected bundle, and the
  **EM upload set** `upload_ready/` including the still-missing **Graphical Abstract** (built from the
  CORRECTED numbers — 0.72 method vs 0.02 regime, measurement apparatus as lead) and the **standalone
  Declaration of Interest**. Rewrite `MANIFEST.md` tagging each file JOURNAL vs ZENODO + status.
- Remove any remaining duplicate/stale copies so the folder contains only current artifacts.

## Recompile + OBJECTIVE re-verification (not "gate PASS" alone)
- Recompile via CI. Run all gates incl. the new strict consistency gate → PASS.
- Prove, with evidence in the report:
  - `paper/figures/fig2*` == corrected `results/real_v1/figures/fig2*` (mtime/size).
  - `figure-catalog.md` shows 0.717/0.425 (grep), 0 occurrences of method-share 0.55.
  - DOCX mtime > fig2 copy mtime.
  - No `submission_package/dataset/`, no `release/aih2_dataset_v1/`; the surviving bundle == canonical CSV.
  - Grep across `paper/` : new numbers present in abstract+results+discussion+highlights; old
    method-share 0.55 absent; fig1 optimism 0.55 intact.
- Write `paper/FINAL_VERIFICATION_v2.md` with this evidence + the deletion list. Commit per group + push.
- **Deliver:** present the final cited DOCX path + CI-PDF instructions + the clean `submission_package/`
  tree + the verification report. Stop for the user's final check.

## Definition of done
- Corrected fig2 in the paper; DOCX rebuilt on it; strict consistency gate PASS; stale derived files
  updated; all stale/duplicate bundles + previews + temp deleted; ONE corrected dataset bundle ==
  canonical; clean consolidated `submission_package/` incl. Graphical Abstract + Declaration of
  Interest; objective verification evidence in `FINAL_VERIFICATION_v2.md`; committed + pushed; stop.
