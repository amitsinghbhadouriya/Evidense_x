import numpy as np
import pandas as pd
from evidense_x.diagnostics import (
    IsolationForestDriftDetector,
    LocalOutlierFactorAuditor,
    RobustMahalanobisAuditor,
    EnergyDistanceDriftDetector,
)


def test_isolation_forest_drift_detector():
    np.random.seed(42)
    baseline_df = pd.DataFrame(np.random.normal(0, 1, (100, 3)), columns=["f1", "f2", "f3"])
    shifted_df = pd.DataFrame(np.random.normal(5, 1, (50, 3)), columns=["f1", "f2", "f3"])
    
    detector = IsolationForestDriftDetector(contamination=0.05, random_state=42)
    detector.fit(baseline_df)
    
    scores = detector.score_samples(baseline_df)
    assert len(scores) == 100
    
    drift_result = detector.evaluate_drift(shifted_df)
    assert drift_result["drift_detected"] is True
    assert drift_result["detected_anomaly_ratio"] > 0.05


def test_local_outlier_factor_auditor():
    np.random.seed(42)
    df = pd.DataFrame(np.random.normal(0, 1, (60, 2)), columns=["x1", "x2"])
    # Add an extreme outlier
    df.loc[len(df)] = [50.0, 50.0]
    
    auditor = LocalOutlierFactorAuditor(n_neighbors=10, contamination=0.05)
    auditor.fit(df)
    
    report = auditor.audit_sparsity(df)
    assert report["total_records"] == 61
    assert report["outlier_count"] >= 1


def test_robust_mahalanobis_auditor():
    np.random.seed(42)
    df = pd.DataFrame(np.random.normal(0, 1, (100, 3)), columns=["a", "b", "c"])
    auditor = RobustMahalanobisAuditor(contamination=0.05)
    auditor.fit(df)
    
    preds = auditor.predict(df)
    assert len(preds) == 100
    assert 1 in preds


def test_energy_distance_drift_detector():
    np.random.seed(42)
    ref_df = pd.DataFrame(np.random.normal(0, 1, (80, 2)), columns=["v1", "v2"])
    target_same = pd.DataFrame(np.random.normal(0, 1, (80, 2)), columns=["v1", "v2"])
    target_shifted = pd.DataFrame(np.random.normal(10, 2, (80, 2)), columns=["v1", "v2"])
    
    detector = EnergyDistanceDriftDetector(drift_threshold=0.5)
    detector.fit(ref_df)
    
    eval_same = detector.evaluate(target_same)
    eval_shifted = detector.evaluate(target_shifted)
    
    assert eval_same["energy_distance"] < eval_shifted["energy_distance"]
    assert eval_shifted["is_drift_detected"] is True
