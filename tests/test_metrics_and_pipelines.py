import numpy as np
import pandas as pd
import pytest
from experiment_runner import get_pipeline

def test_pipeline_instantiation():
    num_cols = ['age', 'fare']
    cat_cols = ['sex']
    for model_name in ['Logistic Regression', 'Decision Tree', 'Random Forest']:
        pipe = get_pipeline(model_name, num_cols, cat_cols, seed=42)
        assert pipe is not None
        assert 'preprocessor' in pipe.named_steps
        assert 'classifier' in pipe.named_steps

def test_pipeline_fit_predict():
    X = pd.DataFrame({
        'num1': [1.0, 2.0, np.nan, 4.0, 5.0, 6.0, 7.0, 8.0],
        'cat1': ['a', 'b', 'a', np.nan, 'b', 'a', 'b', 'a']
    })
    y = np.array([0, 1, 0, 1, 0, 1, 0, 1])
    pipe = get_pipeline('Decision Tree', ['num1'], ['cat1'], seed=42)
    pipe.fit(X, y)
    preds = pipe.predict(X)
    assert len(preds) == len(y)
    assert set(preds).issubset({0, 1})
