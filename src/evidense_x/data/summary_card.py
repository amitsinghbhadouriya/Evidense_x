from typing import Dict, Any

def format_dataset_card(name: str, meta: Dict[str, Any]) -> str:
    return f"""### Dataset Card: {name}
- Rows: {meta.get('n_rows')}
- Columns: {meta.get('n_cols')}
- Memory: {meta.get('memory_mb')} MB
"""
