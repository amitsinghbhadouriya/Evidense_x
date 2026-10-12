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
    return df_masked

# -------------------------------------------------------------
# 3. Model Pipeline
# -------------------------------------------------------------
def get_pipeline(model_name, num_cols, cat_cols, seed):
    transformers = []
    if num_cols:
        num_transformer = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        transformers.append(('num', num_transformer, num_cols))
    if cat_cols:
        cat_transformer = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])
        transformers.append(('cat', cat_transformer, cat_cols))
        
    preprocessor = ColumnTransformer(transformers=transformers)
    
    if model_name == 'Logistic Regression':
        clf = LogisticRegression(max_iter=2000, random_state=seed)
    elif model_name == 'Decision Tree':
        clf = DecisionTreeClassifier(random_state=seed)
    elif model_name == 'Random Forest':
        clf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)
    else:
        raise ValueError(f"Unknown model: {model_name}")
        
    return Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', clf)
    ])

def compute_metrics(y_true, y_pred, y_prob):
    f1 = f1_score(y_true, y_pred, zero_division=0)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0)
    acc = accuracy_score(y_true, y_pred)
    try:
        auc = roc_auc_score(y_true, y_prob)
    except:
        auc = np.nan
    return f1, prec, rec, acc, auc

# -------------------------------------------------------------
# 4. Main Experiment Runner
# -------------------------------------------------------------
def run_experiments():
    datasets = load_datasets()
    models = ['Logistic Regression', 'Decision Tree', 'Random Forest']
    missing_rates = [0.0, 0.10, 0.20, 0.30]
    overlap_rates = [0.10, 0.25, 0.50]
    seeds = list(range(10))
    
    results_main = []
    results_supp = []
    
    print("Starting full experimental suite...")
    start_time = time.time()
    
    for d_name, d_info in datasets.items():
        print(f"\nProcessing Dataset: {d_name} (shape: {d_info['df'].shape})")
        df_base = d_info['df']
        feat_cols = d_info['feat_cols']
        num_cols = d_info['num_cols']
        cat_cols = d_info['cat_cols']
        target_col = d_info['target_col']
        
        for seed in seeds:
            # 1. Generate partition indices for this seed
            tr_idx_ref, te_idx_ref = stratified_group_train_test_split(df_base, feat_cols, target_col, 0.25, seed)
            tr_idx_rnd, te_idx_rnd = train_test_split(np.arange(len(df_base)), test_size=0.25, random_state=seed, stratify=df_base[target_col])
            
            # Select overlap candidate indices from te_idx_ref (stratified)
            rng_ov = np.random.RandomState(seed + 100)
            shuffled_te_idx = te_idx_ref.copy()
            rng_ov.shuffle(shuffled_te_idx)
            
            for m in missing_rates:
                # Mask entire dataset once per (seed, m)
                df_masked = apply_mcar_mask(df_base, feat_cols, m, seed=seed * 100 + int(m * 1000))
                
                # Evaluation test set for reference and controlled overlap
                X_te_ref = df_masked.iloc[te_idx_ref][feat_cols]
                y_te_ref = df_base.iloc[te_idx_ref][target_col]
                
                # Training sets
                X_tr_ref = df_masked.iloc[tr_idx_ref][feat_cols]
                y_tr_ref = df_base.iloc[tr_idx_ref][target_col]
                
                # Random split sets
                X_tr_rnd = df_masked.iloc[tr_idx_rnd][feat_cols]
                y_tr_rnd = df_base.iloc[tr_idx_rnd][target_col]
                X_te_rnd = df_masked.iloc[te_idx_rnd][feat_cols]
                y_te_rnd = df_base.iloc[te_idx_rnd][target_col]
                
                # Reference model evaluation
                ref_metrics = {}
                for m_name in models:
                    pipe = get_pipeline(m_name, num_cols, cat_cols, seed)
                    pipe.fit(X_tr_ref, y_tr_ref)
                    y_pred = pipe.predict(X_te_ref)
                    y_prob = pipe.predict_proba(X_te_ref)[:, 1] if hasattr(pipe.named_steps['classifier'], 'predict_proba') else y_pred
                    f1, prec, rec, acc, auc = compute_metrics(y_te_ref, y_pred, y_prob)
                    
                    ref_metrics[m_name] = f1
                    results_main.append({
                        'dataset': d_name, 'seed': seed, 'missing_rate': m, 'condition': 'Reference (0% Overlap)',
                        'overlap_rate': 0.0, 'model': m_name, 'f1': f1, 'precision': prec, 'recall': rec,
                        'accuracy': acc, 'roc_auc': auc, 'ref_f1': f1, 'delta_f1': 0.0, 'eri': 0.0
                    })
                    
                # Controlled Overlap Conditions
                for ov in overlap_rates:
                    n_copy = int(round(ov * len(te_idx_ref)))
                    copy_indices = shuffled_te_idx[:n_copy]
                    
                    # Contaminated training set (exact copy)
                    X_tr_contam = pd.concat([X_tr_ref, df_masked.iloc[copy_indices][feat_cols]], ignore_index=True)
                    y_tr_contam = pd.concat([y_tr_ref, df_base.iloc[copy_indices][target_col]], ignore_index=True)
                    
                    for m_name in models:
                        pipe = get_pipeline(m_name, num_cols, cat_cols, seed)
                        pipe.fit(X_tr_contam, y_tr_contam)
                        y_pred = pipe.predict(X_te_ref)
                        y_prob = pipe.predict_proba(X_te_ref)[:, 1] if hasattr(pipe.named_steps['classifier'], 'predict_proba') else y_pred
                        f1, prec, rec, acc, auc = compute_metrics(y_te_ref, y_pred, y_prob)
                        
                        delta_f1 = f1 - ref_metrics[m_name]
                        eri = (delta_f1 / (1.0 - ref_metrics[m_name])) * 100.0 if (1.0 - ref_metrics[m_name]) > 1e-6 else np.nan
                        
                        results_main.append({
                            'dataset': d_name, 'seed': seed, 'missing_rate': m, 'condition': f'{int(ov*100)}% Overlap',
                            'overlap_rate': ov, 'model': m_name, 'f1': f1, 'precision': prec, 'recall': rec,
                            'accuracy': acc, 'roc_auc': auc, 'ref_f1': ref_metrics[m_name], 'delta_f1': delta_f1, 'eri': eri
                        })
                        
                        # If 50% overlap, record for supplementary comparison as Exact Copy
                        if ov == 0.50:
                            results_supp.append({
                                'dataset': d_name, 'seed': seed, 'missing_rate': m, 'mechanism': 'Exact Copy',
                                'model': m_name, 'f1': f1, 'delta_f1': delta_f1, 'ref_f1': ref_metrics[m_name]
                            })
                            
                # Ordinary Random Split Condition
                for m_name in models:
                    pipe = get_pipeline(m_name, num_cols, cat_cols, seed)
                    pipe.fit(X_tr_rnd, y_tr_rnd)
                    y_pred = pipe.predict(X_te_rnd)
           
# ERI calculation routine added
