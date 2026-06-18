"""
Clean fetched BibTeX and append to references.bib.
Fixes: HTML tags in titles, &amp; entities, Unicode dashes in pages.
"""
import re


def clean_bib(text: str) -> str:
    # Remove HTML tags (e.g. <scp>, </scp>, <sub>, </sub>)
    text = re.sub(r"</?(?:scp|sub|sup|i|b|em)[^>]*>", "", text)
    # &amp; → \&
    text = text.replace("&amp;", r"\&")
    # Unicode en-dash in page ranges → --
    text = text.replace("–", "--")
    # Remove url= fields (keep DOI; urls add noise)
    text = re.sub(r",?\s*url=\{[^}]+\}", "", text)
    # Remove ISSN= fields (not needed; save space)
    text = re.sub(r",?\s*ISSN=\{[^}]+\}", "", text)
    # Fix publisher= fields with line-break artifacts
    text = re.sub(r"\s+", " ", text)
    return text


def main():
    with open("tools/fetched_bibtex.txt", encoding="utf-8") as f:
        raw = f.read()

    cleaned = clean_bib(raw)

    # Append to references.bib with a section header
    with open("paper/references.bib", "a", encoding="utf-8") as f:
        f.write("\n\n% ==== Tier-A data-source studies (28 entries — attribution obligation) ====\n")
        f.write("% Fetched from Crossref by DOI via tools/fetch_bibtex.py — never written from memory.\n\n")
        f.write(cleaned)

    print("Done — appended cleaned entries to paper/references.bib")


if __name__ == "__main__":
    main()
