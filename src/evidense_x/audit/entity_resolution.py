import pandas as pd
from typing import List, Dict

def audit_entity_leakage(train_df: pd.DataFrame, test_df: pd.DataFrame, id_col: str) -> Dict[str, Any]:
    common = set(train_df[id_col]).intersection(set(test_df[id_col]))
    return {"leaked_entities": len(common), "overlap_ratio": len(common) / len(test_df)}
