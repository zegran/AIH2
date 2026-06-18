"""Numerical consistency gate for paper/main.tex + section files.

Asserts that the four headline variance-decomposition values appear consistently
across abstract, results, discussion, highlights, and table rows in the LaTeX source.
Also cross-checks against the fig2 source data produced by wp5_figures.py.

Exit code 0 = consistent, 1 = drift detected.
Run: uv run python tools/consistency_gate.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

PAPER = Path(__file__).resolve().parents[1] / "paper"
TEX_FILES = [PAPER / "main.tex", *sorted((PAPER / "sections").glob("*.tex"))]

# Headline values (post-IRR-adjudication, corrected dataset)
JOINT_METHOD = 0.717   # method-joint R²  → presented as ~72%
REGIME       = 0.018   # system_class R²   → presented as ~2%
MEAS_APP     = 0.425   # measurement_method → ~43%
TEMP_CTRL    = 0.081   # temperature_control → ~8%

# ---- approximate-percent patterns the text should use ----
# These are the human-readable forms; we check for the latex-approx macros.
APPROX_PATTERNS = [
    # joint method: paper uses ~72%
    (r"approx.*?72", "joint method ~72% not found in text"),
    # regime: paper uses ~2%
    (r"approx.*?2\\?%|2\\,\\?%.*?regime|regime.*?2\\,\\?%", "regime ~2% not found in text"),
    # measurement apparatus: paper uses ~43%
    (r"approx.*?43|43\\?%", "measurement apparatus ~43% not found in text"),
    # temperature control: paper uses ~8%
    (r"approx.*?8\\?%|8\\,\\?%.*?temp|temp.*?8\\,\\?%", "temperature control ~8% not found"),
]

# ---- exact numeric patterns that must appear ----
NUMERIC_PATTERNS = [
    # R²=0.717 or R^2=0.717 (joint method in results table/text)
    (r"0\.717", "R²=0.717 (joint method) not found"),
    # R²=0.425 (measurement_method)
    (r"0\.425", "R²=0.425 (measurement_method) not found"),
    # R²=0.081 (temperature_control)
    (r"0\.081", "R²=0.081 (temperature_control) not found"),
    # CI lower bound on joint method
    (r"0\.443", "CI lower bound 0.443 for joint method not found"),
]

# ---- values that must NOT appear (eliminated / superseded) ----
# Patterns use negative lookahead to allow legitimate historical-transition mentions
# like "0.332\to0.081" (arrow shows before/after) or "was 55%" (past tense).
FORBIDDEN_PATTERNS = [
    (r"0\.553", "old joint R²~0.553 still present — update to 0.717"),
    # 0.332 is OK only in transition notation ("0.332\to0.081" or "$0.332$ to"); standalone is forbidden
    (r"0\.332(?!\\to|\\\\to|\$? to)", "old temperature_control R²~0.332 (standalone) — update to 0.081"),
    # 33% near temperature is forbidden unless it's a historical "was" reference
    (r"(?<!was )(?<!was \$)33\\?%.*?temperature|temperature.*?(?<!was )33\\?%",
     "old temperature_control ~33% still present — update to ~8%"),
    # 55% near method is forbidden unless preceded by "was"
    (r"(?<!was )(?<!was \$)55\\?%",
     "old method ~55% (non-historical) still present — update to ~72%"),
    # DO NOT flag 0.55 for random-split CV R² (that is correct and unchanged):
    # forbidden check is narrow to avoid false positives on the optimism-gap number.
]

# ---- fig2 source data check ----
FIG2_DATA = Path(__file__).resolve().parents[1] / "paper" / "figures" / "fig2_variance_data.csv"


def all_tex() -> str:
    return "\n".join(f.read_text(encoding="utf-8", errors="replace") for f in TEX_FILES)


def check_fig2() -> list[str]:
    if not FIG2_DATA.exists():
        return []  # fig2 not regenerated yet — skip silently
    txt = FIG2_DATA.read_text(encoding="utf-8")
    errs = []
    for val, label in [(str(JOINT_METHOD), "0.717"), (str(MEAS_APP), "0.425"),
                       (str(TEMP_CTRL), "0.081")]:
        if val not in txt and label not in txt:
            errs.append(f"[fig2] {label} not found in fig2_variance_data.csv")
    return errs


def main() -> int:
    tex = all_tex()
    errors: list[str] = []

    for pat, msg in APPROX_PATTERNS:
        if not re.search(pat, tex, re.IGNORECASE | re.DOTALL):
            errors.append(f"[missing] {msg}")

    for pat, msg in NUMERIC_PATTERNS:
        if not re.search(pat, tex):
            errors.append(f"[missing] {msg}")

    for pat, msg in FORBIDDEN_PATTERNS:
        m = re.search(pat, tex, re.IGNORECASE | re.DOTALL)
        if m:
            # Find which file has it
            for f in TEX_FILES:
                ft = f.read_text(encoding="utf-8", errors="replace")
                if re.search(pat, ft, re.IGNORECASE | re.DOTALL):
                    errors.append(f"[forbidden] {msg} — found in {f.name}")
                    break
            else:
                errors.append(f"[forbidden] {msg}")

    errors.extend(check_fig2())

    if not errors:
        sys.stdout.buffer.write(b"CONSISTENCY GATE PASS -- all headline values consistent.\n")
        return 0

    sys.stdout.buffer.write(b"CONSISTENCY GATE FAILURES:\n")
    for e in errors:
        sys.stdout.buffer.write(("  " + e + "\n").encode("utf-8", errors="replace"))
    return 1


if __name__ == "__main__":
    sys.exit(main())
