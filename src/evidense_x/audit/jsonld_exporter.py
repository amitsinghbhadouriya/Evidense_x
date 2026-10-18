"""Schema.org compliant JSON-LD certificate exporter for FAIR data governance."""
import json
from typing import Dict, Any

def export_to_jsonld(audit_results: Dict[str, Any], dataset_name: str) -> str:
    """Format audit results as a W3C / Schema.org compliant Dataset JSON-LD document."""
    doc = {
        "@context": "https://schema.org/",
        "@type": "Dataset",
        "name": dataset_name,
        "description": "Evidense-X Empirical Data Defect & Leakage Audit Certificate",
        "auditMetadata": {
            "@type": "AuditingReport",
            "leakageScore": audit_results.get("exact_leakage_rate", 0.0),
            "nearLeakageScore": audit_results.get("near_leakage_rate", 0.0),
            "isCertifiedContaminationFree": audit_results.get("exact_leakage_count", 0) == 0
        }
    }
    return json.dumps(doc, indent=2)
