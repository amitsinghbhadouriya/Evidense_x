import numpy as np
import pandas as pd
from typing import List

def apply_mnar_mask(df: pd.DataFrame, feature_cols: List[str], threshold_percentile: float = 75.0) -> pd.DataFrame:
    """Applies Missing Not At Random (MNAR) by masking values exceeding high percentiles."""
    out = df.copy()
    for col in feature_cols:
        val = np.percentile(out[col].dropna(), threshold_percentile)
        out.loc[out[col] > val, col] = np.nan
    return out
