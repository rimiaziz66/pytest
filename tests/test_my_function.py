from source import my_function  as mf

import pytest


def test_add():
    result = mf.add(1,2)
    assert result == 3


@pytest.mark.parametrize("a,b,c",[(5,2,2.5),(10,2,5),(20,2,10)])
def test_division(a,b,c):
    result = mf.division(a,b)
    assert result == c


@pytest.mark.parametrize("a,b",[(2,4),(3,6)])
def test_double(a,b):
    result = mf.double(a)
    assert result == b

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        mf.division(10,0)

def test_add_string():
    result = mf.add("I ","Love")
    assert result == "I Love"


@pytest.mark.parametrize("data", [])
def test_square(data, load_data):
    x = data["input"]
    actual = mf.square(x)
    expected = data["expected"]
    assert actual == expected