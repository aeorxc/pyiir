from pyiir import pyiir

def test_get_access_token():
    res = pyiir.get_access_token()
    assert res is not None

def test_summary_call():
    res = pyiir.summary_call("2017-08-01", "2024-12-01", tradingRegion="III", unitTypeGroup="Reforming", country="U.S.A.")
    assert res is not None

def test_details_call():
    res = pyiir.details_call("641989")
    assert res is not None