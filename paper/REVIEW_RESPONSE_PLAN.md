# Reviewer Question Pack — Correction Plan

> **Status:** PLAN ONLY — do NOT apply manuscript changes until author approves.
> Generated: 2026-06-18. Target journal: Energy and AI (Elsevier).
> Verdict: **0 blockers / 4 major / 6 minor** — submission-ready after major fixes.

---

## Overall Verdict

| Severity | Count | Action |
|----------|-------|--------|
| Blocker  | 0     | — |
| Major    | 4     | Must fix before submission |
| Minor    | 6     | Fix before submission; each is one sentence or a two-line change |

Core headline numbers (55%/2%/33%, gap 0.62–0.85, n=31, 315+76 rows) are consistent
across abstract, highlights, results, discussion, and conclusion. No fabrication risk.
Conclusions do not change for any item below.

---

## Q1 — Numerical Consistency

**Finding:**
Three minor drifts detected:

1. `in_wt_pct` permutation importance: `results.tex:162` says **0.489**;
   `supplementary.tex` Table SI-2 says **0.488**. Off by 1 in the last decimal.

2. Regime CI rounding: abstract and conclusion report **[0.02, 0.37]** (2 d.p.);
   `results.tex:59` gives **[0.015, 0.373]** (3 d.p.). Rounding 0.015 → 0.02 is
   technically upward — inflates the lower bound. Should be "[0.01, 0.37]" or use 3 d.p.
   consistently.

