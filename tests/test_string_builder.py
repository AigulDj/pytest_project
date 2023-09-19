from lib.string_builder import *

def test_initially_return_an_empty_string():
    builder = StringBuilder()
    assert builder.output() == ""

def test_len_of_the_string():
    builder = StringBuilder()
    builder.add("New string")
    result = builder.size()
    assert result == 10

def test_output_multiple_strings_added():
    builder = StringBuilder()
    builder.add("New string")
    builder.add(" added.")
    result = builder.output()
    assert result == "New string added."
    
