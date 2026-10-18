"""Empirical calibration curve reliability diagrams."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

def plot_reliability_diagram(y_true: np.ndarray, y_prob: np.ndarray, model_label: str, output_path: str) -> None:
    """Plots empirical calibration reliability curve compared against perfect calibration."""
    prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=10)
    plt.figure(figsize=(5, 5))
    plt.plot([0, 1], [0, 1], "k--", label="Perfect Calibration")
    plt.plot(prob_pred, prob_true, "s-", label=model_label)
    plt.xlabel("Mean Predicted Confidence")
    plt.ylabel("Observed Fraction of Positives")
    plt.title("Reliability Diagram")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
