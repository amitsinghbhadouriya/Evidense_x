import numpy as np
from typing import Tuple

def compute_eri_bootstrap_ci(f1_leaks: list, f1_refs: list, n_boot: int = 1000) -> Tuple[float, float]:
    rng = np.random.RandomState(42)
    eris = []
    for _ in range(n_boot):
        idx = rng.randint(0, len(f1_leaks), len(f1_leaks))
        l = np.mean(np.array(f1_leaks)[idx])
        r = np.mean(np.array(f1_refs)[idx])
        eris.append(((1-r) - (1-l)) / (1-r) if (1-r) > 0 else 0)
    return float(np.percentile(eris, 2.5)), float(np.percentile(eris, 97.5))
