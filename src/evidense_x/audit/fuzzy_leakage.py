import numpy as np
import pandas as pd
from typing import List

def estimate_fuzzy_leakage(train_df: pd.DataFrame, test_df: pd.DataFrame, num_cols: List[str], epsilon: float = 1e-4) -> float:
    """Estimates fraction of test samples lying within epsilon ball of training instances."""
    count = 0
    tr_vals = train_df[num_cols].values
    for val in test_df[num_cols].values:
        dists = np.max(np.abs(tr_vals - val), axis=1)
        if np.min(dists) <= epsilon:
            count += 1
    return count / len(test_df) if len(test_df) > 0 else 0.0
