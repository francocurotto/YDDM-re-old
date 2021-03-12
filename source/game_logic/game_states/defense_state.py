from duel_substate import DuelSubstate

class DefenseState(DuelSubstate):
    """
    State where the opponent is asked if he wants to defend
    from the player attack.
    """
    def __init__(self, duel, log):
        super().__init__(duel, log)
        self.tile_i = None
        self.tile_f = None
        self.help_text = self.help_text + help_text

    def restart(self):
        """
        Restart state.
        """
        # reset next state
        self.next_state = self

        # set start message
        self.start_message  = self.duel.opponent.name
        self.start_message += ", do you want to defend the "
        self.start_message += "attack? [y/n]\n\n"

    def update(self, command):
        """
        Update state given command.
        """
        # defense command
        if command.equals("y") or command.equals("n"):
            self.run_defense_command(command)

        # generic commands
        else:
            super().update(command)

    def run_defense_command(self, command):
        """
        Run command were a desition between defending or not
        was taken.
        """
        # get monsters
        attacker = self.tile_i.content
        attacked = self.tile_f.content

        # opponent defends
        if command.equals("y"):
            self.duel.opponent.crest_pool.defense -= 1
            attacker.attack_monster(attacked, defending=True)

        # opponent does not defend
        elif command.equals("n"):
            attacker.attack_monster(attacked,defending=False)

        # check if any of the monsters is dead
        self.duel.player.check_for_death(self.tile_i)
        self.duel.opponent.check_for_death(self.tile_f)
        self.log.add("\n")

        # define next state
        self.next_state = self.dun_state
        self.next_state.restart()

    def get_params(self, dun_state):
        """
        Get necessary parameters from previous dungeon state.
        """
        self.tile_i = dun_state.tile_i
        self.tile_f = dun_state.tile_f

help_text = "\
Defense commands: \n\
    y: defend from player attack.\n\
    n: do not defend from player attack."
