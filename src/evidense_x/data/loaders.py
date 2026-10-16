import os
import pandas as pd
from sklearn.model_selection import train_test_split
from .schemas import DatasetSchema

class DatasetLoader:
    @staticmethod
    def load_red_wine(base_dir: str = "wine quality"):
        path = os.path.join(base_dir, "winequality-red.csv")
        df = pd.read_csv(path, sep=';')
        df['target'] = (df['quality'] >= 6).astype(int)
        feats = [c for c in df.columns if c not in ['quality', 'target']]
        schema = DatasetSchema(name="Wine Quality—Red", target_column="target", numeric_features=feats)
        return df, schema

    @staticmethod
    def load_white_wine(base_dir: str = "wine quality"):
        path = os.path.join(base_dir, "winequality-white.csv")
        df = pd.read_csv(path, sep=';')
        df['target'] = (df['quality'] >= 6).astype(int)
        feats = [c for c in df.columns if c not in ['quality', 'target']]
        schema = DatasetSchema(name="Wine Quality—White", target_column="target", numeric_features=feats)
        return df, schema

    @staticmethod
    def load_adult(base_dir: str = "Adult", subsample_size: int = 10000, seed: int = 26):
        path = os.path.join(base_dir, "adult.data")
        cols = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
                'hours-per-week', 'native-country', 'income']
        df = pd.read_csv(path, names=cols, sep=r',\s*', engine='python', na_values='?')
        df['target'] = (df['income'] == '>50K').astype(int)
        if subsample_size and len(df) > subsample_size:
            df, _ = train_test_split(df, train_size=subsample_size, random_state=seed, stratify=df['target'])
            df = df.reset_index(drop=True)
        num_cols = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
        cat_cols = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
        schema = DatasetSchema(name="Adult Census Income", target_column="target", numeric_features=num_cols, categorical_features=cat_cols)
        return df, schema
