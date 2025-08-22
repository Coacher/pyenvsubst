"""pyenvsubst entry point."""

import sys

from os import environ

from pyenvsubst.cli import CLI
from pyenvsubst.substitute import find_variables, substitute


def main(*args: str) -> None:
    """Substitute the values of environment variables."""
    options = CLI.parse_args(args or sys.argv[1:])

    variables = set(environ.keys())

    if options.shell_format:
        variables &= find_variables(options.shell_format)
    if options.exclude:
        variables -= find_variables(options.exclude)
    if options.variables:
        for var in variables:
            options.output.write(var)
        return

    variables = {var: environ[var] for var in variables}

    for line in options.input:
        options.output.write(substitute(line, variables))

    return


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
