from numb3rs import validate

def test_validate1():
    assert validate("140.247.235.144") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
def test_validate2():
    assert validate("256.255.255.255") == False
def test_validate3():
    assert validate("64.128.256.512") == False
def test_validate4():
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
def test_validate5():
    assert validate("cat") == False
def test_validate6():
    assert validate("8.8.8") == False
def test_validate7():
    assert validate("10.11.11.11.11") == False
def test_validate8():
    assert validate("75.456.76.65") == False
    assert validate('127.300.1.2') == False
    assert validate('127.1.300.2') == False
    assert validate('127.1.2.300') == False
    assert validate('127.300.300.300') == False
