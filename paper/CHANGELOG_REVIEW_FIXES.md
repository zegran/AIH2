# Changelog — Review Fixes (approved plan applied 2026-06-18)

All fixes trace to `paper/REVIEW_RESPONSE_PLAN.md`. Conclusion impact: **none** for every item.

---

## Major fixes

### M1 — Q3: Mixed-effects / variance-decomposition reconciliation
**File:** `paper/sections/discussion.tex`
**Location:** After first paragraph of "What the contradictions are, and are not"
**Before:** No reconciliation; H2 null and T_B 55% figure stated consecutively without explanation.
**After:** Added paragraph explaining that T_B is a study-level regression (n=31 aggregated rows) attributing between-study variance to study-level covariates, while H2 is a row-level mixed-effects model (n=299) whose random intercept absorbs all between-study heterogeneity. Both consistently show that regime explains little relative to methodology.
**Conclusion impact:** None.

### M2 — Q3/Q6: Mixed-effects display equation + DOF note
**File:** `paper/sections/method.tex`
**Location:** (a) After bootstrap CI sentence in variance-decomp subsection; (b) after mixed-effects prose paragraph.
**Before:** Variance decomposition had Eq. (1) but mixed-effects was prose-only; no DOF context.
**After:**
- Added DOF note: "With n=31 study-level observations and five individual predictors, the effective degrees-of-freedom ratio is approximately 6:1; the cluster-bootstrap CIs reflect this limited precision directly."
- Added Eq. (2): $y_{ij} = \mu + \sum_k \beta_k \mathbf{1}[\text{class}_j=k] + \boldsymbol{\gamma}^{\top}\mathbf{x}_{ij} + u_j + \varepsilon_{ij}$, $u_j \sim \mathcal{N}(0,\sigma_u^2)$, $\varepsilon_{ij} \sim \mathcal{N}(0,\sigma^2)$, REML.
**Conclusion impact:** None.

### M3 — Q5: Energy-and-AI framing
**File:** `paper/main.tex`
**Before:** Keywords: 6 (no "machine learning"); abstract ended without transferability sentence.
**After:**
- Keywords: replaced "open dataset" with "machine learning" (still 6, journal limit).
- Abstract: added concise transferability sentence: "The evaluation framework generalizes to any energy-domain machine-learning application where training and test records share group structure, such as laboratory or protocol identity." Abstract stays at 249 words (limit 250). ✓
**Conclusion impact:** None.

### M4 — Q9: Figure citation order violation
**File:** `paper/sections/results.tex`
**Before:** Figure environments in source: ..., fig:particle (~line 193), fig:ea (~line 203), ... but text cites fig:ea (line 100) before fig:particle (line 138) → PDF would number them 4/5 in reverse citation order.
**After:** Swapped the two `\begin{figure}...\end{figure}` blocks so environment order is: gap, variance, ea, particle, surface — matching the text citation order exactly.
**Conclusion impact:** None.

---

## Minor fixes

### m1 — Q1: Three numerical drifts
**Files:** `results.tex:162`, `main.tex` abstract, `conclusion.tex`
- `in_wt_pct` permutation importance: 0.489 → **0.488** (matches SI-2 source table).
- Regime bootstrap CI lower bound: [0.02, 0.37] → **[0.01, 0.37]** in abstract and conclusion (honest downward rounding of 0.015).
- Particle-size 5th study: added **`deng2010`** to `\citep{zhang2024,...,deng2010}` in discussion.tex (5 cites for 5/5 studies).

### m2 — Q4: Open-access selection bias
**File:** `paper/sections/discussion.tex`, Limitations paragraph "Single material system and open-access bias"
**Before:** One sentence noting OA bias without direction analysis.
**After:** Expanded to: the 31 studies are the OA-reachable subset, not a complete/random sample; no mechanistic reason OA status correlates with temperature-control method or measurement protocol; null expectation is no directional bias on the primary finding; direction cannot be verified from current corpus; external validation would resolve this.

### m3 — Q7: Causal language ("drives")
**Files:** `method.tex:146`, `results.tex:165`
- "what **drives** between-study disagreement" → "what **accounts for** between-study disagreement"
- "methodology rather than regime **drives** apparent yield differences" → "**accounts for** apparent yield differences"
(Instance at results.tex:114 — "drives the null finding" — retained as mechanical, not causal.)

### m4 — Q8: Code availability
**File:** `paper/sections/conclusion.tex`
Added sentence: "The Zenodo deposit comprises the curated dataset, analysis scripts, and figure-generation code only; draft manuscripts, command history, and other internal workflow artifacts are excluded from the public release."

### m5 — Q10: Pre-registered family
**File:** `paper/sections/method.tex`, Discipline subsection
Added paragraph: "The pre-registered family comprises four primary tests: H2 (mixed-effects regime moderation of yield), H3 (activation-energy regime structure), T_A (within-study predictability), and T_B (between-study variance decomposition). Holm correction is applied to all secondary interaction tests within H2 (8 parameter×system_class terms)."

---

## Senior additions

### S1 — Fix all 58/58 DOCX citations
**Files:** `paper/references.bib`
- Root cause: the section-header comment lines (`% ==== Tier A ==== @article{prabu2021,...}`) placed the first entry of each tier on a `%`-prefixed line, which BibTeX/pandoc treats as a comment → entries invisible to citeproc.
- Fix: regex split to place `@article` entries on clean lines after the comment headers.
- Also fixed 5× Unicode HYPHEN (U+2010) in author fields → ASCII hyphen-minus.
- Result: pandoc citeproc now renders **all 58/58** citations as `[n]` with no warnings.

### S2 — Em-dash reduction (prior item iii re-verified)
The earlier bash grep on Windows returned a false negative (empty). The Grep tool confirms em-dashes remained in prose. All prose `---` converted to commas, parentheses, or colons across:
- `introduction.tex`: 1 instance (optimism gap sentence)
- `method.tex`: 2 instances (screened papers list; regressor list)
- `results.tex`: 4 instances (porciuncula parenthetical; collapse sentence; permutation importance)
- `discussion.tex`: 5 instances (subsection title; temp-control sentence; kinetics parenthetical; fields parenthetical; leakage gap sentence)
- `related_work.tex`: 3 instances (alkali solution; grouped CV; round-robin standards)
- `conclusion.tex`: 2 instances (infrastructure list; checklist relative clause)
Table `---` entries (empty cells) retained.

---

## Gate results after all fixes

| Gate | Result |
|------|--------|
| compliance_gate.py | **PASS** (abstract 249 w, 6 keywords) |
| lint_paper.py cite check | 58/58 keys defined and cited |
| pandoc DOCX citeproc | **58/58 citations [n]**, 0 warnings |
| Em-dash count (prose) | **0** remaining |

Warnings retained (pre-existing, not blockers):
- 2 highlight bullets >85 chars (cosmetic)
- 2 `\todo{Zenodo DOI}` placeholders (expected pre-submission)
