# w02_markus.py
#
# Complete the following steps:
#  (1) Add one new example to the docstring in the function ariana_says.
#  (2) Change the function body so that the function runs as described by the
#      docstring.
#  (3) Save your file after you make a change, and then run the file by 
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the shell. An asterisk * on the Wing101 
#      w02_markus.py tab indicates that modifications have NOT been saved.
#  (4) Test your ariana_says function in the Wing101 shell by evaluating the
#      statement
#      >>> ariana_says('Thank u')
#      and confirm that the correct result is displayed.
#  (5) Test your ariana_says function using different function arguments.
#  (6) When you are convinced that your ariana_says function is correct, 
#      submit your modified file to MarkUs. You can find instructions on 
#      submitting a file to MarkUs in Week 2 Perform -> Accessing Part 2 of
#      the Week 2 Perform (For Credit) on PCRS.
#  (7) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (8) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (2) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.

def ariana_says(word: str) -> str:
    """Return word repeated four times with the string ', next ' between each
    occurrence.
    
    >>> ariana_says('Thank u')
    'Thank u, next Thank u, next Thank u, next Thank u'
    >>> ariana_says('You are welcome')
    'You are welcome, next You are welcome, next You are welcome, next You are welcome'
    """

    return word + ', ' + ('next' + ' ' + word + ', ') * 2 + 'next ' + word
