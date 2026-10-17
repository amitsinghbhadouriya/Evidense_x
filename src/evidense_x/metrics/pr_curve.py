from sklearn.metrics import precision_recall_curve, auc

def compute_auprc(y_true, y_prob) -> float:
    p, r, _ = precision_recall_curve(y_true, y_prob)
    return float(auc(r, p))
