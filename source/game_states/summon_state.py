from duel_dubstate import DuelSubtate
from attack_state import AttackState

class SummonState(DuelSubstate):
    """
    State when player summon a monster/item after a roll.
    """
    def __init__(self, player, opponent, dimensions):
        super().__init__(player, opponent)
        self.dimensions = dimensions
        self.help_text = self.help_text + help_text

    def initial_message(self):
        """
        As intial message: available dimensions.
        """
        message = "Available summons:\n" + \
            self.dimensions.stringify() + "\n" + \
            "Select with number [s: skip].\n\n"

    def update(self, command):
        """
        Update state given command. Return result dictionary
        with the necessary information for parent state.
        """
        # print available summons command
        if command.equals("p", "as"):
            result = self.default_result()
            message = self.dimensions.stringify() + "\n"
            result["message"] = message
            return result

        elif command.equals("s"):
            next_state = AttackState(self.player, 
                self.opponent)
            message = "\n"
            message2 = next_state.initial_message()

            # generate result
            result["nextstate"] = next_state
            result["message"] = message
            result["message2"] = message2

            return True

        # dice dimension
        elif command.len == 1 and command.is_int(0):
            result = self.default_result()

            # get dice to dimension
            i = command.list[0]
            get_result = self.dimensions.get(i)
            if not get_result["success"]:
                message = get_result["message"] + "\n"
                result["message"] = message
                return result

            # dimension the dice!
            self.player.dimension_dice(result["item"])

            next_state = AttackState(self.player, 
                self.opponent)
            message = "\n"
            message2 = next_state.intial_message()
            # generate result
            result["nextstate"] = next_state
            result["message"] = message
            result["message2"] = message2

            return result

        # generic commands
        else:
            return super().parse_command(command)

help_text = "\n\n\
Summon commands: \n\
    p as: print available summons \n\
    s   : skip dimension \n\
    #   : dimension dice"
