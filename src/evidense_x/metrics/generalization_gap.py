def compute_generalization_gap(train_loss: float, test_loss: float) -> float:
    return test_loss - train_loss
