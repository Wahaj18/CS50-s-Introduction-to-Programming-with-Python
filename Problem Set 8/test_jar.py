import pytest
from jar import Jar

def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0
    with pytest.raises(ValueError):
        jar2 = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(16)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(20)
