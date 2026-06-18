"""Approximate manuscript counts from the LaTeX source for the compliance report.
Crude LaTeX stripping (good enough for word-budget checks). Run: uv run python tools/paper_counts.py
"""
import re
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1] / "paper"
SECTIONS = ["introduction", "related_work", "method", "results", "discussion", "conclusion"]


def strip_latex(t: str) -> str:
    t = re.sub(r"(?<!\\)%.*", "", t)                 # comments
    t = re.sub(r"\\(begin|end)\{[^}]*\}", " ", t)     # environments
    t = re.sub(r"\$[^$]*\$", " ", t)                  # inline math
    t = re.sub(r"\\includegraphics(\[[^\]]*\])?\{[^}]*\}", " ", t)
    t = re.sub(r"\\(label|ref|eqref|cite[a-z]*|input|url|todo|ead|cortext|corref|affiliation)\b(\[[^\]]*\])?\{[^}]*\}", " ", t)
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", t)  # remaining commands
    t = re.sub(r"[{}~&\\]", " ", t)
    return t


def wc(t: str) -> int:
    return len([w for w in re.split(r"\s+", strip_latex(t).strip()) if re.search(r"[A-Za-z0-9]", w)])


main = (PAPER / "main.tex").read_text(encoding="utf-8")

# abstract
abs_m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main, re.S)
abs_wc = wc(abs_m.group(1)) if abs_m else 0

# highlights: each \item line, char length incl spaces (stripped of latex)
hi_block = re.search(r"\\section\*\{Highlights\}.*?\\begin\{itemize\}(.*?)\\end\{itemize\}", main, re.S)
highlights = []
if hi_block:
    for it in re.findall(r"\\item\s*(.*)", hi_block.group(1)):
        txt = strip_latex(it).strip()
        txt = re.sub(r"\s+", " ", txt)
        highlights.append(txt)

# keywords
kw_m = re.search(r"\\begin\{keyword\}(.*?)\\end\{keyword\}", main, re.S)
keywords = [k.strip() for k in re.split(r"\\sep", kw_m.group(1))] if kw_m else []
keywords = [strip_latex(k).strip() for k in keywords if strip_latex(k).strip()]

print(f"ABSTRACT words: {abs_wc}")
print(f"KEYWORDS ({len(keywords)}): {keywords}")
print(f"HIGHLIGHTS ({len(highlights)}):")
for h in highlights:
    n = len(h)
    print(f"   [{n:>3} chars] {'OK ' if n <= 85 else 'OVER'} | {h}")

total = abs_wc
print("\nPER-SECTION words:")
for s in SECTIONS:
    f = PAPER / "sections" / f"{s}.tex"
    n = wc(f.read_text(encoding="utf-8")) if f.exists() else 0
    total += n
    print(f"   {s:<14} {n}")
print(f"\nBODY+ABSTRACT total words: {total}")

# figures / tables / equations / refs
allsec = "\n".join((PAPER / "sections" / f"{s}.tex").read_text(encoding="utf-8") for s in SECTIONS)
nfig = allsec.count(r"\begin{figure}")
ntab = allsec.count(r"\begin{table}") + allsec.count(r"\begin{tabular}")
neq = len(re.findall(r"\\begin\{equation\}|\\\[", allsec))
nref = len(re.findall(r"@\w+\{", (PAPER / "references.bib").read_text(encoding="utf-8")))
print(f"\nfigures={nfig}  tables(env/tabular)={ntab}  display-eqs={neq}  references={nref}")
