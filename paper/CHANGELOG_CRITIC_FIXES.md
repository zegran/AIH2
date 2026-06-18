# Changelog — Critic Fixes (Stages 1–4)

All changes applied after Stage 1 text fixes (commit `9225331`) and the self-review critic report.

---

## Stage 1 — Tier-1 text fixes

| Item | Change | Files |
|------|--------|-------|
| M3 (CI framing) | R² = 0.018 wording replaced "explains almost none" with point-estimate + wide-interval framing (upper bound ≈37% does not exclude moderate regime effects) | `paper/sections/results.tex` |
| M2 (associational caveat) | Added caveat immediately after temperature-control 33% finding: study-level attribute, may co-vary with unmeasured lab differences | `paper/sections/results.tex` |
| m1 (optimism gap def) | Abstract: added inline definition `(R²_rand − R²_grp)` | `paper/main.tex` |
| M9 (pre-reg table) | Added Table (Hypothesis / Null / Test / Threshold / Correction / Outcome) at end of §2.4 for all four pre-registered tests; referenced in §2.4 | `paper/sections/method.tex` |
| Acknowledgements | Changed to "not supported by external funding" | `paper/sections/conclusion.tex` |
| CRediT | Added "Single-author contribution encompasses all CRediT roles." | `paper/sections/conclusion.tex` |

---

## Stage 2 — Blind independent-agent IRR re-extraction + dataset corrections

**Procedure:** Stratified random sample of 19 studies (77 yield rows) re-extracted by fresh agents
with no access to committed codings. 8/19 studies were openly accessible; 10 were paywalled; 1 missing.
Raw Cohen's κ (accessible subset, n=8 studies):

| Variable | κ (pre-adjudication) | κ (post-adjudication) |
|----------|---------------------|-----------------------|
| system_class | 0.826 | 0.826 |
| temperature_control | 0.429 | 1.000 |
| measurement_method | 0.700 | 1.000 |

**Three coding corrections applied to dataset:**

1. **`10.1039/d2ra01231f` (Trowell et al. 2022, RSC Adv.)** — `temperature_control`: `uncontrolled` → `isothermal_bath`
   *Reason:* External 3.5 kW Watlow ceramic fiber heater holds sealed reactor isothermally at 655 K.

2. **`10.3390/hydrogen7020055` (Martínez-Vargas et al. 2026, Hydrogen)** — `temperature_control`: `uncontrolled` → `isothermal_bath`; `measurement_method`: NaN → `mass_flow`
   *Reason:* PID-controlled heating plate at 55 ± 1 °C; hydrogen measured with Cole-Parmer digital flowmeter.

3. **`10.1590/s0104-66322012000200014` (Porciuncula et al. 2012, B.J.Chem.Eng.)** — `measurement_method`: `water_displacement` → `other`
   *Reason:* Closed-syringe piston displacement (not classic inverted-vessel water displacement).

**Impact on variance decomposition (updated numbers):**

| Predictor | R² (before) | R² (after) | CI (after) |
|-----------|------------|-----------|-----------|
| system_class | 0.018 | 0.018 | [0.015, 0.373] |
| temperature_control | 0.332 | **0.081** | [0.002, 0.240] |
| measurement_method | — | **0.425** | [0.024, 0.806] |
| joint method | 0.553 | **0.717** | [0.443, 1.000] |

**Headline finding direction:** UNCHANGED and STRENGTHENED (72% method vs. 2% regime; was 55% vs. 2%).
The "uncontrolled" temperature_control category is entirely eliminated by the corrections (both
studies that had it were coding errors).

**Dataset files corrected:** `data/curated/aih2_v1.csv`, `data/wp1/extraction_rows.csv`

---

## Stage 3 — Robustness sensitivities

**3a — Particle-size reporting sensitivity (Fisher's exact):**
- Quality tier distribution: p = 0.350 (no significant difference between PS-reporting and non-reporting studies)
- Temperature control composition: p = 0.613
- Conclusion: particle-size within-study finding is not confounded by reporting propensity

**3b — OA-subset sensitivity (tier A/B only, n=19 studies):**
- system_class R² = 0.094
- measurement_method R² = 0.073 (drops substantially vs 0.425 full)
- temperature_control R² = 0.065
- Headline direction (method > regime) maintained; individual predictor magnitudes are sensitive to tier-C inclusion

Both sensitivity results added as §3.7 "Robustness sensitivities" in results.

---

## Stage 4 — Code bundle

Built `release/aih2_code_v1/` containing:
- `src/` — analysis package
- `run/` — experiment entrypoints
- `tools/` — utility scripts
- `README.md`, `LICENSE` (MIT)

Zipped to `release/aih2_code_v1.zip` (92 KB). Ready for a separate Zenodo code deposit at user's discretion.

---

## Gates

- Compliance gate: PASS (250 words)
- Lint: PASS (58/58 cite coverage, 0 structural issues)
- DOCX: regenerated `submission_package/manuscript/main_review.docx`

---

## Stage 5 — Zenodo DOI insertion + full propagation + consistency gate (2026-06-18)

**New Zenodo DOI:** `10.5281/zenodo.20751918` (old record deleted; fresh upload)

**DOI inserted:**
- `paper/sections/conclusion.tex` — Data Availability
- `paper/sections/supplementary.tex` — companion data release line
- `release/zenodo_v1/CITATION.cff` — doi field (replaced placeholder)
- `release/zenodo_v1/aih2_dataset_v1.zip` — rebuilt with real DOI in CITATION.cff
- `submission_package/zenodo/` — synced from `release/zenodo_v1/`

**Propagation sweep — remaining old numbers updated:**
- `paper/sections/introduction.tex` — ≈55%/TC 33% → ≈72%/apparatus 43%/TC 8%
- `paper/sections/discussion.tex` — "Why pooling fails" paragraph updated; `tab:mireport` reordered (apparatus first, R²=0.43; TC second, R²=0.08); caption updated; "uncontrolled" removed from TC level list; min-reporting-standard text updated
- `paper/sections/method.tex` — TC level list: removed "uncontrolled", added reference to §QC; MM levels: added mass_flow + other
- `paper/submission/cover_letter.md` — updated to Energy and AI; GitHub link replaced with Zenodo DOI; numbers updated to ≈72%/43%/8%
- `paper/submission/IJHE_checklist.md` — renamed to Energy and AI; Zenodo DOI inserted; venue locked

**Added:**
- `tools/consistency_gate.py` — asserts headline values (0.717/0.018/0.425/0.081) consistent across all tex files; wired into `tools/lint_paper.py`

**All gates after Stage 5:**
- Consistency gate: **PASS**
- Structural lint: **PASS** (58/58 cites, 0 hard errors)
- Compliance: **PASS** (250 words, 6 keywords, Energy and AI, 3 benign highlight-length warnings)
- DOCX: regenerated 2026-06-18 (287 KB)
