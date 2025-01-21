def multiply(a, b):
    return a * b

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    assert multiply(-2, 3) == -6
