import util
import token

class Lexer:
    current_position = 0
    line = 0
    tokens = []

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

     def identifier_transitions(self, state, char):
        if state == 1:
            if char.isalpha():
                return 2
        elif state == 2:
            if char.isdigit() or char.isalpha() or char == '_':
                return 2
        return util.NO_NEXT_STATE

    def recognize_identifiers(self):
        identifier_fsm = util.Fsm([1, 2], 1, [2], self.identifier_transitions)
        [recognized, value] = identifier_fsm.run(self.input_str[self.current_position:])
        self.current_position += len(value)
        print(self.current_position)
        print(recognized)
        print(value)

    def recognize_numbers(self):
        number_fsm = util.Fsm([1, 2, 3, 4], 1, [2, 4], self.number_transitions)
        
        [recognized, value] = number_fsm.run(self.input_str[self.current_position:])
        self.current_position += len(value)
        print(self.current_position)
        print(recognized)
        print(value)
    
    # def recognize_delimiters(self, char):
    #     tokens.append(token.Token())

    def next_token(self):
        char = self.input_str[self.current_position]
        if char.isdigit():
            return self.recognize_numbers()
        elif char.isalpha():
            return self.recognize_identifiers()


FILE = open('entrada/entrada1.txt', 'r')

lex = Lexer(FILE.read())

lex.run()