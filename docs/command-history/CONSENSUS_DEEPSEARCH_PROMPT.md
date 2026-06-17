# Consensus Deep Search — research prompt (paste into Consensus Deep Search)

## Primary question
To what extent are the well-documented inter-study contradictions in **aluminum–water hydrolysis
for hydrogen generation** (e.g., direction-changing particle-size effects; reported activation
energies spanning ~3.5–102.6 kJ/mol for nominally the same reaction; conflicting rate–yield
trade-offs) attributable to **non-standardized experimental and measurement methodology** rather
than to genuine physico-chemical differences between systems? Has any prior work (a) quantified
this, (b) unified the scattered literature into a dataset/model with leakage-controlled evaluation,
or (c) proposed reporting/data standards for this reaction? Be objective: actively surface evidence
that would **weaken** this hypothesis as well as evidence that supports it.

## Sub-questions (answer each explicitly, with citations, and state whether a gap exists)
1. **Prior quantitative synthesis.** Are there meta-analyses, systematic cross-study data
   compilations, or machine-learning models trained on **multi-study** aluminum–water hydrolysis
   data (yield or kinetics)? Identify any single-study ML models vs any multi-study/transferable ones.
2. **Measurement-method effects.** Evidence that measured H₂ yield or rate depends on the
   measurement technique (water displacement vs pressure transducer vs gas chromatography vs
   mass-loss), reaction vessel (open vs closed), temperature control (isothermal bath vs
   uncontrolled/self-heating), or water type/purity (DI vs tap vs sea vs alkaline). Any
   inter-laboratory or round-robin comparison studies for metal–water hydrogen generation.
3. **Activation-energy spread.** How does the literature explain the very wide reported Eₐ range for
   this reaction family — as real mechanistic/regime differences, or as artifacts of differing
   methods, temperature ranges, rate definitions, or fitting procedures?
4. **Methodological precedent (ML-for-materials).** Prior demonstrations of **study-level data
   leakage**, the need for **grouped / leave-one-study-out cross-validation**, or
   **out-of-distribution / cross-study generalization failure**, and the use of **mixed-effects /
   hierarchical meta-regression** on heterogeneous multi-source experimental datasets in energy
   materials, catalysis, or batteries. (Used to position our method as established, not novel.)
5. **Reporting-standard precedents.** Minimum-information / FAIR-data / standardized-reporting
   frameworks in hydrogen generation, heterogeneous catalysis, or energy materials that could serve
   as a template for a proposed aluminum-hydrolysis reporting standard.
6. **Counter-evidence / scooping risk.** Any existing successful cross-study transferable predictive
   model, any convincing single physical-mechanism resolution of the contradictions, or any already
   released standardized/curated open dataset for this reaction — i.e., findings that would weaken,
   pre-empt, or compete with the "contradictions are methodological artifacts" thesis.

## Scope & quality
- Prioritize peer-reviewed work; include foundational older work where relevant.
- Primary domain: **aqueous aluminum–water hydrolysis** (pure Al, Al-alloy, mechanically/liquid-metal
  activated, waste Al). Secondary/analogous: Mg–water hydrolysis and broader energy-materials ML
  (only for methodological precedent in #4–#5).
- Exclude water electrolysis / PEM / supercritical-water gasification except where they provide
  methodological precedent.

## Required output
For each sub-question: a short synthesis of what is known, the key papers (with citations/links),
and an explicit "GAP / NO GAP" verdict. Then a closing section with:
1. **Consolidated novelty assessment** — what is genuinely unaddressed (the gap our paper fills).
2. **Strongest existing support** for the methodological-artifact hypothesis.
3. **Strongest threats** to it (counter-evidence, competing explanations, scooping risk).
4. **Recommended citations** to position the introduction and discussion.
