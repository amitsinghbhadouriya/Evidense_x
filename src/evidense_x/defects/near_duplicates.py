import numpy as np
import pandas as pd
from typing import List

def generate_near_duplicates(df: pd.DataFrame, feature_cols: List[str], noise_scale: float = 0.01, seed: int = 42) -> pd.DataFrame:
    """Creates near-duplicates by injecting small Gaussian jitter into numeric coordinates."""
    rng = np.random.RandomState(seed)
    jitter = rng.normal(0, noise_scale, size=(len(df), len(feature_cols)))
    out = df.copy()
    out[feature_cols] = out[feature_cols] + jitter
    return out
