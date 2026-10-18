"""JSON and YAML serialization helpers for audit reports and configs."""
import json
from typing import Any, Dict
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    """Custom JSON encoder converting numpy scalars and arrays to native types."""
    def default(self, obj: Any) -> Any:
        if isinstance(obj, (np.integer, int)):
            return int(obj)
        elif isinstance(obj, (np.floating, float)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

def to_audit_json(data: Dict[str, Any], indent: int = 2) -> str:
    """Serialize dictionary with numpy types to structured JSON string."""
    return json.dumps(data, cls=NumpyEncoder, indent=indent)
