# CLI Command — Apply validated critic fixes + independent inter-rater re-extraction (κ/ICC) + recalculation

> Paste into Claude Code at the AIH2 repo root. Execute (not plan-only) the validated items from the
> self-review. The CLI environment may run everything, including a genuine independent re-extraction
> via fresh agents. **Binding integrity rules:** the re-extraction is BLIND (fresh agents, no access
> to the committed codings); κ/ICC are reported **honestly regardless of outcome**; if disagreements
> reveal coding errors, adjudicate against the source, **correct the dataset, and re-run the FULL
> pipeline** — report any changed numbers transparently, never hide a moved headline. New analyses
> are validity/robustness checks (not HARKing). Keep anti-AI style, associational language; gates
> PASS; regenerate the cited DOCX. Commit per stage, push, report, stop for user review.

## Stage 1 — Tier-1 text fixes (confirmed; cheap; no new analysis)
- **M3:** Results §3.4 — replace "explains almost none of it" with point-estimate-plus-uncertainty,
  power-limited wording: "R²=0.018 (cluster-bootstrap 95% CI [0.015, 0.373]); the point estimate is
  low, but the wide interval (upper bound ≈37%) reflects the limited corpus (n=31) and does not
  exclude moderate regime effects."
- **M2:** add an associational caveat **immediately after** the 33% temperature-control result in
  Results §3.4 (study-level covariate; may reflect unmeasured laboratory practice).
- **m1:** Abstract — define inline: "(optimism gap 0.62–0.85, defined as R²_random − R²_grouped)".
- **M9:** add a compact table (end of Methods §2.4 or SI): Hypothesis | Null | Test statistic |
  Threshold | Correction | Outcome — for the four pre-registered tests, from existing values;
  reference it in §2.4 and at each Results subsection opening.
- **Polish:** Acknowledgements → "This research was not supported by external funding."; add a
  single-author CRediT note ("Single-author contribution encompasses all CRediT roles.").
- GATE: `paper-self-review` + `lint_paper.py` PASS.

## Stage 2 — M1: BLIND independent re-extraction + inter-rater κ/ICC (the key fix)
1. Draw a **stratified random sample of ≥60 yield rows (≥20%)** spanning all 5 system_classes and the
   A/B/C tiers, plus ≥15 kinetic rows.
2. Dispatch **fresh independent agents with NO access to the committed codings** to re-extract from the
   SOURCE papers: the high-variance categoricals **`temperature_control` and `measurement_method`**
   (priority), plus `system_class`, and the key numerics `h2_yield_pct`, `temperature_k`.
3. Compute **Cohen's κ** (categoricals) and **ICC** (numerics) between original and blind re-extraction.
4. **If κ ≥ 0.80** on the priority covariates: report agreement (κ, ICC, % exact) in Table 2 + Methods
   + Limitations; upgrade the QC description from intra-rater to **independent-agent inter-rater**
   (state honestly it is independent *agent* re-extraction, not human dual-coding — agents share a
   base model, so model-level systematic error is not fully excluded).
5. **If κ < 0.80** on any covariate: adjudicate every disagreement against the source; **correct the
   dataset**; **re-run the entire pipeline** (variance decomposition, mixed-effects, particle-size,
   Eₐ, figures, tables); report the **updated numbers** and the agreement stats; if the headline
   (method ≫ regime) moves, say so plainly and adjust claims/strength accordingly.
- GATE: `results-analysis` + `paper-self-review` (no hidden change; honest framing of agent-based IRR).

## Stage 3 — Robustness sensitivities (move M5/M6/M10 from "future work" to "done")
- Run, if data permit: **leave-one-study-out** for the particle-size claim; **OA-subset sensitivity**
  (drop any flaggable group) on the headline variance decomposition. Report whether method ≫ regime
  holds; honest regardless. Add a short Results/SI paragraph; update Limitations to reflect they were
  performed. GATE: `results-analysis`.

## Stage 4 — m17: prepare a clean code-only release (user deposits)
- Build `release/aih2_code_v1/` = analysis scripts + `tools/` + figure code ONLY (NO manuscript, NO
  `docs/command-history/`, NO drafts) + a short README + MIT LICENSE + zip. Ready for a Zenodo CODE
  deposit. Leave Data Availability "on request" for now; flag for the user to deposit + switch to a
  code DOI at submission/acceptance (their decision).

## Stage 5 — Rebuild + report
- Recompile via CI; regenerate `submission_package/manuscript/main_review.docx` (cited).
- Re-run all gates (lint, citation_coverage, compliance, self-review) → PASS.
- Write `paper/CHANGELOG_CRITIC_FIXES.md`: each item → change → and for Stage 2 the **κ/ICC values +
  whether any headline number moved**. Commit per stage + push.
- Report: Tier-1 done; κ/ICC results + any recomputation; sensitivities outcome; code bundle ready.
  Stop for user review.

## Definition of done
- Tier-1 fixes applied; M9 table added; abstract/funding/CRediT polished.
- BLIND independent re-extraction done; κ/ICC reported honestly; dataset corrected + full pipeline
  re-run **if** agreement was low; updated numbers transparent.
- Sensitivities run + reported; clean code bundle prepared.
- Gates PASS; CI compiles; cited DOCX regenerated; CHANGELOG committed + pushed; stop for user.
