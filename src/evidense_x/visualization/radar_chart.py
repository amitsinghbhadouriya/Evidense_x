"""Multivariate radar / spider chart generator for multi-metric model profiles."""
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict

def plot_multivariate_radar(categories: List[str], values_dict: Dict[str, List[float]], output_path: str) -> None:
    """Generates radar chart comparing model trade-offs across calibration, AUC, and leakage."""
    n = len(categories)
    angles = [i / float(n) * 2 * np.pi for i in range(n)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    for label, vals in values_dict.items():
        v = vals + vals[:1]
        ax.plot(angles, v, linewidth=1.5, label=label)
        ax.fill(angles, v, alpha=0.15)
        
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
