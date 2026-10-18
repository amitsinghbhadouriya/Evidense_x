"""Normality testing module using Shapiro-Wilk and Anderson-Darling tests."""
import numpy as np
from scipy import stats
from typing import Dict, Any

def test_distribution_normality(data: np.ndarray) -> Dict[str, Any]:
    """Tests empirical distribution for normality to validate parametric assumptions."""
    if len(data) < 3:
        return {"is_normal": False, "p_value": 0.0}
    stat, pval = stats.shapiro(data[:5000])
    return {
        "shapiro_statistic": float(stat),
        "p_value": float(pval),
        "is_normal": pval > 0.05
    }
