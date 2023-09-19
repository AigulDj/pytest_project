import pytest
from lib.present import *

"""
When wrap an item 
We get it back when unwraped
"""
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(11)
    assert present.unwrap() == 11

"""
If unwrap before wrapping
Get an error message
"""
def test_present_wrap_error_message():
    present = Present()
    present.wrap(12)
    with pytest.raises(Exception) as e:
        present.wrap(22)
    error_msg = str(e.value)
    assert error_msg == "A contents has already been wrapped."


def test_present_unwrap_error_message():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_msg = str(e.value)
    assert error_msg == "No contents have been wrapped."

"""
if we try to wrap an already-wraped present
The 1st-wrapped value is unchaged
"""
def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44