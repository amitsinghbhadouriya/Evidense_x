"""Equalized odds disparity assessing TPR and FPR balance across sensitive demographic groups."""
import numpy as np
from typing import Dict, Any

def compute_equalized_odds_disparity(y_true: np.ndarray, y_pred: np.ndarray, sensitive_attr: np.ndarray) -> Dict[str, float]:
    """Calculates maximum between TPR gap and FPR gap across demographic groups."""
    groups = np.unique(sensitive_attr)
    tpr_list = []
    fpr_list = []
    
    for g in groups:
        mask = sensitive_attr == g
        y_t, y_p = y_true[mask], y_pred[mask]
        pos_mask = y_t == 1
        neg_mask = y_t == 0
        tpr = float(y_p[pos_mask].mean()) if pos_mask.sum() > 0 else 0.0
        fpr = float(y_p[neg_mask].mean()) if neg_mask.sum() > 0 else 0.0
        tpr_list.append(tpr)
        fpr_list.append(fpr)
        
    tpr_gap = max(tpr_list) - min(tpr_list)
    fpr_gap = max(fpr_list) - min(fpr_list)
    return {
        "equalized_odds_gap": float(max(tpr_gap, fpr_gap)),
        "tpr_gap": float(tpr_gap),
        "fpr_gap": float(fpr_gap)
    }
