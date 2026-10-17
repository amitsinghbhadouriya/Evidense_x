import seaborn as sns
import matplotlib.pyplot as plt

def plot_seed_distribution_violin(df, x="model", y="f1", title="F1 Score Variance Across Seeds"):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.violinplot(data=df, x=x, y=y, ax=ax, inner="quartile")
    ax.set_title(title)
    return fig
