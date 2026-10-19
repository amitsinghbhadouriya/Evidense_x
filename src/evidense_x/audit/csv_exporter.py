"""CSV audit summary table exporter for pipeline logging."""
import pandas as pd
from typing import Dict, Any

def export_audit_to_csv(audit_dict: Dict[str, Any], output_path: str) -> None:
    """Dumps nested audit findings into a structured key-value CSV artifact."""
    rows = []
    for k, v in audit_dict.items():
        if isinstance(v, (int, float, str, bool)):
            rows.append({"metric": k, "value": v})
    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)
