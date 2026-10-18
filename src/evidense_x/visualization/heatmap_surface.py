"""Defect interaction 2D contour and heatmap surface plotter."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_interaction_heatmap(df: pd.DataFrame, index_col: str, col_name: str, val_col: str, output_path: str) -> None:
    """Plots pivot heatmap visualizing the non-linear interaction surface of data defects."""
    pivot = df.pivot_table(index=index_col, columns=col_name, values=val_col, aggfunc="mean")
    plt.figure(figsize=(7, 5))
    sns.heatmap(pivot, annot=True, fmt=".3f", cmap="magma", cbar_kws={"label": val_col})
    plt.title(f"Interaction Surface: {val_col}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
