import numpy as np
import pandas as pd
from typing import List

def compute_gower_matrix(df: pd.DataFrame, num_cols: List[str]) -> np.ndarray:
    """Computes simplified Gower proximity matrix for numeric coordinates."""
    norm = (df[num_cols] - df[num_cols].min()) / (df[num_cols].max() - df[num_cols].min() + 1e-9)
    diff = np.abs(norm.values[:, None, :] - norm.values[None, :, :])
    return 1.0 - np.mean(diff, axis=-1)
