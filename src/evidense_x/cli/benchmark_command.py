"""CLI subcommand executing multi-model multi-defect benchmark matrices."""
import argparse
import pandas as pd
from ..audit.composite_auditor import CompositeAuditor

def execute_benchmark_cli(args: argparse.Namespace) -> None:
    """Run benchmark protocol from CLI."""
    print(f"Executing Evidense-X Benchmark on: {args.data}")
    df = pd.read_csv(args.data)
    print(f"Loaded {len(df)} rows across {len(df.columns)} columns.")
