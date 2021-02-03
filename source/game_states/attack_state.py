from prompt_state import PromptState

class AttackState(PromptState):
    """
    State where player can attack an opponent monster.
    """
    def __init__(self, player, opponent):
        super().__init__(player, opponent)
        self.help_text = self.help_text + help_text

    def run_initial_state(self):
        """
        As initial actions, print player and opponent 
        summons.
        """
        print("Attack phase.")
        print(self.player.name + " summons:")
        print(self.player.stringify_summons())
        print(self.opponent.name + " summons:")
        print(self.opponent.stringify_summons())

    def parse_command(self, command):
        """
        Parse the command obtained from prompt. Return True 
        if player is done with state.
        """
        # finish attack phase command
        if command.equals("f"):
            self.finish =  True

        # attack command
        elif command.len == 2 and command.params_are_int():
            self.run_attack_command(command)
        
        # ML attack command
        elif command.len == 1 and command.params_are_int():
            self.run_ml_attack_command(command)

        # generic commands
        else:
            super().parse_commands(command)

    def run_attack_command(self, command):
        """
        Run command that makes a player monster to attack an
        opponent monster.
        """
        # first get player monster
        result = self.player.get_monster(command.list[0])
        if not result["success"]:
            print(result["message"])
            return

        attacker = result["item"]

        # then get opponent monster
        result = self.opponent.get_monster(command.list[1])
        if not result["success"]:
            print(result["message"])
            return

        attacked = result["item"]
        
        # inform the battle situation
        print(attacker.stringify_prebattle(attacked))

        # then get defense flag
        defense_state = DefenseState(self.opponent)
        defense_state.start()
        defend = defense_state.defend

        # do the attack
        message = attacker.attack_monster(attacked, defend)
        print(message)

        # check if any of the monsters is dead
        message = self.player.check_for_casualties()
        print(message, end="")
        message = self.opponent.check_for_casualties()
        print(message, end="")

def run_attack_ml_command(self, command):
        """
        Run command that makes a player monster to attack the
        opponent monster lord.
        """
        # first get player monster
        result = self.player.get_monster(command.list[0])
        if not result["success"]:
            print(result["message"])
            return

        attacker = result["item"]

        # then check that opponent has no monster left
        if self.opponent.has_monsters():
            print("Cannot attack ML. Opponent still has \
                monsters left.")
            return

        # do the attack
        message = attacker.attack_ml(self.opponent)
        print(message)
        
        # check opponent dm is dead
        self.finish = self.opponent.is_dead()

help_text = "\
Attack commands: \n\
    #1 #2: player's monster #1 attacks opponent \n\
           monster's #2 \n\
    #    : player's monster # attacks opponent \n\
           dungeon master \n\
    f    : finish phase.\n\
"
