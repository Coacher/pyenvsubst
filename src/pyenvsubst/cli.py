"""CLI interface for pyenvsubst."""

import argparse
import sys


CLI = argparse.ArgumentParser(
    description="Substitutes the values of environment variables.",
    allow_abbrev=False,
)

CLI.add_argument(
    "shell_format",
    action="store",
    nargs="?",
    default="",
    type=str,
    metavar="SHELL-FORMAT",
    help="""
        If a %(metavar)s is given, only those environment variables that are
        referenced in %(metavar)s are substituted; otherwise all environment
        variables references occurring in the input file are substituted.
    """,
)
CLI.add_argument(
    "-v",
    "--variables",
    action="store_true",
    help="output the variables occurring in SHELL-FORMAT without substitution",
)
CLI.add_argument(
    "-e",
    "--exclude",
    action="store",
    default="",
    type=str,
    metavar="EXCLUDE-SHELL-FORMAT",
    help="exclude the variables occurring in %(metavar)s from substitution",
)
CLI.add_argument(
    "-i",
    "--input",
    nargs="?",
    default=sys.stdin,
    type=argparse.FileType("r"),
    help="read the input from the given file (default: STDIN)",
)
CLI.add_argument(
    "-o",
    "--output",
    nargs="?",
    default=sys.stdout,
    type=argparse.FileType("w"),
    help="write the output to the given file (default: STDOUT)",
)
