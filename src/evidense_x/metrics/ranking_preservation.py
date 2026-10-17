from scipy.stats import spearmanr
from typing import List

def compute_rank_correlation(ranks_clean: List[float], ranks_leaked: List[float]) -> float:
    rho, _ = spearmanr(ranks_clean, ranks_leaked)
    return float(rho)
