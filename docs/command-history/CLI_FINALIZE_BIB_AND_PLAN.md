# CLI Command — Accept PDF constraint → complete bibliography from verified metadata → plan remaining WPs → push

> Paste into Claude Code at the AIH2 repo root. **Accept the reality:** no further reference PDFs
> are obtainable. Do NOT leave the paper blocked on missing PDFs. Complete the citations from
> **verified metadata** (DOIs already held + the metadata below + archived studies' own data),
> with honest two-tier verification. Then plan the remaining work packages in order, present the
> plan, and push the final state. No fabrication; no rescue narratives. Stop for the user after.

## Verification policy (honest, two-tier)
- **full-text-verified** — source PDF/MD is in the archive (`data/raw/literature/`). Use for any
  specific quantitative claim.
- **metadata-verified** — DOI + title + abstract are known/verified (Consensus refs / Crossref),
  but no full text. Acceptable for **general attribution** (citing a paper for what it is known
  for). If a sentence makes a *specific quantitative* claim citing a metadata-only source, **soften
  the wording to what the abstract supports** or flag it `% NEEDS-FULLTEXT` for the user — never
  invent a number.

## Step 1 — Complete the bibliography (unblock the draft)
1. Add the 6 verbatim BibTeX entries below to `paper/references.bib` (metadata-verified).
2. For refs **already in the archive** — `testa2024`, `wen2018`, `musicco2025`, `urbonav2024`,
   `porciuncula2012` — build BibTeX from their own archived metadata / `master_dois.csv`
   (porciuncula DOI = `10.1590/s0104-66322012000200014`). These are full-text-verified.
3. For the two reviews `xiao2021review` (Active aluminum composites … A review, IJHE 2021) and
   `dupreez2021review` (On-demand H2 by hydrolysis of ball-milled Al composites: process overview,
   IJHE 2021): resolve their DOIs via Crossref; if resolved → metadata-verified BibTeX + cite; if
   not resolvable, leave a single `\todocite` and list it.
4. Convert every resolved `\todocite{...}` to `\cite{<citekey>}`. Tag each new bib entry with a
   comment `% verified: full-text | metadata`. Target: **zero remaining placeholders** (or a short,
   explicit list of any that truly cannot be verified).
5. Run `citation-verification` at the general-attribution layer on the new citations; flag (don't
   fix) any mismatch in `paper/SELF_REVIEW.md`.

### Verbatim BibTeX (paste; metadata-verified)
```bibtex
@article{das2023fuel,
  author  = {Das, Biswajyoti and Robi, P. S. and Mahanta, Pinakeswar},
  title   = {Experimental Investigation and Modelling by Machine Learning Techniques for Hydrogen Generation by Reacting Aluminium with Aqueous NaOH Solution},
  journal = {Fuel},
  year    = {2023},
  doi     = {10.1016/j.fuel.2023.128924}
}

@article{saceleanu2019,
  author  = {Saceleanu, Flaviu and Vuong, Thu V. and Master, Emma R. and Wen, John Z.},
  title   = {Tunable kinetics of nanoaluminum and microaluminum powders reacting with water to produce hydrogen},
  journal = {International Journal of Energy Research},
  year    = {2019},
  volume  = {43},
  pages   = {7384--7396},
  doi     = {10.1002/er.4769}
}

@article{pomerantsev2021,
  author  = {Pomerantsev, Alexey L. and Rodionova, Oxana Ye.},
  title   = {Procrustes Cross-Validation of short datasets in PCA context},
  journal = {Talanta},
  year    = {2021},
  volume  = {226},
  pages   = {122104},
  doi     = {10.1016/j.talanta.2021.122104}
}

@article{urbonavicius2023,
  author  = {Urbonavi{\v c}ius, Marius and Varnagiris, {\v S}ar{\=u}nas and Mezulis, Ainars and Lesnicenoks, Peteris and Knoks, Ainars and Richter, Christiaan and Mil{\v c}ius, Darius and Meirbekova, Rauan and Gunnarsson, Gudmundur and Kleperis, Janis},
  title   = {Hydrogen from industrial aluminium scraps: Hydrolysis under various conditions, modelling of pH behaviour and analysis of reaction by-product},
  journal = {International Journal of Hydrogen Energy},
  year    = {2023},
  doi     = {10.1016/j.ijhydene.2023.09.065}
}

@article{wulf2021,
  author  = {Wulf, Christoph and Beller, Matthias and Boenisch, Tim and Deutschmann, Olaf and Hanf, Schirin and Kockmann, Norbert and Kraehnert, Ralph and Oezaslan, Mehtap and Palkovits, Stefan and Schimmler, Sonja and Schunk, Stephan and Wagemann, Kurt and Linke, David},
  title   = {A Unified Research Data Infrastructure for Catalysis Research -- Challenges and Concepts},
  journal = {ChemCatChem},
  year    = {2021},
  volume  = {13},
  doi     = {10.1002/cctc.202001974}
}

@article{hoque2018,
  author  = {Hoque, Md Ariful and Guzman, Marcelo I.},
  title   = {Photocatalytic Activity: Experimental Features to Report in Heterogeneous Photocatalysis},
  journal = {Materials},
  year    = {2018},
  volume  = {11},
  number  = {10},
  pages   = {1990},
  doi     = {10.3390/ma11101990}
}
```

## Step 2 — Plan the remaining work packages, in order (and present)
Write `paper/SUBMISSION_PLAN.md` — an ordered, dependency-aware path to submission. Each WP:
goal · output · blocker/dependency · owner (CLI vs user). Seed it with at least:

1. **WP-CITE — bibliography completion** (this command): convert placeholders; report residual.
2. **WP-COMPILE — build the PDF.** Blocker: no `pdflatex` on this machine. Options to state:
   (a) install a TeX distribution, (b) Overleaf/online, (c) a CI LaTeX action. Mark as
   user-dependency; verify structure/refs compile-clean in the meantime.
3. **WP-FRONTMATTER — elsarticle conversion:** switch to `elsarticle`, add authors/affiliations,
   highlights, graphical abstract, keywords. Blocker: author/affiliation info (user).
4. **WP-POLISH — final pass:** `writing-anti-ai` style sweep + `paper-self-review` end-to-end;
   confirm every number traces to `results/real_v1/`; nulls power-framed; associational language.
5. **WP-DATA-RELEASE — Zenodo:** mint a versioned DOI for the curated dataset (CC-BY) + code (MIT);
   cite it in the Data Availability section. Blocker: user Zenodo account.
6. **WP-SUBMISSION-PREP:** cover letter, suggested reviewers, IJHE author checklist; final
   read-through. Decide venue (IJHE primary / Energy and AI floor) at this gate.

Order the WPs by dependency; mark which are CLI-doable now vs user-gated. Present the plan in the
final message.

## Step 3 — Push final state
Commit (`docs(paper): complete bibliography from verified metadata + submission plan`) and push to
GitHub. Working tree clean.

## Rules / Definition of done
- No fabricated bib entries or numbers; verification tier tagged per entry.
- Residual `\todocite` count reported explicitly (target zero; list any exceptions).
- `paper/SUBMISSION_PLAN.md` written, committed, pushed, and presented to the user.
- Pipeline stops for the user after presenting the plan.
