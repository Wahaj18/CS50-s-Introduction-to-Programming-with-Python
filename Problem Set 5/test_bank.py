from bank import value

def test_value_lower():
    assert value("hello world") == 0
    assert value("hey") == 20
    assert value("world") == 100

def test_value_upper():
    assert value("HeLlo wOrld") == 0
    assert value("HEy") == 20
    assert value("WoRld") == 100

def test_value_incorrect():
    assert value("hello 123") == 0
    assert value("hssx  123") == 20
    assert value("_world") == 100
