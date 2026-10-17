from evidense_x.metrics.calibration import compute_ece

def test_ece():
    y_true = [1, 0, 1, 0]
    y_prob = [0.9, 0.1, 0.8, 0.2]
    ece = compute_ece(y_true, y_prob)
    assert ece >= 0.0
