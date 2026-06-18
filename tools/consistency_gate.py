"""Strict numerical consistency gate for paper/main.tex + section files + figure catalog.

Checks:
  1. Headline values present in the ABSTRACT (main.tex) specifically.
  2. Headline values present in RESULTS (results.tex) specifically.
  3. Figure-catalog.md carries 0.717/0.425 and NOT the stale method-share 0.55/0.33.
  4. Old method-share values (0.553, 0.332 standalone) absent from all .tex files.
  5. The fig1 optimism-gap R2~0.55 is correctly preserved (should remain in text).

Exit code 0 = consistent, 1 = drift detected.
Run: uv run python tools/consistency_gate.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1] / "paper"
RESULTS_DIR = Path(__file__).resolve().parents[1] / "results" / "real_v1" / "figures"
TEX_FILES = [PAPER / "main.tex", *sorted((PAPER / "sections").glob("*.tex"))]

MAIN_TEX   = PAPER / "main.tex"
RESULTS_TEX = PAPER / "sections" / "results.tex"
CATALOG    = RESULTS_DIR / "figure-catalog.md"


def read(p: Path) -> str:
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8", errors="replace")


def all_tex() -> str:
    return "\n".join(read(f) for f in TEX_FILES)


errors: list[str] = []


def require(text: str, pattern: str, msg: str, flags: int = 0) -> None:
    if not re.search(pattern, text, flags):
        errors.append(f"[MISSING] {msg}")


def forbid(text: str, pattern: str, msg: str, filename: str = "", flags: int = 0) -> None:
    if re.search(pattern, text, flags):
        loc = f" (in {filename})" if filename else ""
        errors.append(f"[FORBIDDEN] {msg}{loc}")


def main() -> int:
    main_src   = read(MAIN_TEX)
    results_src = read(RESULTS_TEX)
    catalog_src = read(CATALOG)
    all_src    = all_tex()

    # ── 1. ABSTRACT must contain the headline approx-percent forms ──────────────
    # The abstract lives in main.tex between \begin{abstract} and \end{abstract}
    abs_match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main_src,
                          re.DOTALL)
    abstract = abs_match.group(1) if abs_match else ""
    require(abstract, r"72",        "abstract: ~72% (joint method) not found in abstract block")
    require(abstract, r"43",        "abstract: ~43% (measurement apparatus) not found in abstract block")
    require(abstract, r"approx.*?2\\,?\\%|2\\,?\\%.*?regime|regime.*?2",
            "abstract: ~2% (regime) not found in abstract block", re.DOTALL)

    # ── 2. RESULTS must contain the exact R² values ──────────────────────────────
    require(results_src, r"0\.717", "results.tex: R2=0.717 (joint method) not found")
    require(results_src, r"0\.425", "results.tex: R2=0.425 (measurement_method) not found")
    require(results_src, r"0\.081", "results.tex: R2=0.081 (temperature_control) not found")
    require(results_src, r"0\.443", "results.tex: CI lower bound 0.443 for joint method not found")

    # ── 3. FIGURE CATALOG must carry corrected values and NOT stale ones ─────────
    if not CATALOG.exists():
        errors.append("[MISSING] figure-catalog.md not found at results/real_v1/figures/")
    else:
        require(catalog_src, r"0\.717",
                "figure-catalog.md: 0.717 (corrected joint R2) not found")
        require(catalog_src, r"0\.425",
                "figure-catalog.md: 0.425 (corrected measurement_method R2) not found")
        # Stale method-share 0.55 must be absent from the fig2 section
        # (fig1 section legitimately has "0.55" for optimism-gap — that's OK)
        fig2_section = re.search(r"## fig2.*?(?=## fig[3-9]|\Z)", catalog_src, re.DOTALL)
        if fig2_section:
            fig2_text = fig2_section.group(0)
            forbid(fig2_text, r"(?<![0-9])0\.5[3-5][0-9]?(?![0-9])",
                   "figure-catalog.md fig2 section still contains stale method-share ~0.55",
                   "figure-catalog.md")
            forbid(fig2_text, r"\b0\.33\b",
                   "figure-catalog.md fig2 section still contains stale TC R2=0.33",
                   "figure-catalog.md")

    # ── 4. OLD method-share values absent from .tex source ──────────────────────
    # 0.553 must not appear anywhere as a current value
    forbid(all_src, r"0\.553",
           "stale joint R2=0.553 found in paper source — update to 0.717",
           "paper/*.tex")

    # 0.332 is only OK in transition notation "0.332 to 0.081" or "0.332\to0.081"
    for f in TEX_FILES:
        ft = read(f)
        # Match 0.332 not immediately followed by transition words/symbols
        standalone = re.findall(r"0\.332(?!\$? to|\\to)", ft)
        if standalone:
            errors.append(f"[FORBIDDEN] stale R2=0.332 (standalone) in {f.name}")

    # Old TC-as-lead phrasing: check per-line to avoid DOTALL false positives
    # Flag lines where TC is described as "single largest" or "alone explains ~33%"
    for f in TEX_FILES:
        for line in read(f).splitlines():
            if re.search(r"temperature.control", line, re.IGNORECASE):
                # Line mentions TC AND claims it as the single largest source AND cites ~33%
                if (re.search(r"single.largest|alone.*explain|largest.source", line, re.IGNORECASE)
                        and re.search(r"(?:33|0\.33)(?!\d)", line)):
                    errors.append(
                        f"[FORBIDDEN] stale 'TC single-largest/~33%' on line in {f.name}: "
                        + line.strip()[:80]
                    )

    # ── 5. FIG1 optimism-gap R2~0.55 must still be present (positive control) ──
    require(results_src, r"0\.5[4-7]",
            "results.tex: R2~0.55 optimism-gap value missing (must be preserved)")
    require(main_src, r"0\.5[4-7]",
            "main.tex: R2~0.55 optimism-gap value missing in abstract/highlights (must be preserved)")

    # ── Report ──────────────────────────────────────────────────────────────────
    if not errors:
        sys.stdout.buffer.write(b"CONSISTENCY GATE PASS -- all headline values consistent.\n")
        return 0

    sys.stdout.buffer.write(b"CONSISTENCY GATE FAILURES:\n")
    for e in errors:
        sys.stdout.buffer.write(("  " + e + "\n").encode("utf-8", errors="replace"))
    return 1


if __name__ == "__main__":
    sys.exit(main())
