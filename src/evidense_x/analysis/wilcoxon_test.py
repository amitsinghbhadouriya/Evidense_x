"""Non-parametric Wilcoxon signed-rank test for paired benchmark comparisons."""
import numpy as np
from scipy import stats
from typing import Dict, Any

def run_paired_wilcoxon_test(scores_a: np.ndarray, scores_b: np.ndarray) -> Dict[str, Any]:
    """Computes paired Wilcoxon signed-rank test between two experimental conditions."""
    diff = scores_a - scores_b
    if np.all(diff == 0):
        return {"statistic": 0.0, "p_value": 1.0, "significant": False}
    stat, pval = stats.wilcoxon(scores_a, scores_b)
    return {
        "statistic": float(stat),
        "p_value": float(pval),
        "significant": pval < 0.05
    }
