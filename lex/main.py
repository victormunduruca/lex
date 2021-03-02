import util

def next_state(state, char):
    if state == 1:
        if char.isdigit():
            return 2
    elif state == 2:
        if char.isdigit():
            return 2
        elif char == '.':
            return 3
    elif state == 3:
        if char.isdigit():
            return 4
    elif state == 4:
        if char.isdigit():
            return 4
    return 666

fsm = util.Fsm([1, 2, 3, 4], 1, [2, 4], next_state)



print(fsm.run("1.2 "))