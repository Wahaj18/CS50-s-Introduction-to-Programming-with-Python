from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("2/4") == 50
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_ex():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("1.3/2")
    # assert convert("3/0") == ZeroDivisionError
    # assert convert("5/4") == ValueError

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
