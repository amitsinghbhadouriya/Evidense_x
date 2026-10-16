from scipy import stats
from typing import Tuple, List

def run_paired_wilcoxon(baseline: List[float], leaked: List[float]) -> Tuple[float, float]:
    """Computes Wilcoxon signed-rank test across paired seeds."""
    stat, p = stats.wilcoxon(baseline, leaked)
    return stat, p

def bonferroni_correct(p_values: List[float], alpha: float = 0.05) -> List[bool]:
    n = len(p_values)
    adj_threshold = alpha / n
    return [p < adj_threshold for p in p_values]
