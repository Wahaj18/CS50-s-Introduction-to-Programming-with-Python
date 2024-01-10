from plates import is_valid

def test_is_valid1():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_is_valid2():
    assert is_valid("CS50P") == False

def test_is_valid3():
    assert is_valid("PI3.14") == False

def test_is_valid4():
    assert is_valid("OUTATIME") == False

def test_is_valid5():
    assert is_valid("50") == False
