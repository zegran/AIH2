"""
Fetch BibTeX from Crossref for all Tier-A (28) and Tier-B (12) missing citations.
NEVER writes BibTeX from memory — all entries fetched by DOI from Crossref.
Outputs to tools/fetched_bibtex.txt for review before insertion into references.bib.

Usage: uv run python tools/fetch_bibtex.py
"""
import time
import urllib.request
import urllib.parse
import urllib.error
import json
import sys

POLITE_HEADER = {"User-Agent": "AIH2-paper/1.0 (mailto:dunal@ipec.com.tr)"}

# 28 Tier-A data sources (must cite — attribution obligation)
TIER_A = {
    "prabu2021":      "10.1002/er.6478",
    "gupta2025":      "10.1007/s40243-024-00287-2",
    "wanghq2017":     "10.1016/j.energy.2017.05.031",
    "xiao2018":       "10.1016/j.energy.2018.05.201",
    "guan2019":       "10.1016/j.energy.2019.116107",
    "ilyukhina2012":  "10.1016/j.ijhydene.2012.02.175",
    "yavor2013":      "10.1016/j.ijhydene.2013.09.070",
    "ho2016":         "10.1016/j.ijhydene.2015.11.083",
    "dudoladov2016":  "10.1016/j.ijhydene.2015.11.122",
    "liuyh2017":      "10.1016/j.ijhydene.2017.02.205",
    "preez2018":      "10.1016/j.ijhydene.2018.09.133",
    "qiao2019":       "10.1016/j.ijhydene.2018.12.124",
    "chen2020":       "10.1016/j.ijhydene.2020.03.027",
    "fischman2020":   "10.1016/j.ijhydene.2020.04.161",
    "rin2021":        "10.1016/j.ijhydene.2021.06.101",
    "meng2022":       "10.1016/j.ijhydene.2022.09.127",
    "xiao2020":       "10.1016/j.jallcom.2019.152800",
    "lu2017":         "10.1039/c7ra01839h",
    "trowell2022":    "10.1039/d2ra01231f",
    "deng2010":       "10.1111/j.1551-2916.2010.03969.x",
    "zhang2024":      "10.3389/fenrg.2024.1441155",
    "knoks2025":      "10.3390/app15052640",
    "mezulis2023":    "10.3390/en16145554",
    "martinezv2026":  "10.3390/hydrogen7020055",
    "davies2022mat":  "10.3390/ma15031197",
    "buryakov2023met":"10.3390/met13020185",
    "jayaraman2015":  "10.4236/epe.2015.79041",
    "fadhilah2023":   "10.9767/bcrec.20041",
}

# 12 Tier-B domain-context studies (screening funnel + regime context)
TIER_B = {
    "razavi2016":   "10.1016/j.ijhydene.2015.11.080",
    "yang2018":     "10.1002/er.3953",
    "shmelev2016":  "10.1016/j.ijhydene.2016.05.159",
    "noland2020":   "10.1016/j.ijhydene.2020.06.165",
    "wangxy2021":   "10.1016/j.ijhydene.2021.07.191",
    "elitzur2014":  "10.1016/j.ijhydene.2014.02.037",
    "tan2016":      "10.1016/j.ijhydene.2016.10.090",
    "godart2019":   "10.1016/j.ijhydene.2019.03.140",
    "razavi2013":   "10.1016/j.ijhydene.2012.10.106",
    "preez2019":    "10.1016/j.ijhydene.2019.06.154",
    "david2012":    "10.1016/j.jhazmat.2012.01.064",
    "slocum2020":   "10.1016/j.apenergy.2020.115712",
}


def fetch_bibtex_crossref(doi: str) -> str | None:
    """Fetch BibTeX from Crossref transform endpoint."""
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded}/transform/application/x-bibtex"
    req = urllib.request.Request(url, headers=POLITE_HEADER)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return None
    except Exception as e:
        return None


