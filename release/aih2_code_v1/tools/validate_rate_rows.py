"""Validate the separate kinetic table data/wp1/rate_extraction.csv.

Checks schema, enums, ranges, and provenance for the rate/Arrhenius rows used by H3. Kept distinct
from the yield validator (tools/validate_rows.py); this table must NOT be merged into aih2_v1.csv.

Run: uv run python tools/validate_rate_rows.py data/wp1/rate_extraction.csv
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.data_module import schema  # noqa: E402

COLUMNS = [
    "study_id", "system_class", "kinetic_metric", "value", "unit", "rate_definition",
    "n_temperatures", "temp_range_k", "fit_method", "source_ref", "extraction_method",
    "value_origin", "quality_tier", "notes",
]
KINETIC_METRICS = {"ea_kj_mol", "rate_k", "max_rate", "t80"}
FIT_METHODS = {"reported", "arrhenius_fit", "derived"}
EXTRACTION_METHODS = {"table", "webplotdigitizer"}
VALUE_ORIGINS = {"reported", "derived"}
TIERS = {"A", "B", "C"}
SYSTEM_CLASSES = set(schema.CATEGORICAL_LEVELS["system_class"])
LIT_BAND = (3.5, 102.6)  # kJ/mol


def _num(v: str):
    v = (v or "").strip()
    if v == "":
        return None
    try:
        return float(v)
    except ValueError:
        return "BAD"


def validate(path: str) -> int:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    print(f"== validate {Path(path).name} : {len(rows)} rows ==")
    errors, warns = [], []

    header = list(rows[0].keys()) if rows else []
    if header != COLUMNS:
        errors.append(f"header mismatch.\n  expected: {COLUMNS}\n  got:      {header}")

    for i, r in enumerate(rows, start=2):
        def err(m): errors.append(f"row {i} ({r.get('study_id','?')}/{r.get('kinetic_metric','?')}): {m}")
        def warn(m): warns.append(f"row {i} ({r.get('study_id','?')}/{r.get('kinetic_metric','?')}): {m}")

        if r["system_class"] not in SYSTEM_CLASSES:
            err(f"bad system_class '{r['system_class']}'")
        if r["kinetic_metric"] not in KINETIC_METRICS:
            err(f"bad kinetic_metric '{r['kinetic_metric']}'")
        if r["fit_method"] not in FIT_METHODS:
            err(f"bad fit_method '{r['fit_method']}'")
        if r["extraction_method"] not in EXTRACTION_METHODS:
            err(f"bad extraction_method '{r['extraction_method']}'")
        if r["value_origin"] not in VALUE_ORIGINS:
            err(f"bad value_origin '{r['value_origin']}'")
        if r["quality_tier"] not in TIERS:
            err(f"bad quality_tier '{r['quality_tier']}'")
        if not r["source_ref"].strip():
            err("missing source_ref (provenance)")

        val = _num(r["value"])
        if val == "BAD":
            err(f"non-numeric value '{r['value']}'")
        elif val is None:
            if r["extraction_method"] != "webplotdigitizer":
                err("blank value but extraction_method != webplotdigitizer (must be pending-digitization)")
            else:
                warn("blank value (digitization pending)")
        else:
            if r["kinetic_metric"] == "ea_kj_mol":
                if not (0 < val < 300):
                    err(f"Ea {val} kJ/mol implausible (expect 0-300)")
                elif not (LIT_BAND[0] <= val <= LIT_BAND[1]):
                    warn(f"Ea {val} kJ/mol OUTSIDE literature band {LIT_BAND} (flag, not error)")

        nt = _num(r["n_temperatures"])
        if r["kinetic_metric"] == "ea_kj_mol" and r["fit_method"] in {"reported", "arrhenius_fit"}:
            if nt not in (None, "BAD") and nt < 3:
                warn(f"Ea row with only {int(nt)} temperatures (<3) — weak Arrhenius basis")

    # summary
    print("\nper-system_class Ea rows (kinetic_metric=ea_kj_mol):")
    ea = [r for r in rows if r["kinetic_metric"] == "ea_kj_mol"]
    for cls, n in sorted(Counter(r["system_class"] for r in ea).items(), key=lambda x: -x[1]):
        vals = [_num(r["value"]) for r in ea if r["system_class"] == cls]
        vals = [v for v in vals if isinstance(v, float)]
        rng = f"[{min(vals):.1f},{max(vals):.1f}]" if vals else "-"
        print(f"  {cls:24} {n:>2} Ea rows  {rng} kJ/mol")
    classes_with_3plus = sum(c >= 3 for c in Counter(r["system_class"] for r in ea).values())
    print(f"\nclasses with >=3 Ea rows: {classes_with_3plus}")
    print(f"metric mix: {dict(Counter(r['kinetic_metric'] for r in rows))}")

    for w in warns:
        print(f"  WARN   {w}")
    if errors:
        print("\nFAIL:")
        for e in errors:
            print(f"  ERROR  {e}")
        return 1
    print(f"\nPASS, {len(warns)} warnings")
    return 0


if __name__ == "__main__":
    sys.exit(validate(sys.argv[1] if len(sys.argv) > 1 else "data/wp1/rate_extraction.csv"))
