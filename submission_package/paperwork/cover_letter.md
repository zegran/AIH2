# Cover letter — draft

> Placeholders in [brackets] are user gates (author identity, date). Do not invent.

[DATE]

To the Editors,
*Energy and AI*

Dear Editors,

We submit our manuscript, **"Apparent Contradictions in the Aluminum–Water Hydrolysis Literature are
Predominantly Methodological: a Provenance-Tracked, Leakage-Controlled Analysis,"** for consideration
as a research article.

Hydrogen generation by aluminum–water hydrolysis is an active area in the energy-materials literature,
but its accumulated results are hard to build on: reported parameter effects contradict one another
across studies — most visibly a direction-changing particle-size effect and activation energies spanning
3.5–102.6 kJ mol⁻¹. It has not been clear whether these contradictions reflect genuine physico-chemical
regimes or artifacts of isolated, non-standardized experiments. That ambiguity blocks data-driven design.

We address it directly. We unify the scattered literature into a provenance-tracked open dataset
(315 condition-level yield rows from 31 studies, plus a separate 76-row kinetic table) and analyze it
with pre-registered, leakage-controlled methods. Three findings stand out:

1. **Naive pooling fails.** Under study-grouped cross-validation, the strong apparent predictability of
   random splits collapses (optimism gap 0.62–0.85 in R²) — a quantitative warning against the
   in-sample model fits common in this literature.
2. **The disagreement is methodological.** A between-study variance decomposition attributes ≈72% of
   the between-study yield variance to methodological covariates versus ≈2% to the physico-chemical
   regime label; the hydrogen measurement apparatus is the single largest source (≈43%), temperature
   control explains ≈8%, and the joint method effect survives controlling for regime.
3. **The flagship contradiction resolves.** The direction-changing particle-size effect is internally
   consistent within every study that varies size (5/5 negative): it is a cross-study integration
   artifact, not a physical sign reversal.

We are careful about claims: the analysis is observational, so we state findings associationally,
report nulls transparently as power-limited at n ≈ 31 studies, and pre-registered our thresholds. We
say *predominantly*, not purely, methodological — finer kinetic↔diffusion physics still operates within
studies.

Beyond the finding, the contribution is durable infrastructure the community can reuse: an open dataset
(CC-BY-4.0), a reproducible leakage-controlled benchmark (MIT), and a minimum-information reporting
standard so future aluminum-hydrolysis studies become comparable. We believe this fit — a hydrogen-materials topic addressed with reproducibility-first methodology and
an open data resource, with direct relevance to energy-domain machine-learning evaluation — is well
suited to *Energy and AI*.

The manuscript is original and not under consideration elsewhere. The author declares no competing
interests. The curated dataset is openly available at Zenodo (<https://doi.org/10.5281/zenodo.20751918>,
CC-BY-4.0). Analysis code is available from the corresponding author on reasonable request.

Sincerely,
Dogukan Unal
IPEC, Industrial Project Engineering Consulting, Çankaya, Ankara, 06550, Türkiye
dunal@ipec.com.tr · ORCID 0009-0006-5102-8013
