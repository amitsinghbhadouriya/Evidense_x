"""Precision-Recall Gain curve area metric correcting for baseline class skew."""
import numpy as np
from sklearn.metrics import precision_recall_curve

def compute_pr_gain_area(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    """Calculates Area Under the Precision-Recall Gain Curve (AUPRG)."""
    prec, rec, _ = precision_recall_curve(y_true, y_prob)
    pi = float(y_true.mean())
    if pi <= 0 or pi >= 1:
        return 0.0
        
    rec_gain = np.where(rec > pi, (rec - pi) / ((1.0 - pi) * rec + 1e-8), 0.0)
    prec_gain = np.where(prec > pi, (prec - pi) / ((1.0 - pi) * prec + 1e-8), 0.0)
    
    # Trapezoidal approximation
    order = np.argsort(rec_gain)
    auc_gain = np.trapz(prec_gain[order], rec_gain[order])
    return float(np.clip(auc_gain, 0.0, 1.0))
