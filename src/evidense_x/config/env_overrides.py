import os
from typing import Dict, Any

def apply_env_overrides(config_dict: Dict[str, Any]) -> Dict[str, Any]:
    if "EVIDENSE_SEEDS" in os.environ:
        config_dict["seeds"] = int(os.environ["EVIDENSE_SEEDS"])
    return config_dict
