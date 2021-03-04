import util

FILE = open('entrada/entrada1.txt', 'r')
input = FILE.read()

current_position = 0
line = 0

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

def recognize_numbers():
    number_fsm = util.Fsm([1, 2, 3, 4], 1, [2, 4], number_transitions)
    
    [recognized, value] = number_fsm.run(input[current_position:])
   # current_position += len(value)
    print(recognized)
    print(value)
# while current_position < len(input):
    
#    # current_position += 1
#     print(char)
# FILE.close()
def next_token():
    char = input[current_position]
    if char.isdigit():
        return recognize_numbers()
        

next_token()






