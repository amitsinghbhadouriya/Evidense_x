from scipy import stats

def run_mann_whitney(x: list, y: list):
    return stats.mannwhitneyu(x, y, alternative='two-sided')
