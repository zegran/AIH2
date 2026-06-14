# AIH2 — Design Specification

**Project:** Physics-validated interpretable machine learning to explain contradictory
parameter effects in aluminum–water hydrolysis for hydrogen production.

**Working title (draft):** *Explaining Contradictory Parameter Effects in Aluminum–Water
Hydrolysis for Hydrogen Production via Physics-Validated Interpretable Machine Learning.*

**Status:** Design spec — awaiting sign-off before scaffolding.
**Date:** 2026-06-14
**Primary venue:** International Journal of Hydrogen Energy (IJHE).
**Fallback venue:** *Energy and AI*.
**LaTeX:** generic now, structured for a clean switch to Elsevier `elsarticle`.

---

## 0. Language & artifact conventions

- All durable artifacts are in **English**: code, identifiers, file names, commit messages,
  the paper, the data dictionary, this spec, and `README`.
- Turkish is allowed only for (1) conversation/explanations with the author and
  (2) personal thinking notes inside `vault/`.
- Commits follow Conventional Commits. Python is managed with `uv`; configs with
  Hydra + OmegaConf. Reproducibility uses a `set_seed` helper.

---

## 1. Problem statement

The aluminum–water hydrolysis literature reports **contradictory parameter effects** on
hydrogen generation:

- **Direction-changing particle-size effect:** smaller particles accelerate generation in
  some studies but suppress yield in others.
- **Activation energies spanning 3.5–102.6 kJ/mol** across studies for nominally the same
  reaction family.
- **An inconsistently characterized rate–yield trade-off.**

These contradictions plausibly arise from heterogeneous reaction conditions, materials
systems (pure Al, alloys, mechanically/liquid-metal-activated composites, waste Al), and
non-standardized measurement protocols. The field therefore lacks transferable design rules.

## 2. Core idea

Build a **literature-derived unified dataset** with per-row provenance and quality metadata;
apply **interpretable ML** (gradient-boosted trees with SHAP and ALE) under **study-grouped
cross-validation**; resolve apparent contradictions by conditioning on `system_class` and
data quality; and **validate** the learned effects against **Arrhenius** and
**shrinking-core** physics.

## 3. Research questions & hypotheses

- **RQ1.** Can a unified, provenance-tracked literature dataset plus interpretable ML
  reproduce and explain the contradictory parameter effects reported across studies?
- **RQ2.** Are the contradictions (especially the direction-changing particle-size effect)
  genuine mechanistic regime switches or artifacts of study heterogeneity and measurement
  protocol?
- **RQ3.** Do ML-derived parameter sensitivities agree with established physical kinetics
  (Arrhenius Eₐ; shrinking-core regimes)?

- **H1.** The direction-changing particle-size effect corresponds to a **shrinking-core
  regime switch** (diffusion-controlled vs. reaction/passivation-controlled), surfacing as a
  `particle_size × {temperature, alkalinity}` interaction in SHAP.
- **H2.** A large share of apparent inter-study contradiction is explained by `system_class`
  and data-quality covariates; conditioning on them reduces the contradiction.
- **H3.** ML-learned temperature sensitivity recovers Arrhenius-consistent Eₐ within the
  literature **3.5–102.6 kJ/mol** band, per `system_class`.

## 4. Contributions

1. A unified, provenance-tracked, quality-tiered **literature dataset** for Al–water
   hydrolysis H₂ yield, openly released (Zenodo DOI, CC-BY-4.0).
2. A **leakage-controlled** (study-grouped / leave-one-study-out) interpretable-ML
   methodology that distinguishes genuine mechanistic contradictions from study artifacts.
3. **Physics-validated XAI:** cross-checking SHAP/ALE-derived sensitivities against Arrhenius
   and shrinking-core kinetics.
4. Resolution of the **direction-changing particle-size effect** as a regime switch — the
   paper's visual headline (`fig3`).

---

## 5. Scope — Phase 1 vs Phase 2

**Guiding principle ("fix the caravan en route"): keep Phase 1 lean.** Anything that carries
uncertainty, inflates scope, or depends on data availability is deferred to Phase 2. The
scaffold is built around a single target and the core pipeline; extension points are left in
the architecture but not implemented.

### Phase 1 — end-to-end working pipeline on a single target (yield %)

