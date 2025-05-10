#Test-driven development example

import pytest


def is_even(n):
    """
    Check if a number is even.
    
    :param n: The number to check.
    :return: True if n is even, False otherwise.
    """
    return n % 2 == 0


# Test cases for is_even function
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False

# Test cases for is_even function with invalid inputs
def test_is_even_invalid():
    with pytest.raises(TypeError):
        is_even("string")
    with pytest.raises(TypeError):
        is_even(None)
    with pytest.raises(TypeError):
        is_even([])

# Test cases for is_even function with edge cases
def test_is_even_edge_cases():
    assert is_even(1.0) == False
    assert is_even(2.0) == True
    assert is_even(float('inf')) == False
    assert is_even(float('-inf')) == False
    assert is_even(float('nan')) == False


