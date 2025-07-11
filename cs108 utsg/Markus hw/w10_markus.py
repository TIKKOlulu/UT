"""Week 10 Perform - Part 2"""

# file name: w10_markus.py
#
# Complete the following steps:
# (1) Below is a contains_even function that has been fully implemented for you.
#     Assume that the function is correct, and do not change it.
#     You will be completing four pytest test functions for this function.
#     The headers for four pytest test functions are given below. We have also
#     provided the completed test function test_empty for your reference.
#     Your task is to complete the bodies of the four incomplete test functions
#     so that they implement the test case described in the method docstring.
#     You should only add code inside the four function bodies; do not make any
#     other changes to this file.
# (2) Save your file after you make changes, and then run the file by
#     clicking on the green Run button in Wing101.  An asterisk * on the Wing101
#     w10_markus.py tab indicates that modifications have NOT been saved.
# (3) When convinced that your test functions are correct, submit your modified
#     file to MarkUs. You can find instructions on submitting a file to MarkUs
#     in the Week *2* Perform on PCRS.
# (4) Verify you have submitted the right file to MarkUs by downloading it again
#     and checking it is the one you meant to submit.
# (5) We have also provided a checker test for you to run in MarkUs. Run this to
#     make sure your code passes a simple test case. Note that we will test
#     your test functions when we mark your submission.
#

import pytest


def contains_even(values: list[int]) -> bool:
    """Return True if and only if values contains at least one even number.
    """

    for item in values:
        if item % 2 == 0:
            return True
    return False


# This completed test function is provided as an example for you to refer to.
# Do not edit or remove it.
def test_empty() -> None:
    """Test that the contains_even function works correctly when the argument
    is an empty list."""

    actual = contains_even([])
    expected = False
    assert actual == expected


def test_even_first() -> None:
    """Test that the contains_even function works correctly when the first
    value in the list is even and the rest are odd, and the list contains
    at least 3 items."""
    # TODO: Implement the body of this test case to match the docstring
    #       specifications.
    actual = contains_even([4, 7, 5])
    expected = True
    assert actual == expected

def test_even_last() -> None:
    """Test that the contains_even function works correctly when the last
    value in the list is even and the rest are odd, and the list contains
    at least 3 items."""
    # TODO: Implement the body of this test case to match the docstring
    #       specifications.
    actual = contains_even([5, 3, 8])
    expected = True
    assert actual == expected


def test_all_odd() -> None:
    """Test that the contains_even function works correctly on a list
    containing only odd items, and the list contains at least 3 items."""
    # TODO: Implement the body of this test case to match the docstring
    #       specifications.
    actual = contains_even([3, 5, 7])
    expected = False
    assert actual == expected

def test_no_mutation() -> None:
    """Test that the contains_even function does not mutate the list
    argument when the list contains at least 3 items."""
    # TODO: Implement the body of this test case to match the docstring
    #       specifications.
    actual = contains_even([3, 8, 6])
    expected = True
    assert actual == expected
    


if __name__ == '__main__':
    pytest.main(['w10_markus.py'])
