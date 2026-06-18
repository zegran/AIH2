# CLI Command — Apply the approved correction plan (4 major + 6 minor), regenerate cited DOCX, recompile

> Paste into Claude Code at the AIH2 repo root. The author APPROVED `paper/REVIEW_RESPONSE_PLAN.md`.
> Apply all 10 fixes exactly as specified there. No fabrication; conclusions unchanged; every edit
> traces to a committed artifact/the plan. Maintain anti-AI style (em-dash ≈ 0, no causal language).
> Regenerate the cited review DOCX (standing rule) and recompile via CI. Commit per logical group,
> push, present a change log, and stop for author review.

## Apply (per REVIEW_RESPONSE_PLAN.md)
**Major:**
- **Q3** — add the reconciliation paragraph (mixed-effects row-level + random intercept absorbing
  study identity & methodology vs. study-level variance decomposition; both consistent); add the
  n=31 / ~6:1 DOF sentence + bootstrap-CI note; add the **mixed-effects display equation** in Methods.
- **Q5** — foreground the AI/ML contribution for Energy and AI: add "machine learning" to keywords;
  add one abstract sentence on the **transferable ML lesson** (leakage-controlled evaluation +
  study-level variance attribution for heterogeneous energy-data ML); ensure title/intro reflect it.
- **Q9** — fix figure ordering/numbering so in-text reference order matches `\label`/`\ref`
  (particle-size vs Eₐ); verify no figure/table is out of sequence after the fix.
**Minor:**
- **Q1** — `results.tex` `0.489`→`0.488`; CI `[0.02,0.37]`→`[0.01,0.37]` (round the lower bound
  **down**, honest); add `deng2010` to the particle-size `\citep` (→ 5/5 matches 5 cites).
- **Q4** — add a **prominent** Limitations sentence on **open-access selection bias**: the 31 studies
  are the OA-reachable subset, not a complete/random sample; state the plausible direction/neutrality
  and that method-covariate status is not expected to correlate with OA status. Do not bury it.
- **Q7** — remove the 2 residual "drives" → associational wording.
- **Q8** — Data/Code Availability: state a **clean public code release** plan (separate from the
  unpublished manuscript / `docs/command-history/`); keep the Zenodo-DOI placeholder flagged.
- **Q10** — state the family of pre-registered tests + multiplicity handling (Holm where used).

## Two senior additions (beyond the plan)
- **Resolve the 2 non-rendering citations** in `main_review.docx` (56/58): identify why they fail
  in pandoc citeproc; confirm the **CI PDF renders all 58** via bibtex. Fix the docx so all render.
- Re-verify **em-dash ≈ 0** across all sections after edits.

## After applying
- Regenerate `submission_package/manuscript/main_review.docx` (pandoc `--citeproc` + numbered CSL,
  figures embedded) — the standing review deliverable; all 58 citations render as [n].
- Recompile via CI; re-run `tools/lint_paper.py` + `citation_coverage.py --check` + `compliance_gate.py`
  + `paper-self-review`. All must stay PASS.
- Write `paper/CHANGELOG_REVIEW_FIXES.md`: each fix → file/line → before→after → "conclusion impact: none".
- Commit per group (`fix(paper): Q3 reconciliation+eq`, `fix(paper): Q5 AI framing`, `fix(paper):
  Q1/Q4/Q7/Q8/Q9/Q10`) + push.

## Definition of done
- All 10 fixes applied per plan + the 2 senior additions; conclusions unchanged (verified per item).
- Gates PASS; CI compiles; `main_review.docx` renders all 58 citations; em-dash ≈ 0.
- `CHANGELOG_REVIEW_FIXES.md` committed; updated DOCX + change log presented; stop for author review.
