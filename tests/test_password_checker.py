import pytest
from lib.password_checker import *

"""
Check if password is valid
"""
def test_password_is_valid():
    password_checker = PasswordChecker()
    assert password_checker.check('12345678') == True

"""
Check if password is invalid
"""
def test_password_invalid():
    password_chacker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_chacker.check('123')
    assert str(e.value) == "Invalid password, must be 8+ characters."
