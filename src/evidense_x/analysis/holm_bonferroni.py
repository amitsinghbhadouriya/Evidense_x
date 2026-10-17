from statsmodels.stats.multitest import multipletests

def adjust_pvalues_holm(p_values: list):
    rejected, p_adj, _, _ = multipletests(p_values, method='holm')
    return rejected, p_adj
