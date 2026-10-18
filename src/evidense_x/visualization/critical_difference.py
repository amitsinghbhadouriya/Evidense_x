"""Demšar-style critical difference diagram for model ranking comparisons."""
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict

def plot_critical_difference_bar(mean_ranks: Dict[str, float], output_path: str) -> None:
    """Visualizes average model ranks with rank difference ordering."""
    sorted_items = sorted(mean_ranks.items(), key=lambda x: x[1])
    names = [x[0] for x in sorted_items]
    ranks = [x[1] for x in sorted_items]
    
    plt.figure(figsize=(8, 3.5))
    plt.barh(names, ranks, color="#2c3e50")
    plt.xlabel("Average Rank (Lower is Better)")
    plt.title("Critical Rank Ordering Across Benchmark Suites")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
