from parity import classify

def test_even_number():
    assert classify(4) == "even"

def test_divisible_by_3():
    assert classify(9) == "divisible by 3"

def test_other_number():
    assert classify(7) == "other"

def test_even_and_divisible_by_3():
    assert classify(6) == "even"
