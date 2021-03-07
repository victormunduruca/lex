import util
from states import * 
class Lexer:
    current_position = 0
    line = 0
    tokens = []

    def __init__(self, input_str):
        self.input_str = input_str
    
    def run(self):
        while(self.current_position < len(self.input_str)):
            self.next_token()
        for token in self.tokens:
            print(token[0] + ' ' + str(token[1]) + ' ' + str(token[2]))

    def next_token(self):
        char = self.input_str[self.current_position]
        if char.isdigit():
            return self.recognize_numbers()
        elif char.isalpha():
            return self.recognize_identifiers()
        elif util.isdelimiter(char):
            print('is delimiter')
        elif char.isspace():
            self.current_position += 1
    # def logical_transitionss(self, state, char):
    #     if state == States.start:
    #         if char == ''
    def relationals_transitions(self, state, char):
        relational = ['>', '<', '=']
        if state == States.rel_start:
            if char in relational:
                return States.rel
            elif char == '!':
                return States.exclamation
        elif state == States.rel:
            if char == '=':
                return States.rel_equal
        elif state == States.exclamation:
            if char == '=':
                return States.rel_equal
        return States.invalid_state


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
        return States.invalid_state

    def identifier_transitions(self, state, char):
        if state == 1:
            if char.isalpha():
                return 2
        elif state == 2:
            if char.isdigit() or char.isalpha() or char == '_':
                return 2
        return States.invalid_state

    def recognize_identifiers(self):
        identifier_fsm = util.Fsm([1, 2], 1, [2], self.identifier_transitions)
        [recognized, value] = identifier_fsm.run(self.input_str[self.current_position:])
        self.current_position += len(value)
        if(util.isreserved(value)):
            self.tokens.append(['PRE', value, self.line])
        else:
            self.tokens.append(['IDE', value, self.line])
        # print(self.current_position)
        # print(recognized)
        # print(value)

    def recognize_numbers(self):
        number_fsm = util.Fsm([1, 2, 3, 4], 1, [2, 4], self.number_transitions)
        [recognized, value] = number_fsm.run(self.input_str[self.current_position:])
        self.current_position += len(value)
        if (not recognized):
            self.tokens.append(['NMF', value, self.line])
        else:
            self.tokens.append(['NUM', value, self.line])
        # print(self.current_position)
        # print(recognized)
        # print(value)
    def recognize_relationals(self):
        relational_fsm = util.Fsm([0], States.rel_start, [States.rel, States.rel_equal], self.relationals_transitions)
        [recognized, value] = relational_fsm.run(self.input_str[self.current_position:])
        self.current_position += len(value)
        if (not recognized):
            self.tokens.append(['RELMF', value, self.line])
        else:
            self.tokens.append(['REL', value, self.line])
    # def recognize_delimiters(self, char):
    #     tokens.append(token.Token())







FILE = open('entrada/entrada1.txt', 'r')

lex = Lexer(FILE.read())

#lex.run()
relational_fsm = util.Fsm([0], States.rel_start, [States.rel, States.rel_equal], lex.relationals_transitions)

[recognized, value] = relational_fsm.run('!sdasd')

print(recognized)
print(value)