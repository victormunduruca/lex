import re
import util
from states import *

delimiters = [
    ';',
    ',',
    '(',
    ')',
    '{',
    '}',
    '[',
    ']',
    '.'
]

def isdigit(x):
    return re.match(r'\d', x, re.ASCII) is not None


def isletter(x):
    return re.match(r'([a-z] || [A-Z])', x) is not None


def issymbol(x):
    return (ord(x) > 31) and (ord(x) < 127) and not (ord(x) == 34)

# def isdelimiter(x):
#     return x is in delimiters

def temp_transitions(state, char):
    if state == States.start:
        if isdigit(char):
            return States.num 
        elif char.isalpha():
            return States.ide
        elif char in delimiters:
            return States.delimiter
        elif char == '>' or char == '<' or char == '=':
            return States.rel
        elif char == '!':
            return States.exclamation
        elif char == '&' or char == '|':
            return States.log_incomplete
        elif char == '+':
            return States.art_plus
        elif char == '-':
            return States.art_minus
        elif char == '*':
            return States.art_complete
        elif char == '/':
            return States.slash
        elif char == "\"":
            return States.string


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

    elif state == States.art_plus:
        if char == '+':
            return States.art_complete
    elif state == States.art_minus:
        if char == '-':
            return States.art_complete

    elif  state == States.slash:
        if char == '/':
            return States.com_line
        elif char == '*':
            return States.com_block

    elif state == States.com_line:
        if char == '\n':
            return States.com_line_complete
        return States.com_line
    elif state == States.com_block:
        if char == '*':
            return States.com_block_after_asterisk
        return States.com_block
    elif state == States.com_block_after_asterisk:
        if char == '*':
            return States.com_block_after_asterisk
        elif char == '/':
            return States.com_block_complete
        return States.com_block_complete

    #String 
    elif state == States.string:
        if char == '\\':
            return States.string_escape
        if char.isalpha() or char.isdigit() or issymbol(char):
            return States.string
        elif char == "\"":
            return States.string_final
    elif state == States.string_escape:
        if char == "\"":
            return States.string_escape_quote
        elif char == "\\":
            return States.string_escape
        elif char.isalpha() or char.isdigit() or issymbol(char):
            return States.string
    elif state == States.string_escape_quote:
        if char == "\"":
            return States.string_final
        elif char == "\\":
            return States.string_escape
        elif char.isalpha() or char.isdigit() or issymbol(char):
            return States.string





    return States.invalid_state #TODO Save buffer logic

FILE = open('entrada/entrada1.txt', 'r')
input_string = FILE.read()
fsm = util.Fsm([0], States.start, [States.num, States.num_after_dot, States.rel_equal, States.rel, States.exclamation, States.ide, States.log_complete, States.art_complete, States.art_plus, States.art_minus, States.slash, States.delimiter, States.com_line_complete, States.com_block_complete, States.string_final], temp_transitions)

[recognized, value] = fsm.run(input_string)
print(recognized)
print(value)