3. Particle-size citation gap: text says "5/5 studies" (abstract, results, discussion)
   but discussion.tex:29 cites only 4 papers for the within-study effect:
   `{zhang2024,prabu2021,wen2018,porciuncula2012}`. The 5th study is `deng2010`
   (title: "Role of Particle Sizes in Hydrogen Generation by the Reaction of Al with
   Water") — confirmed in supplementary Table SI-1 as a pure_al_alkali study. It must
   be added to the discussion citation list.

All core headline numbers verified consistent: R²≈0.55 random / R²<0 grouped ✓,
gap 0.62–0.85 (tree models) ✓, 5/5 particle-size direction ✓, n=31 / 315+76 rows ✓,
55%/2%/33% decomposition ✓, per-class N (162/45/69/19/20) sum to 315 ✓.

**Severity:** Minor

**Proposed fix:**
- `results.tex:162`: change `0.489` → `0.488` (match the SI-2 source table).
- Abstract and conclusion CI: change `[0.02,\,0.37]` → `[0.01,\,0.37]` (round 0.015 down).
- `discussion.tex:29`: add `deng2010` to the particle-size citation:
  `\citep{zhang2024,prabu2021,wen2018,porciuncula2012,deng2010}`.

**Conclusion impact:** None — cosmetic numerical consistency only.

---

## Q2 — Citation Integrity

**Finding:**
All 58 cited keys have bib entries; all 58 bib entries are cited — no orphaned or
missing references. **Clean.**

- `das2023fuel`: NEEDS-FULLTEXT flag honored. Text attributes only "near-perfect
  in-sample fit" (related_work.tex:55–57) without specific R² numbers. ✓
- `xiao2021review` and `testa2024`: documented as RESIDUAL in bib header comment,
  not in the bib, not cited. ✓
- `\todocite` macro defined in main.tex but unused in all section files. ✓
- No over-reliance: `porciuncula2012` cited frequently because it is the dominant
  study (120/315 rows); this is explained and appropriate. ✓
- `urbonavicius2023` (2023 IJHE paper on vessel insulation) and `urbonav2024` (2024
  Materials paper on plasma treatment) are distinct entries. ✓

**One technical note:** pandoc citeproc emitted warnings for `prabu2021` and
`razavi2016` during DOCX generation. Both entries are syntactically present and
correct in the reformatted bib file; the warnings likely reflect a character-encoding
mismatch between the auto-fetched Unicode author field (`Hong‐Wen`, U+2011 non-breaking
hyphen) and pandoc's citation key resolver. LaTeX/BibTeX compilation is unaffected.
The DOCX renders 56/58 citations as numbered references.

**Severity:** Minor (DOCX-only technical note; no manuscript change needed)

**Proposed fix:** In the reformatted `references.bib`, replace the Unicode non-breaking
hyphen in `prabu2021`'s author field with a standard ASCII hyphen-minus.

**Conclusion impact:** None.

---

## Q3 — Reconcile the Two Core Analyses

**Finding (Major):** Two sub-issues.

### 3a — Missing reconciliation sentence

The paper presents (a) mixed-effects null H2 (no regime moderation, p=0.32–0.45) and
(b) variance decomposition showing method ≈55% >> regime ≈2%. Discussion section
"What the contradictions are" (discussion.tex:1–13) states both findings consecutively
but never explicitly explains why they are mutually consistent.

A reader may ask: if methodology explains 55% between-study variance, why does the
mixed-effects model—which includes methodology in spirit (via between-study random
effects)—still fail to detect regime moderation? The answer: the two analyses operate
at different levels. The variance decomposition is a study-level OLS (n=31 aggregated
rows), attributing between-study variance to study-level covariates. The mixed-effects
model is a row-level regression (n=299 rows) that absorbs all unmodeled between-study
heterogeneity into a random intercept per study — so the random intercept absorbs
methodology and study identity together, leaving regime as the only tested fixed effect.
They are not in tension: (i) says "methodology explains the gap between studies";
(ii) says "even after controlling for between-study noise, regime doesn't predict yield
within studies." This reconciliation is currently absent.

### 3b — Overfit / DOF concern for the 55% figure

n=31 study-level observations, 5 individual methodological covariates tested (and 1
joint model with 5 parameters). At 31/5 ≈ 6:1 ratio, overfitting is plausible. The
current bootstrap mitigates this: the lower CI bound on method-joint R² is 0.361
(excluding zero), and temperature-control alone achieves 0.332 with a CI excluding 0.
This is adequately reported. However, the paper does not explicitly state the sample
size (n=31 studies) in the variance decomposition section, nor mention the DOF concern
and why bootstrap bounds address it. Reviewers will raise this.

"Variance explained" is formally defined via Eq. (1) (method.tex:150–153): ✓

### 3c — Missing mixed-effects model equation

The mixed-effects meta-regression is described in prose (method.tex:164–173) but has
**no display equation**. For a methods paper at this venue, reviewers expect formal
specification.

**Severity:** Major (3a and 3c); Minor (3b)

**Proposed fix:**
- Add one paragraph in Discussion after the current first paragraph reconciling the
  two analyses: mixed-effects operates on row-level data with a random intercept
  absorbing all unmodeled study-level differences (including methodology); variance
  decomposition is a study-level analysis. Both consistently show that regime, not
  methodology, is the residual discriminator.
- Add one sentence in method.tex variance-decomp subsection: "At n=31 study-level
  observations, the DOF:predictor ratio is approximately 6:1; the cluster-bootstrap
  CIs (which resample complete studies) reflect this limited precision."
- Add a display equation for the mixed-effects model in method.tex:
  `$y_{ij} = \mu + \sum_k \beta_k \mathbf{1}[\text{class}_{j}=k] + \boldsymbol{\gamma}^{\top}\mathbf{x}_{ij} + u_j + \varepsilon_{ij}$`
  where $u_j \sim \mathcal{N}(0, \sigma_u^2)$, $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2)$, REML.

**Conclusion impact:** None — reconciliation clarifies the existing findings; numbers
and claims do not change.

---

## Q4 — Selection-Bias Disclosure

**Finding:**
The Limitations section (discussion.tex:131–135) currently reads: "Open-access
retrieval may bias the sample toward English-language, higher-impact, more-systematic
studies; we mitigate this with a quality tier and report the access constraint here."

The CLI question asks: **could OA-only retrieval bias the methodological-variance
finding specifically?** This is a real concern. Systematic, well-funded studies are
more likely to be open-access AND more likely to control their protocols carefully
(standardized temperature, known particle size). If the paywall-gated studies are
predominantly less systematic, including them would likely *increase* the observed
methodological variance — meaning the 55% figure could be a lower bound. However,
if paywall-gated studies are primarily from more controlled facilities, the direction
reverses. The current text does not address this direction question.

