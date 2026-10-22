from evidense_x.streaming import (
    SlidingWindowLeakageMonitor,
    AdaptiveWindowDriftDetector,
    ExponentialMovingAverageMissingnessAuditor,
)


def test_sliding_window_leakage_monitor():
    monitor = SlidingWindowLeakageMonitor(window_size=50, leakage_alert_rate=0.20)
    train_record = {"feature_a": 1.0, "feature_b": 2.0}
    h = monitor.compute_hash(train_record)
    monitor.reference_hashes.add(h)
    
    # Ingest innocent records
    for i in range(25):
        alert = monitor.ingest_record({"feature_a": float(i + 10), "feature_b": 0.0})
        assert alert is None
        
    # Ingest duplicated records to trigger threshold
    alert_triggered = False
    for _ in range(20):
        alert = monitor.ingest_record(train_record)
        if alert is not None:
            alert_triggered = True
            assert alert.metric_name == "window_leakage_rate"
            break
            
    assert alert_triggered is True
    summary = monitor.get_window_summary()
    assert summary["total_ingested"] > 25


def test_adaptive_window_drift_detector():
    detector = AdaptiveWindowDriftDetector(window_size=100, confidence_delta=0.05)
    # Feed clean baseline
    for _ in range(50):
        detector.ingest_record({"error": 0.0})
        
    # Sudden surge of prediction errors
    alert_triggered = False
    for _ in range(40):
        alert = detector.ingest_record({"error": 1.0})
        if alert is not None:
            alert_triggered = True
            assert alert.metric_name == "streaming_error_drift"
            break
            
    assert alert_triggered is True


def test_ema_missingness_auditor():
    auditor = ExponentialMovingAverageMissingnessAuditor(alpha=0.2, missingness_alert_rate=0.30)
    # Feed complete records
    for _ in range(20):
        auditor.ingest_record({"col1": 1.0, "col2": 2.0})
        
    # Feed records with high missingness
    alert_triggered = False
    for _ in range(20):
        alert = auditor.ingest_record({"col1": None, "col2": None})
        if alert is not None:
            alert_triggered = True
            assert alert.metric_name == "smoothed_missingness_rate"
            break
            
    assert alert_triggered is True
