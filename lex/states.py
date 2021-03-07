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