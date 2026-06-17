# Submission plan — ordered, dependency-aware path to submission

Status snapshot (2026-06-17, FINALE): full honest draft; 6 Q1 figures wired + bundled in
`paper/figures/`; `elsarticle` frontmatter + highlights + keywords; bibliography complete (zero
placeholders); structural lint clean; LaTeX CI added; data-release + submission packages drafted.
All CLI-doable finalization is done — only three user gates remain. Venue: IJHE primary, Energy and
AI floor. Below, each work package lists goal · output · blocker/dependency · owner.

| # | WP | % | gate |
|---|---|---|---|
| 1 | WP-CITE | **100%** | done (CLI) |
| 4 | WP-POLISH | **100%** | done (CLI) |
| 3 | WP-FRONTMATTER | **~85%** | elsarticle + highlights + keywords done; needs real author/affiliation/ORCID + CRediT roles |
| 2 | WP-COMPILE | **~90%** | CI YAML + lint clean; needs the user to confirm the GitHub Actions build is green |
| 5 | WP-DATA-RELEASE | **~70%** | `.zenodo.json` + dataset card done; user mints the Zenodo DOI |
| 6 | WP-SUBMISSION-PREP | **~80%** | cover letter / reviewers / checklist drafted; needs venue sign-off + author identity |

**Overall submission-readiness ≈ 88%.** Content and packaging are complete (≈100% of what the CLI can
do): draft, 6 figures, self-contained build, bibliography, reporting standard, elsarticle frontmatter,
CI compile, data-release metadata, cover letter, reviewer template, checklist. The remaining ~12% is
**three user gates only**: **(a) real author/affiliation/ORCID + CRediT**, **(b) Zenodo deposit to
mint the dataset DOI** (insert it where `\todo{Zenodo DOI}` appears), **(c) final venue sign-off +
submit**. Confirming the CI build is green is the one mechanical check the dev environment cannot run.

## 1. WP-CITE — bibliography completion ✅ DONE
- **Goal:** every citation backed by verified BibTeX; zero placeholders.
- **Output:** `references.bib` (18 entries, tier-tagged) wired into the draft; `SELF_REVIEW.md` §5
  records the verification flags (testa2024 claim removed; das $R^2$ softened; xiao review omitted).
- **Residual (non-blocking):** confirm the Das exact in-sample $R^2$ against full text if wanted.
- **Owner:** CLI (complete).

## 2. WP-COMPILE — build the PDF  ⛔ user-gated
- **Goal:** `main.tex` compiles clean (no undefined refs, floats placed).
- **Blocker:** no `pdflatex` in this environment. **Options:** (a) install TeX Live/MiKTeX locally,
  (b) upload `paper/` to Overleaf, (c) add a GitHub Actions LaTeX workflow (CLI can write the YAML).
- **CLI can do now:** structure already verified (all `\input` present, no stray `\end{document}`,
  `\todocite` macro defined, zero placeholders, figures regenerable via the WP5 script). On request,
  CLI will add a `.github/workflows/latex.yml` so each push produces a PDF artifact.
- **Owner:** user (choose a build path) + CLI (CI YAML).

## 3. WP-FRONTMATTER — elsarticle conversion  ⛔ user-gated
- **Goal:** Elsevier `elsarticle` format with authors, affiliations, highlights (3–5 bullets),
  graphical abstract, keywords, and corresponding-author block.
- **Blocker:** author names, affiliations, ORCIDs, corresponding-author email (user).
- **CLI can do now:** the mechanical `\documentclass[preprint,review,12pt]{elsarticle}` +
  `\begin{frontmatter}` conversion, highlights drafted from the results, keyword list, and a
  graphical-abstract figure (reuse fig2). Names inserted once provided.
- **Owner:** user (identity) + CLI (conversion + highlights/keywords/graphical abstract).

## 4. WP-POLISH — final language + traceability pass  ⏳ CLI-doable now
- **Goal:** `writing-anti-ai` style sweep; end-to-end `paper-self-review`; confirm every number
  traces to `results/real_v1/`; nulls power-framed; associational language; soften residual "driver".
- **Output:** revised sections + updated `SELF_REVIEW.md` verdict.
- **Owner:** CLI. **Recommended next CLI step.**

## 5. WP-DATA-RELEASE — Zenodo deposit  ⛔ user-gated
- **Goal:** versioned DOI for the curated dataset (CC-BY) + code (MIT); cite it in Data Availability.
- **Blocker:** user Zenodo account / GitHub–Zenodo link.
- **CLI can do now:** prepare the deposit package — `.zenodo.json` metadata, a `DATASET_CARD.md`
  (schema, provenance, quality tiers, licensing), and the file manifest (yield + kinetic tables,
  data dictionary). User mints the DOI; CLI inserts it into the paper.
- **Owner:** user (account/mint) + CLI (package + metadata).

## 6. WP-SUBMISSION-PREP — cover letter, reviewers, checklist, venue  ⏳ CLI-draftable
- **Goal:** submission-ready package and a final venue decision (IJHE vs Energy and AI).
- **Output:** cover letter (honest framing: methodological-heterogeneity finding + open dataset +
  reporting standard), 3–5 suggested reviewers with justification, IJHE author-checklist pass, final
  read-through.
- **Blocker:** venue choice + reviewer preferences (user); author identity (WP-FRONTMATTER).
- **Owner:** CLI (drafts) + user (decisions, sign).

## Critical path
WP-CITE ✅ → **WP-POLISH (CLI, now)** → WP-FRONTMATTER (needs author info) → WP-COMPILE (needs a TeX
build path) → WP-DATA-RELEASE (needs Zenodo) → WP-SUBMISSION-PREP → submit.
The two hard user gates are **author/affiliation info** (WP-FRONTMATTER) and a **TeX build path**
(WP-COMPILE); everything else CLI can advance now.
