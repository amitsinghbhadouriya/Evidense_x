import numpy as np
import pandas as pd

def inject_duplicate_label_noise(df: pd.DataFrame, target_col: str, noise_rate: float = 0.05, seed: int = 42) -> pd.DataFrame:
    """Flips binary labels with given probability to simulate imperfect duplicate labeling."""
    rng = np.random.RandomState(seed)
    out = df.copy()
    flip_mask = rng.rand(len(df)) < noise_rate
    out.loc[flip_mask, target_col] = 1 - out.loc[flip_mask, target_col]
    return out
