from sklearn.metrics import log_loss

def compute_cross_entropy(y_true, y_prob) -> float:
    return float(log_loss(y_true, y_prob))
