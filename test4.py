def add(a,b):
    x = a+ b
    return x


def subtract(a, b):
    return a -b


class Calculator:
    def __init__(self, name):
        self.name=name

    def multiply(self, a, b):
        return a*  b
    
def test_add():
    assert add(2,3)== 5

def test_subtract():
    assert subtract(5,2) ==3


def test_multiply():
    calc = Calculator("test" )
    assert calc.multiply(3, 4)== 12