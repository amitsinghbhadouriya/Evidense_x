import pandas as pd
from typing import List, Dict

def get_cluster_size_distribution(df: pd.DataFrame, feature_cols: List[str]) -> Dict[int, int]:
    counts = df.groupby(feature_cols).size()
    return counts.value_counts().to_dict()
