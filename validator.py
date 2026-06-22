"""Validator module with a few minor style issues."""
import re


def is_valid_email(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern,email))

def is_valid_phone( number ):
    digits = re.sub(r'\D', '', number)
    return len(digits)==10
