"""3D interactive wireframe and surface plotter for 2-factor defect grid."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_3d_loss_surface(df: pd.DataFrame, x_col: str, y_col: str, z_col: str, output_path: str) -> None:
    """Generates 3D surface plot showing non-linear error topology across defect parameters."""
    pivot = df.pivot_table(index=y_col, columns=x_col, values=z_col, aggfunc="mean")
    X, Y = np.meshgrid(pivot.columns, pivot.index)
    Z = pivot.values
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none", alpha=0.85)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_zlabel(z_col)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
