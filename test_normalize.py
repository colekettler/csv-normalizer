import normalize


def test_normalize_row_returns_row():
    row = "val1,val2"
    assert normalize.normalize_row(row)
