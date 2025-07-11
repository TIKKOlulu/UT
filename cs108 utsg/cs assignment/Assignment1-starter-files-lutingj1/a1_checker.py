"""A simple checker for types of functions in puzzle_functions.py."""

import sys
sys.path.insert(0, 'pyta')
import puzzle_functions as pf

FILENAME = 'puzzle_functions.py'
PYTA_CONFIG = 'pyta/a1_pythonta.json'

print('==================== Start: checking coding style ===================')

import json

error_message = '\nCould not run PythonTA correctly.\n' \
                'Please make sure you have run the setup.py provided on ' \
                'Quercus: that should install PythonTA for you.\n' \
                'Please attend office hours if you require assistance ' \
                'in running PythonTA.'

try:
    import python_ta
    with open(PYTA_CONFIG) as cf:
        config_dict = json.loads(cf.read())
        config_dict['output-format'] = 'python_ta.reporters.PlainReporter'

    python_ta.check_all(FILENAME, config=config_dict)
except:
    print(error_message)

print('=================== End: checking coding style ===================\n')

print('============ Start: checking parameter and return types ============')

# Get the initial values of the constants
CONSTS_BEFORE = [pf.UP, pf.DOWN, pf.FORWARD, pf.BACKWARD, 
                 pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                 pf.UP_FACTOR,
                 pf.THRESHOLD, pf.BONUS,
                 pf.P1, pf.P2, pf.P1_WINS, pf.P2_WINS, pf.TIE]

def type_error_message(func_name: str, expected: str, got: str) -> str:
    """Return an error message for function func_name returning type got,
    where the correct return type is expected."""

    return ('{0} should return a {1}, but returned {2}' +
            '.').format(func_name, expected, got)


# Type check puzzle_functions.get_current_player
print('Checking get_current_player...')
got = pf.get_current_player(True)
assert isinstance(got, str), \
    type_error_message('puzzle_functions.get_current_player', 'str', type(got))
print('  check complete')

# Type check puzzle_functions.get_winner
print('Checking get_winner...')
got = pf.get_winner(17, 32)
assert isinstance(got, str), \
    type_error_message('puzzle_functions.get_winner', 'str', type(got))
print('  check complete')

# Type check puzzle_functions.get_factor
print('Checking get_factor...')
got = pf.get_factor('forward')
assert isinstance(got, int), \
    type_error_message('puzzle_functions.get_factor', 'int', type(got))
print('  check complete')

# Type check puzzle_functions.reverse
print('Checking reverse...')
got = pf.reverse('hello')
assert isinstance(got, str), \
    type_error_message('puzzle_functions.reverse', 'str', type(got))
print('  check complete')

# Type check puzzle_functions.get_row
print('Checking get_row...')
got = pf.get_row('abcd\nefgh\nijkl\n', 1)
assert isinstance(got, str), \
        type_error_message('puzzle_functions.get_row', 'str', type(got))
print('  check complete')

# Type check puzzle_functions.get_points
print('Checking get_points...')
got = pf.get_points('up', 7)
assert isinstance(got, int), \
    type_error_message('puzzle_functions.get_points', 'int', type(got))
print('  check complete')

# Type check puzzle_functions.check_guess
print('Checking check_guess...')
got = pf.check_guess('abcd\nefgh\nijkl\n', 'forward', 'bcd', 2, 4)
assert isinstance(got, int), \
    type_error_message('puzzle_functions.check_guess', 'int', type(got))
print('  check complete')

print('============= End: checking parameter and return types =============\n')

print('========== Start: checking whether constants are unchanged ==========')

# Get the final values of the constants
CONSTS_AFTER  = [pf.UP, pf.DOWN, pf.FORWARD, pf.BACKWARD, 
                 pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                 pf.UP_FACTOR,
                 pf.THRESHOLD, pf.BONUS,
                 pf.P1, pf.P2, pf.P1_WINS, pf.P2_WINS, pf.TIE]

# Check whether the constants are unchanged.
print('Checking constants...')
assert CONSTS_BEFORE == CONSTS_AFTER, \
       ('Your function(s) modified the value of some constant(s). Edit your' +
        '\ncode so that the values of constants are unchanged by your' +
        ' functions.')
print('  check complete')

print('=========== End: checking whether constants are unchanged ===========')
