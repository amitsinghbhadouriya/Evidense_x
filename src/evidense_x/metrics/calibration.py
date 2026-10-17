import numpy as np

def compute_ece(y_true, y_prob, n_bins: int = 10) -> float:
    """Expected Calibration Error (ECE)."""
    bins = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for i in range(n_bins):
        idx = (y_prob >= bins[i]) & (y_prob < bins[i+1])
        if np.sum(idx) > 0:
            acc = np.mean(np.array(y_true)[idx])
            conf = np.mean(np.array(y_prob)[idx])
            ece += (np.sum(idx) / len(y_true)) * np.abs(acc - conf)
    return float(ece)
