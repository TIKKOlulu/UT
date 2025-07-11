"""Versions of all_fluffy to test your tests for Week 9 Perform Part 2."""


# Correct version
def all_fluffy_v0(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy.
    Fluffy letters are those that appear in the word 'fluffy'.

    >>> all_fluffy_v0('fullfly')
    True
    >>> all_fluffy_v0('firefly')
    False
    """

    for ch in s:
        if not ch in 'fluffy':
            return False
    return True


# Three buggy versions
def all_fluffy_v1(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy.
    Fluffy letters are those that appear in the word 'fluffy'.
    """

    for ch in s:
        if ch in 'fluffy':
            return True
        else:
            return False


def all_fluffy_v2(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy.
    Fluffy letters are those that appear in the word 'fluffy'.
    """

    for ch in s:
        if ch in 'fluffy':
            result = True
        else:
            result = False

    return result


def all_fluffy_v3(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy.
    Fluffy letters are those that appear in the word 'fluffy'.
    """

    result = True
    for ch in 'fluffy':
        if ch not in s:
            result = False

    return result
