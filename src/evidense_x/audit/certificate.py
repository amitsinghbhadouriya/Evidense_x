import json
from typing import Dict, Any

def generate_leakage_certificate(dataset_name: str, overlap_count: int, status: str) -> Dict[str, Any]:
    return {
        "dataset": dataset_name,
        "certified_leakage_free": overlap_count == 0,
        "overlap_count": overlap_count,
        "audit_verdict": status
    }
