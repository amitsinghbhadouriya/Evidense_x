import numpy as np
import pandas as pd
from typing import List

def apply_mcar_mask(df: pd.DataFrame, feature_cols: List[str], mask_rate: float, seed: int = 42) -> pd.DataFrame:
    """Applies Missing Completely at Random (MCAR) feature masking."""
    if mask_rate <= 0.0:
        return df.copy()
    rng = np.random.RandomState(seed)
    df_masked = df.copy()
    mask = rng.rand(len(df), len(feature_cols)) < mask_rate
    for j, col in enumerate(feature_cols):
        series = df_masked[col].copy()
        series[mask[:, j]] = np.nan
        df_masked[col] = series
    return df_masked

def apply_mar_mask(df: pd.DataFrame, feature_cols: List[str], conditioning_col: str, mask_rate: float, seed: int = 42) -> pd.DataFrame:
    """Applies Missing at Random (MAR) feature masking conditioned on a covariate."""
    if mask_rate <= 0.0:
        return df.copy()
    rng = np.random.RandomState(seed)
    df_masked = df.copy()
    median_val = df[conditioning_col].median()
    high_cond = df[conditioning_col] > median_val
    for col in feature_cols:
        if col == conditioning_col:
            continue
        p = np.where(high_cond, mask_rate * 1.5, mask_rate * 0.5)
        p = np.clip(p, 0.0, 1.0)
        mask = rng.rand(len(df)) < p
        series = df_masked[col].copy()
        series[mask] = np.nan
        df_masked[col] = series
    return df_masked
