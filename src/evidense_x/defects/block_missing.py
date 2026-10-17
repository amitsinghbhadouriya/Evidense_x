import numpy as np
import pandas as pd
from typing import List

def apply_block_missing(df: pd.DataFrame, feature_cols: List[str], block_prob: float = 0.1, seed: int = 42) -> pd.DataFrame:
    """Masks entire blocks of correlated features simultaneously."""
    rng = np.random.RandomState(seed)
    out = df.copy()
    mask = rng.rand(len(df)) < block_prob
    out.loc[mask, feature_cols] = np.nan
    return out
