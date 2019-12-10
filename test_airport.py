from airport_classes import *
import pytest

# Test where method of class just returned Sam
def test_passname():
    assert Passengers('Sam', 33212).name == 'Sam'

# Test where method of class returned self
def test_passname2():
    assert Passengers('Dave', 3223).name == 'Dave'

# Test where method of class just returned the number
def test_passPN():
    assert Passengers('Roger', 2345).passnum == 2345

# Test where method of class returned self
def test_passPN2():
    assert Passengers('John', 6712).passnum == 6712

# Testing whether error 'TypeError' is produced when not enough arguments are passed into a class
def test_error():
    with pytest.raises(TypeError):
        Passengers('Sam')

try:
    Sam = Passengers('Sam')
except TypeError as error:
    print('Whoops, looks like you missed something')
    print(error)