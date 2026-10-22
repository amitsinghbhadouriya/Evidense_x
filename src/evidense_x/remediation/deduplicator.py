"""Automated deduplication resolver with configurable tie-breaking priority."""
from typing import List, Tuple, Optional
import pandas as pd
from .base import BaseRemediator, RemediationActionLog


class DeduplicationAutoResolver(BaseRemediator):
    """Resolves duplicate record clusters by prioritizing complete or recent rows."""

    def __init__(
        self,
        subset_columns: Optional[List[str]] = None,
        priority_rule: str = "least_missing",
    ) -> None:
        super().__init__(name="DeduplicationAutoResolver")
        self.subset_columns = subset_columns
        self.priority_rule = priority_rule  # 'least_missing', 'first', 'last'

    def remediate(self, df: pd.DataFrame, **kwargs) -> Tuple[pd.DataFrame, RemediationActionLog]:
        """Perform deterministic deduplication according to selected policy."""
        initial_count = len(df)
        cols = self.subset_columns if self.subset_columns is not None else list(df.columns)

        if self.priority_rule == "least_missing":
            # Sort by number of non-null values descending so rows with least missingness appear first
            non_null_counts = df.notna().sum(axis=1)
            sorted_indices = non_null_counts.sort_values(ascending=False).index
            sorted_df = df.loc[sorted_indices]
            cleaned_df = sorted_df.drop_duplicates(subset=cols, keep="first").sort_index()
        elif self.priority_rule == "last":
            cleaned_df = df.drop_duplicates(subset=cols, keep="last")
        else:
            cleaned_df = df.drop_duplicates(subset=cols, keep="first")

        removed = initial_count - len(cleaned_df)
        log = RemediationActionLog(
            remediator_name=self.name,
            action_type="deduplication",
            rows_affected=removed,
            columns_affected=cols,
            diagnostics={
                "initial_row_count": initial_count,
                "retained_row_count": len(cleaned_df),
                "priority_rule": self.priority_rule,
            },
        )
        return cleaned_df.reset_index(drop=True), log
