from logger import Logger
from duel import Duel
from roll_state import RollState
from summon_state import SummonState
from dimension_state import DimensionState
from dungeon_state import DungeonState
from defense_state import DefenseState

class DuelState():
    """
    A YDDM duel state.
    """
    def __init__(self, pfile1, pfile2):
        self.log = Logger()
        self.duel = Duel(pfile1, pfile2, self.log)

        # duel substates
        self.roll_state = RollState(self.duel, self.log)
        self.sum_state  = SummonState(self.duel, self.log)
        self.dim_state  = DimensionState(self.duel, self.log)
        self.dun_state  = DungeonState(self.duel, self.log)
        self.def_state  = DefenseState(self.duel, self.log)
        
        # add next state options to states
        self.roll_state.sum_state = self.sum_state
        self.roll_state.dun_state = self.dun_state
        self.sum_state.dun_state  = self.dun_state
        self.sum_state.dim_state  = self.dim_state
        self.dim_state.dun_state  = self.dun_state
        self.dun_state.def_state  = self.def_state
        self.dun_state.roll_state = self.roll_state
        self.def_state.dun_state  = self.dun_state

        # set inital status
        self.state = self.roll_state
        self.log_start_message()
        self.finished = False

    def log_start_message(self):
        """
        Log starting duel message.
        """
        self.log.add("GAME ON!\n")
        self.state.restart()
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
