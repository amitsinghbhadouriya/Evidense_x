"""Partial Dependence Plot (PDP) grid visualizer capturing feature marginal effects."""
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Any

def plot_partial_dependence_curve(predict_fn, X_sample: np.ndarray, feature_idx: int, feature_name: str, output_path: str) -> None:
    """Generates 1D partial dependence curve across feature percentiles."""
    vals = np.linspace(np.min(X_sample[:, feature_idx]), np.max(X_sample[:, feature_idx]), 30)
    pdp = []
    for v in vals:
        X_mut = X_sample.copy()
        X_mut[:, feature_idx] = v
        pdp.append(np.mean(predict_fn(X_mut)))
        
    plt.figure(figsize=(6, 4))
    plt.plot(vals, pdp, color="#2980b9", linewidth=2)
    plt.xlabel(feature_name)
    plt.ylabel("Partial Dependence (Marginal Prob)")
    plt.title(f"PDP: {feature_name}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
