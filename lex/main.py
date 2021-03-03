import util

FILE = open('entrada/entrada1.txt', 'r')
input = FILE.read()

current_position = 0
line = 0

while current_position < len(input):
    char = input[current_position]
    current_position += 1
    print(char)
FILE.close()



def recognize_numbers():
    number_fsm = util.Fsm([1, 2, 3, 4], 1, [2, 4], number_transitions)

def number_transitions(state, char):
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
            return
    return util.NO_NEXT_STATE