"""Interactive SVG/HTML dashboard exporter without heavy browser runtime dependencies."""
import json
from typing import Dict, Any

def generate_interactive_svg_report(title: str, metrics: Dict[str, float], output_path: str) -> None:
    """Generates a standalone responsive HTML/SVG interactive bar visualizer."""
    bars_html = ""
    y_offset = 50
    for name, val in metrics.items():
        width = int(val * 400)
        bars_html += f"""
        <text x="20" y="{y_offset + 15}" font-family="sans-serif" font-size="12">{name}</text>
        <rect x="220" y="{y_offset}" width="{width}" height="20" fill="#3498db" rx="3"/>
        <text x="{230 + width}" y="{y_offset + 15}" font-family="sans-serif" font-size="12">{val:.4f}</text>
        """
        y_offset += 35
        
    html = f"""<!DOCTYPE html>
<html>
<head><title>{title}</title></head>
<body style="font-family: sans-serif; padding: 2rem;">
    <h2>{title}</h2>
    <svg width="700" height="{y_offset + 20}">
        {bars_html}
    </svg>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
