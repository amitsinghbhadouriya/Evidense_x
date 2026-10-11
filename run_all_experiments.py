import os
import sys
import time
import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

def load_datasets():
    datasets = {}
    # Red Wine
    df_red = pd.read_csv(os.path.join('wine quality', 'winequality-red.csv'), sep=';')
    df_red['target'] = (df_red['quality'] >= 6).astype(int)
    red_features = [c for c in df_red.columns if c not in ['quality', 'target']]
    datasets['Wine Quality—Red'] = {
        'df': df_red, 'feat_cols': red_features, 'num_cols': red_features, 'cat_cols': [], 'target_col': 'target'
    }
    
    # White Wine
    df_white = pd.read_csv(os.path.join('wine quality', 'winequality-white.csv'), sep=';')
    df_white['target'] = (df_white['quality'] >= 6).astype(int)
    white_features = [c for c in df_white.columns if c not in ['quality', 'target']]
    datasets['Wine Quality—White'] = {
        'df': df_white, 'feat_cols': white_features, 'num_cols': white_features, 'cat_cols': [], 'target_col': 'target'
    }
    
    # Adult Census Income
    cols = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
            'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
            'hours-per-week', 'native-country', 'income']
    df_adult = pd.read_csv(os.path.join('Adult', 'adult.data'), names=cols, sep=r',\s*', engine='python', na_values='?')
    df_adult['target'] = (df_adult['income'] == '>50K').astype(int)
    sub_adult, _ = train_test_split(df_adult, train_size=10000, random_state=26, stratify=df_adult['target'])
    sub_adult = sub_adult.reset_index(drop=True)
    adult_num = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    adult_cat = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    adult_features = adult_num + adult_cat
    datasets['Adult Census Income'] = {
        'df': sub_adult, 'feat_cols': adult_features, 'num_cols': adult_num, 'cat_cols': adult_cat, 'target_col': 'target'
    }
    return datasets
