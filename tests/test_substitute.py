"""Test substitute module."""

from pyenvsubst.substitute import find_variables, substitute


def test_find_variables_empty_string() -> None:
    """Test empty string."""
    assert find_variables("") == set()


def test_find_variables_single_variable() -> None:
    """Test detection of a single variable."""
    assert find_variables("$FOO") == {"FOO"}
    assert find_variables("${FOO}") == {"FOO"}


def test_find_variables_multiple_variables() -> None:
    """Test detection of multiple unique variables."""
    assert find_variables("$FOO ${BAR}") == {"FOO", "BAR"}
    assert find_variables("$FOO $BAR $FOO") == {"FOO", "BAR"}  # Duplicates removed


def test_find_variables_special_characters() -> None:
    """Test handling of variables with special characters."""
    assert find_variables("${F_00} $BAR123") == {"F_00", "BAR123"}


def test_find_variables_invalid_variables() -> None:
    """Test patterns that don't form valid identifiers."""
    assert find_variables("$1INVALID $.") == set()
    assert find_variables("$!@#") == set()


def test_substitute_empty_mapping() -> None:
    """Test substitution with empty environment mapping."""
    source = "$A $B"
    env = {}
    target = "$A $B"

    assert substitute(source, env) == target

def test_substitute_empty_value() -> None:
    """Test substitution with empty value."""
    source = "FOO is $EMPTY"
    env = {"EMPTY": ""}
    target = "FOO is "

    assert substitute(source, env) == target

def test_substitute_multiple_variables() -> None:
    """Test basic variable substitution."""
    source = "Hello $NAME! Age: ${AGE}"
    env = {"NAME": "Alice", "AGE": "30"}
    target = "Hello Alice! Age: 30"

    assert substitute(source, env) == target


def test_substitute_missing_variables() -> None:
    """Test missing variables remain unchanged."""
    source = "$EXISTING $MISSING"
    env = {"EXISTING": "FOO"}
    target = "FOO $MISSING"

    assert substitute(source, env) == target


def test_substitute_case_sensitivity() -> None:
    """Test substitution is case-sensitive."""
    source = "$lower ${LOWER}"
    env = {"lower": "a", "LOWER": "A"}
    target = "a A"

    assert substitute(source, env) == target


def test_substitute_inside_text() -> None:
    """Test substitution adjacent to text."""
    source = "start$STOP, ${BEGIN}end"
    env = {"STOP": "FOO", "BEGIN": "BAR"}
    target = "startFOO, BARend"

    assert substitute(source, env) == target


def test_substitute_special_characters() -> None:
    """Test substitution with special characters."""
    source = "FOO is $F_00"
    env = {"F_00": "BAR"}
    target = "FOO is BAR"

    assert substitute(source, env) == target


def test_substitute_same_prefix() -> None:
    """Test substitution with same prefixed variables."""
    source = "FOO is $LONG, but FOOOO is $LONGER"
    env = {"LONG": "long", "LONGER": "longer"}
    target = "FOO is long, but FOOOO is longer"

    assert substitute(source, env) == target
