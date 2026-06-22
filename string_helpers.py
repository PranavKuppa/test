"""String helper utilities. Already fully compliant - no changes expected."""


def reverse_string(text: str) -> str:
    """Return the reversed version of the input string."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Return True if the input string is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
