import os
import pandas as pd
import numpy as np

df_main = pd.read_csv('results/results_main.csv')

# Complete summary table grouped by dataset, missing_rate, condition, model
agg_funcs = {
    'f1': ['mean', 'std'],
    'delta_f1': ['mean', 'std'],
    'precision': ['mean', 'std'],
    'recall': ['mean', 'std'],
    'accuracy': ['mean', 'std'],
    'roc_auc': ['mean', 'std'],
    'eri': ['mean', 'std']
}

summary = df_main.groupby(['dataset', 'missing_rate', 'condition', 'model']).agg(agg_funcs)
# Flatten columns
summary.columns = ['_'.join(c).strip() for c in summary.columns.values]
summary = summary.reset_index()
summary.to_csv('tables/comprehensive_summary_table.csv', index=False)
print("Saved tables/comprehensive_summary_table.csv with", len(summary), "rows.")

# Detailed Table I
table1_data = [
    {
        'Dataset': 'Wine Quality—Red',
        'Records': 1599,
        'Features': '11 numerical',
        'Duplicate Rows': '240 (15.0%)',
        'Class Target': 'quality ≥ 6',
        'Positive Class Ratio': '53.5%',
        'Missing Values in Source': '0 (0.0%)'
    },
    {
        'Dataset': 'Wine Quality—White',
        'Records': 4898,
        'Features': '11 numerical',
        'Duplicate Rows': '937 (19.1%)',
        'Class Target': 'quality ≥ 6',
        'Positive Class Ratio': '66.5%',
        'Missing Values in Source': '0 (0.0%)'
    },
    {
        'Dataset': 'Adult Census Income (Subsample)',
        'Records': 10000,
        'Features': '6 numerical, 8 categorical (14 total)',
        'Duplicate Rows': '5 (0.05%)',
        'Class Target': 'income > 50K',
        'Positive Class Ratio': '23.9%',
        'Missing Values in Source': 'Pre-existing in 3 features (workclass, occupation, native-country)'
    }
]
pd.DataFrame(table1_data).to_csv('tables/table1_dataset_characteristics.csv', index=False)
print("Saved table1_dataset_characteristics.csv")
