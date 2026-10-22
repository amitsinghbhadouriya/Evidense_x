"""CLI subcommand executing complete AutoCleanPipeline dataset remediation."""
import argparse
import pandas as pd
from evidense_x.remediation import AutoCleanPipeline


def execute_remediate_cli(args: argparse.Namespace) -> None:
    """Run full automated defect remediation and write cleaned CSV."""
    df = pd.read_csv(args.input_file)
    pipeline = AutoCleanPipeline()
    cleaned_df, logs = pipeline.clean(df)
    
    out_file = args.output_file or "cleaned_dataset.csv"
    cleaned_df.to_csv(out_file, index=False)
    summary = pipeline.summarize_logs(logs)
    print(f"Dataset successfully remediated and saved to: {out_file}")
    print(f"Executed {summary['total_repair_steps']} repair steps affecting {summary['total_items_remediated']} elements.")
