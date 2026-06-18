# CLI Command — Apply the 3 IJHE compliance fixes (show abstract before commit)

> Paste into Claude Code at the AIH2 repo root. Apply the three fixes from
> `COMPLIANCE_REPORT.md`. The abstract trim is the only content edit — produce it, **show the
> before/after + word count, and STOP for user approval before committing that change.** The other
> two are mechanical. No fabrication; preserve all reported numbers and honest qualifiers.

## Fix 1 — Abstract → ≤150 words (IJHE limit)
Rewrite the abstract to ≤150 words. **Must preserve, verbatim-equivalent:**
- the contradiction setup (1 short clause: direction-changing particle size + Eₐ spread);
- the dataset (315 yield + 76 kinetic rows, 31 studies, provenance-tracked, open);
- the method in brief (leakage-controlled grouped CV + between-study variance decomposition +
  within-study consistency; pre-registered);
- **the headline numbers exactly:** optimism gap 0.62–0.85; method covariates ≈55% vs regime ≈2%;
  temperature-control ≈33%; particle-size 5/5 within-study consistent;
- the honest conclusion wording: "predominantly methodological", "associational", "at n≈31 studies";
- the deliverables (open dataset + minimum-information reporting standard).
**Framing:** lead with the hydrogen-production research contribution (IJHE has no methods/data
article type) — the dataset + what it reveals — not only the reproducibility critique.
→ Print the OLD abstract, the NEW abstract, and both word counts. **Do not commit until the user
approves the new abstract.**

## Fix 2 — Keywords 7 → 6 (IJHE max)
Drop the weakest/overlapping keyword (recommend removing "methodological heterogeneity", which
overlaps "reproducibility"/"data leakage"). Keep the 6 most discoverable.

## Fix 3 — Funding statement (both journals require it)
Add to the declarations: *"This research received no specific grant from funding agencies in the
public, commercial, or not-for-profit sectors."* — flag `% AUTHOR: confirm no funding (author is at
IPEC; confirm this is accurate)`.

## After approval
- Apply Fix 1 (post user OK) + Fix 2 + Fix 3; rerun structural lint (must stay clean) and trigger
  the CI build; regenerate `paper/preview/` (PDF/DOCX/MD) so the preview matches.
- Update `COMPLIANCE_REPORT.md` verdicts (abstract ✅, keywords ✅, funding ✅).
- Commit (`docs(paper): IJHE compliance — abstract ≤150w, keywords→6, funding statement`) + push.
- Report: new abstract word count, CI status, and confirm only the genuine user gates remain
  (Zenodo DOI, AI-disclosure confirmation, venue sign-off, submission).

## Rules / Definition of done
- Abstract ≤150 words with every headline number and honest qualifier preserved; shown and approved
  before commit. Keywords = 6. Funding statement present (flagged for author confirmation).
- Lint clean; CI green; preview regenerated; committed + pushed. No other content changed.