**Severity:** Minor (disclosure is partially present; needs one strengthening sentence)

**Proposed fix:**
Append to the existing sentence in the "Single material system and open-access bias"
paragraph: "The direction of this bias on the methodological-variance finding is
unknown: if paywall-gated studies are less protocol-controlled, the true methodology
share may exceed 55%; if they are more controlled, it could be lower. External validation
using a broader corpus—including non-OA studies obtained through inter-library access—
would resolve this."

**Conclusion impact:** None.

---

## Q5 — Energy-and-AI Framing

**Finding (Major):**
`\journal{Energy and AI}` is confirmed correct (main.tex:19). The ML framing is
present in the abstract (leakage-controlled, six comparative models, optimism gap) and
the related work section (last two paragraphs).

Two gaps for an Energy and AI audience:

**5a — Missing "machine learning" keyword:** Current keywords are
`aluminum--water hydrolysis`, `hydrogen production`, `data leakage`,
`meta-analysis`, `reproducibility`, `open dataset`. None names machine learning,
AI, or cross-study generalization explicitly. Energy and AI editors and reviewers
search by keyword.

**5b — Transferable ML lesson not foregrounded in abstract:** The abstract ends
with "We release the curated dataset, the reproducible analysis pipeline, and a
proposed minimum-information reporting checklist." The AI-methodology angle — that
this is a transferable benchmark showing how leakage-controlled grouped CV exposes
generalization failure in energy-data ML — is stated in related work but not in the
abstract. Energy and AI readers care about whether the methodological lesson
generalizes beyond one reaction system.

**Severity:** Major (5a is a one-word fix; 5b is one sentence)

**Proposed fix:**
- Add `\sep machine learning` to the keyword list (main.tex:63), making 7 keywords.
- Append one sentence to the abstract after "... across laboratories": "The
  leakage-controlled evaluation framework is transferable: any energy-domain ML
  study in which training and test data share group structure (lab, protocol,
  electrode batch) risks the same optimism gap we quantify here."

**Conclusion impact:** None — editorial framing adjustment only.

---

## Q6 — Formal Model Specifications

**Finding:**
Variance decomposition Eq. (1) is present (method.tex:150–153). ✓

The mixed-effects meta-regression is described in four prose sentences
(method.tex:164–173) but has **no display equation**. For a venue like Energy and AI
that publishes ML-heavy methods, reviewers expect a formal specification: the linear
predictor, random effect structure, and estimation method.

**Severity:** Major (addressed together with Q3c above)

**Proposed fix:** Add display equation as specified in Q3c. The proposed form
formalizes what is already described in prose; no new information is introduced.

**Conclusion impact:** None.

---

## Q7 — Causal vs Associational Language

**Finding:**
Three instances of "drives" remain in the manuscript:

1. `method.tex:146`: "To identify **what drives** between-study disagreement, we
   aggregate..." — In a methods sentence introducing the decomposition analysis. Mild
   but technically causal framing for an observational study.

2. `results.tex:114`: "the within-regime spread **drives** the null finding" — Here
   "drives" describes a mechanical consequence within the analysis (the within-class
   spread inflates the denominator of the effect size), not a causal claim about
   physical reality. Acceptable as-is.

3. `results.tex:165`: "methodology rather than regime **drives** apparent yield
   differences" — This is in the permutation importance summary and asserts a
   directional attributional claim. Should be softened.

All other causal-language checks passed. No "causes", "proves", "leads to", "results
in" found. The Discussion, Limitations, and Discipline sections use "associational"
language throughout. ✓

**Severity:** Minor

**Proposed fix:**
- `method.tex:146`: "what drives" → "what accounts for"
- `results.tex:165`: "drives apparent yield differences" → "accounts for apparent
  yield differences"
- Leave `results.tex:114` unchanged (mechanical, not physical causation claim).

**Conclusion impact:** None.

---

## Q8 — Code Availability

**Finding:**
Two `\todo{Zenodo DOI}` placeholders remain:
- `conclusion.tex:18`: in the Data and Code Availability statement
- `supplementary.tex:16`: in the supplementary contents note

