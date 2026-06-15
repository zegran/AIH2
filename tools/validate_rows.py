"""Phase B extraction validator. Checks an extraction file (CSV or the .xlsx `Extraction` tab)
against the curated-dataset schema and reports per-row errors + per-system_class counts.

Usage:  uv run python tools/validate_rows.py [path]
        default path: data/wp1/extractions_v0.csv
Reuses src/data_module/schema.py so it can never drift from the pipeline.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.data_module import schema  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
FIXTURE = REPO / "data/curated/fixture_v0.csv"
EXPECTED_HEADER = list(pd.read_csv(FIXTURE, nrows=0).columns)


def load(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in (".xlsx", ".xls"):
        return pd.read_excel(path, sheet_name="Extraction", engine="openpyxl")
    return pd.read_csv(path)


def validate(df: pd.DataFrame) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if list(df.columns) != EXPECTED_HEADER:
        missing = set(EXPECTED_HEADER) - set(df.columns)
        extra = set(df.columns) - set(EXPECTED_HEADER)
        errors.append(f"header mismatch: missing={sorted(missing)} extra={sorted(extra)}")
        return errors, warnings  # can't row-check a wrong header

    def rid(i: int) -> str:
        return f"row {i + 2}"  # +2: header + 1-indexed

    for i, r in df.iterrows():
        # target
        y = r[schema.TARGET]
        if pd.isna(y) or not (0 <= float(y) <= 100):
            errors.append(f"{rid(i)}: h2_yield_pct not in [0,100] ({y})")
        # alkali coupling (unreported=NaN is allowed; a contradiction is alkali present + conc==0)
        at, conc = r["alkali_type"], r["alkali_conc_mol_l"]
        if at == "none" and pd.notna(conc) and float(conc) != 0:
            errors.append(f"{rid(i)}: alkali_type=none but conc={conc} (must be 0 or blank)")
        if at in ("NaOH", "KOH"):
            if pd.notna(conc) and float(conc) <= 0:
                errors.append(f"{rid(i)}: alkali_type={at} but conc<=0 ({conc}) — contradiction")
            elif pd.isna(conc):
                warnings.append(f"{rid(i)}: alkali_type={at} but conc unreported (NaN) "
                                "- allowed; flag for completion if the source gives it")
        # wt% bounds + absent/unreported
        for col in schema.WT_PCT_COLUMNS:
            v = r[col]
            if pd.notna(v) and not (0 <= float(v) <= 100):
                errors.append(f"{rid(i)}: {col}={v} out of [0,100]")
        alloy_cols = [c for c in schema.WT_PCT_COLUMNS if c != "al_wt_pct"]
        if r["system_class"] in ("al_alloy", "liquid_metal_activated") and \
                all((pd.notna(r[c]) and float(r[c]) == 0) for c in alloy_cols):
            warnings.append(f"{rid(i)}: {r['system_class']} row has all alloying wt%=0 "
                            "(suspicious — unreported should be blank/NaN, not 0)")
        # categorical enums
        for col, levels in schema.CATEGORICAL_LEVELS.items():
            v = r[col]
            if pd.notna(v) and v not in levels:
                errors.append(f"{rid(i)}: {col}={v} not in {levels}")
        # quality / origin enums
        if r["quality_tier"] not in ("A", "B", "C"):
            errors.append(f"{rid(i)}: quality_tier={r['quality_tier']} not in A/B/C")
        if r["value_origin"] not in ("reported", "derived"):
            errors.append(f"{rid(i)}: value_origin={r['value_origin']} invalid")
        # provenance complete
        for col in [schema.GROUP_COLUMN, "source_ref", "extractor", "extraction_date",
                    "extraction_method"]:
            if pd.isna(r[col]) or str(r[col]).strip() == "":
                errors.append(f"{rid(i)}: missing provenance '{col}'")
        # phase-2 columns must be empty
        for col in schema.RESERVED_TARGETS:
            if pd.notna(r[col]):
                errors.append(f"{rid(i)}: phase-2 column {col} must be empty (got {r[col]})")
    return errors, warnings


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "data/wp1/extractions_v0.csv"
    df = load(path)
    errors, warnings = validate(df)

    print(f"== validate {path.name} : {len(df)} rows ==")
    for e in errors:
        print(f"  ERROR  {e}")
    for w in warnings:
        print(f"  WARN   {w}")

    if "system_class" in df.columns:
        print("\nper-system_class rows:")
        counts = df["system_class"].value_counts()
        for sc, n in counts.items():
            flag = "  <-- EXPLORATORY-ONLY (<40)" if n < schema.EXPLORATORY_MIN_ROWS else ""
            print(f"  {sc:24s} {n}{flag}")
        total = len(df)
        floor = schema.HARD_FLOOR_ROWS
        print(f"\ntotal rows: {total}  (hard floor {floor}: "
              f"{'MET' if total >= floor else 'NOT MET'})")

    print(f"\n{'PASS' if not errors else f'FAIL ({len(errors)} errors)'}"
          f"{f', {len(warnings)} warnings' if warnings else ''}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
