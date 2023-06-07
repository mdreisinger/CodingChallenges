"""
Unit tests to confirm that detect_anagrams.py is working as expected.
Run using pytest from the command line, e.g.: `pytest test_sum_evens.py`
"""

import pytest

from sum_evens import sum_even_numbers


@pytest.mark.parametrize("integer_list,expected_result", [
    ([0,1,2,3,4,5,6,7,8,9,10], 30),
    ([0,2,1,1,2,3,4,10,6], 24),
    ([], 0),
    ([2,4,6,8,10], 30)
])
def test_sum_evens(integer_list, expected_result):
    """
    Simple parameterized unit test to confirm that `sum_even_numbers()` returns the expected
    result given a list of integers.
    """
    assert sum_even_numbers(integer_list) == expected_result

@pytest.mark.parametrize("integer_list", [
    "1,2,3,4,5",
    2+2,
    4.5
])
def test_sum_evens_bad_input(integer_list):
    """
    Simple test to confirm that `is_anagram()` checks that the input parameters are of the correct
    type.
    """
    with pytest.raises(RuntimeError) as exception:
        sum_even_numbers(integer_list)
    print(f"Got exception as expected: {exception}")

@pytest.mark.parametrize("integer_list", [
    [0,1,2, "glean"],
    [1,5,8, [1,2,3]],
    [1,2,4.5],
])
def test_sum_evens_bad_input_list_items(integer_list):
    """
    Simple test to confirm that `is_anagram()` checks that the input parameters are of the correct
    type.
    """
    with pytest.raises(RuntimeError) as exception:
        sum_even_numbers(integer_list)
    print(f"Got exception as expected: {exception}")
