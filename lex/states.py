from enum import Enum
class States(Enum):
    invalid_state = -1
    start = 0
    num_start = 1
    num_final = 2
    num_dot = 3
    num_final_afterdot = 4
    ide_start = 5
    ide_final = 6
    rel_start = 7
    rel_greater = 8
    rel_greater_equal = 9
    rel_less = 10
    rel_less_equal = 11
    rel_equal = 12
    rel_comparison = 13
    rel_exclamation = 14
    rel_different = 15

    log_amper = 16
    log_second_amper = 17
    log_second_exclamation = 18

