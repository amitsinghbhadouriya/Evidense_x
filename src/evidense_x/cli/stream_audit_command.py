"""CLI subcommand for simulating streaming data ingestion and monitoring defect alerts."""
import argparse
import pandas as pd
from evidense_x.streaming import SlidingWindowLeakageMonitor, ExponentialMovingAverageMissingnessAuditor


def execute_stream_audit_cli(args: argparse.Namespace) -> None:
    """Simulate streaming records from input CSV through monitors."""
    df = pd.read_csv(args.data)
    records = df.to_dict(orient="records")
    
    leakage_mon = SlidingWindowLeakageMonitor(window_size=args.window_size or 100)
    missing_mon = ExponentialMovingAverageMissingnessAuditor()
    
    leakage_alerts = 0
    missing_alerts = 0
    
    for r in records:
        if leakage_mon.ingest_record(r):
            leakage_alerts += 1
        if missing_mon.ingest_record(r):
            missing_alerts += 1
            
    print(f"Stream audit completed across {len(records)} records.")
    print(f"Leakage alerts: {leakage_alerts}, Missingness alerts: {missing_alerts}")
