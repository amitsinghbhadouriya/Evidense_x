import pandas as pd
from typing import List

def compute_missingness_correlation(df: pd.DataFrame, feature_cols: List[str]) -> pd.DataFrame:
    """Computes correlation matrix between missingness indicators."""
    indicators = df[feature_cols].isna().astype(int)
    return indicators.corr()
