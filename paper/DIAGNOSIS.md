# Diagnosis — why the manuscript is thin for Q1 (root-cause analysis)

**Verdict (up front):** the manuscript is thin for two dominant, *additive* reasons, not a content
deficit. (1) **Provenance–bibliography decoupling** — 28 of the 31 studies whose data the paper
analyzes are uncited, which is both an attribution failure and the main reason there are only 18
references. (2) **Results under-reporting** — the primary pre-registered tests (H2 mixed-effects,
TEST 1 leakage control) and the permutation-importance evidence are computed and committed but carry
*no numbers in the paper*. Methods compression and discussion under-engagement compound both. **The
analyses exist and the conclusions hold; the paper under-presents its own committed evidence and
under-attributes its own sources.** The fix is additive — deepen and attribute — not a pivot.

## Problem statement (measured)
- Body + abstract ≈ **2,960 words**; **18 references**; 6 figures, 1 table.
- Q1/IJHE norm for a full research paper: ≈ **5,000–8,000 words**, ≈ **40–80 references**
  (IJHE cap: ≤8000 words / ≤12 diagrams, per the Guide for Authors).
- The dataset is built from **31 source studies** (`data/curated/aih2_v1.csv` +
  `data/wp1/rate_extraction.csv`), and ≈59 studies were ingested with full text on hand.

## Candidate root causes — tested against evidence

### Cause 1 — Provenance–bibliography decoupling — **DOMINANT (references)**
The 18 references were assembled from *positioning* sources (data-leakage/meta-analysis methodology,
field reviews) plus only the 3 data studies cited inline for specific claims. The studies whose data
was actually extracted were never added systematically.

**Evidence** (`tools/citation_coverage.py`, matching the 31 dataset `study_id` DOIs against
`references.bib`): **3 of 31 cited** (`wen2018`, `porciuncula2012`, `urbonav2024`); **28 missing.**
Every missing study has a verified DOI and full text on hand (`canonical_studies.csv`,
`has_md_text=Y`). This is an **attribution obligation**, not optional padding: a paper that analyzes
these studies' data must cite them. Backfilling them alone takes references 18 → **46**.

### Cause 2 — Results under-reporting — **DOMINANT (words + depth)**
Committed analyses are summarized to a single number or omitted entirely. The primary pre-registered
tests are the worst affected.

**Evidence** (results-coverage audit over `results/real_v1/*`):
- **H2 mixed-effects meta-regression — entirely absent.** Computed: `system_class` joint Wald
  p = 0.32 / 0.45 (porc-out) / 0.41 (A/B-tier); 0/8 parameter×regime interactions Holm-significant;
  main effect significant in only 34% of cluster-bootstrap resamples (`H2_mixed_effects.md`). The
  Discussion asserts "no regime moderation" with **no supporting statistic** in any `.tex`.
- **TEST 1 (leakage robustness) — entirely absent.** Row-weighted within-regime LOSO skill +0.83 vs
  study-macro **−0.31**; porc-out MAE nearly doubles (9.3→17.2); only 4/9 studies beat the mean
  (`TEST1_porciuncula_robustness.md`). This negative control is *why* the ML-prediction angle was
  demoted — reportable, currently unreported.
- **Permutation importance — entirely absent.** particle_size #1 (0.60) vs `system_class` #14 (0.03)
  vs alkali_conc #15 (0.01) (`tables/permutation_importance.csv`) — directly corroborates the
  headline; the paper reports zero ML-attribution numbers.
- **Per-class Eₐ medians, full CV table, porc-out per-model values, coverage tables, η²_study exact,
  SHAP-rank stability** — 14 committed quantities total are missing (see `REMEDIATION_PLAN.md` §
  Results). Each is traceable to a committed artifact.

Traceability is sound the other direction: every number currently in `results.tex` resolves to a
committed artifact (one location caveat — the "52/52" QC lives in `data/wp1/QC_DOUBLE_EXTRACTION.md`,
not under `results/real_v1/`; the Das R² is the one acknowledged external-citation softening).

### Cause 3 — Methods compression — **SECONDARY (compounding)**
`method.tex` is **494 words**. The extraction protocol, schema (30 columns), double-extraction QC,
leakage-CV design, between-study variance decomposition, and the mixed-effects specification are each
stated in a sentence. No **data-sources table** exists (the 31 studies, their regimes, n rows,
condition ranges), so the dataset's scale is asserted, not shown. Q1 methods for a data paper run
~1,000–1,300 words plus a sources table.

### Cause 4 — Discussion under-engagement — **SECONDARY (compounding)**
`discussion.tex` is **583 words**. It does not engage the *specific* contradicting studies by name
(e.g. which studies anchor the particle-size disagreement across size ranges), nor the round-robin /
reproducibility analogues from neighbouring fields, and the reporting-standard rationale is asserted
rather than argued item by item.

## Synthesis
Causes 1 and 2 dominate; 3 and 4 compound. Crucially, **none is a content or validity problem** —
the dataset, the pre-registered analyses, and the conclusions are intact and were already verified.
The manuscript simply (a) fails to cite ~90% of its own data sources and (b) reports a fraction of
what it computed. Both are fixed by *adding* — verified-DOI citations and committed numbers/tables —
which simultaneously raises references to ~46–58 and words to the Q1 range **without changing a single
conclusion**. The detailed treatment is in `REMEDIATION_PLAN.md`; the citation matrix in
`CITATION_COVERAGE.md`.
