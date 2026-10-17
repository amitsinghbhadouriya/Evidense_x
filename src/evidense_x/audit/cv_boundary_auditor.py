from typing import List, Tuple

def audit_cv_splits(fold_splits: List[Tuple[list, list]]) -> bool:
    for tr, te in fold_splits:
        if set(tr).intersection(set(te)):
            return False
    return True
