# CLI Command — FINAL: harden → figures → IJHE draft → self-review

> Paste into Claude Code at the AIH2 repo root. The analysis campaign is done; this takes the
> validated result to a complete, honest first draft. Maintain the project's discipline:
> pre-registered claims, transparent nulls, associational (not causal) language on observational
> findings, no overclaim. Reference downloads are in flight — integrate citations as they land;
> never block the draft on them. **Stop after self-review for user sign-off before any submission.**

## Locked findings (do not re-litigate)
- **Headline (T_B):** methodological covariates explain ~55% of between-study yield variance
  (CI excludes 0) vs ~2% for physical regime (`system_class`); **temperature-control method is the
  single largest source (~33%)**. → The literature's apparent contradictions are **predominantly
  methodological**, not physico-chemical.
- **Supporting:** large, robust optimism gap (random vs grouped CV); the flagship particle-size
  "contradiction" is **within-study consistent (5/5 negative)** → a cross-study artifact, not
  physics; curated provenance-tracked open dataset (315 yield + 76 kinetic rows, QC'd); a proposed
  domain reporting standard.
- **Novelty (Consensus-confirmed, all GAP):** no prior cross-study synthesis / unified open dataset
  / multi-study leakage-controlled ML / domain reporting standard for Al–water hydrolysis. Foil =
  **Das 2023** single-study ANN (R²≈0.998 in-sample).
- **Venue:** draft for **IJHE**, but it must stand as an **Energy and AI** paper too — i.e., do not
  let the IJHE framing overclaim beyond what survives the hardening. Report the **T_A predictive
  null** transparently.

## Step 1 — Pre-write hardening (do first; commit separately)
1. **T_B confound/robustness check (critical).** Verify the method-covariate variance is not merely
   re-encoding study identity: test whether method covariates explain between-study variance
   **among studies that share a method level** (not just separating one-method-per-study clusters).
   Report covariate coverage/imbalance, cluster-bootstrap CI, and multi-seed. **Temper all language
   to associational** ("methodological covariates *explain/are associated with*", not "*cause*").
   If the attribution is partly confounded with study identity, state it as a limitation.
2. **Physics reconciliation (Saceleanu 2019, `10.1002/er.4769`).** Add to
   `plan/analysis-protocol.md` + discussion: the *coarse* `system_class` regime label does not
   explain the spread, but a *finer* kinetic↔diffusion regime transition (Saceleanu) genuinely
   contributes. Lock the claim as **"predominantly/substantially methodological"**, never "purely".
3. **Particle-size resolution writeup.** Formalize the 5/5 within-study-consistent negative
   direction as "the flagship contradiction resolved as a cross-study artifact."
**Gate:** hardening committed; claims tempered; `GO_NOGO_SUMMARY.md` updated with the final claim set.

## Step 2 — WP5 figures (real data, `results/real_v1/`)
1. **Optimism gap** — random vs grouped CV R² across models (leakage demonstration).
2. **Variance decomposition (headline)** — between-study variance explained: method covariates
   (~0.55) vs physical regime (~0.02), with the temperature-control breakdown.
3. **Particle-size within-study consistency** — per-study direction (5/5 negative) → contradiction
   resolved.
4. **Eₐ spread + method dependence** — reported Eₐ vs method/temperature-control, with the Saceleanu
   regime caveat annotated.
5. **Dataset composition** — per-`system_class` N, quality tiers, kinetic vs yield (data-resource figure).
Use `writing-anti-ai` discipline for captions; deterministic, reproducible figure scripts.

## Step 3 — WP6 draft (IJHE elsarticle) — use the skills
Invoke `ml-paper-writing` (structure/draft), `writing-anti-ai` (style), `citation-verification`
(refs). Draft `paper/main.tex` + sections:
- **Framing:** decades of documented Al–water hydrolysis contradictions; we unify the scattered
  literature and show they are predominantly methodological. Foil = Das 2023 (single-study, in-sample).
- **Method precedent (cite):** study-level leakage / grouped CV — **Bernett 2024 (Nature Methods,
  `10.1038/s41592-024-02362-y`)**, John 2025 (`10.1016/j.geoderma.2025.117223`), Pomerantsev 2021
  (`10.1016/j.talanta.2021.122104`); data-science-in-catalysis framing — **Suvarna & Pérez-Ramírez
  2024 (Nature Catalysis, `10.1038/s41929-024-01150-3`)**, Bozal-Ginesta 2025
  (`10.1038/s41570-025-00740-4`), Coelho 2022 (`10.1038/s41529-022-00218-4`), Xue 2024
  (`10.1002/advs.202410065`), Noble 2022 (`10.1242/jeb.243225`).
- **External corroboration:** method shifts measured values 2×+ (Testa 2024; Wen 2018; Urbonavičius
  2023 `10.1016/j.ijhydene.2023.09.065`); MgH₂/biohydrogen round-robin precedent (temperature
  control dominant) — frame our internal temperature-control finding as convergent.
- **Reporting-standard contribution:** propose a minimum-information standard for Al-hydrolysis,
  templated on Wulf 2021 (`10.1002/cctc.202001974`) and Hoque & Guzman 2018 (`10.3390/ma11101990`).
- **Limitations (honest, prominent):** nulls framed as "no detectable effect at n≈31 studies / 3–9
  per regime" (not "no effect exists"); T_A predictive null; T_B attribution is observational
  (associational); Saceleanu physics caveat; thin exploratory classes.
- **Open data + reproducibility:** CC-BY dataset + code; never redistribute Sci-Hub PDFs.
- **Reference handling:** integrate positioning DOIs as they are ingested into `data/raw/literature/`;
  for any not yet present, insert a clearly-marked `\todo{cite: <doi>}` placeholder — do NOT block.

## Step 4 — Self-review, then STOP
Run `paper-self-review`: check every quantitative claim traces to a committed result; no causal
overclaim; nulls correctly framed; novelty statements match the Consensus GAP findings; citations
verified. Write `paper/SELF_REVIEW.md`. **Stop for user sign-off before any submission step.**

## Rules / Definition of done
- Associational language on T_B; transparent T_A null; "predominantly methodological" locked.
- Figures reproducible; every number traces to `results/real_v1/`.
- `paper/main.tex` compiles; `SELF_REVIEW.md` committed; positioning citations integrated or
  placeholdered. Durable artifacts English; Conventional Commits; pipeline stopped for user review.
