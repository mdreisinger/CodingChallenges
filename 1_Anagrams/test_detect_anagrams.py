"""
Unit tests to confirm that detect_anagrams.py is working as expected.
Run using pytest from the command line, e.g.: `pytest test_detect_anagrams.py`
"""

import pytest

from detect_anagrams import is_anagram


@pytest.mark.parametrize("word_list,expected_result", [
    (["angel", "glean"], True),
    (["AnGel", "gleaN"], True),
    (["Bigword", "smallword"], False),
    (["players", "Parsley"], True)
])
def test_is_anagram(word_list, expected_result):
    """
    Simple parameterized unit test to confirm that a number of words pairs return the expected
    result when given to `is_anagram()`.
    """
    assert is_anagram(word_list[0], word_list[1]) == expected_result

@pytest.mark.parametrize("word_list", [
    [1234, "glean"],
    ["AnGel", [1,2,3]],
])
def test_is_anagram_bad_input(word_list):
    """
    Simple test to confirm that `is_anagram()` checks that the input parameters are of the correct
    type.
    """
    with pytest.raises(RuntimeError) as exception:
        is_anagram(word_list[0], word_list[1])
    print(f"Got exception as expected: {exception}")
