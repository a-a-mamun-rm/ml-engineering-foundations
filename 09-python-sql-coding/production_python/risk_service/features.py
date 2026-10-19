"""Feature engineering for the heart-disease risk model (module 02), written as production code."""
from __future__ import annotations

import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

AGE_BINS = [0, 40, 55, 70, 120]
AGE_LABELS = ["<40", "40-54", "55-69", "70+"]
REQUIRED_COLUMNS = {
    "Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS",
    "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope",
}


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of ``df`` with cleaned and engineered columns.

    - 0 in Cholesterol / RestingBP means "not measured", so it becomes NaN.
    - AgeBand: coarse age groups.
    - HR_reserve: how far below the age-predicted maximum heart rate the patient reached.
    """
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")

    out = df.copy()
    for col in ("Cholesterol", "RestingBP"):
        zeros = int((out[col] == 0).sum())
        if zeros:
            logger.info("%s: %d zero values treated as missing", col, zeros)
        out[col] = out[col].replace(0, np.nan)
    out["AgeBand"] = pd.cut(out["Age"], AGE_BINS, labels=AGE_LABELS, right=False).astype(str)
    out["HR_reserve"] = 220 - out["Age"] - out["MaxHR"]
    out["FastingBS"] = out["FastingBS"].astype(str)
    return out
