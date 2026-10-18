"""Compound multi-stage defect injection pipeline chaining missingness and contamination."""
from typing import List, Tuple, Any
import pandas as pd
from ..core.interfaces import BaseDefectSimulator

class CompoundDefectPipeline:
    """Executes ordered sequences of defect injectors on a single dataset."""
    
    def __init__(self, steps: List[Tuple[BaseDefectSimulator, float, dict]]) -> None:
        self.steps = steps
        
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        current_df = df.copy()
        for simulator, rate, kwargs in self.steps:
            current_df = simulator.inject(current_df, rate=rate, **kwargs)
        return current_df
