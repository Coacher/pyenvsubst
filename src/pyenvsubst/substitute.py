"""String parsing for pyenvsubst."""

from collections.abc import Mapping
from string import Template


def find_variables(string: str) -> set[str]:
    """Find all variable names in the given string."""
    return set(Template(string).get_identifiers())


def substitute(string: str, env: Mapping[str, str]) -> str:
    """Substitute all variable names in the given string from the given map."""
    return Template(string).safe_substitute(env)
