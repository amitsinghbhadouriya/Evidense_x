import os
import sys
import time
import warnings
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, roc_auc_score

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings('ignore')

# Set aesthetic styling
sns.set_theme(style="whitegrid", font="sans-serif")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

# -------------------------------------------------------------
# 1. Dataset Loading
# -------------------------------------------------------------
def load_datasets():
    datasets = {}
    
    # Red Wine
    df_red = pd.read_csv(os.path.join('wine quality', 'winequality-red.csv'), sep=';')
    df_red['target'] = (df_red['quality'] >= 6).astype(int)
    red_features = [c for c in df_red.columns if c not in ['quality', 'target']]
    datasets['Wine Quality—Red'] = {
        'df': df_red,
        'feat_cols': red_features,
        'num_cols': red_features,
        'cat_cols': [],
        'target_col': 'target'
    }
    
    # White Wine
    df_white = pd.read_csv(os.path.join('wine quality', 'winequality-white.csv'), sep=';')
    df_white['target'] = (df_white['quality'] >= 6).astype(int)
    white_features = [c for c in df_white.columns if c not in ['quality', 'target']]
    datasets['Wine Quality—White'] = {
        'df': df_white,
        'feat_cols': white_features,
        'num_cols': white_features,
        'cat_cols': [],
        'target_col': 'target'
    }
    
    # Adult Census Income
    cols = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
            'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
            'hours-per-week', 'native-country', 'income']
    df_adult = pd.read_csv(os.path.join('Adult', 'adult.data'), names=cols, sep=r',\s*', engine='python', na_values='?')
    df_adult['target'] = (df_adult['income'] == '>50K').astype(int)
    # Stratified subsample to 10,000 records
    sub_adult, _ = train_test_split(df_adult, train_size=10000, random_state=26, stratify=df_adult['target'])
    sub_adult = sub_adult.reset_index(drop=True)
    
    adult_num = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    adult_cat = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    adult_features = adult_num + adult_cat
    datasets['Adult Census Income'] = {
        'df': sub_adult,
        'feat_cols': adult_features,
        'num_cols': adult_num,
        'cat_cols': adult_cat,
        'target_col': 'target'
    }
    
    return datasets

# -------------------------------------------------------------
# 2. Partitioning & Masking
# -------------------------------------------------------------
def stratified_group_train_test_split(df, feature_cols, target_col, test_size=0.25, random_state=42):
    df_temp = df[feature_cols + [target_col]].copy()
    groups = df_temp.groupby(feature_cols + [target_col], sort=False, dropna=False).indices
    rng = np.random.RandomState(random_state)
    
    pos_groups = []
    neg_groups = []
    for g_key, idxs in groups.items():
        target_val = g_key[-1]
        if target_val == 1:
            pos_groups.append(idxs)
        else:
            neg_groups.append(idxs)
            
    rng.shuffle(pos_groups)
    rng.shuffle(neg_groups)
    
    test_indices = []
    for grp_list in [pos_groups, neg_groups]:
        total_class_count = sum(len(idxs) for idxs in grp_list)
        target_test_count = int(round(test_size * total_class_count))
        curr_count = 0
        for idxs in grp_list:
            if curr_count + len(idxs) <= target_test_count or curr_count == 0:
                test_indices.extend(idxs)
                curr_count += len(idxs)
                
    test_set = set(test_indices)
    train_indices = [i for i in range(len(df)) if i not in test_set]
    return np.array(train_indices), np.array(test_indices)

def apply_mcar_mask(df, feature_cols, mask_rate, seed):
    if mask_rate == 0.0:
        return df.copy()
    rng = np.random.RandomState(seed)
    df_masked = df.copy()
    mask = rng.rand(len(df), len(feature_cols)) < mask_rate
    for j, col in enumerate(feature_cols):
        col_series = df_masked[col].copy()
        col_series[mask[:, j]] = np.nan
        df_masked[col] = col_series
    r
# Helper metrics added
