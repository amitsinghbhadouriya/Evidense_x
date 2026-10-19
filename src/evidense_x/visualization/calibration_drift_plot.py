"""Calibration drift strip plot visualizing reliability degradation across defect levels."""
import numpy as np
import matplotlib.pyplot as plt
from typing import List

def plot_calibration_drift_strips(missing_rates: List[float], ece_scores: List[float], output_path: str) -> None:
    """Plots ECE score evolution as missingness and duplicate leakage increase."""
    plt.figure(figsize=(6, 4))
    plt.plot(missing_rates, ece_scores, marker="o", color="#8e44ad", linewidth=2)
    plt.xlabel("Defect Severity Level (Missing / Overlap %)")
    plt.ylabel("Expected Calibration Error (ECE)")
    plt.title("Calibration Reliability Degradation")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
