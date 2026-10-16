import numpy as np
import pandas as pd
import pytest
from evidense_x.defects.masking import apply_mcar_mask, apply_mar_mask
from evidense_x.defects.duplicates import compute_row_hashes, detect_duplicate_clusters

def test_mar_mask():
    df = pd.DataFrame({
        'f1': np.random.randn(200),
        'f2': np.random.randn(200)
    })
    masked = apply_mar_mask(df, ['f1', 'f2'], conditioning_col='f1', mask_rate=0.2)
    assert masked['f2'].isna().sum() > 0

def test_duplicate_clustering():
    df = pd.DataFrame({
        'f1': [1, 1, 2, 3],
        'f2': [1, 1, 2, 3]
    })
    res = detect_duplicate_clusters(df, ['f1', 'f2'])
    assert res['total_duplicate_rows'] == 2
    assert res['cluster_count'] == 1
