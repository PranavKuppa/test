from calculator import add, divide


def test_add():
    assert add(2, 3) == 5  # This will FAIL because of the bug above


def test_divide():
    assert divide(10, 2) == 5

