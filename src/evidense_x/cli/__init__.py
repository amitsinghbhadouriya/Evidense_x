"""Command-line interface router and entrypoint definitions for Evidense-X."""
from .commands import setup_cli_parser
from .benchmark_command import execute_benchmark_cli
from .report_command import execute_report_cli
from .clean_command import execute_clean_cli

__all__ = [
    "setup_cli_parser",
    "execute_benchmark_cli",
    "execute_report_cli",
    "execute_clean_cli",
]
