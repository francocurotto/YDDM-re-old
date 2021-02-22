from duel_substate import DuelSubstate

class DimensionState(DuelSubstate):
    """
    State when player dimension a dice and summon a 
    monster/item after a roll.
    """
    def __init__(self, duel, log):
        super().__init__(duel, log)
        self.help_text = self.help_text + help_text

    def set_start_message(self):
        """
        As start message show available dimensions.
        """
        self.start_message  = "Available summons:\n"
        self.start_message += \
            self.dimensions.stringify() + "\n"
        self.start_message += \
            "Select with number [s: skip].\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # default values for update
        self.next_state = self

        # print available summons command
        if command.equals("p", "as"):
            self.log.add(self.dimensions.stringify())
            self.log.add("\n\n")

        # skip dimension and go to next state
        elif command.equals("s"):
            self.log.add("\n")
            self.next_state = self.atk_state
            self.next_state.set_new_start_message()

        # dice dimension
        elif command.len == 1 and command.is_int(0):
            # get dice to dimension
            i = command.list[0]
            dice = self.dimensions.get(i)
            if not dice:
                self.log.add("\n")
                return

            # dimension the dice!
            self.duel.player.dimension_dice(dice)

            # define next state
            self.log.add("DIMENSION THE DICE!\n\n")
            self.next_state = self.atk_state
            self.next_state.set_new_start_message()

        # generic commands
        else:
            super().update(command)

help_text = "\n\n\
Dimension commands: \n\
    p as: print available summons \n\
    s   : skip dimension \n\
    #   : dimension dice"
