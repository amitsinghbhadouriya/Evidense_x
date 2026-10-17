from sklearn.metrics import matthews_corrcoef

def compute_mcc(y_true, y_pred) -> float:
    return float(matthews_corrcoef(y_true, y_pred))
