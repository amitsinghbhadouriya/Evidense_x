"""Intelligent imputation router selecting strategy based on missingness severity."""
from typing import Tuple, List, Optional
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from .base import BaseRemediator, RemediationActionLog


class IntelligentImputationRouter(BaseRemediator):
    """Dynamically routes columns to appropriate imputation strategies based on missingness rate."""

    def __init__(
        self,
        knn_threshold: float = 0.15,
        simple_threshold: float = 0.50,
        n_neighbors: int = 5,
    ) -> None:
        super().__init__(name="IntelligentImputationRouter")
        self.knn_threshold = knn_threshold
        self.simple_threshold = simple_threshold
        self.n_neighbors = n_neighbors

    def remediate(self, df: pd.DataFrame, **kwargs) -> Tuple[pd.DataFrame, RemediationActionLog]:
        """Impute missing values using KNN for low-rate missingness and median for high-rate."""
        out_df = df.copy()
        numeric_cols = out_df.select_dtypes(include=[np.number]).columns.tolist()
        missing_rates = out_df[numeric_cols].isna().mean()
        
        cols_imputed: List[str] = []
        strategy_map = {}
        total_missing_cells = int(out_df.isna().sum().sum())

        for col in numeric_cols:
            rate = missing_rates[col]
            if rate == 0.0:
                continue
            cols_imputed.append(col)
            if rate <= self.knn_threshold and len(out_df) <= 5000:
                # Use KNN imputer for subtle low-rate missingness
                strategy_map[col] = "knn"
                imputer = KNNImputer(n_neighbors=self.n_neighbors)
                out_df[[col]] = imputer.fit_transform(out_df[[col]])
            else:
                # Use robust median imputation for heavier missingness
                strategy_map[col] = "median"
                imputer = SimpleImputer(strategy="median")
                out_df[[col]] = imputer.fit_transform(out_df[[col]])

        # Fill remaining non-numeric categorical columns with most frequent
        cat_cols = out_df.select_dtypes(exclude=[np.number]).columns
        for c in cat_cols:
            if out_df[c].isna().any():
                cols_imputed.append(c)
                strategy_map[c] = "mode"
                mode_val = out_df[c].mode().iloc[0] if not out_df[c].mode().empty else "missing"
                out_df[c] = out_df[c].fillna(mode_val)

        log = RemediationActionLog(
            remediator_name=self.name,
            action_type="imputation",
            rows_affected=total_missing_cells,
            columns_affected=cols_imputed,
            diagnostics={
                "strategy_map": strategy_map,
                "initial_missing_cells": total_missing_cells,
                "residual_missing_cells": int(out_df.isna().sum().sum()),
            },
        )
        return out_df, log
