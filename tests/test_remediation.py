import numpy as np
import pandas as pd
from evidense_x.remediation import (
    DeduplicationAutoResolver,
    IntelligentImputationRouter,
    AdaptiveOutlierClipperRemediator,
    ConfidentLabelNoiseRemediator,
    AutoCleanPipeline,
)


def test_deduplication_auto_resolver():
    df = pd.DataFrame({
        "id": [1, 1, 2],
        "val": [10.0, np.nan, 20.0],
    })
    resolver = DeduplicationAutoResolver(subset_columns=["id"], priority_rule="least_missing")
    cleaned_df, log = resolver.remediate(df)
    
    assert len(cleaned_df) == 2
    assert log.rows_affected == 1
    # Priority least_missing should keep non-nan value for id=1
    assert cleaned_df.loc[cleaned_df["id"] == 1, "val"].values[0] == 10.0


def test_intelligent_imputation_router():
    df = pd.DataFrame({
        "num1": [1.0, 2.0, np.nan, 4.0, 5.0],
        "cat1": ["a", "b", np.nan, "a", "a"],
    })
    router = IntelligentImputationRouter()
    cleaned_df, log = router.remediate(df)
    
    assert cleaned_df["num1"].isna().sum() == 0
    assert cleaned_df["cat1"].isna().sum() == 0
    assert log.action_type == "imputation"


def test_adaptive_outlier_clipper():
    df = pd.DataFrame({"val": [10.0, 11.0, 10.5, 12.0, 1000.0]})
    clipper = AdaptiveOutlierClipperRemediator(iqr_multiplier=1.5)
    cleaned_df, log = clipper.remediate(df)
    
    assert cleaned_df["val"].max() < 1000.0
    assert log.rows_affected == 1


def test_confident_label_noise_cleaner():
    np.random.seed(42)
    # 2 well separated clusters
    X1 = np.random.normal(0, 0.5, (30, 2))
    X2 = np.random.normal(5, 0.5, (30, 2))
    y1 = np.zeros(30, dtype=int)
    y2 = np.ones(30, dtype=int)
    
    # Intentionally flip a label in the middle of cluster 1
    y1[0] = 1
    
    df = pd.DataFrame(np.vstack([X1, X2]), columns=["f1", "f2"])
    df["target"] = np.concatenate([y1, y2])
    
    cleaner = ConfidentLabelNoiseRemediator(target_column="target", confidence_threshold=0.80)
    cleaned_df, log = cleaner.remediate(df)
    
    assert len(cleaned_df) <= len(df)
    assert log.action_type == "label_noise_cleaning"


def test_auto_clean_pipeline():
    df = pd.DataFrame({
        "id": [1, 1, 2, 3],
        "val": [10.0, 10.0, np.nan, 500.0],
    })
    pipeline = AutoCleanPipeline()
    cleaned_df, logs = pipeline.clean(df)
    
    assert len(cleaned_df) == 3
    assert cleaned_df["val"].isna().sum() == 0
    summary = pipeline.summarize_logs(logs)
    assert summary["total_repair_steps"] == 3
