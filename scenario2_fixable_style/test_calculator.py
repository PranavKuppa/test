from calculator import add, subtract, Calculator


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    calc = Calculator("test")
    assert calc.multiply(3, 4) == 12
