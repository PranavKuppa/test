from discount import apply_discount


def test_discount_as_fraction():
    assert apply_discount(100, 0.1) == 90


def test_discount_as_percent():
    assert apply_discount(100, 10) == 90
