"""Standalone responsive HTML audit dashboard exporter."""
from typing import Dict, Any

def export_audit_to_html(results: Dict[str, Any], title: str) -> str:
    """Generates an embeddable HTML report card with status color indicators."""
    leak_rate = results.get("exact_leakage_rate", 0.0) * 100
    color = "#28a745" if leak_rate == 0 else "#dc3545"
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Audit Certificate: {title}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 2rem; background: #f8f9fa; }}
        .card {{ background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }}
        .header {{ border-bottom: 2px solid #e9ecef; padding-bottom: 1rem; }}
        .badge {{ background: {color}; color: white; padding: 0.25rem 0.75rem; border-radius: 4px; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <h2>Data Leakage Certificate: {title}</h2>
            <span class="badge">{'CLEAN' if leak_rate == 0 else 'CONTAMINATED'}</span>
        </div>
        <p><strong>Exact Leakage Rate:</strong> {leak_rate:.2f}%</p>
    </div>
</body>
</html>
"""
