"""Structural lint for paper/main.tex before a LaTeX build (no TeX install required).

Checks, across main.tex + sections/*.tex:
  1. every \cite/\citep/\citet/\citealp key exists in references.bib;
  2. every \ref{label} resolves to a \label{label};
  3. every \includegraphics path exists under the graphicspath (paper/figures/);
  4. no \todocite{...} *usage* remains (the \newcommand definition is allowed).

Exit code 0 = clean, 1 = problems found. Run: uv run python tools/lint_paper.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1] / "paper"
FIGDIR = PAPER / "figures"
TEX_FILES = [PAPER / "main.tex", *sorted((PAPER / "sections").glob("*.tex"))]
# sections actually pulled in via \input (orphans are reported, not linted for refs)
INPUTS = {"introduction", "related_work", "method", "results", "discussion", "conclusion"}


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def bib_keys() -> set[str]:
    txt = read(PAPER / "references.bib")
    return set(re.findall(r"@\w+\{\s*([^,\s]+)", txt))


def collect(pattern: str, files: list[Path]) -> list[tuple[str, Path]]:
    out: list[tuple[str, Path]] = []
    for f in files:
        for m in re.findall(pattern, read(f)):
            out.append((m, f))
    return out


def main() -> int:
    problems: list[str] = []
    keys = bib_keys()

    # 1. citations -> bib
    cited: set[str] = set()
    for grp, _f in collect(r"\\cite[a-z]*\{([^}]*)\}", TEX_FILES):
        cited.update(k.strip() for k in grp.split(",") if k.strip())
    missing = sorted(cited - keys)
    if missing:
        problems.append(f"[cite] keys used but NOT in references.bib: {missing}")
    unused = sorted(keys - cited)
    if unused:
        problems.append(f"[cite] references.bib entries never cited (warning): {unused}")

    # 2. refs -> labels
    labels = {m for m, _ in collect(r"\\label\{([^}]*)\}", TEX_FILES)}
    refs = {m for m, _ in collect(r"\\(?:ref|eqref|autoref)\{([^}]*)\}", TEX_FILES)}
    dangling = sorted(refs - labels)
    if dangling:
        problems.append(f"[ref] \\ref to undefined \\label: {dangling}")

    # 3. includegraphics -> file exists
    for path, f in collect(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", TEX_FILES):
        name = path.strip()
        cand = [FIGDIR / name]
        if not Path(name).suffix:
            cand += [FIGDIR / f"{name}.pdf", FIGDIR / f"{name}.png"]
        if not any(c.exists() for c in cand):
            problems.append(f"[fig] missing graphic '{name}' (referenced in {f.name})")

    # 4. todocite usage (definition line excluded)
    for f in TEX_FILES:
        for ln in read(f).splitlines():
            if "\\todocite{" in ln and "newcommand" not in ln:
                problems.append(f"[todocite] unresolved placeholder in {f.name}: {ln.strip()[:70]}")

    # 5. amssymb-only macros require \usepackage{amssymb} (a common "undefined control sequence")
    def strip_comments(txt: str) -> str:
        return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in txt.splitlines())
    amssymb_macros = ["blacksquare", "square", "mathbb", "checkmark", "varnothing",
                      "lesssim", "gtrsim", "therefore", "because", "blacktriangle"]
    has_amssymb = "amssymb" in strip_comments(read(PAPER / "main.tex"))
    used_sym = sorted({m for f in TEX_FILES for m in amssymb_macros
                       if re.search(r"\\" + m + r"\b", strip_comments(read(f)))})
    if used_sym and not has_amssymb:
        problems.append(f"[pkg] amssymb macros used without \\usepackage{{amssymb}}: {used_sym}")

    # orphan section files (present but not \input)
    present = {p.stem for p in (PAPER / "sections").glob("*.tex")}
    orphans = sorted(present - INPUTS)
    if orphans:
        problems.append(f"[orphan] sections/*.tex not \\input by main.tex (warning): {orphans}")

    print(f"cite keys: {len(keys)} defined, {len(cited)} cited | "
          f"labels: {len(labels)} | refs: {len(refs)}")
    if not problems:
        print("LINT CLEAN — structure is build-ready.")
        return 0
    print("\nLINT FINDINGS:")
    for p in problems:
        print("  -", p)
    # warnings (unused refs / orphan files) do not fail the build; hard errors do.
    hard = [p for p in problems if "(warning)" not in p]
    print(f"\n{len(hard)} hard error(s), {len(problems) - len(hard)} warning(s).")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
