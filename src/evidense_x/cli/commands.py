"""Custom subcommands for the Evidense-X CLI interface."""
import argparse
import sys
import pandas as pd
from ..audit.composite_auditor import CompositeAuditor
from ..core.serialization import to_audit_json

def audit_command(args: argparse.Namespace) -> None:
    """Execute leakage audit on specified train and test files."""
    train_df = pd.read_csv(args.train)
    test_df = pd.read_csv(args.test)
    auditor = CompositeAuditor()
    results = auditor.audit_partitions(train_df, test_df)
    print(to_audit_json(results))

def setup_cli_parser() -> argparse.ArgumentParser:
    """Constructs command line argument parser."""
    parser = argparse.ArgumentParser(prog="evidense-x", description="Evidense-X Data Defect & Leakage CLI")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    
    audit_parser = subparsers.add_parser("audit", help="Audit train and test datasets for contamination")
    audit_parser.add_argument("--train", required=True, help="Path to training CSV")
    audit_parser.add_argument("--test", required=True, help="Path to testing CSV")
    audit_parser.set_defaults(func=audit_command)
    return parser
