import util

def next_state(state, char):
    if state == 1:
        if  char == 'a' or char == 'b':
            return 1
        elif char == 'c':
            return 2
    elif state == 2:
        if char == 'c':
            return 2
    return 666

fsm = util.Fsm([1, 2], 1, [2], next_state)



print(fsm.run("accc"))