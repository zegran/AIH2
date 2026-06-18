# CLI Command — Standing DOCX deliverable + reviewer question pack → ultrathink correction PLAN (approve before applying)

> Paste into Claude Code at the AIH2 repo root. Two parts. **(A) New standing rule:** from now on,
> alongside your own output, always produce a **publication-quality, properly-cited DOCX** of the
> current manuscript so the user can review/edit. **(B)** Ultrathink the reviewer question pack
> below, investigate each against the source/results, and write a **correction PLAN** — do NOT apply
> changes yet; stop for user approval. No fabrication; conclusions must not change; every proposed
> fix maps to a committed artifact or verified DOI; if a question exposes a real weakness, say so.

## Part A — Standing deliverable: cited, review-ready DOCX (do this now, every run hereafter)
- Generate `submission_package/manuscript/main_review.docx` via `pandoc --citeproc` with a
  **Vancouver/Elsevier-numbered CSL** + `references.bib`, figures embedded, sections resolved.
  Fix the earlier citeproc failure (reformat the single-line BibTeX / pass `--bibliography` +
  `--csl` correctly) so citations render as **[n]** with a numbered reference list — not raw keys.
- State in the file header: this DOCX is for author review/editing; the **CI PDF remains
  authoritative** for final typesetting.
- Going forward, regenerate this DOCX after any manuscript change.

## Part B — Reviewer question pack (ultrathink each; evidence from source + `results/real_v1/`)
Investigate and answer each in the plan, with: **finding** (with file/line or artifact),
**severity** (blocker / major / minor), **proposed fix** (mapped to a committed artifact/DOI),
**conclusion impact** (must be "none").

1. **Numerical consistency:** Do ALL headline numbers match across abstract, results, discussion,
   figures, tables, highlights, AND the graphical abstract — 55/2/33%, optimism gap 0.62–0.85,
   particle-size 5/5, n=31 studies, 315 yield + 76 kinetic rows, per-class N (162/19/…)? List any drift.
2. **Citation integrity:** Any **orphan references** (in `references.bib` but never `\cite`d)? Any
   `\cite` key with no bib entry? Is `das2023`'s softened claim consistent and the `NEEDS-FULLTEXT`
   flag resolved or clearly retained? Any over-reliance on a few sources?
3. **Reconcile the two core analyses:** The mixed-effects result (regime×parameter interactions
   n.s.) and the variance decomposition (method covariates ≈55%) — does the manuscript explain how
   they are mutually consistent? Is the ≈55% **robust to the small-n / many-covariate degrees-of-
   freedom concern** (not overfit), and is "variance explained" formally defined?
4. **Selection-bias disclosure:** The 31 studies are the **open-access-reachable subset**, not a
   complete or random sample of the literature. Could OA-only retrieval bias the methodological-
   variance finding? Is this explicitly disclosed in Limitations? (If not — add it; it's real.)
5. **Energy-and-AI framing:** Is the **AI/ML methodological contribution foregrounded enough** for
   this journal (leakage-controlled evaluation + variance attribution as a transferable lesson for
   energy-data ML), or does it read as a chemistry meta-analysis with light ML? Should the
   title/abstract/intro lift the AI-methodology angle?
6. **Formal model specs:** Methods has **0 display equations**. Should the variance-decomposition
   and mixed-effects models be written as explicit equations (reviewers expect formal specification)?
7. **Causal vs associational:** Does any sentence slip into causal language ("drives/causes/proves")
   given the observational design? Verify nothing residual after the earlier "driver" softening.
8. **Code availability:** Is the analysis code cited with a plan for a **clean public release** at
   submission (without exposing the unpublished manuscript / `docs/command-history/`)? Reconcile with
   the Data Availability statement.
9. **Numbering/order:** Tables T1–T6 numbered consistently and cited in order; figures referenced in
   order; the reporting-standard table renumbered correctly; no dangling `\ref`.
10. **Multiple-testing + multiplicity:** Is the family of pre-registered tests stated and multiple-
    comparison handling disclosed (Holm where used)?

Also re-confirm the four already-raised items in the plan: (i) citation style = numbered Vancouver
(correct, no APA); (ii) negatives are framed as alternative-ruling-out controls (keep — integrity);
(iii) em-dash reduction to ≈0; (iv) lighten the heaviest content-parentheses. And fix the **stale
"International Journal of Hydrogen Energy" comment** in `main.tex` + confirm `\journal{Energy and AI}`.

## Output → `paper/REVIEW_RESPONSE_PLAN.md`, then STOP
- The plan: per-question finding/severity/fix/conclusion-impact, ordered by severity, with an
  overall verdict (how many blockers/major/minor) and a projected end-state.
- Generate `main_review.docx` (Part A) now so the user can review in parallel.
- Commit (`docs(paper): cited review DOCX + reviewer question pack + correction plan`) + push.
- **Do NOT apply manuscript changes.** Present the plan + the DOCX path; stop for user approval.

## Rules / Definition of done
- `main_review.docx` renders proper [n] citations + reference list (citeproc fixed).
- `REVIEW_RESPONSE_PLAN.md` answers all 10 questions + the 4 prior items with evidence, severity,
  artifact-mapped fixes, and "conclusion impact: none" verified per item; honest about any real
  weakness (esp. Q3 overfit, Q4 selection bias).
- Committed + pushed; no manuscript prose changed yet; stopped for user approval.
