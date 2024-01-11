import pytest
import datetime
from seasons import get_minutes
from seasons import get_date

def test_get_date():
    assert get_date("1998-10-12") == datetime.date(1998,10,12)
    assert get_date("1990-12-10") == datetime.date(1990,12,10)

def test_get_date2():
    with pytest.raises(SystemExit):
        get_date("January 18, 1998")

def test_get_minutes():
    assert get_minutes(datetime.date.today(), datetime.date(1998,10,12)) == 13271040
