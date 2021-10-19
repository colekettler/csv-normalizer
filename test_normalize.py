import normalize


def test_normalize_row_returns_row():
    row = "val1,val2"
    assert normalize.normalize_row(row)


def test_normalize_timestamp_uses_RFC3339():
    timestamp_am = "4/1/11 11:00:00 AM"
    assert normalize.normalize_timestamp(timestamp_am) == "2011-04-01T11:00:00"

    timestamp_pm = "4/1/11 11:00:00 PM"
    assert normalize.normalize_timestamp(timestamp_pm) == "2011-04-01T23:00:00"
