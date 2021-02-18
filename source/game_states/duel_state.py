from duel import Duel
from roll_state import RollState

class DuelState():
    """
    A YDDM duel state.
    """
    def __init__(self):
        self.duel = Duel()
        self.state = RollState(self.duel)
        self.initial_message()
        self.finished = False

    def initial_message(self):
        """
        As initial message: duel started message.
        """
        self.message  = "GAME ON!\n"
        self.state.set_initial_message()
        self.message += self.state.message

    def update(self, command):
        """
        Update state given command.
        """
        # update state
        self.state.update(command)
        self.message = self.state.message

        # check if winning condition is met
        # if duel finished, early return
        self.finished = self.duel.finished()
        if self.finished:
            self.message += self.duel.message
            return

        # change state and duel
        self.state = self.state.next_state
        self.duel = self.state.duel
        self.message += self.state.message
