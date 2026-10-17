from typing import Dict, Any

DEFAULT_HYPERPARAMETERS: Dict[str, Dict[str, Any]] = {
    "Logistic Regression": {"max_iter": 2000, "solver": "lbfgs"},
    "Decision Tree": {"criterion": "gini", "max_depth": None, "min_samples_split": 2},
    "Random Forest": {"n_estimators": 100, "criterion": "gini", "max_depth": None, "n_jobs": -1}
}
