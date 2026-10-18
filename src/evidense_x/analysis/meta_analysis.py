"""Random-effects meta-analysis aggregator for multi-dataset effect sizes."""
import numpy as np
from typing import List, Dict, Any

def random_effects_meta_analysis(effects: List[float], variances: List[float]) -> Dict[str, Any]:
    """Computes DerSimonian-Laird random effects pooled summary estimate."""
    eff = np.array(effects)
    var = np.array(variances)
    k = len(eff)
    w_fixed = 1.0 / var
    q_stat = np.sum(w_fixed * (eff - np.sum(w_fixed * eff) / np.sum(w_fixed)) ** 2)
    
    df = k - 1
    c_val = np.sum(w_fixed) - (np.sum(w_fixed ** 2) / np.sum(w_fixed))
    tau2 = max(0.0, (q_stat - df) / c_val) if c_val > 0 else 0.0
    
    w_random = 1.0 / (var + tau2)
    pooled_eff = np.sum(w_random * eff) / np.sum(w_random)
    pooled_se = np.sqrt(1.0 / np.sum(w_random))
    
    return {
        "pooled_effect": float(pooled_eff),
        "pooled_se": float(pooled_se),
        "between_study_variance_tau2": float(tau2),
        "cochran_q": float(q_stat)
    }
