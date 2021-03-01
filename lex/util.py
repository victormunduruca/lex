class Fsm:
    def __init__(self, states, initial_state, accepting_states, next_state):
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.next_state = next_state

    def run(self, input_string):
        current_state = self.initial_state
        for char in input_string:
            next_state = self.next_state(current_state, char)
            print(next_state)
            if (current_state in self.accepting_states) and next_state == 666:
                return True
            if next_state == 666:
                return False
            current_state = next_state
        return True 


