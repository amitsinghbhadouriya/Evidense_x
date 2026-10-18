"""Auto-generator converting benchmark summaries to camera-ready LaTeX tables."""
import pandas as pd

def dataframe_to_latex_table(df: pd.DataFrame, caption: str, label: str) -> str:
    """Generates clean booktabs LaTeX table markup formatted for IEEE/ACM publication."""
    latex_code = df.to_latex(index=False, float_format="%.4f", caption=caption, label=label)
    return latex_code
