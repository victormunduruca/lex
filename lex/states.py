from enum import Enum
class States(Enum):
    invalid_state = -1
    start = 0

    num = 2
    num_dot = 3
    num_after_dot = 4

    ide = 6

    rel = 7
    rel_equal = 8

    exclamation = 9

    log_incomplete = 10
    log_complete = 11

    art_plus = 12
    art_minus = 13
    art_complete = 14
    slash = 15

    delimiter = 16

    com_line = 17
    com_line_complete = 18
    com_block = 19
    com_block_after_asterisk = 20
    com_block_complete = 21

    string = 22 
    string_escape = 23
    string_escape_quote = 24
    string_final = 25