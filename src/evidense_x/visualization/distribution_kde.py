"""Empirical density KDE overlay plotter for test/train feature comparisons."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_kde_overlay(train_s: pd.Series, test_s: pd.Series, feature_name: str, output_path: str) -> None:
    """Visualizes feature distribution shift between train and test partitions using KDE."""
    plt.figure(figsize=(6, 4))
    sns.kdeplot(train_s, label="Train Partition", fill=True, alpha=0.3)
    sns.kdeplot(test_s, label="Test Partition", fill=True, alpha=0.3)
    plt.title(f"Empirical Density: {feature_name}")
    plt.xlabel(feature_name)
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
