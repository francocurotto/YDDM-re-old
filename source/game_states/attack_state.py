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
            return True

        # attack command
        elif command.len == 2 and command.params_are_int():
            self.run_attack_command(command)
            return False
        
        # DM attack command
        elif command.len == 1 and command.params_are_int():
            return self.run_dm_attack_command(command)

        # generic commands
        return super().parse_commands(command)

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
        attacker = result["monster"]

        # then get opponent monster
        result = self.opponent.get_monster(command.list[1])
        if not result["success"]:
            print(result["message"])
            return
        attacked = result["monster"]

        # then get defense flag
        defense_state = DefenseState(self.player, 
            self.opponent, attacker, attacked)
        defend = defense_state.get_answer()

        # do the attack
        result = self.player.attack(attacker, attacked, 
            defend)
        print(result["message"])

def run_attack_dm_command(self, command):
        """
        Run command that makes a player monster to attack the
        opponent dungeon master.
        """
        # first get player monster
        result = self.player.get_monster(command.list[0])
        if not result["success"]:
            print(result["message"])
            return
        attacker = result["monster"]

        # then check that opponent has no monster left
        if self.opponent.has_monsters():
            print("Cannot attack DM. Opponent still has \
                monsters left.")
            return

        # do the attack
        result = self.player.attack_dm(attacker, 
            self.opponent)
        print(result["message"])
        
        # check opponent dm is dead
        return self.opponent.is_dead()

help_text = "\
Attack commands: \n\
    #1 #2: player's monster #1 attacks opponent \n\
           monster's #2 \n\
    #    : player's monster # attacks opponent \n\
           dungeon master \n\
    f    : finish phase.
"
