import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, roc_auc_score
from typing import Dict, Any

def compute_lsi(f1_leak: float, f1_ref: float) -> float:
    """Leakage Sensitivity Index: ΔF1 between leaked and reference splits."""
    return f1_leak - f1_ref

def compute_eri(f1_leak: float, f1_ref: float) -> float:
    """Error-Reduction Illusion: Proportion of reference classification errors eliminated by leakage."""
    err_ref = 1.0 - f1_ref
    err_leak = 1.0 - f1_leak
    if err_ref <= 0.0:
        return 0.0
    return (err_ref - err_leak) / err_ref

def evaluate_performance(y_true, y_pred, y_prob=None) -> Dict[str, float]:
    f1 = f1_score(y_true, y_pred, zero_division=0)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    acc = accuracy_score(y_true, y_pred)
    try:
        auc = roc_auc_score(y_true, y_prob) if y_prob is not None else np.nan
    except:
        auc = np.nan
    return {"f1": f1, "precision": prec, "recall": rec, "accuracy": acc, "roc_auc": auc}
