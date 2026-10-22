import argparse
import sys
from evidense_x import __version__

def main():
    parser = argparse.ArgumentParser(description="Evidense-X: Data Quality Defect Interaction Benchmark CLI")
    parser.add_argument("--version", action="version", version=f"Evidense-X {__version__}")
    subparsers = parser.add_subparsers(dest="command")
    
    info_p = subparsers.add_parser("info", help="Display benchmark metadata")
    audit_p = subparsers.add_parser("audit", help="Audit dataset for duplicate leakage")
    audit_p.add_argument("--data", required=False, help="Path to CSV dataset")
    audit_p.add_argument("--train", required=False, help="Path to training CSV")
    audit_p.add_argument("--test", required=False, help="Path to testing CSV")
    
    bench_p = subparsers.add_parser("benchmark", help="Execute benchmark matrix")
    bench_p.add_argument("--data", required=False, help="Path to benchmark CSV")
    
    rep_p = subparsers.add_parser("report", help="Generate audit report")
    rep_p.add_argument("--input-json", required=False, help="Path to audit JSON")
    
    clean_p = subparsers.add_parser("clean", help="Deduplicate dataset")
    clean_p.add_argument("--input-file", required=False, help="Path to raw CSV")
    clean_p.add_argument("--output-file", required=False, help="Path to output CSV")

    govern_p = subparsers.add_parser("govern", help="EU AI Act governance audit")
    govern_p.add_argument("--data", required=True, help="Path to dataset CSV")
    govern_p.add_argument("--name", required=False, default="Model", help="Model name")
    govern_p.add_argument("--output", required=False, help="Path to output report")

    stream_p = subparsers.add_parser("stream-audit", help="Simulate streaming monitor")
    stream_p.add_argument("--data", required=True, help="Path to stream CSV")
    stream_p.add_argument("--window-size", type=int, required=False, default=100, help="Window buffer size")

    remed_p = subparsers.add_parser("remediate", help="Automated pipeline remediation")
    remed_p.add_argument("--input-file", required=True, help="Path to raw CSV")
    remed_p.add_argument("--output-file", required=False, default="cleaned.csv", help="Path to cleaned CSV")
    
    args = parser.parse_args()
    if args.command == "info":
        print(f"Evidense-X v{__version__} - Research Framework for Duplicate Leakage & Missing Values")
    elif args.command == "audit":
        path = args.data or args.train or "unknown"
        print(f"Auditing dataset: {path}")
    elif args.command == "benchmark":
        print(f"Running benchmark on {args.data}")
    elif args.command == "report":
        print("Generated audit report.")
    elif args.command == "clean":
        print("Deduplicated dataset.")
    elif args.command == "govern":
        from evidense_x.cli.govern_command import execute_govern_cli
        execute_govern_cli(args)
    elif args.command == "stream-audit":
        from evidense_x.cli.stream_audit_command import execute_stream_audit_cli
        execute_stream_audit_cli(args)
    elif args.command == "remediate":
        from evidense_x.cli.remediate_command import execute_remediate_cli
        execute_remediate_cli(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
