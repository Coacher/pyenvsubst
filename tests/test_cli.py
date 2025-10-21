"""Test CLI interface."""

import sys

from pathlib import Path
from unittest.mock import patch

from pyenvsubst.cli import CLI


def test_cli_default_arguments() -> None:
    """Test default arguments."""
    args = CLI.parse_args([])

    assert args.shell_format == ""
    assert args.variables is False
    assert args.exclude == ""
    assert args.input == sys.stdin
    assert args.output == sys.stdout


def test_cli_positional_arguments() -> None:
    """Test positional arguments."""
    shell_format = "$FOO $BAR BAZ"
    args = CLI.parse_args([shell_format])

    assert args.shell_format == shell_format


def test_cli_variables_argument() -> None:
    """Test -v/--variables flag parsing."""
    for flag in ("-v", "--variables"):
        args = CLI.parse_args([flag])

        assert args.variables is True


def test_cli_exclude_argument() -> None:
    """Test -e/--exclude flag parsing."""
    exclude_shell_format = "$FOO $BAR BAZ"
    for flag in ("-e", "--exclude"):
        args = CLI.parse_args([flag, exclude_shell_format])

        assert args.exclude == exclude_shell_format


def test_cli_input_argument(tmp_path: Path) -> None:
    """Test -i/--input file handling."""
    test_file = tmp_path / "input.txt"
    file_path = str(test_file)

    # Create file for reading.
    test_file.write_text("")

    with patch("sys.stdout"):
        for flag in ("-i", "--input"):
            args = CLI.parse_args([flag, file_path])

            assert args.input.name == file_path

            args.input.close()


def test_cli_output_argument(tmp_path: Path) -> None:
    """Test -o/--output file handling."""
    test_file = tmp_path / "output.txt"
    file_path = str(test_file)

    with patch("sys.stdin"):
        for flag in ("-o", "--output"):
            args = CLI.parse_args([flag, file_path])

            assert args.output.name == file_path

            args.output.close()
