# CLI Command — Fill author identity + AI-use disclosure (CLI-doable now)

> Paste into Claude Code at the AIH2 repo root. The user provided author identity. Fill the
> placeholders exactly; do not invent anything beyond what is given. Single author unless told
> otherwise. Commit + push. Then report what still needs the user.

## Author details (use verbatim)
- **Name:** Dogukan Unal
- **ORCID:** 0009-0006-5102-8013  (https://orcid.org/0009-0006-5102-8013)
- **Email (corresponding):** dunal@ipec.com.tr
- **Affiliation:** IPEC, Industrial Project Engineering Consulting, Çankaya, Ankara, 06550, Türkiye
- **Zenodo username:** dunal  (for `.zenodo.json` creator; ORCID as above)

## Do
1. `paper/main.tex` frontmatter: set the author, affiliation, ORCID, corresponding-author email
   (replace all `[AUTHOR …]` placeholders). Single author.
2. **CRediT:** assign all roles to Dogukan Unal (conceptualization, methodology, software,
   formal analysis, data curation, writing — original draft, writing — review & editing,
   visualization). Leave a one-line note that co-authors can be added if applicable.
3. `.zenodo.json`: creators = [{name: "Unal, Dogukan", orcid: 0009-0006-5102-8013,
   affiliation: "IPEC, Industrial Project Engineering Consulting, Ankara, Türkiye"}]; licenses
   already CC-BY-4.0 (data) / MIT (code).
4. **AI-use disclosure (Elsevier requirement — write it honestly, do NOT minimize).** Add a
   "Declaration of generative AI and AI-assisted technologies" statement to `main.tex` stating
   plainly that AI agents (Claude / Claude Code) were used for literature triage, data extraction
   assistance, statistical analysis, figure generation, and manuscript drafting **under the
   author's direction, with the author verifying all data, results, and claims and taking full
   responsibility for the content.** AI is not listed as an author. Put a copy in
   `paper/submission/ai_disclosure.md`. Flag it `% AUTHOR: confirm accuracy & completeness`.
5. Update `paper/submission/cover_letter.md` and `suggested_reviewers.md` with the corresponding
   author block.
6. Structural lint (`tools/lint_paper.py`) must stay clean. Commit
   (`docs(paper): add author identity, CRediT, and AI-use disclosure`) + push.

## Still requires the user (report these back, do not fabricate)
- Zenodo **DOI** (after the user deposits) → to replace `\todo{Zenodo DOI}`.
- Confirmation of **single author** (or co-author list).
- **Venue** sign-off and the actual **journal submission**.
- Author confirms the **AI-disclosure** wording is accurate and complete.

## Definition of done
- All author placeholders filled (main.tex, .zenodo.json, cover letter); CRediT set; AI disclosure
  added (flagged for author confirmation); lint clean; committed + pushed; remaining user gates listed.
