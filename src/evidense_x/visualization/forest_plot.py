"""Meta-analysis forest plot displaying effect sizes and confidence intervals."""
import numpy as np
import matplotlib.pyplot as plt
from typing import List

def plot_meta_analysis_forest(study_names: List[str], effects: List[float], ci_low: List[float], ci_high: List[float], output_path: str) -> None:
    """Generates standard meta-analytic forest plot with individual and pooled effect bounds."""
    y_pos = np.arange(len(study_names))
    plt.figure(figsize=(8, 4))
    plt.errorbar(effects, y_pos, xerr=[np.array(effects) - np.array(ci_low), np.array(ci_high) - np.array(effects)], fmt="o", color="#2980b9", ecolor="#7f8c8d", capsize=4)
    plt.axvline(0, color="k", linestyle="--", alpha=0.6)
    plt.yticks(y_pos, study_names)
    plt.xlabel("Standardized Effect Size (Hedges' g)")
    plt.title("Meta-Analytic Forest Plot: Data Defect Effect Sizes")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
