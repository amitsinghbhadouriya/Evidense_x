import seaborn as sns
import matplotlib.pyplot as plt

def plot_split_comparison_boxplot(df):
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x='condition', y='f1', hue='model', ax=ax)
    return fig
