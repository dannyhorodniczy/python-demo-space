import pytest

class MyClass:
    def __init__(self, value):
        self.value = value

    def increment_value(self):
        self.value += 1

    def decrement_value(self):
        self.value -= 1

    def get_value(self):
        return self.value


class MySecondClass : MyClass

def f():
    return 3

# Tests must begin with the word "test"
def test_function():
    assert f() == 3

def test_a_class():
    cls = MyClass(5)
    assert cls.get_value() == 5

def test_a_class2():
    cls = MyClass(5)
    cls.increment_value()
    assert cls.get_value() == 6

def test_a_class2():
    cls = MySecondClass()
    cls2 = MyClass(5)
    # assert isinstance(cls, MyClass)
    assert isinstance(cls, MySecondClass)
    assert isinstance(cls2, MyClass)

testdata = [
    (1, 2, -1),
    (2, 1, 1),
    (3, 3, 0),
    (2, 2, 0),
    (1, 1, 0)
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected



