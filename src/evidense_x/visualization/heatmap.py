import seaborn as sns
import matplotlib.pyplot as plt

def plot_missingness_heatmap(corr_df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_df, cmap='coolwarm', annot=True, ax=ax)
    return fig
