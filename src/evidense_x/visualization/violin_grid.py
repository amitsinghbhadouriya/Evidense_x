"""Multi-model violin distribution grid across defect levels."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_violin_distribution_grid(df: pd.DataFrame, x_col: str, y_col: str, hue_col: str, output_path: str) -> None:
    """Generates multi-model violin plot capturing variance and multimodality across seeds."""
    plt.figure(figsize=(8, 4.5))
    sns.violinplot(data=df, x=x_col, y=y_col, hue=hue_col, split=True, inner="quart", palette="Set2")
    plt.title(f"Model Robustness Distribution: {y_col}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
