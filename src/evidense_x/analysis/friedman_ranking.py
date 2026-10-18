"""Friedman non-parametric test and average rank calculator across multi-dataset benchmarks."""
import numpy as np
import pandas as pd
from scipy import stats
from typing import Dict, Any

def compute_friedman_ranks(performance_matrix: pd.DataFrame) -> Dict[str, Any]:
    """Computes Friedman test statistic and average model ranks across datasets."""
    ranks = performance_matrix.rank(axis=1, ascending=False)
    mean_ranks = ranks.mean(axis=0).to_dict()
    stat, pval = stats.friedmanchisquare(*[performance_matrix[c].values for c in performance_matrix.columns])
    return {
        "mean_ranks": mean_ranks,
        "friedman_statistic": float(stat),
        "p_value": float(pval),
        "significant_differences": pval < 0.05
    }
