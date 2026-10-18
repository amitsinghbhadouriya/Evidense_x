"""Boxplot with overlaid jitter points for multi-seed variance visualization."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_box_with_jitter(df: pd.DataFrame, x_col: str, y_col: str, output_path: str) -> None:
    """Renders distribution boxplot overlaid with jitter points representing individual random seeds."""
    plt.figure(figsize=(7, 4.5))
    sns.boxplot(data=df, x=x_col, y=y_col, color="#bdc3c7", showfliers=False)
    sns.stripplot(data=df, x=x_col, y=y_col, color="#e74c3c", jitter=0.2, alpha=0.6, size=5)
    plt.title(f"Empirical Spread: {y_col} vs {x_col}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
