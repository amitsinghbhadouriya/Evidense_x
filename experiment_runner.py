import os
import numpy as np
import pandas as pd

def apply_mcar_mask(df, feature_cols, mask_rate, seed):
    """
    Applies Missing Completely at Random (MCAR) masking to feature columns at given mask_rate.
    """
    if mask_rate == 0.0:
        return df.copy()
    
    rng = np.random.RandomState(seed)
    df_masked = df.copy()
    
    mask = rng.rand(len(df), len(feature_cols)) < mask_rate
    for j, col in enumerate(feature_cols):
        col_series = df_masked[col].copy()
        col_series[mask[:, j]] = np.nan
        df_masked[col] = col_series
        
    return df_masked
