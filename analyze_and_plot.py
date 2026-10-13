import os
import sys
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations_and_tables():
    os.makedirs('figures', exist_ok=True)
    os.makedirs('tables', exist_ok=True)
    
    # Check if results exist
    main_path = os.path.join('results', 'results_main.csv')
    supp_path = os.path.join('results', 'results_supp.csv')
    
    if not os.path.exists(main_path) or not os.path.exists(supp_path):
        print("Results files not found yet.")
        return
        
    df_main = pd.read_csv(main_path)
    df_supp = pd.read_csv(supp_path)
    
    print(f"Loaded df_main with {len(df_main)} records, df_supp with {len(df_supp)} records.")
    
    # Set overall aesthetic style
    sns.set_theme(style="whitegrid", font_scale=1.1)
    palette = {'Logistic Regression': '#1f77b4', 'Decision Tree': '#ff7f0e', 'Random Forest': '#2ca02c'}
    
    # -------------------------------------------------------------
    # Figure 1: F1 Inflation by Controlled Duplicate Overlap
    # -------------------------------------------------------------
    # Filter controlled overlap conditions at 0% missingness
    df_fig1 = df_main[(df_main['missing_rate'] == 0.0) & (df_main['condition'] != 'Ordinary Random Split')].copy()
    df_fig1['overlap_pct'] = df_fig1['overlap_rate'] * 100
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    datasets = ['Wine Quality—Red', 'Wine Quality—White', 'Adult Census Income']
    
    for i, d_name in enumerate(datasets):
        ax = axes[i]
        d_sub = df_fig1[df_fig1['dataset'] == d_name]
        sns.lineplot(
            data=d_sub, x='overlap_pct', y='delta_f1', hue='model',
            style='model', markers=True, dashes=False, markersize=8,
            palette=palette, linewidth=2.2, ax=ax, errorbar=('ci', 95)
        )
        ax.set_title(d_name, fontsize=13, fontweight='bold', pad=10)
        ax.set_xlabel('Duplicate Overlap (%)', fontsize=11, fontweight='bold')
        if i == 0:
            ax.set_ylabel('F1 Inflation (ΔF1)', fontsize=12, fontweight='bold')
        else:
            ax.set_ylabel('')
        ax.axhline(0, color='gray', linestyle='--', alpha=0.7)
        ax.set_ylim(-0.02, 0.25)
        if i != 1:
            ax.get_legend().remove()
        else:
            ax.legend(title='Classifier', frameon=True, framealpha=0.9, loc='upper left')
            
    plt.suptitle('Figure 1: F1-Score Inflation Across Controlled Duplicate Overlap (at 0% Additional Missingness)', fontsize=14, fontweight='bold', y=1.03)
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'fig1_f1_inflation_by_overlap.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved Figure 1.")
    
    # -------------------------------------------------------------
    # Figure 2: Missingness x Overlap Interaction (50% Overlap)
    # -------------------------------------------------------------
    df_fig2 = df_main[df_main['condition'] == '50% Overlap'].copy()
    df_fig2['missing_pct'] = df_fig2['missing_rate'] * 100
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    for i, d_name in enumerate(datasets):
        ax = axes[i]
        d_sub = df_fig2[df_fig2['dataset'] == d_name]
        sns.lineplot(
            data=d_sub, x='missing_pct', y='delta_f1', hue='model',
            style='model', markers=True, dashes=False, markersize=8,
            palette=palette, linewidth=2.2, ax=ax, errorbar=('ci', 95)
        )
        ax.set_title(d_name, fontsize=13, fontweight='bold', pad=10)
        ax.set_xlabel('Additional Missingness (%)', fontsize=11, fontweight='bold')
        if i == 0:
            ax.set_ylabel('ΔF1 at 50% Overlap', fontsize=12, fontweight='bold')
        else:
            ax.set_ylabel('')
        ax.axhline(0, color='gray', linestyle='--', alpha=0.7)
        ax.set_ylim(-0.02, 0.28)
        if i != 1:
            ax.get_legend().remove()
        else:
            ax.legend(title='Classifier', frameon=True, framealpha=0.9, loc='upper left')
            
    plt.suptitle('Figure 2: Interaction Between MCAR Missingness and Duplicate Leakage (50% Overlap)', fontsize=14, fontweight='bold', y=1.03)
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'fig2_missingness_interaction.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved Figure 2.")
    
    # -------------------------------------------------------------
    # Figure 3: Ordinary Random Splitting vs Duplicate-Aware Reference
    # -------------------------------------------------------------
    df_fig3 = df_main[df_main['condition'] == 'Ordinary Random Split'].copy()
    df_fig3['missing_pct'] = df_fig3['missing_rate'] * 100
    
    g = sns.catplot(
        data=df_fig3, x='missing_pct', y='delta_f1', hue='model', col='dataset',
        kind='bar', palette=palette, height=4.5, aspect=1.1, errorbar=('ci', 95),
        capsize=0.08, edgecolor='black', linewidth=0.8
    )
    g.set_axis_labels('Additional Missingness (%)', 'F1 Bias vs Ref (ΔF1)')
    g.set_titles(col_template='{col_name}', size=12, weight='bold')
    for ax in g.axes.flat:
        ax.axhline(0, color='gray', linestyle='--', alpha=0.7)
    g.fig.subplots_adjust(top=0.85)
    g.fig.suptitle('Figure 3: Evaluation Bias in Ordinary Random Splitting vs. Duplicate-Aware Reference', fontsize=14, fontweight='bold')
    plt.savefig(os.path.join('figures', 'fig3_ordinary_vs_duplicate_aware.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved Figure 3.")
    
    # -------------------------------------------------------------
    # Figure 4: Exact vs Independent Mask Copies (Supplementary)
    # -------------------------------------------------------------
    # Calculate retention percentage per seed: Delta_F1(Indep) / Delta_F1(Exact) * 100
    piv = df_supp.pivot(index=['dataset', 'seed', 'missing_rate', 'model'], columns='mechanism', values='delta_f1').reset_index()
    piv['retention_pct'] = (piv['Independently Masked'] / piv['Exact Copy'].replace(0, np.nan)) * 100
    piv['missing_pct'] = piv['missing_rate'] * 100
    
    # Focus on Tree models where leakage is significant
    piv_trees = piv[piv['model'].isin(['Decision Tree', 'Random Forest'])].copy()
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    tree_palette = {'Decision Tree': '#ff7f0e', 'Random Forest': '#2ca02c'}
    
    for i, d_name in enumerate(datasets):
        ax = axes[i]
        d_sub = piv_trees[piv_trees['dataset'] == d_name]
        sns.barplot(
            data=d_sub, x='missing_pct', y='retention_pct', hue='model',
            palette=tree_palette, ax=ax, errorbar=('ci', 95), capsize=0.08, edgecolor='black', linewidth=0.8
        )
        ax.set_title(d_name, fontsize=13, fontweight='bold', pad=10)
        ax.set_xlabel('Additional Missingness (%)', fontsize=11, fontweight='bold')
        if i == 0:
            ax.set_ylabel('Leakage Retention Ratio (%)', fontsize=12, fontweight='bold')
        else:
            ax.set_ylabel('')
        ax.axhline(100, color='gray', linestyle=':', alpha=0.7)
        ax.set_ylim(0, 130)
        if i != 1:
            ax.get_legend().remove()
        else:
            ax.legend(title='Tree Classifier', frameon=True, framealpha=0.9, loc='upper right')
            
    plt.suptitle('Figure 4: Retention of Duplicate Leakage Effect: Independently Masked vs. Exact Copies (at 50% Overlap)', fontsize=14, fontweight='bold', y=1.03)
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'fig4_exact_vs_independent_mask.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved Figure 4.")
    
    # -------------------------------------------------------------
    # 5. Statistical Calculations & Tables
    # -------------------------------------------------------------
    # Table II: F1-Score Inflation at 50% Overlap and 0% Missingness
    t2_sub = df_main[(df_main['missing_rate'] == 0.0) & (df_main['condition'] == '50% Overlap')]
    t2_summary = t2_sub.groupby(['dataset', 'model'])['delta_f1'].agg(['mean', 'std']).reset_index()
    t2_piv = t2_summary.pivot(index='dataset', columns='model', values='mean')[['Decision Tree', 'Random Forest', 'Logistic Regression']]
    t2_piv.to_csv(os.path.join('tables', 'table2_inflation_50pct_0missing.csv'))
    print("\n--- Table II: F1-Score Inflation at 50% Overlap and 0% Missingness ---")
    print(t2_piv.to_string())
    
    # Table III: Ordinary Random Split minus Duplicate-Aware Reference at 0% Missingness
    t3_sub = df_main[(df_main['missing_rate'] == 0.0) & (df_main['condition'] == 'Ordinary Random Split')]
    t3_summary = t3_sub.groupby(['dataset', 'model'])['delta_f1'].agg(['mean', 'std']).reset_index()
    t3_piv = t3_summary.pivot(index='dataset', columns='model', values='mean')[['Decision Tree', 'Random Forest', 'Logistic Regression']]
    t3_piv.to_csv(os.path.join('tables', 'table3_ordinary_vs_ref_0missing.csv'))
    print("\n--- Table III: F1 Bias in Ordinary Random Split (0% Missingness) ---")
    print(t3_piv.to_string())
    
    # Leakage Sensitivity Index (LSI) & Error-Reduction Illusion (ERI)
    lsi_rows = []
    ctrl_sub = df_main[(df_main['condition'] != 'Ordinary Random Split') & (df_main['missing_rate'] == 0.0)]
    for (d_name, m_name), grp in ctrl_sub.groupby(['dataset', 'model']):
        # Fit linear regression of delta_f1 on overlap_rate
        slope, intercept, r_val, p_val, std_err = stats.linregress(grp['overlap_rate'], grp['delta_f1'])
        lsi = slope * 0.10 # per 10 percentage points
        
        # Mean ERI at 50% overlap
        grp_50 = grp[grp['overlap_rate'] == 0.50]
        eri_mean = grp_50['eri'].mean()
        eri_std = grp_50['eri'].std()
        
        lsi_rows.append({
            'dataset': d_name, 'model': m_name, 'lsi_per_10pct': lsi,
            'lsi_p_val': p_val, 'eri_mean_50pct': eri_mean, 'eri_std_50pct': eri_std
        })
    df_lsi = pd.DataFrame(lsi_rows)
    df_lsi.to_csv(os.path.join('tables', 'table_lsi_eri.csv'), index=False)
    print("\n--- LSI and ERI Summary ---")
    print(df_lsi.to_string())
    
    # OLS Interaction Regressions: Delta_F1 ~ Overlap + Missingness + Overlap:Missingness
    print("\n--- OLS Interaction Models (Delta_F1 ~ Overlap + Missingness + Overlap*Missingness) ---")
    reg_df = df_main[df_main['condition'] != 'Ordinary Random Split'].copy()
    
    models = ['Logistic Regression', 'Decision Tree', 'Random Forest']
    ols_results = []
    for d_name in datasets:
        d_sub = reg_df[reg_df['dataset'] == d_name]
        # Pooled model
        mod_pool = ols('delta_f1 ~ overlap_rate * missing_rate', data=d_sub).fit()
        p_inter = mod_pool.pvalues.get('overlap_rate:missing_rate', np.nan)
        ols_results.append({
            'dataset': d_name, 'model': 'Pooled (All)',
            'overlap_coef': mod_pool.params['overlap_rate'],
            'missing_coef': mod_pool.params['missing_rate'],
            'inter_coef': mod_pool.params['overlap_rate:missing_rate'],
            'inter_pval': p_inter,
            'r_squared': mod_pool.rsquared
        })
        
        # Per-model
        for m_name in models:
            m_sub = d_sub[d_sub['model'] == m_name]
            mod_m = ols('delta_f1 ~ overlap_rate * missing_rate', data=m_sub).fit()
            ols_results.append({
                'dataset': d_name, 'model': m_name,
                'overlap_coef': mod_m.params['overlap_rate'],
                'missing_coef': mod_m.params['missing_rate'],
                'inter_coef': mod_m.params['overlap_rate:missing_rate'],
                'inter_pval': mod_m.pvalues.get('overlap_rate:missing_rate', np.nan),
                'r_squared': mod_m.rsquared
            })
            
    df_ols = pd.DataFrame(ols_results)
    df_ols.to_csv(os.path.join('tables', 'table_ols_interaction.csv'), index=False)
    print(df_ols.to_string())
    
    # Supplementary Retention at 30% Missingness
    print("\n--- Supplementary Experiment: Leakage Retention Ratio at 30% Missingness ---")
    piv_30 = piv[piv['missing_rate'] == 0.30].groupby(['dataset', 'model'])['retention_pct'].agg(['mean', 'std']).reset_index()
    piv_30.to_csv(os.path.join('tables', 'table_retention_30pct_missing.csv'), index=False)
    print(piv_30.to_string())

if __name__ == '__main__':
    generate_visualizations_and_tables()
