from logger import Logger
from duel import Duel
from roll_state import RollState
from summon_state import SummonState
from attack_state import AttackState
from defense_state import DefenseState

class DuelState():
    """
    A YDDM duel state.
    """
    def __init__(self):
        self.log = Logger()
        self.duel = Duel(self.log)

        # duel substates
        self.roll_state = RollState(self.duel, self.log)
        self.sum_state  = SummonState(self.duel, self.log)
        self.atk_state  = AttackState(self.duel, self.log)
        self.def_state  = DefenseState(self.duel, self.log)
        
        # add next state options to states
        self.roll_state.sum_state = self.sum_state
        self.roll_state.atk_state = self.atk_state
        self.sum_state.atk_state = self.atk_state
        self.atk_state.def_state  = self.def_state
        self.atk_state.roll_state = self.roll_state
        self.def_state.atk_state = self.atk_state

        # set inital status
        self.state = self.roll_state
        self.log_start_message()
        self.finished = False

    def log_start_message(self):
        """
        Log starting duel message.
        """
        self.log.add("GAME ON!\n")
        self.state.set_start_message()
        self.state.log_start_message()

    def update(self, command):
        """
        Update state given command.
        """
        # update state
        self.state.update(command)

        # check if winning condition is met
        # if duel finished, early return
        self.finished = self.duel.finished()
        if self.finished:
            return

        # change state and duel
        self.state = self.state.next_state
        self.state.log_start_message()
