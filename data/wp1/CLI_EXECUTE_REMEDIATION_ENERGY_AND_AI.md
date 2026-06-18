# CLI Command — Execute remediation, end-to-end to ENERGY AND AI (Q1) standard — STRICT, skill-gated

> Paste into Claude Code at the AIH2 repo root. **Primary venue is now Energy and AI (Q1); IJHE is
> secondary.** Execute `paper/REMEDIATION_PLAN.md`, re-targeted to Energy and AI's scope and author
> guidelines. This is a **strict, stage-gated** run: a stage may NOT begin until the prior stage's
> REVIEW GATE (a named skill) passes. No fabrication; conclusions unchanged; every added number
> traces to a committed artifact; every added citation is Crossref-verified BibTeX by DOI. Invoke:
> `ml-paper-writing`, `results-analysis`, `citation-verification`, `writing-anti-ai`,
> `paper-self-review`. Commit per stage; push; stop for the user after the final review.

## HARD RULES (binding for every stage)
- A stage's work starts only after the previous stage's REVIEW GATE returns pass; if a gate fails,
  fix and re-run the gate — **do not advance**.
- No invented content or numbers. Added quantities trace to `results/real_v1/*` (or `data/wp1/*`);
  added citations are fetched from Crossref by DOI (never written from memory), tier-tagged.
- Conclusions do not change. Associational (not causal) language. Nulls framed "no detectable effect
  at n≈31 studies / 3–9 per regime."
- **Energy and AI standards govern, not IJHE** (e.g., abstract ≤250 words — do NOT over-trim to 150).

## Stage 0 — Re-baseline for Energy and AI (scope + targets)
- Fetch the live **Energy and AI Guide for Authors**; re-derive targets (abstract ≤250, highlights
  3–5 ≤85 chars, keywords ≤6, article type = **full research article**, numeric reference style).
  Rewrite `paper/submission/COMPLIANCE_REPORT.md` targets to Energy and AI (drop the IJHE-150 rule).
- **Reframe scope (honest):** foreground the **AI/ML methodology** as the contribution — leakage-
  controlled evaluation, mixed-effects meta-regression, between-study variance decomposition, SHAP/
  negative-control, and the **open dataset as a reusable ML benchmark** — with Al–water hydrolysis
  as the application domain. `ml-paper-writing`: tune title + abstract framing to Energy and AI.
- **REVIEW GATE 0:** `paper-self-review` on the new framing (scope fit, no overclaim) → must pass.

## Stage 1 — Citation backfill (28 Tier-A data sources + ~12 Tier-B)
- From `paper/CITATION_COVERAGE.md`, fetch verified BibTeX from Crossref by DOI for all missing
  data-source + domain studies; add to `references.bib` (tier-tagged). Cite each data-source study
  where its data is introduced (Methods sources table + Related work, by regime).
- **REVIEW GATE 1:** `citation-verification` — every new cite resolves and is correctly attributed;
  `tools/lint_paper.py` clean; **every dataset `study_id` is now cited** → must pass.

## Stage 2 — Methods expansion + Tables (data-sources, QC)
- Expand to ~1,150 w per plan: screening funnel, full schema (30 cols, absent=0 vs unreported=NaN),
  double-extraction QC (52/52; dudoladov reclass; ≈1.5% digitization; 13/13 Eₐ), leakage-CV spec,
  variance-decomposition formula + cluster-bootstrap, mixed-effects (REML, study random intercept,
  Holm), Arrhenius gate. Add **Table: data sources** (31 studies × regime/n/ranges) and **Table: QC**.
- **REVIEW GATE 2:** `results-analysis` (methods faithfully describe the committed analyses) +
  `paper-self-review` (every number traces) → must pass.

## Stage 3 — Results expansion + Tables (CV summary, per-class Eₐ)
- Add the 14 committed-but-unreported quantities (REMEDIATION_PLAN §Results table), each traced:
  full per-model CV; porc-out per-model; permutation importance; TEST 1 negative control
  (row-weighted +0.83 vs study-macro −0.31); H2 mixed-effects (p=0.32/0.45/0.41; 0/8 Holm);
  per-class Eₐ medians + η² CI; coverage/power; η²_study=0.496 + within-study skills; SHAP-rank
  stability 0.66–0.70. Add the **"why ML prediction was demoted"** negative-control paragraph. Add
  **Table: CV+variance summary** and **Table: per-class Eₐ**.
- **REVIEW GATE 3:** `paper-self-review` (traceability) + `results-analysis` (no overclaim,
  associational, nulls power-framed) → must pass.

## Stage 4 — Related work + Introduction (Energy and AI framing)
- Expand per plan; lead with the AI/data-science framing + leakage/reproducibility precedent
  (Bernett, John, Suvarna…); engage the Al–water data-source studies organized **by regime**.
- **REVIEW GATE 4:** `citation-verification` + `writing-anti-ai` → must pass.

## Stage 5 — Discussion
- Expand per plan: name the specific contradicting studies per apparent contradiction; the MgH₂/
  biohydrogen round-robin analogues; item-by-item reporting-standard rationale; "predominantly, not
  purely" with `saceleanu2019`; **prominent Limitations** (power n≈31, associational, single-system,
  unvalidated standard, single-author/AI-assisted disclosure).
- **REVIEW GATE 5:** `paper-self-review` (limitations honest, no causal overclaim) → must pass.

## Stage 6 — Energy and AI compliance + Supplementary
- Abstract ≤250 (keep substance — do NOT cut to 150); keywords ≤6; add **funding statement**;
  highlights tuned. Build **Supplementary Material** (full per-study within-study skills, per-study
  Arrhenius fits, full permutation ranking, complete 31-row sources table, coverage tables).
- **REVIEW GATE 6:** `tools/compliance_gate.py` vs the Energy and AI live GfA → must pass.

## Stage 7 — Preventive gates + recompile + final review
- Enable `tools/citation_coverage.py --check` (every dataset study_id cited) and `compliance_gate.py`
  in `lint_paper.py` + CI.
- Recompile via CI; run end-to-end `paper-self-review` + final `writing-anti-ai` sweep + full
  `citation-verification`. Update `COMPLIANCE_REPORT.md`, `SUBMISSION_PLAN.md`,
  `submission_package/MANIFEST.md`.
- Commit per stage (small commits); push. **Present:** compiled PDF, the Energy and AI compliance
  verdict, final word/ref/figure/table counts, and the only remaining user gates (Zenodo DOI; final
  submit). Stop for the user.

## Definition of done
- All sections expanded per plan; refs 18 → 46–58 (every Tier-A data source cited); 4–5 tables +
  Supplementary; abstract/keywords/funding/highlights to **Energy and AI** spec; preventive gates
  enabled; CI compiles; `paper-self-review` + compliance **pass for Energy and AI**; conclusions
  unchanged; committed + pushed + presented; stopped for user.
