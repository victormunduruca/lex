import utils

def next_state(state, char):
    if state == 1:
        if  char == 'a' or char == 'b':
            return 1
        elif char == 'c':
            return 2
    else:
        return 666;

fsm = utils.Fsm([1, 2], 1, [2], next_state)




print(fsm.run("bbabaabbc"))