from sklearn.metrics import balanced_accuracy_score

def compute_balanced_accuracy(y_true, y_pred) -> float:
    return float(balanced_accuracy_score(y_true, y_pred))
