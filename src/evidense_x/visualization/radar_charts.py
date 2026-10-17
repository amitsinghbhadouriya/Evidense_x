import numpy as np
import matplotlib.pyplot as plt

def plot_vulnerability_radar(categories: list, values: list, title: str = "Model Vulnerability Profile"):
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    vals = values + values[:1]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, vals, linewidth=1.5, linestyle='solid')
    ax.fill(angles, vals, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title(title, y=1.08)
    return fig
