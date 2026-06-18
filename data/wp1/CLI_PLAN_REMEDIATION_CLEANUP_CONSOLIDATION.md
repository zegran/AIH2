# CLI Command — PLAN ONLY: audit + remediation + cleanup + consolidation into ONE clean folder

> Paste into Claude Code at the AIH2 repo root. **Produce a PLAN; do NOT execute, edit, or delete
> anything.** Investigate (one pass) under the directions below, then write a single reviewable plan.
> Use OBJECTIVE checks (file timestamps + actual content), never "a gate passed" as proof. Stop for
> user approval.

## Verified concerns to confirm/resolve (the senior review found these — audit each)
1. **fig2 (headline figure) is STALE.** `figure-catalog.md` still reads "method ... 0.55 ... vs 0.02";
   `fig2_variance_decomposition.pdf` mtime predates the data correction → it was NOT regenerated. It
   must show the corrected 0.717 (joint) / measurement_method 0.425 / temperature_control 0.081.
2. **DOI not in conclusion.tex Data Availability.** `10.5281/zenodo.20751918` was found in
   supplementary/cover-letter/checklist but NOT in `conclusion.tex` — verify the primary DA statement.
3. **DOCX not regenerated** (`main_review.docx` mtime unchanged at 15:30) — review copy is stale.
4. **Number propagation likely incomplete:** the corrected values (0.717/0.425/0.081) appear to be in
   `discussion.tex` only; confirm/deny presence in **abstract (main.tex), introduction, results,
   highlights, and every table**.
5. **consistency_gate.py is too weak:** it only checks the new numbers exist somewhere in the `.tex`
   (discussion satisfies it) — it does NOT check figures, does NOT assert OLD numbers are absent, and
   does NOT require per-section presence. Hence its false PASS.
6. **The "other 0.55" (fig1 random-split optimism gap) is correct and must stay** — do not conflate.

## Part A — Audit (objective; one pass)
- For each concern 1–6, verify against the real files (mtime + grep the actual content) and record
  CONFIRMED / NOT-CONFIRMED with evidence.
- **Inventory every artifact** and tag each **CURRENT** (canonical or freshly-derived) vs **STALE**
  (pre-correction / duplicate / orphan / superseded):
  - Dataset bundles: `data/curated/aih2_v1.csv` (canonical), `release/zenodo_v1/`,
    `submission_package/zenodo/`, `submission_package/dataset/` — which are corrected vs old; which
    duplicate which.
  - Figures: `results/real_v1/figures/*` (which predate the correction); the figure scripts.
  - Results/metrics: `results/real_v1/*` + any fixture-era outputs — which reflect corrected data.
  - Manuscript copies/DOCX: `paper/` (canonical source), `submission_package/manuscript/`,
    `paper/preview/`, `main.docx` vs `main_review.docx` — which are stale duplicates.
  - Misc: `temp/`, `paper/preview/`, old command files, `docs/command-history/`.
- State the **single source of truth** for each artifact type (data, figures, manuscript, dataset
  bundle) so everything else can be regenerated from it or deleted.

## Part B — Remediation plan (content fixes; map each to its source)
For concerns 1–5, write the exact fix steps + how each will be **objectively verified** (mtime newer
than the correction commit; grep shows new numbers in the named files; grep shows ZERO stale
method-share 0.55 / temperature-control-as-lead; fig2 catalog + PDF updated). Include: regenerate
fig2 (+ any other correction-affected figure/table) by running the figure script; insert DOI into the
conclusion DA; propagate numbers to abstract/intro/results/highlights/tables; regenerate the cited
DOCX; **rewrite consistency_gate.py** to (a) cross-check figure-source values, (b) assert old numbers
are absent, (c) require the headline numbers in the abstract + results, not just somewhere.

## Part C — Cleanup plan (what to DELETE — list explicitly, with rationale)
Propose a deletion list: every stale/duplicate/orphan artifact — old/duplicate Zenodo bundles (keep
ONE corrected), pre-correction figure outputs, fixture/pre-correction results, stale manuscript/DOCX
copies, `paper/preview/`, the duplicate `submission_package/dataset/` vs `zenodo/`, `temp/` scratch,
and (propose: keep or archive) the `data/wp1/CLI_*.md` command history. For each item: path, why
stale, and the canonical replacement. **Nothing deleted in this run — list only.**

## Part D — Consolidation plan (ONE clean folder)
Define the final single deliverable folder (e.g., a clean `submission_package/`) and its exact tree:
final manuscript (source + CI PDF + cited DOCX + figures), paperwork, the EM upload set (incl. the
still-missing Graphical Abstract + Declaration of Interest), ONE corrected dataset bundle, and a
MANIFEST. Everything derived is regenerated fresh from the single source of truth; everything stale
is gone. Note what is canonical-in-repo vs packaged-for-submission.

## Output, then STOP
- Write `paper/REMEDIATION_CLEANUP_PLAN.md`: Part A audit findings (CONFIRMED/NOT, evidence) ·
  Part B remediation steps + objective verification · Part C explicit deletion list · Part D final
  folder tree. Commit the plan doc + push. **Execute nothing; delete nothing.** Present the plan; stop.

## Rules
- Plan only — no edits, no regeneration, no deletion this run.
- Objective evidence (mtime + content) for every audit claim; no reliance on prior "gate PASS".
- Conclusions unchanged; the corrected thesis (method ≈72% ≫ regime ≈2%, lead = measurement
  apparatus) is the target end-state.
