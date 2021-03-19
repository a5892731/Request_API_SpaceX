from state_machine.state import State

from state_machine.states.my_states import state3


# Start of our states
class Initialization(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def on_event(self, event):
        if event == 'device_locked':
            return state3()

        return self