import normalize


def test_normalize_row():
    row = "val1,val2"
    assert normalize.normalize_row(row)


def test_normalize_timestamp():
    timestamp_am = "4/1/11 11:00:00 AM"
    assert normalize.normalize_timestamp(timestamp_am) == "2011-04-01T14:00:00"

    timestamp_pm = "4/1/11 11:00:00 PM"
    assert normalize.normalize_timestamp(timestamp_pm) == "2011-04-02T02:00:00"
