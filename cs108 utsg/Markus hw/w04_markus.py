"""Week 4 Perform - Part 2"""

# file name: w04_markus.py
#
# Complete the following steps:
#  (1) Complete the following function according to its docstring.
#  (2) Save your file after you make changes, and then run the file by
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the Python shell. An asterisk * on the Wing101
#      w04_markus.py tab indicates that modifications have NOT been saved.
#  (3) Test your function in the Wing101 shell by evaluating the examples from
#      the docstring and confirming that the correct result is displayed.
#  (4) Test your function using different function arguments.
#  (5) When you are convinced that your functions are correct, submit your
#      modified file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in Week *2* Perform -> Accessing Part 2 of the
#      Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.


def is_strong_password(passwd: str) -> bool:
    """Return True if and only if passwd is considered to be a strong password.

    A string is considered to be a strong password when it satisfies each of
    the following conditions:
    - it has a length greater than or equal to 6,
    - it contains at least one lowercase letter,
    - it contains at least one uppercase letter, and
    - it contains at least one digit.

    Hint: Try using boolean variables or counting variables in your solution.
          They can be used when determining whether or not each condition has
          been met.

    >>> is_strong_password('I<3csc108')
    True
    >>> is_strong_password('compsci!!')
    False
    >>> is_strong_password('Csc108')
    True
    """

    count_upper_letters = 0
    count_lower_letters = 0
    count_digit = 0

    for ch in passwd:
        if ch.isupper():
            count_upper_letters += 1
        elif ch.islower():
            count_lower_letters += 1
        elif ch.isdigit():
            count_digit += 1            
    if count_upper_letters >= 1 and count_lower_letters >= 1 \
       and count_digit >= 1:
        return True
    else:
        return False
