def compute_memorization_capacity(train_acc: float, test_acc: float) -> float:
    """Computes memorization capacity as training-test divergence under leakage."""
    return max(0.0, train_acc - test_acc)