The GitHub URL is provided (https://github.com/zegran/AIH2). The code is described
as MIT-licensed. These placeholders are expected pre-submission TODOs.

**No plan exists** in the manuscript for excluding internal workflow artifacts
(e.g., `docs/command-history/`, draft manuscript files) from the public release.
The CLI explicitly flags this. The Zenodo deposit should include only:
- The curated dataset (`data/` or equivalent clean export)
- The analysis pipeline (`analysis/` or `src/`)
- Figure-generation scripts
- The bib file and dataset card

It should NOT include: draft manuscripts, command history logs, internal plan docs,
API keys or `.env` files, intermediate scratch outputs.

**Severity:** Minor (the Zenodo DOI is an expected pre-submission gap; the release
scope note is a one-sentence clarification)

**Proposed fix:**
- Add one sentence to the Data Availability section: "The deposit excludes
  internal workflow artifacts (draft manuscripts, command history); only the
  dataset, analysis pipeline, and figure scripts are deposited."
- Create `tools/RELEASE_CHECKLIST.md` listing what to include/exclude from
  the Zenodo deposit (not a manuscript change).

**Conclusion impact:** None.

---

## Q9 — Numbering / Order

**Finding (Major):**
**Figure citation order violation.** In the compiled PDF, LaTeX numbers figures in
the order their `\begin{figure}` environments appear in the source. In `results.tex`,
figure environments appear in this order at the end of the file:

| Environment label | Source order | Expected PDF number |
|-------------------|-------------|---------------------|
| `fig:gap`         | 1st (line ~171) | Figure 2 |
| `fig:variance`    | 2nd (~181)  | Figure 3 |
| `fig:particle`    | 3rd (~192)  | Figure 4 |
| `fig:ea`          | 4th (~203)  | Figure 5 |
| `fig:surface`     | 5th (~212)  | Figure 6 |

(`fig:dataset` in method.tex is Figure 1.)

However, in the results **text**, the citation order is:
`fig:gap` (line 29) → `fig:variance` (line 61) → `fig:ea` (line 100) →
`fig:particle` (line 138) → `fig:surface` (line 151).

`fig:ea` is cited in the text BEFORE `fig:particle`, but in the source the
`fig:particle` environment comes BEFORE `fig:ea`. In the compiled PDF this means
the text references Figure 5 (ea) before Figure 4 (particle) — a LaTeX citation
order warning and potential reviewer flag.

**Tables T1–T5:** all cited in order within the text (T1 in method, T2 in method,
T3 in results, T4 in results, T5 in discussion). ✓

**No dangling `\ref`** found. ✓

**Filename vs. compiled number mismatch** (cosmetic only): `fig5_dataset_composition.pdf`
will compile as Figure 1 in the PDF. Filenames don't affect LaTeX numbering but may
confuse future maintenance.

**Severity:** Major (figure numbering order violation)

**Proposed fix:**
In `results.tex`, swap the figure environments: move the `fig:ea` environment block
(lines ~203–210) to appear BEFORE the `fig:particle` environment block (lines ~192–201).
After the swap the environment order becomes: gap, variance, ea, particle, surface —
matching the citation order in text.

**Conclusion impact:** None — no text changes, only figure environment reordering.

---

## Q10 — Multiple-Testing / Multiplicity

**Finding:**
Holm correction is stated throughout: "all parameter×system_class interactions use
Holm correction" (method.tex:172), "incremental comparisons and cross-tabulations
use Holm correction throughout" (method.tex:161), and results report "0/8 Holm-corrected
interactions" and "bootstrap 95% CI excludes 0" for the primary decomposition.

The pre-registered hypothesis family is described (H2, H3, T_A, T_B). However, the
**number of pre-registered primary tests** is never stated explicitly. A reviewer may
ask: "how many hypotheses were pre-registered, and was the overall family-wise error
rate controlled?"

**Severity:** Minor

**Proposed fix:**
Add one sentence in the Discipline subsection (method.tex): "The pre-registered
family comprises four primary tests (H2: mixed-effects regime moderation; H3:
activation-energy regime structure; T\_A: within-study predictability; T\_B:
between-study variance decomposition); Holm correction is applied to all secondary
interaction tests within H2."

**Conclusion impact:** None.

---

## Prior Items Carried Over (4 items from earlier review rounds)

### (i) Citation style = numbered Vancouver
**Status: Resolved.** `\bibliographystyle{elsarticle-num}` in main.tex renders
numbered references matching Elsevier/Energy and AI requirements. ✓

### (ii) Negatives framed as alternative-ruling-out controls
**Status: Resolved.** Null results are consistently framed as "not supported at
this sample size" or "no detectable effect at n≈31 studies". No language claiming
proof of absence. ✓

### (iii) Em-dash reduction
**Status: Resolved.** `grep` for `---` in all section files returns zero matches
(excluding table rules and code that uses `---`). ✓

### (iv) Lighten heaviest content-parentheses
**Status: Substantially resolved.** Spot-check of introduction and method sections
finds no multi-clause parenthetical blocks. The longest surviving parenthetical is
"(not yet prospectively validated; see Section~\ref{sec:limitations})" — one clause,
acceptable. No action needed. ✓

---

## Stale Comment Fix (already applied)

`paper/main.tex` line 1 comment updated: "International Journal of Hydrogen Energy
submission" → "**Energy and AI** submission". This was a pre-existing stale comment;
`\journal{Energy and AI}` was already correct on line 19. ✓

---

## Part A — DOCX Status

`submission_package/manuscript/main_review.docx` generated via:
```
pandoc main.tex --bibliography=references.bib --csl=elsevier-vancouver.csl \
  --citeproc -o main_review.docx
```

- Citations render as **[n]** numbered references ✓
- 56/58 citations resolved; 2 warnings (`prabu2021`, `razavi2016`) due to Unicode
  author field in auto-fetched BibTeX — fix: replace U+2011 non-breaking hyphen with
  standard hyphen-minus in `prabu2021`'s author field.
- `references.bib` reformatted: auto-fetched entries moved from one long line to
  individual entries (was causing `citeproc: unexpected end of input` at line 119).
- DOCX is for author review/editing; **CI PDF remains authoritative** for final typesetting.

---

## Ordered Action List (by severity)

### Major — fix before submission

| # | File | Change |
|---|------|--------|
| M1 | `paper/sections/discussion.tex` | Add reconciliation paragraph after para 1 explaining how mixed-effects H2 and variance decomp T_B are mutually consistent |
| M2 | `paper/sections/method.tex` | Add display equation for mixed-effects model (mixed-effects subsection, after prose description) |
| M3 | `paper/main.tex` | Add `\sep machine learning` keyword; add one abstract sentence foregrounding the transferable leakage-CV lesson |
| M4 | `paper/sections/results.tex` | Swap `fig:ea` and `fig:particle` figure environments to match text citation order |

### Minor — fix before submission

| # | File | Change |
|---|------|--------|
| m1 | `results.tex:162` + `supplementary.tex` SI-2 | Fix permutation importance: 0.489 → 0.488 |
| m2 | abstract + conclusion | Fix regime CI lower bound: [0.02, 0.37] → [0.01, 0.37] |
| m3 | `discussion.tex:29` | Add `deng2010` to particle-size 5/5 citation |
| m4 | `discussion.tex` Limitations | Add one sentence on direction of OA-bias effect on methodology finding |
| m5 | `method.tex:146` + `results.tex:165` | Replace "drives" → "accounts for" (2 instances) |
| m6 | `method.tex` Discipline subsection | State number of pre-registered primary tests (4) explicitly |

### Pre-submission TODOs (not manuscript changes)

- Replace `\todo{Zenodo DOI}` with actual DOI in `conclusion.tex` and `supplementary.tex`
- Add one sentence about Zenodo deposit scope (exclude command history)
- Fix `prabu2021` author field Unicode hyphen in `references.bib`
- Regenerate `main_review.docx` after any of the above changes

---

*Prepared by Claude Sonnet 4.6 — Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>*
*Stop here. Apply changes only after author approves this plan.*
