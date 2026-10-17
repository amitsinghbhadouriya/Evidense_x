import numpy as np

def permutation_test_diff(x: list, y: list, n_resamples: int = 2000) -> float:
    diff_observed = np.mean(x) - np.mean(y)
    combined = np.concatenate([x, y])
    rng = np.random.RandomState(42)
    count = 0
    for _ in range(n_resamples):
        shuffled = rng.permutation(combined)
        d = np.mean(shuffled[:len(x)]) - np.mean(shuffled[len(x):])
        if abs(d) >= abs(diff_observed):
            count += 1
    return count / n_resamples
