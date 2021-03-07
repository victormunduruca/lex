import re
import util
from states import *


def isdigit(x):
    return re.match(r'\d', x, re.ASCII) is not None


def isletter(x):
    return re.match(r'([a-z] || [A-Z])', x) is not None


def issymbol(x):
    return (ord(x) > 31) and (ord(x) < 127)

# def isdelimiter(x):
#     return x is in delimiters

def temp_transitions(state, char):
    if state == States.start:
        if isdigit(char):
            return States.num 
        elif char.isalpha():
            return States.ide
        elif char == '>' or char == '<' or char == '=':
            return States.rel
        elif char == '!':
            return States.exclamation
        elif char == '&' or char == '|':
            return States.log_incomplete


    elif state == States.num:
        if isdigit(char):
            return States.num
        elif char == '.':
            return States.num_dot
    elif state == States.num_dot:
        if isdigit(char):
            return States.num_after_dot
    elif state == States.num_after_dot:
        if isdigit(char):
            return States.num_after_dot

    elif state == States.ide:
        if isletter(char) or isdigit(char) or char == '_':
            return States.ide

    elif state == States.rel:
        if char == '=':
            return States.rel_equal
    elif state == States.exclamation:
        if char == '=':
            return States.rel_equal

    elif state == States.log_incomplete:
        if char == '&' or char == '|':
            return States.log_complete

    return States.invalid_state #TODO Save buffer logic


fsm = util.Fsm([0], States.start, [States.num, States.num_after_dot, States.rel_equal, States.rel, States.exclamation, States.ide, States.log_complete], temp_transitions)

[recognized, value] = fsm.run('||')
print(recognized)
print(value)