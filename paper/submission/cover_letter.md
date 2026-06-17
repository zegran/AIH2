# Cover letter — draft

> Placeholders in [brackets] are user gates (author identity, date). Do not invent.

[DATE]

To the Editors,
*International Journal of Hydrogen Energy*

Dear Editors,

We submit our manuscript, **"Apparent Contradictions in the Aluminum–Water Hydrolysis Literature are
Predominantly Methodological: a Provenance-Tracked, Leakage-Controlled Analysis,"** for consideration
as a research article.

Hydrogen generation by aluminum–water hydrolysis is an active area in IJHE, but its literature is hard
to build on: reported parameter effects contradict one another across studies — most visibly a
direction-changing particle-size effect and activation energies spanning 3.5–102.6 kJ mol⁻¹. It has
not been clear whether these contradictions reflect genuine physico-chemical regimes or artifacts of
isolated, non-standardized experiments. That ambiguity blocks data-driven design.

We address it directly. We unify the scattered literature into a provenance-tracked open dataset
(315 condition-level yield rows from 31 studies, plus a separate 76-row kinetic table) and analyze it
with pre-registered, leakage-controlled methods. Three findings stand out:

1. **Naive pooling fails.** Under study-grouped cross-validation, the strong apparent predictability of
   random splits collapses (optimism gap 0.62–0.85 in R²) — a quantitative warning against the
   in-sample model fits common in this literature.
2. **The disagreement is methodological.** A between-study variance decomposition attributes ≈55% of
   the between-study yield variance to methodological covariates versus ≈2% to the physico-chemical
   regime label; the temperature-control method alone is the single largest source (≈33%) and survives
   controlling for regime.
3. **The flagship contradiction resolves.** The direction-changing particle-size effect is internally
   consistent within every study that varies size (5/5 negative): it is a cross-study integration
   artifact, not a physical sign reversal.

We are careful about claims: the analysis is observational, so we state findings associationally,
report nulls transparently as power-limited at n ≈ 31 studies, and pre-registered our thresholds. We
say *predominantly*, not purely, methodological — finer kinetic↔diffusion physics still operates within
studies.

Beyond the finding, the contribution is durable infrastructure the community can reuse: an open dataset
(CC-BY-4.0), a reproducible leakage-controlled benchmark (MIT), and a minimum-information reporting
standard so future aluminum-hydrolysis studies become comparable. We believe this fit — a hydrogen
materials topic addressed with reproducibility-first methodology and an open data resource — is well
suited to IJHE.

The manuscript is original, not under consideration elsewhere, and all authors approve the submission.
We declare no competing interests. The data and code are available at
<https://github.com/zegran/AIH2> and archived at Zenodo (DOI to be activated on acceptance).

Sincerely,
[CORRESPONDING AUTHOR NAME — USER INPUT]
on behalf of all authors
[AFFILIATION — USER INPUT] · [EMAIL — USER INPUT]
