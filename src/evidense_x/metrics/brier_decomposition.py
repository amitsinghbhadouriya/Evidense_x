"""Murphy Brier score decomposition into reliability, resolution, and uncertainty."""
import numpy as np
from typing import Dict, Any

def decompose_brier_score(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> Dict[str, float]:
    """Decomposes Brier loss into calibration reliability and discriminatory resolution."""
    base_rate = float(y_true.mean())
    uncertainty = base_rate * (1.0 - base_rate)
    
    bin_edges = np.linspace(0.0, 1.0, n_bins + 1)
    reliability = 0.0
    resolution = 0.0
    n = len(y_true)
    
    for i in range(n_bins):
        mask = (y_prob >= bin_edges[i]) & (y_prob < bin_edges[i + 1])
        n_k = mask.sum()
        if n_k > 0:
            o_k = y_true[mask].mean()
            f_k = y_prob[mask].mean()
            reliability += (n_k / n) * ((f_k - o_k) ** 2)
            resolution += (n_k / n) * ((o_k - base_rate) ** 2)
            
    brier_score = reliability - resolution + uncertainty
    return {
        "brier_score": float(brier_score),
        "reliability": float(reliability),
        "resolution": float(resolution),
        "uncertainty": float(uncertainty)
    }
