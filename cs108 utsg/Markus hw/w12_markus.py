"""Week 12 Perform - Part 2

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files provided for this exercise are:
Copyright (c) 2024 The CSC108 Team

Complete the following steps:
(1) Below is a function bubble_up that takes 3 parameters: a list, a start 
    index, and an end index. It bubbles 'up' the items in the given range. 
    We have started a function called bubble_down that takes the same 3 
    parameters but bubbles in the opposite direction. 
    Complete function bubble_down according to its docstring.
(2) Save your file after you make changes, and then run the file by
    clicking on the green Run button in Wing101. This will let you call your
    modified function in the shell. An asterisk * on the Wing101
    w12_markus.py tab indicates that modifications have NOT been saved.
(3) Test your function in the Wing101 shell by evaluating the examples from
    the docstring and confirming that the correct result is displayed.
(4) Test your function using different function arguments.
(5) When convinced that your function is correct, submit your modified
    file to MarkUs. You can find instructions on submitting a file to MarkUs
    in the Week *2* Perform on PCRS.
(6) Verify you have submit the right file to MarkUs by downloading it again
    and checking it is the one you meant to submit.
(7) We have also provided a checker test for you to run in MarkUs. Run this to 
    make sure your code passes a simple test case (the one from the docstring). 
    Note that we will run additional tests when we mark your submission.
"""


# The function bubble_up is complete and provided for reference only.
# The function bubble_up will not be marked.
def bubble_up(values: list, left: int, right: int) -> None:
    """Bubble up through values[left: right + 1], swapping items that are out of
    order. Note that use of this slicing notation means that items
    values[left], values[left + 1], values[left + 2], ..., values[right] could
    be modified.

    Precondition: left and right are valid indexes in values.

    >>> list_example_1 = [4, 3, 2, 1, 0]
    >>> bubble_up(list_example_1, 0, 3)
    >>> list_example_1
    [3, 2, 1, 4, 0]
    >>> list_example_2 = [4, 3, 2, 1, 0]
    >>> bubble_up(list_example_2, 2, 4)
    >>> list_example_2
    [4, 3, 1, 0, 2]
    """

    for i in range(left, right):
        if values[i] > values[i + 1]:
            temp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = temp


# Read the bubble_up function as a starting point to help you complete the
# bubble_down function.  Read the examples below to resolve any uncertainty
# about the direction of the comparisons.
def bubble_down(values: list, left: int, right: int) -> None:
    """Bubble down through values[left: right+1], swapping items that are out
    of order. Note that use of this slicing notation means that items
    values[left], values[left + 1], values[left + 2], ..., values[right] could
    be modified.

    Precondition: left and right are valid indexes in values.

    >>> list_example_1 = [4, 3, 2, 1, 0]
    >>> bubble_down(list_example_1, 1, 3)
    >>> list_example_1
    [4, 1, 3, 2, 0]
    >>> list_example_2 = [4, 3, 2, 1, 0]
    >>> bubble_down(list_example_2, 0, 4)
    >>> list_example_2
    [0, 4, 3, 2, 1]
    """

    for i in range(right, left, -1):
        if values[i] < values[i - 1]:
            temp = values[i]
            values[i] = values[i - 1]
            values[i - 1] = temp
