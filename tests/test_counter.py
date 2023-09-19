from lib.counter import *

# counter = Counter()

def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_adds_a_single_number():
    counter = Counter()
    counter.add(5)
    # result = counter.report()
    assert counter.report() == "Counted to 5 so far."

def test_counter_adds_a_multiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    # result = counter.report()
    assert counter.report() == "Counted to 15 so far."