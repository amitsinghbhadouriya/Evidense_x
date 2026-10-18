"""Group-level clustering leakage scanner for identifying correlated patient/client IDs."""
import pandas as pd
from typing import Dict, Any, List

class GroupLeakageScanner:
    """Scans categorical grouping identifier columns for cross-split group leakage."""
    
    def scan_groups(self, train_df: pd.DataFrame, test_df: pd.DataFrame, id_cols: List[str]) -> Dict[str, Any]:
        results = {}
        for col in id_cols:
            if col in train_df.columns and col in test_df.columns:
                train_ids = set(train_df[col].dropna())
                test_ids = set(test_df[col].dropna())
                leaked_ids = train_ids.intersection(test_ids)
                results[col] = {
                    "leaked_groups_count": len(leaked_ids),
                    "group_leakage_rate": len(leaked_ids) / max(len(test_ids), 1),
                    "violates_group_isolation": len(leaked_ids) > 0
                }
        return results
