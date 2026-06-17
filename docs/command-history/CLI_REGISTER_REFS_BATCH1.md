# CLI Command — Register reference batch 1 (7 positioning refs) + wire citations

> Paste into Claude Code at the AIH2 repo root. These 7 are **citation/positioning references**
> (method-precedent & framing) — NOT Al-hydrolysis data sources. Do **not** add them to the dataset;
> add them to the bibliography and convert the matching `\todocite` placeholders to real `\cite`.
> Verified bibliographic metadata is provided below (from the Consensus reference list) so **no
> BibTeX is fabricated**. Leave all other placeholders as-is until their refs arrive.

## What to do
1. Append the 7 entries below to `paper/references.bib` (exact, verbatim).
2. In `paper/sections/*.tex`, find the `\todocite{...}` placeholders that correspond to these
   references (by topic/DOI) and replace them with `\cite{<citekey>}`. Leave non-matching
   placeholders untouched.
3. If the PDFs are available (user's downloads folder), run **`citation-verification`** to confirm
   each draft claim that cites these matches the source; record results in `paper/SELF_REVIEW.md`.
   Do not change claims to fit citations — flag mismatches instead.
4. Report: which placeholders were resolved (count), which remain (count), any verification flags.

## Verified BibTeX (paste verbatim)
```bibtex
@article{bernett2024,
  author  = {Bernett, Judith and Blumenthal, David B. and Grimm, Dominik G. and Haselbeck, Florian and Joeres, Roman and Kalinina, Olga V. and List, Markus},
  title   = {Guiding questions to avoid data leakage in biological machine learning applications},
  journal = {Nature Methods},
  year    = {2024},
  volume  = {21},
  pages   = {1444--1453},
  doi     = {10.1038/s41592-024-02362-y}
}

@article{john2025,
  author  = {John, Kingsley and Saurette, Daniel D. and Heung, Brandon},
  title   = {The problematic case of data leakage: A case for leave-profile-out cross-validation in 3-dimensional digital soil mapping},
  journal = {Geoderma},
  year    = {2025},
  doi     = {10.1016/j.geoderma.2025.117223}
}

@article{suvarna2024,
  author  = {Suvarna, Manu and P{\'e}rez-Ram{\'i}rez, Javier},
  title   = {Embracing data science in catalysis research},
  journal = {Nature Catalysis},
  year    = {2024},
  volume  = {7},
  pages   = {624--635},
  doi     = {10.1038/s41929-024-01150-3}
}

@article{bozalginesta2025,
  author  = {Bozal-Ginesta, Carlota and Pablo-Garc{\'i}a, Sergio and Choi, Changhyeok and Taranc{\'o}n, Albert and Aspuru-Guzik, Al{\'a}n},
  title   = {Developing machine learning for heterogeneous catalysis with experimental and computational data},
  journal = {Nature Reviews Chemistry},
  year    = {2025},
  doi     = {10.1038/s41570-025-00740-4}
}

@article{coelho2022,
  author  = {Coelho, Leonardo B. and Zhang, Dawei and Van Ingelgem, Yves and Steckelmacher, Denis and Now{\'e}, Ann and Terryn, Herman},
  title   = {Reviewing machine learning of corrosion prediction in a data-oriented perspective},
  journal = {npj Materials Degradation},
  year    = {2022},
  volume  = {6},
  pages   = {1--16},
  doi     = {10.1038/s41529-022-00218-4}
}

@article{xue2024,
  author  = {Xue, Pengcheng and Qiu, Ruihu and Peng, Cheng and Peng, Zhuoran and Ding, Kang and Long, Rui and Zheng, Qi},
  title   = {Solutions for Lithium Battery Materials Data Issues in Machine Learning: Overview and Future Outlook},
  journal = {Advanced Science},
  year    = {2024},
  volume  = {11},
  doi     = {10.1002/advs.202410065}
}

@article{noble2022,
  author  = {Noble, Daniel W. A. and Pottier, Patrice and Lagisz, Malgorzata and Burke, Samantha and Drobniak, Szymon M. and O'Dea, Rose E. and Nakagawa, Shinichi},
  title   = {Meta-analytic approaches and effect sizes to account for `nuisance heterogeneity' in comparative physiology},
  journal = {Journal of Experimental Biology},
  year    = {2022},
  volume  = {225},
  number  = {Suppl_1},
  doi     = {10.1242/jeb.243225}
}
```

## Suggested citation placement (verify against the draft, don't force)
- `bernett2024`, `john2025` — Introduction/Method: study-level data leakage & grouped/leave-group-out CV precedent.
- `suvarna2024`, `bozalginesta2025` — Introduction/Discussion: data-science/standardization in catalysis & heterogeneous-data ML.
- `coelho2022`, `xue2024` — Related work: data-quality/heterogeneity problems in materials ML (corrosion, batteries).
- `noble2022` — Method/Discussion: meta-analytic handling of nuisance heterogeneity (supports the mixed/variance-decomposition framing).

## Rules / Definition of done
- Only these 7 added; dataset untouched; remaining `\todocite` placeholders preserved.
- No fabricated entries; metadata exactly as above. Conventional Commit
  (`docs(paper): add positioning refs batch 1 (7) + wire citations`).
- Report resolved/remaining placeholder counts + any citation-verification flags; stop for user.
