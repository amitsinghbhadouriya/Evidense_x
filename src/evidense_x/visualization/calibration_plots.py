from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt

def plot_calibration_comparison(y_true_clean, prob_clean, y_true_leak, prob_leak):
    fig, ax = plt.subplots(figsize=(7, 5))
    f_c, m_c = calibration_curve(y_true_clean, prob_clean, n_bins=10)
    f_l, m_l = calibration_curve(y_true_leak, prob_leak, n_bins=10)
    ax.plot(m_c, f_c, "s-", label="Clean Split")
    ax.plot(m_l, f_l, "o-", label="Leaked Split")
    ax.plot([0, 1], [0, 1], "k--", label="Perfect Calibration")
    ax.legend()
    return fig
