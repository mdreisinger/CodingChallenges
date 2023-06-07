"""
This module provides the simple functionality to sum all the even numbers in a given list.
"""

def sum_even_numbers(integer_list: list) -> int:
    """
    This is the main function of this module which takes in a list of integers and returns the
    sum of all the even integers.
    """
    if not isinstance(integer_list, list):
        raise RuntimeError("sum_even_numbers expected a list input but got something else.")

    result = 0
    for item in integer_list:
        if not isinstance(item, int):
            raise RuntimeError("sum_even_numbers expected a list of integers but "
                               "at least one item in the list is not an integer.")
        if item % 2 == 0:
            result += item

    return result
