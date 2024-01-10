from twttr import shorten

def test_shorten_lower():
    assert shorten("word") == "wrd"
    assert shorten("worldie") == "wrld"
    assert shorten("hello") == "hll"

def test_shorten_caps():
    assert shorten("WORD") == "WRD"
    assert shorten("WORLDIE") == "WRLD"
    assert shorten("HELLO") == "HLL"
    assert shorten("hELLO") == "hLL"

def test_shorten_nums():
    assert shorten("WORD123") == "WRD123"
    assert shorten("WORLDIE786") == "WRLD786"
    assert shorten("HELLO154") == "HLL154"
    assert shorten("23hELLO123") == "23hLL123"

def test_shorten_punc():
    assert shorten("W,ORD123") == "W,RD123"
    assert shorten("WORLD,E786") == "WRLD,786"
    assert shorten("HELLO.154") == "HLL.154"
    assert shorten("23hEL,LO123") == "23hL,L123"
