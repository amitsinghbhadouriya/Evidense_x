from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def plot_roc_shift(y_clean, p_clean, y_leak, p_leak):
    fig, ax = plt.subplots(figsize=(6, 5))
    fpr_c, tpr_c, _ = roc_curve(y_clean, p_clean)
    fpr_l, tpr_l, _ = roc_curve(y_leak, p_leak)
    ax.plot(fpr_c, tpr_c, label=f"Clean (AUC={auc(fpr_c, tpr_c):.3f})")
    ax.plot(fpr_l, tpr_l, label=f"Leaked (AUC={auc(fpr_l, tpr_l):.3f})")
    ax.legend()
    return fig
