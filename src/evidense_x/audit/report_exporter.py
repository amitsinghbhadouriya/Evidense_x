from typing import Dict, Any

def export_audit_markdown(audit_res: Dict[str, Any]) -> str:
    return f"""# Data Quality Audit Report
- **Dataset:** {audit_res.get('dataset', 'Unknown')}
- **Leakage Free:** {audit_res.get('certified_leakage_free', False)}
- **Verdict:** {audit_res.get('audit_verdict', 'PENDING')}
"""
