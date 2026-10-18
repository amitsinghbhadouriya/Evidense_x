"""Pareto efficiency frontier visualizer comparing accuracy vs leakage vulnerability."""
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

def plot_pareto_frontier(acc_scores: List[float], leakage_vuln: List[float], labels: List[str], output_path: str) -> None:
    """Plots multi-objective Pareto trade-off between baseline accuracy and defect sensitivity."""
    plt.figure(figsize=(6, 5))
    plt.scatter(leakage_vuln, acc_scores, color="#8e44ad", s=60)
    for i, label in enumerate(labels):
        plt.annotate(label, (leakage_vuln[i] + 0.005, acc_scores[i] + 0.005), fontsize=9)
    plt.xlabel("Leakage Vulnerability Index (LSI)")
    plt.ylabel("Baseline Clean AUC")
    plt.title("Pareto Efficiency: Robustness vs Performance")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
