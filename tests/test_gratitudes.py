from lib.gratitudes import Gratitudes

"""Returns emty list if nothig was added
"""
def test_returns_if_nothing_added():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

"""
Format list to a string after joing strings
"""
def test__adding_multiple_strings_and_format_them():
    gratitude = Gratitudes()
    gratitude.add('every new day')
    gratitude.add('healthy parents')
    assert gratitude.format() == "Be grateful for: every new day, healthy parents"
