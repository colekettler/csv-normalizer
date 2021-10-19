import normalize


def test_normalize_row():
    row = {
        "Timestamp": "4/1/11 11:00:00 AM",
        "ZIP": "94121",
        "FullName": "Monkey Alberto",
    }
    assert normalize.normalize_row(row)


def test_normalize_timestamp():
    timestamp_am = normalize.normalize_timestamp("4/1/11 11:00:00 AM")
    assert timestamp_am == "2011-04-01T14:00:00-05:00"

    timestamp_pm = normalize.normalize_timestamp("4/1/11 11:00:00 PM")
    assert timestamp_pm == "2011-04-02T02:00:00-05:00"


def test_normalize_zip():
    full_zip = "12345"
    assert normalize.normalize_zip(full_zip) == "12345"

    short_zip = "123"
    assert normalize.normalize_zip(short_zip) == "00123"


def test_normalize_full_name():
    ascii_name = "Monkey Alberto"
    assert normalize.normalize_full_name(ascii_name) == "MONKEY ALBERTO"

    diacritics_name = "Superman übertan"
    assert normalize.normalize_full_name(diacritics_name) == "SUPERMAN ÜBERTAN"

    japanese_name = "株式会社スタジオジブリ"
    assert normalize.normalize_full_name(japanese_name) == "株式会社スタジオジブリ"
