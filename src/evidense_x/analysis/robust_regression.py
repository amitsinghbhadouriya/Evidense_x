"""Huber robust M-estimator regression for outlier-resistant trend estimation."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from typing import Dict, Any

def fit_huber_regression(X: np.ndarray, y: np.ndarray) -> Dict[str, Any]:
    """Fits Huber T-norm robust linear model to attenuate influence of contamination outliers."""
    X_const = sm.add_constant(X)
    rlm_model = sm.RLM(y, X_const, M=sm.robust.norms.HuberT()).fit()
    return {
        "params": [float(p) for p in rlm_model.params],
        "bse": [float(b) for b in rlm_model.bse],
        "converged": bool(rlm_model.converged)
    }
