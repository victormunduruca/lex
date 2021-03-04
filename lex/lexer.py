import util

class Lexer:
    current_position = 0
    line = 0

    def __init__(self, input_str):
        self.input_str = input_str
    
    def run(self):
        self.next_token()

    def number_transitions(self, state, char):
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

    def recognize_numbers(self):
        number_fsm = util.Fsm([1, 2, 3, 4], 1, [2, 4], self.number_transitions)
        
        [recognized, value] = number_fsm.run(self.input_str[self.current_position:])
        self.current_position += len(value)
        print(self.current_position)
        print(recognized)
        print(value)
    # while current_position < len(input_str):
        
    #    # current_position += 1
    #     print(char)
    # FILE.close()
    def next_token(self):
        char = self.input_str[self.current_position]
        if char.isdigit():
            return self.recognize_numbers()
        


FILE = open('entrada/entrada1.txt', 'r')

lex = Lexer(FILE.read())

lex.run()