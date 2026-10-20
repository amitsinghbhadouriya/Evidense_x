"""CLI subcommand offering automated deduplication and partition repair options."""
import argparse
import pandas as pd

def execute_clean_cli(args: argparse.Namespace) -> None:
    """Perform exact deduplication on input CSV."""
    df = pd.read_csv(args.input_file)
    initial_len = len(df)
    cleaned = df.drop_duplicates()
    cleaned.to_csv(args.output_file, index=False)
    print(f"Deduplicated dataset: removed {initial_len - len(cleaned)} duplicate rows.")
