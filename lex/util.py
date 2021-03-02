NO_NEXT_STATE = "No Next State"
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
            if (current_state in self.accepting_states) and next_state == NO_NEXT_STATE:
                return True
            if next_state == NO_NEXT_STATE:
                return False
            current_state = next_state
            print(next_state)
        return current_state in self.accepting_states