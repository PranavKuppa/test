from validator import is_valid_email, is_valid_phone


def test_valid_email():
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("not-an-email") is False


def test_valid_phone():
    assert is_valid_phone("123-456-7890") is True
    assert is_valid_phone("123") is False
