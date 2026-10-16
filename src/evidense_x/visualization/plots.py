import matplotlib.pyplot as plt
import seaborn as sns

def set_publication_style():
    sns.set_theme(style="whitegrid", font_scale=1.1)
    plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
    plt.rcParams['axes.edgecolor'] = '#cccccc'
    plt.rcParams['axes.linewidth'] = 0.8