Data schema + provenance/quality metadata → grouped/LOSO cross-validation with a comparative
model set → ALE + SHAP (main + 2-way interaction) → Arrhenius Eₐ-distribution validation →
`fig1`/`fig2`/`fig3` + CV-gap + calibration → Zenodo-ready data/code.

### Phase 2 — deferred (DEFER)

- Additional targets: `max_rate (mL·min⁻¹·g⁻¹)` and `t80 (time to 80% conversion)`.
- Multi-target model expansion.
- Shrinking-core **regime-switch** analysis and the SHAP↔physics **consistency metric**.
- Rate–yield trade-off map.

Phase 2 items appear in the architecture only as **columns/stubs/extension points** — no
implementation in Phase 1.

### Publication-readiness note (do not conflate "Phase 1 done" with "paper ready")

Because Phase 1 is single-target, the **mechanistic closure of H1** (particle-size
contradiction = shrinking-core regime switch) **slips to Phase 2**. Therefore:

- **Phase 1 alone is NOT a submission-ready paper.** It delivers a working, leakage-controlled
  interpretable pipeline and the contradiction-resolution visuals, but not the mechanistic
  proof that anchors the central claim.
- **Publishable paper = Phase 1 + core Phase 2**, where core Phase 2 = the **SCM regime-switch
  analysis** and the **SHAP↔physics consistency metric** (§9.1b–c). Multi-target and the
  rate–yield map remain optional extensions, not gating for submission.
- Acceptance criteria in §12 describe **engineering completeness of Phase 1**, not manuscript
  readiness. Track the two separately.

---

## 6. Dataset design (A)

### 6.1 Target variable (A1)
- **Phase 1 single target:** `h2_yield_pct` — H₂ yield (%) relative to the theoretical
  1.245 L H₂ per gram Al at STP.
- **Schema reserves (Phase 2, left empty/nullable):** `max_rate_ml_min_g`, `t80_min`.
- The data pipeline is built to be **extensible to multi-target**, but Phase 1 trains and
  analyzes the yield target only.

### 6.2 Input features & encoding (A2)
Hybrid encoding (tree ensembles handle mixed types; preserves mechanism for SHAP):

- **Numeric:** `temperature_k`, `alkali_conc_mol_l`, `particle_size_d50_um`,
  `activator_ratio`, and **per-element alloy composition in wt%** as separate columns
  (`al_wt_pct`, `ga_wt_pct`, `in_wt_pct`, `sn_wt_pct`, `bi_wt_pct`, `mg_wt_pct`, `zn_wt_pct`, …).
- **Categorical:** `alkali_type` (NaOH/KOH/none), `activation_method`
  (ball-milling/plasma/liquid-metal/none), `water_type` (DI/tap/sea/alkaline),
  `morphology_flag`, and `system_class` (see 6.3).
- **Encoding rule:** in wt% columns, distinguish **`absent = 0`** from
  **`unreported = NaN`**. Models and imputation must respect this distinction.

### 6.3 Data scope (A3)
- **Included:** alkaline and activated **aqueous** Al-hydrolysis systems — pure Al-alkali,
  Al-alloy, mechanically activated, liquid-metal-activated, waste Al.
- **Excluded:** acid hydrolysis, Al–NaBH₄ hybrids, non-aqueous systems.
- `system_class` is not merely a covariate; it is the **central analysis axis** for
  separating genuine contradictions from artifacts.

### 6.4 Target N and floor (A4)
- **Hard floor:** ≈ 150 rows — the minimum to begin **any** modeling.
- **Real target:** ≈ 300 rows (range 300–500) from ~40–80 studies, because analysis is
  stratified by `system_class`; 150 is too thin once split per class.
- **Per-class reporting:** report N **per `system_class`** explicitly. Mark any `system_class`
  with **< 40 rows as exploratory-only** (no headline claims drawn from it).
- **Small-data strategy:** grouped cross-validation, regularized GBMs, bootstrap/conformal
  uncertainty.

---

## 7. Data-extraction protocol (B)

### 7.1 Extraction & provenance (B1)
- **Method:** semi-automated hybrid — manual table extraction plus **WebPlotDigitizer** for
  figure curves.
- **Per-row provenance:** `study_id` (DOI), table/figure reference, extractor, date,
  extraction method.
- **QC:** double-extract a **10–15% sample**; report extraction error as a separate table.

