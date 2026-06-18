# CLI Command — TWO STAGES: (1) prepare fresh Zenodo upload set → STOP for DOI; (2) insert DOI + propagate ALL corrections + deliver

> Paste into Claude Code at the AIH2 repo root. The old Zenodo record was DELETED; we do a fresh
> upload. Run **STAGE 1 only**, then STOP and wait for the user's new DOI. Do NOT start STAGE 2 until
> the user provides a DOI. No fabrication; conclusions unchanged (the thesis holds and is
> strengthened); honest inter-rater framing; em-dash ≈ 0; gates PASS.

---

# STAGE 1 — Prepare the fresh Zenodo upload set (run now; then STOP)

1. **Regenerate the dataset bundle from the CORRECTED data** (the old bundle in
   `submission_package/zenodo/` is pre-correction — rebuild it). Into `release/zenodo_v1/`:
   - `aih2_v1.csv` (current corrected 315-row file: Trowell & Martínez-Vargas TC→isothermal_bath;
     Porciuncula measurement→other; "uncontrolled" category eliminated) + `rate_extraction.csv`.
   - `data_dictionary.md` (reflect corrected categories), `README.md` (note: corrected dataset;
     independent-agent re-extraction κ→1.0 after correcting 3 coding errors), `CITATION.cff`
     (version 1.0.0, `doi:` left blank/placeholder), `LICENSE_CC-BY-4.0.txt`.
   - Zip → `release/zenodo_v1/aih2_dataset_v1.zip`.
   - **Verify:** 0 occurrences of `uncontrolled` in the TC column; Trowell rows = isothermal_bath;
     bundle is dataset-only (no manuscript / internal files).
2. Write `release/zenodo_v1/ZENODO_FILL_GUIDE.md` — exact field-by-field values for the fresh upload:
   - Files: drag the 6 loose files (not the zip). Visibility: Public. Community: skip.
   - DOI: **"No, I need one."** · Resource type: **Dataset**.
   - Title: `Aluminum–Water Hydrolysis Hydrogen-Yield and Kinetics Dataset (provenance-tracked, leakage-aware), v1.0`
   - Publication date: today. · Author: **Unal, Dogukan**, ORCID 0009-0006-5102-8013,
     IPEC, Industrial Project Engineering Consulting, Çankaya, Ankara, Türkiye.
   - Description: the dataset paragraph (31 studies, 315 yield + 76 kinetic rows, scope, accompanies
     the manuscript). · License: **CC-BY-4.0**. · Keywords (≤6) · Language: English · Version: `1.0.0`
     · Publisher: Zenodo. · **No GitHub "Related works" link** (repo kept private).
3. Present the bundle path + `ZENODO_FILL_GUIDE.md`. **STOP. Wait for the user's new DOI.**

---

# STAGE 2 — ONLY after the user provides the new DOI (e.g. "10.5281/zenodo.NNNN")

1. **Insert the DOI:** conclusion.tex Data Availability + `CITATION.cff`; remove any old/placeholder DOI.
   Copy the corrected `release/zenodo_v1/` files into `submission_package/zenodo/` (sync).
2. **Propagate the CORRECTED numbers EVERYWHERE** (they are currently only in Discussion):
   - Joint method variance share **0.55 → 0.72** (CI [0.443, 1.000]); regime **0.02 unchanged**.
   - **New lead factor: `measurement_method` R²=0.425** (single largest); `temperature_control`
     **0.332 → 0.081**; the **"uncontrolled" TC category is eliminated**.
   - Update: **Abstract, Results** (variance-decomposition reporting + the new lead factor +
     per-covariate values & CIs), **Discussion** (narrative lead = measurement apparatus, not
     temperature control), **Highlights**, **all tables** (CV/variance summary).
   - ⚠️ **Do NOT touch the OTHER 0.55:** fig1 / Results report random-split CV R²≈0.55 (optimism gap),
     which is UNCHANGED by the correction. Only the variance-decomposition 0.55→0.72 changes.
   - **Regenerate fig2** (variance decomposition) with the new numbers + update `figure-catalog.md`;
     check fig4/Eₐ and any table for correction-affected values and regenerate if needed.
3. **Document the inter-rater result:** raw κ (TC 0.43, measurement 0.70) → 3 corrections → post-
   correction κ=1.0 / ICC; list the corrections; place in Methods/QC Table 2 + Limitations (upgrade
   intra-rater → **independent-agent** inter-rater; state honestly it is agent-based, not human).
4. **Cleanups:** remove the GitHub residual in `paper/submission/cover_letter.md`; fix any stale
   "IJHE" → "Energy and AI" in checklists.
5. **Add a numerical-consistency gate** `tools/consistency_gate.py`: assert the headline values
   (0.72, 0.02, 0.425, 0.081) are identical across abstract/results/discussion/highlights/tables AND
   the fig2 source data; wire into `lint_paper.py` + CI so figure↔text drift cannot recur.
6. Recompile via CI; regenerate `submission_package/manuscript/main_review.docx` (cited, current).
   Re-run all gates (lint, citation_coverage, compliance, **consistency**, paper-self-review) → PASS.
7. **Independent re-verification:** grep the whole manuscript to confirm **zero** residual old
   variance-share numbers and that 0.72 / measurement_method appear consistently everywhere; confirm
   fig2 shows the new numbers.
8. Write `paper/FINAL_VERIFICATION.md` (all numbers consistent across text+figures, gates PASS, DOI
   inserted, fig2 current, IRR documented) + update CHANGELOG. Commit per group + push.
   **Deliver:** present the final PDF (CI) + cited DOCX + FINAL_VERIFICATION. This completes the work.

## Definition of done (Stage 2)
- DOI inserted; corrected numbers propagated to every section + fig2 + tables (the other 0.55 left
  intact); IRR/κ documented; cover-letter GitHub removed; consistency gate added + PASS; all gates
  PASS; CI compiles; cited DOCX current; FINAL_VERIFICATION committed + pushed + presented.
