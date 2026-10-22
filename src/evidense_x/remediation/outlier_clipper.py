"""Adaptive outlier winsorizer and clipper remediator."""
from typing import Tuple, List, Optional
import numpy as np
import pandas as pd
from .base import BaseRemediator, RemediationActionLog


class AdaptiveOutlierClipperRemediator(BaseRemediator):
    """Clips extreme numerical tail values based on dynamic interquartile range (IQR) boundaries."""

    def __init__(self, iqr_multiplier: float = 1.5) -> None:
        super().__init__(name="AdaptiveOutlierClipperRemediator")
        self.iqr_multiplier = iqr_multiplier
        self.bounds_dict = {}

    def remediate(self, df: pd.DataFrame, **kwargs) -> Tuple[pd.DataFrame, RemediationActionLog]:
        """Clip extreme outliers across all numerical columns and track clipped count."""
        out_df = df.copy()
        numeric_cols = out_df.select_dtypes(include=[np.number]).columns.tolist()
        total_clipped = 0
        columns_affected: List[str] = []

        for col in numeric_cols:
            series = out_df[col].dropna()
            if len(series) == 0:
                continue
            q25 = series.quantile(0.25)
            q75 = series.quantile(0.75)
            iqr = q75 - q25
            lower_bound = q25 - (self.iqr_multiplier * iqr)
            upper_bound = q75 + (self.iqr_multiplier * iqr)
            
            mask = (out_df[col] < lower_bound) | (out_df[col] > upper_bound)
            num_clipped = int(mask.sum())
            if num_clipped > 0:
                total_clipped += num_clipped
                columns_affected.append(col)
                out_df[col] = out_df[col].clip(lower=lower_bound, upper=upper_bound)
            self.bounds_dict[col] = {"lower": float(lower_bound), "upper": float(upper_bound)}

        log = RemediationActionLog(
            remediator_name=self.name,
            action_type="outlier_clipping",
            rows_affected=total_clipped,
            columns_affected=columns_affected,
            diagnostics={
                "iqr_multiplier": self.iqr_multiplier,
                "total_clipped_values": total_clipped,
                "bounds": self.bounds_dict,
            },
        )
        return out_df, log