### 7.2 Heterogeneity / quality schema (B2)
Per-row quality flags: measurement method (water-displacement / mass-loss / pressure / GC),
temperature control (isothermal bath / uncontrolled / self-heating), vessel type
(open/closed), rate definition (initial/avg/max), reported-vs-derived, and a composite
**A/B/C quality tier**. A **high-quality-only sensitivity re-run** is the decisive
contradiction test (real vs. artifact).

---

## 8. Modeling & XAI (C)

### 8.1 Model family (C1)
Comparative set with GBM as the interpretable workhorse:
- **Primary:** XGBoost / LightGBM (TreeSHAP interaction support).
- **Benchmarks:** Random Forest, ElasticNet, kNN, **Gaussian Process** (kept specifically for
  small-data uncertainty).
- Selection by best grouped-CV calibration; the selected model feeds the XAI layer.

### 8.2 XAI layer (C2)
- **ALE plots — primary** dependence tool (robust under correlated features here, where PDP
  extrapolates incorrectly).
- **SHAP** main effects + **2-way interaction values — mandatory** for the H1 hypothesis.
- **PDP/ICE — secondary.**
- **Permutation importance** as a model-agnostic sanity check.
- SHAP stability is checked across CV folds.

### 8.3 Leakage control (C3)
- **GroupKFold + leave-one-study-out (LOSO) are mandatory.**
- Report **both random-split and grouped-split** metrics; the **optimism gap** between them
  is presented as a **headline finding** (quantifies how study-confounded the field's apparent
  predictability is).

---

## 9. Physical-validation layer (D)

### 9.1 Cross-validation against physics (D1)
- **(a) Arrhenius:** fit `ln k` vs `1/T` per `system_class` → Eₐ distribution; check that the
  model's temperature sensitivity reproduces `exp(−Eₐ/RT)` and lands within the literature
  **3.5–102.6 kJ/mol** band.
- **(b) Shrinking-core (DEFER, Phase 2):** fit reaction-controlled `1−(1−X)^{1/3}` vs.
  diffusion-controlled `1−3(1−X)^{2/3}+2(1−X)`; test the sign-changing particle-size effect
  against an SCM regime switch.
- **(c) Consistency metric (DEFER, Phase 2):** sign-agreement rate between SHAP-local
  gradients and SCM/Arrhenius-predicted gradients.

**Phase 1 note:** build the module skeleton and make the **Arrhenius Eₐ-distribution
validation work**. Leave the SCM regime-switch analysis and the consistency metric as
**stubs**, to be filled once the yield model settles.

### 9.2 Module (D2)
`src/analysis/physical_validation/` with:
- `arrhenius.py` — Eₐ fitting (**Phase 1, working**).
- `shrinking_core.py` — SCM regime classification (**Phase 1 stub**).
- `consistency_metrics.py` — XAI↔physics agreement (**Phase 1 stub**).

---

## 10. Reproducibility & outputs (E)

### 10.1 License & archival (E1)
- Code: **MIT** (no patent concern).
- Dataset: **CC-BY-4.0**.
- Versioned **Zenodo DOI** + GitHub mirror, with data dictionary, per-row provenance, and
  `uv.lock`. Meets IJHE/Q1 data-availability expectations.

### 10.2 Primary-result figures (E2)
Reserve all five slots in `results/`; in Phase 1 produce only the yield-based ones.

1. `fig1_shap_summary` — global SHAP beeswarm. **(Phase 1)**
2. `fig2_interaction_map` — SHAP 2-way interaction (size × T / alkalinity). **(Phase 1)**
3. `fig3_contradiction_resolution` — particle-size ALE with sign change by
   `system_class`/regime → **paper's visual headline. (Phase 1)**
4. `fig4_physical_validation` — model-derived Eₐ vs. literature distribution **(Phase 1)**;
   SCM regime classification **(DEFER, Phase 2)**.
5. Supporting — rate–yield trade-off map **(DEFER, Phase 2)**; grouped-vs-random CV gap
   **(Phase 1)**; uncertainty/calibration **(Phase 1)**.

---

## 11. Repository architecture (Approach A — integrated monorepo)

