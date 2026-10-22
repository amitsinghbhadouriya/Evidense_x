"""Confident label noise detection and filtering remediator."""
from typing import Tuple, List, Optional
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from .base import BaseRemediator, RemediationActionLog


class ConfidentLabelNoiseRemediator(BaseRemediator):
    """Filters or corrects noisy training labels using cross-validated probability disagreement."""

    def __init__(
        self,
        target_column: str,
        confidence_threshold: float = 0.85,
        n_splits: int = 3,
        random_state: int = 42,
    ) -> None:
        super().__init__(name="ConfidentLabelNoiseRemediator")
        self.target_column = target_column
        self.confidence_threshold = confidence_threshold
        self.n_splits = n_splits
        self.random_state = random_state

    def remediate(self, df: pd.DataFrame, **kwargs) -> Tuple[pd.DataFrame, RemediationActionLog]:
        """Identify records where out-of-fold model confidence strongly opposes the given label."""
        if self.target_column not in df.columns:
            raise ValueError(f"Target column '{self.target_column}' not found in dataframe.")

        out_df = df.copy()
        y = out_df[self.target_column].to_numpy()
        unique_classes = np.unique(y)
        if len(unique_classes) < 2:
            log = RemediationActionLog(
                remediator_name=self.name,
                action_type="label_noise_cleaning",
                rows_affected=0,
                columns_affected=[self.target_column],
                diagnostics={"note": "Single class target; skipping label filtering."},
            )
            return out_df, log

        feature_cols = [c for c in out_df.columns if c != self.target_column and np.issubdtype(out_df[c].dtype, np.number)]
        if not feature_cols:
            log = RemediationActionLog(
                remediator_name=self.name,
                action_type="label_noise_cleaning",
                rows_affected=0,
                columns_affected=[self.target_column],
                diagnostics={"note": "No numerical features available for out-of-fold estimation."},
            )
            return out_df, log

        X = out_df[feature_cols].fillna(0.0).to_numpy()
        kf = KFold(n_splits=self.n_splits, shuffle=True, random_state=self.random_state)
        
        noisy_indices = []
        for train_idx, val_idx in kf.split(X):
            clf = LogisticRegression(max_iter=200, random_state=self.random_state)
            clf.fit(X[train_idx], y[train_idx])
            probs = clf.predict_proba(X[val_idx])
            pred_classes = clf.classes_[np.argmax(probs, axis=1)]
            max_probs = np.max(probs, axis=1)

            # High-confidence model prediction contradicts annotated label
            for i, actual_label, pred_label, conf in zip(val_idx, y[val_idx], pred_classes, max_probs):
                if actual_label != pred_label and conf >= self.confidence_threshold:
                    noisy_indices.append(i)

        cleaned_df = out_df.drop(index=noisy_indices).reset_index(drop=True)
        log = RemediationActionLog(
            remediator_name=self.name,
            action_type="label_noise_cleaning",
            rows_affected=len(noisy_indices),
            columns_affected=[self.target_column],
            diagnostics={
                "identified_noisy_rows": len(noisy_indices),
                "confidence_threshold": self.confidence_threshold,
                "retained_rows": len(cleaned_df),
            },
        )
        return cleaned_df, log
