NO_NEXT_STATE = -1
class Fsm:
    def __init__(self, states, initial_state, accepting_states, next_state):
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.next_state = next_state

    def run(self, input_string):
        value_buffer = ''
        current_state = self.initial_state
        for char in input_string:
            next_state = self.next_state(current_state, char)
            if next_state == NO_NEXT_STATE:
                return False
            current_state = next_state
            value_buffer += char
        return [current_state in self.accepting_states, value_buffer]
    

def isdelimiter(char):
    if char == '{' or char == '}' or char == '(' or char == ')' or char == '[' or char == ']' or char == ','or char == '.':
        return True
    return False

reserved_words = ['var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start', 'return', 'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean', 'string', 'true', 'false', 'global', 'local']
def isreserved(string):
    return string in reserved_words