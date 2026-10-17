import pandas as pd
import numpy as np
from evidense_x.defects.mnar import apply_mnar_mask

def test_mnar():
    df = pd.DataFrame({"x": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})
    masked = apply_mnar_mask(df, ["x"], threshold_percentile=70.0)
    assert masked["x"].isna().sum() > 0
