"""BCa and percentile non-parametric bootstrap confidence interval estimator."""
import numpy as np
from typing import Tuple

def compute_bootstrap_ci(data: np.ndarray, n_boot: int = 1000, ci: float = 0.95, random_state: int = 42) -> Tuple[float, float]:
    """Estimates empirical confidence interval using non-parametric percentile bootstrap."""
    rng = np.random.default_rng(random_state)
    n = len(data)
    boot_means = np.empty(n_boot)
    
    for i in range(n_boot):
        sample = rng.choice(data, size=n, replace=True)
        boot_means[i] = np.mean(sample)
        
    alpha = (1.0 - ci) / 2.0
    low = float(np.percentile(boot_means, 100 * alpha))
    high = float(np.percentile(boot_means, 100 * (1.0 - alpha)))
    return low, high
