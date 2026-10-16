from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from .preprocessors import build_column_preprocessor
from typing import List

class ModelPipelineFactory:
    @staticmethod
    def create(model_name: str, numeric_features: List[str], categorical_features: List[str], seed: int = 42) -> Pipeline:
        preprocessor = build_column_preprocessor(numeric_features, categorical_features)
        if model_name == 'Logistic Regression':
            clf = LogisticRegression(max_iter=2000, random_state=seed)
        elif model_name == 'Decision Tree':
            clf = DecisionTreeClassifier(random_state=seed)
        elif model_name == 'Random Forest':
            clf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)
        else:
            raise ValueError(f"Unsupported model: {model_name}")
        return Pipeline([('preprocessor', preprocessor), ('classifier', clf)])
