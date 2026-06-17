"""Energy and AI compliance gate.

Checks the manuscript against Energy and AI Guide for Authors requirements.
Exit code 0 = pass, 1 = failures found.
Run: python tools/compliance_gate.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1] / "paper"

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def strip_latex_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in text.splitlines())

def count_abstract_words(main_text: str) -> int:
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main_text, re.DOTALL)
    if not m:
        return 0
    abstract = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", m.group(1))
    abstract = re.sub(r"\\[a-zA-Z]+\s*", " ", abstract)
    abstract = re.sub(r"\$[^$]*\$", " MATH ", abstract)
    abstract = re.sub(r"[{}\\\[\]]", " ", abstract)
    words = abstract.split()
    return len(words)

def check_keywords(main_text: str) -> int:
    m = re.search(r"\\begin\{keyword\}(.*?)\\end\{keyword\}", main_text, re.DOTALL)
    if not m:
        return 0
    kw_block = m.group(1)
    keywords = [k.strip() for k in re.split(r"\\sep", kw_block) if k.strip()]
    return len(keywords)

def check_highlights(main_text: str) -> tuple[int, list[str]]:
    # Strip LaTeX comments before searching
    text = strip_latex_comments(main_text)
    m = re.search(r"\\section\*\{Highlights\}.*?\\end\{itemize\}", text, re.DOTALL)
    if not m:
        return 0, []
    block = m.group(0)
    # Each highlight is one line; count \item occurrences
    items = re.findall(r"\\item\s+([^\n]+)", block)
    long_items = []
    for it in items:
        plain = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", it)
        plain = re.sub(r"\\[a-zA-Z]+\s*", " ", plain)
        plain = re.sub(r"\$[^$]*\$", " MATH ", plain)
        plain = re.sub(r"[{}\$\\]", " ", plain).strip()
        if len(plain) > 85:
            long_items.append(plain[:90] + "...")
    return len(items), long_items

def check_section_present(section_name: str, conclusion_text: str) -> bool:
    # Allow section names that START with section_name (handles longer official names)
    pattern = rf"\\section\*\{{{re.escape(section_name)}"
    return bool(re.search(pattern, conclusion_text, re.IGNORECASE))

def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    main_tex = read(PAPER / "main.tex")
    conclusion_tex = read(PAPER / "sections" / "conclusion.tex")

    # 1. Journal declaration
    if r"\journal{Energy and AI}" not in main_tex:
        failures.append("[FAIL] \\journal{Energy and AI} not found in main.tex")
    else:
        print("[PASS] Journal declaration: Energy and AI")

    # 2. Abstract word count <= 250
    n_words = count_abstract_words(main_tex)
    if n_words == 0:
        failures.append("[FAIL] Could not parse abstract from main.tex")
    elif n_words > 250:
        failures.append(f"[FAIL] Abstract ~{n_words} words (limit 250)")
    else:
        print(f"[PASS] Abstract ~{n_words} words (<= 250)")

    # 3. Keywords: 3–6
    n_kw = check_keywords(main_tex)
    if n_kw < 3:
        failures.append(f"[FAIL] Only {n_kw} keyword(s); Energy and AI requires 3–6")
    elif n_kw > 6:
        failures.append(f"[FAIL] {n_kw} keywords; Energy and AI limit is 6")
    else:
        print(f"[PASS] Keywords: {n_kw} (3–6 required)")

    # 4. Highlights: 3–5 bullets, each <= 85 chars
    n_hl, long_hl = check_highlights(main_tex)
    if n_hl < 3:
        failures.append(f"[FAIL] Only {n_hl} highlight(s); need 3–5")
    elif n_hl > 5:
        failures.append(f"[FAIL] {n_hl} highlights; Elsevier limit is 5")
    else:
        print(f"[PASS] Highlights: {n_hl} bullets (3–5 required)")
    if long_hl:
        for h in long_hl:
            warnings.append(f"[WARN] Highlight >85 chars: {h}")

    # 5. Acknowledgements / funding statement
    if not check_section_present("Acknowledgements", conclusion_tex):
        failures.append("[FAIL] No \\section*{Acknowledgements} in conclusion.tex")
    else:
        print("[PASS] Acknowledgements section present")

    # 6. Declaration of competing interest
    if not check_section_present("Declaration of competing interest", conclusion_tex):
        failures.append("[FAIL] No competing-interest declaration in conclusion.tex")
    else:
        print("[PASS] Declaration of competing interest present")

    # 7. CRediT authorship statement
    if "CRediT" not in conclusion_tex:
        failures.append("[FAIL] No CRediT authorship statement in conclusion.tex")
    else:
        print("[PASS] CRediT authorship statement present")

    # 8. Declaration of generative AI
    if not check_section_present("Declaration of generative AI", conclusion_tex):
        failures.append("[FAIL] No Declaration of generative AI in conclusion.tex")
    else:
        print("[PASS] Declaration of generative AI present")

    # 9. Data and code availability
    if "Data and code availability" not in conclusion_tex:
        failures.append("[FAIL] No data/code availability statement in conclusion.tex")
    else:
        print("[PASS] Data and code availability statement present")

    # 10. No unresolved \todo{} blocks (except Zenodo placeholder — flagged as warning)
    todo_pattern = re.compile(r"\\todo\{([^}]*)\}")
    all_tex = main_tex
    for sec in (PAPER / "sections").glob("*.tex"):
        all_tex += "\n" + read(sec)
    todos = todo_pattern.findall(all_tex)
    if todos:
        for t in todos:
            if "Zenodo" in t or "zenodo" in t:
                warnings.append(f"[WARN] Unresolved \\todo: {t} (needs Zenodo deposit)")
            else:
                failures.append(f"[FAIL] Unresolved \\todo{{{t}}}")
    else:
        print("[PASS] No unresolved \\todo{} blocks")

    # 11. elsarticle document class
    if "elsarticle" not in main_tex:
        failures.append("[FAIL] Not using elsarticle document class")
    else:
        print("[PASS] elsarticle document class in use")

    # 12. booktabs loaded (required for \toprule etc in tables)
    if "booktabs" not in main_tex:
        failures.append("[FAIL] \\usepackage{booktabs} not found")
    else:
        print("[PASS] booktabs loaded")

    # Summary
    print()
    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(" ", w)
        print()
    if failures:
        print("GATE 6 FAILURES:")
        for f in failures:
            print(" ", f)
        print(f"\nGATE 6: FAIL — {len(failures)} blocking issue(s), {len(warnings)} warning(s).")
        return 1
    else:
        print(f"GATE 6: PASS — all Energy and AI compliance checks passed ({len(warnings)} warning(s)).")
        return 0


if __name__ == "__main__":
    sys.exit(main())