```
AIH2/
├── README.md                  # project overview, RQ, status
├── pyproject.toml             # uv-managed deps
├── uv.lock
├── .python-version
├── .gitignore                 # ignores data/raw/, run/outputs/, temp/
├── LICENSE                    # MIT (code)
├── plan/                      # planning & decision docs (this spec lives here)
├── temp/                      # scratch (gitignored)
│
├── paper/                     # LaTeX draft, generic, elsarticle-ready
│   ├── main.tex
│   ├── sections/              # intro, related_work, method, experiments, results, conclusion
│   ├── figures/  tables/
│   └── references.bib
│
├── src/
│   ├── data_module/           # schema, loading, provenance/quality, encoding
│   ├── model_module/          # comparative models (xgb/lgbm/rf/elasticnet/knn/gp)
│   ├── analysis/
│   │   ├── xai/               # SHAP, ALE, PDP/ICE, permutation importance
│   │   └── physical_validation/   # arrhenius.py (live), shrinking_core.py (stub),
│   │                              # consistency_metrics.py (stub)
│   └── utils/                 # set_seed, logging, IO
├── run/
│   ├── conf/                  # Hydra configs
│   ├── pipeline/              # workflow scripts (data → cv → xai → physics → figures)
│   └── outputs/               # Hydra run outputs (gitignored)
│
├── data/
│   ├── raw/                   # GITIGNORED (source extractions in progress)
│   ├── curated/               # VERSIONED (the unified, provenance-tracked dataset)
│   └── data_dictionary.md     # VERSIONED
│
├── results/                   # curated figures/tables/metrics (fig1..fig4 + supporting placeholders)
│
└── vault/                     # Obsidian project KB (repo-internal), bound via
    ├── 00-Hub.md              #   .claude/project-memory/registry.yaml
    ├── Papers/  Knowledge/  Experiments/  Results/  Daily/
```

**Corrections applied vs. the original Approach A:** `data/curated/` is **versioned** (only
`data/raw/` is gitignored); the **Obsidian vault is repo-internal** (`vault/`).

---

## 12. Phase 1 definition of done (acceptance criteria)

> These criteria define **engineering completeness of Phase 1**, not manuscript readiness.
> A submission-ready paper requires Phase 1 + core Phase 2 (see §5 Publication-readiness note).

1. `data/curated/` holds the unified dataset (≥ 150 hard floor; ~300 target) with full
   provenance and A/B/C quality tiers, plus `data_dictionary.md`, and **per-`system_class` N
   reported** with any class < 40 rows flagged exploratory-only.
2. Comparative models train under **GroupKFold + LOSO**; both random-split and grouped-split
   metrics are reported with the optimism gap.
3. XAI layer produces SHAP (main + 2-way interaction) and ALE; SHAP stability across folds is
   recorded.
4. `arrhenius.py` produces a per-`system_class` Eₐ distribution and compares it to the model's
   temperature sensitivity and the 3.5–102.6 kJ/mol band.
5. `fig1`, `fig2`, `fig3`, the Eₐ part of `fig4`, the CV-gap figure, and calibration are
   generated reproducibly from a single pipeline entry point.
6. Repo is Zenodo-ready: MIT `LICENSE`, `uv.lock`, data dictionary, deterministic seeds.

## 13. Risks & mitigations

- **Insufficient N / sparse cells** → enforce floor (≥150), report uncertainty, lean on
  grouped CV; expand `system_class` coverage before adding features.
- **Extraction error inflating false contradictions** → double-extraction QC + quality tiers
  + high-quality-only sensitivity run.
- **Feature correlation distorting attributions** → ALE-primary, SHAP interactions,
  permutation cross-check.
- **Study leakage** → GroupKFold/LOSO mandatory; never random-split for generalization claims.
- **Scope creep** → strict Phase 1/Phase 2 gate; Phase 2 items stay as stubs/columns only.

---

## 14. Skill routing (for execution)

- Knowledge base: `obsidian-project-bootstrap` → `obsidian-project-memory`.
- Environment/deps: `uv-package-manager`.
- Architecture (registries/factories for models): `architecture-design`.
- Physics constants/kinetics support: `thermodynamics`, `scipy-optimization`,
  `numpy-numerics`.
- Analysis & figures: `results-analysis`, `matplotlib-visualization`,
  `publication-chart-skill`.
- Writing: `ml-paper-writing`, `citation-verification`, `writing-anti-ai`,
  `latex-conference-template-organizer` (for the eventual `elsarticle` switch).
- Literature: `consensus-evidence-search`, `obsidian-literature-workflow`.
- Verification: `verification-loop`, `code-review-excellence`.
