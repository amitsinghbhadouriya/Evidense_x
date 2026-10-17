import numpy as np
import pandas as pd

def generate_synthetic_benchmark(n_samples: int = 1000, n_features: int = 10, seed: int = 42) -> pd.DataFrame:
    rng = np.random.RandomState(seed)
    X = rng.randn(n_samples, n_features)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    cols = [f"feat_{i}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=cols)
    df["target"] = y
    return df
