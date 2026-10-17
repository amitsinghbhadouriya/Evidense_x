from sklearn.metrics import cohen_kappa_score

def compute_kappa(y_true, y_pred) -> float:
    return float(cohen_kappa_score(y_true, y_pred))
