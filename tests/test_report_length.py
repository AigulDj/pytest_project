from lib.report_length import *

def test_report_length():
    result = report_length('House')
    assert result == "This string was 5 characters long."