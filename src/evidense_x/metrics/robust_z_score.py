"""Median absolute deviation (MAD) based robust Z-score estimator."""
import numpy as np

def compute_robust_z_scores(values: np.ndarray) -> np.ndarray:
    """Calculates scale-invariant robust Z-scores using median and MAD."""
    med = np.median(values)
    mad = np.median(np.abs(values - med))
    if mad == 0:
        return np.zeros_like(values)
    return 0.6745 * (values - med) / mad
