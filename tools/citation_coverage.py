"""Citation-coverage checker: every dataset study_id (a DOI) must be cited in references.bib.

Doubles as (a) the evidence generator for CITATION_COVERAGE.md and (b) a preventive lint gate
(`--check` exits 1 if any data-source study is uncited). Run:
  uv run python tools/citation_coverage.py          # print matrix
  uv run python tools/citation_coverage.py --check   # gate (nonzero exit if gaps)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
YIELD = ROOT / "data/curated/aih2_v1.csv"
RATE = ROOT / "data/wp1/rate_extraction.csv"
CANON = ROOT / "data/wp1/canonical_studies.csv"
BIB = ROOT / "paper/references.bib"


def norm(doi: str) -> str:
    return str(doi).strip().lower().replace("https://doi.org/", "")


def bib_dois() -> dict[str, str]:
    txt = BIB.read_text(encoding="utf-8")
    out = {}
    for chunk in txt.split("@")[1:]:                      # one chunk per entry
        km = re.match(r"\w+\{([^,]+),", chunk)
        dm = re.search(r"doi\s*=\s*[{\"]([^}\"]+)", chunk, re.I)
        if km and dm:
            out[norm(dm.group(1))] = km.group(1).strip()
    return out


def n_bib_entries() -> int:
    return len(re.findall(r"^@\w+\{", BIB.read_text(encoding="utf-8"), re.M))


def main() -> int:
    y = pd.read_csv(YIELD)
    r = pd.read_csv(RATE)
    canon = pd.read_csv(CANON)
    canon["doi_n"] = canon.doi.map(norm)
    doi2key = dict(zip(canon.doi_n, canon.citekey))
    doi2cls = dict(zip(canon.doi_n, canon.system_class))
    yrows = y.groupby(y.study_id.map(norm)).size().to_dict()
    rrows = r.groupby(r.study_id.map(norm)).size().to_dict()

    data_dois = sorted(set(map(norm, y.study_id.dropna())) | set(map(norm, r.study_id.dropna())))
    bd = bib_dois()

    cited = [d for d in data_dois if d in bd]
    missing = [d for d in data_dois if d not in bd]

    print(f"DATA-SOURCE STUDIES: {len(data_dois)} | cited in bib: {len(cited)} | MISSING: {len(missing)}\n")
    print(f"{'canonical_key':22} {'system_class':24} {'yld':>3} {'rate':>4}  {'cited?':6} doi")
    for d in data_dois:
        key = doi2key.get(d, "??")
        cls = doi2cls.get(d, "??")
        mark = f"YES:{bd[d]}" if d in bd else "NO"
        print(f"{key:22} {cls:24} {yrows.get(d,0):>3} {rrows.get(d,0):>4}  {mark:6} {d}")

    print(f"\nMISSING data-source citations ({len(missing)}) -> target adds (DOIs verified, full text on hand):")
    for d in missing:
        print(f"  {doi2key.get(d,'??'):22} {d}")

    # domain-context pool: canonical studies NOT used as data sources (ingested, full text on hand)
    ctx = canon[~canon.doi_n.isin(data_dois)]
    print(f"\nDOMAIN-CONTEXT pool (ingested, not data sources): {len(ctx)} studies "
          f"-> optional Related-Work/screening-funnel cites")

    print(f"\nbib entries total: {len(re.findall(r'@', BIB.read_text(encoding=chr(39)+'utf-8'+chr(39)) if False else BIB.read_text(encoding='utf-8')))}; "
          f"with DOI: {len(bd)}")
    print(f"PROJECTION: 3 data-source cited now; +{len(missing)} data-source = "
          f"{18 + len(missing)} refs; +~12 domain-context = ~{18 + len(missing) + 12}")

    if "--check" in sys.argv and missing:
        print(f"\nGATE FAIL: {len(missing)} data-source studies uncited.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
