"""A deliberately ambiguous module - the test expects impossible behavior."""


def parse_config(raw: str) -> dict:
    """Parses a simple key=value config string."""
    result = {}
    for line in raw.strip().split("\n"):
        if "=" in line:
            key, value = line.split("=", 1)
            result[key.strip()] = value.strip()
    return result
