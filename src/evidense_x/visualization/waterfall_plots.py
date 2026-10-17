import matplotlib.pyplot as plt

def plot_eri_waterfall(models: list, eris: list):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(models, eris, color=['#2ca02c', '#ff7f0e', '#1f77b4'])
    ax.set_ylabel("Error-Reduction Illusion (%)")
    ax.set_title("Apparent Error Reduction from Duplicate Memorization")
    return fig
