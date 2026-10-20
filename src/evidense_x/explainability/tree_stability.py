"""Feature ranking stability index across duplicate injection levels using Jaccard and Spearman."""
from scipy.stats import spearmanr
from typing import List, Dict, Any

def compute_ranking_stability(rankings_clean: List[str], rankings_perturbed: List[str]) -> float:
    """Computes rank correlation between feature importance lists across clean and defect splits."""
    pos_clean = {f: i for i, f in enumerate(rankings_clean)}
    pos_pert = {f: i for i, f in enumerate(rankings_perturbed)}
    common = [f for f in rankings_clean if f in pos_pert]
    if len(common) < 2:
        return 0.0
    r1 = [pos_clean[f] for f in common]
    r2 = [pos_pert[f] for f in common]
    corr, _ = spearmanr(r1, r2)
    return float(corr)
