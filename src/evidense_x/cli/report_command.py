"""CLI subcommand compiling audit findings into comprehensive Markdown or PDF reports."""
import argparse
import json

def execute_report_cli(args: argparse.Namespace) -> None:
    """Format and dump audit report from JSON artifact."""
    with open(args.input_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Audit Status: {'PASSED' if data.get('has_exact_leakage') is False else 'FAILED'}")
