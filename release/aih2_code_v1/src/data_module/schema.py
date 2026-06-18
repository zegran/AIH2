"""Canonical column schema for the curated AIH2 dataset."""

TARGET = "h2_yield_pct"
RESERVED_TARGETS = ["max_rate_ml_min_g", "t80_min"]  # Phase 2, nullable
GROUP_COLUMN = "study_id"

NUMERIC_FEATURES = [
    "temperature_k",
    "alkali_conc_mol_l",
    "particle_size_d50_um",
    "activator_ratio",
]

WT_PCT_COLUMNS = [
    "al_wt_pct", "ga_wt_pct", "in_wt_pct", "sn_wt_pct",
    "bi_wt_pct", "mg_wt_pct", "zn_wt_pct",
]

CATEGORICAL_FEATURES = [
    "alkali_type",
    "activation_method",
    "water_type",
    "morphology_flag",
    "system_class",
]

CATEGORICAL_LEVELS = {
    "alkali_type": ["NaOH", "KOH", "none"],
    "activation_method": ["ball_milling", "plasma", "liquid_metal", "none"],
    "water_type": ["DI", "tap", "sea", "alkaline"],
    "morphology_flag": ["powder", "flake", "nano", "foil"],
    "system_class": [
        "pure_al_alkali", "al_alloy", "mechanically_activated",
        "liquid_metal_activated", "waste_al",
    ],
}

PROVENANCE_COLUMNS = ["source_ref", "extractor", "extraction_date", "extraction_method"]
QUALITY_COLUMNS = [
    "measurement_method", "temperature_control", "vessel_type",
    "rate_definition", "value_origin", "quality_tier",
]

# Columns fed to models (wt% included; NaN preserved for tree models).
MODEL_NUMERIC = NUMERIC_FEATURES + WT_PCT_COLUMNS
MODEL_FEATURES = MODEL_NUMERIC + CATEGORICAL_FEATURES

EXPLORATORY_MIN_ROWS = 40  # system_class with fewer rows -> exploratory-only
HARD_FLOOR_ROWS = 150
