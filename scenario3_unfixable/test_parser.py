from parser import parse_config


def test_parse_config_basic():
    raw = "name=hello\nage=30"
    result = parse_config(raw)
    assert result == {"name": "hello", "age": 30}  # BUG IN TEST: age should be "30" (str), not int 30
    # parse_config can never satisfy this without changing its return contract
    # for every other call site - a real architectural mismatch, not a style fix.