def fetch_metadata_crossref(doi: str) -> dict | None:
    """Fallback: fetch JSON metadata from Crossref."""
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded}"
    req = urllib.request.Request(url, headers=POLITE_HEADER)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("message", {})
    except Exception:
        return None


def metadata_to_bibtex(key: str, doi: str, meta: dict) -> str:
    """Construct minimal BibTeX from Crossref metadata (fallback)."""
    title = ""
    raw_title = meta.get("title", [""])
    if raw_title:
        title = raw_title[0]

    authors = []
    for a in meta.get("author", []):
        family = a.get("family", "")
        given = a.get("given", "")
        if family:
            authors.append(f"{family}, {given}" if given else family)
    author_str = " and ".join(authors) if authors else "Unknown"

    year = ""
    pub_date = meta.get("published-print") or meta.get("published-online") or meta.get("issued")
    if pub_date:
        parts = pub_date.get("date-parts", [[]])
        if parts and parts[0]:
            year = str(parts[0][0])

    journal = ""
    container = meta.get("container-title", [])
    if container:
        journal = container[0]

    volume = meta.get("volume", "")
    page = meta.get("page", "")
    type_ = meta.get("type", "journal-article")

    bib_type = "article" if type_ in ("journal-article", "proceedings-article") else "misc"

    lines = [f"@{bib_type}{{{key},"]
    lines.append(f"  author  = {{{author_str}}},")
    if title:
        lines.append(f"  title   = {{{title}}},")
    if journal:
        lines.append(f"  journal = {{{journal}}},")
    if year:
        lines.append(f"  year    = {{{year}}},")
    if volume:
        lines.append(f"  volume  = {{{volume}}},")
    if page:
        lines.append(f"  pages   = {{{page}}},")
    lines.append(f"  doi     = {{{doi}}}}}")
    return "\n".join(lines)


def process_all():
    results = {}
    failures = []
    all_dois = {**{k: (v, "full-text") for k, v in TIER_A.items()},
                **{k: (v, "metadata") for k, v in TIER_B.items()}}

    for key, (doi, tier) in all_dois.items():
        print(f"  Fetching {key} ({doi}) ...", end=" ", flush=True)
        bib = fetch_bibtex_crossref(doi)
        if bib:
            # Crossref uses its own key format; replace with canonical key
            import re
            bib = re.sub(r"@(\w+)\{[^,]+,", f"@\\1{{{key},", bib, count=1)
            # Add tier tag comment
            tier_tag = f"  % verified: {tier}"
            bib = bib.rstrip() + "\n" + tier_tag
            results[key] = bib
            print("OK")
        else:
            # Fallback to metadata
            print("BibTeX endpoint failed, trying metadata...", end=" ", flush=True)
            meta = fetch_metadata_crossref(doi)
            if meta:
                bib = metadata_to_bibtex(key, doi, meta)
                tier_tag = f"  % verified: {tier} (metadata fallback)"
                bib = bib + "\n" + tier_tag
                results[key] = bib
                print("OK (metadata)")
            else:
                failures.append((key, doi))
                print("FAILED")
        time.sleep(0.3)  # polite rate limit

    out_path = "tools/fetched_bibtex.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("% ================================================================\n")
        f.write("% Auto-fetched BibTeX from Crossref by DOI — tools/fetch_bibtex.py\n")
        f.write("% ================================================================\n\n")
        f.write("% ==== Tier A — data sources (28 entries) ====\n\n")
        for key in TIER_A:
            if key in results:
                f.write(results[key] + "\n\n")
        f.write("\n% ==== Tier B — domain context (12 entries) ====\n\n")
        for key in TIER_B:
            if key in results:
                f.write(results[key] + "\n\n")

    print(f"\nWrote {len(results)} entries to {out_path}")
    if failures:
        print(f"FAILED ({len(failures)}): " + ", ".join(f"{k} ({d})" for k, d in failures))
    return results, failures


if __name__ == "__main__":
    results, failures = process_all()
    sys.exit(1 if failures else 0)
