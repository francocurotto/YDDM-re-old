from prompt_state import PromptState
from defense_state import DefenseState

class AttackState(PromptState):
    """
    State where player can attack an opponent monster.
    """
    def __init__(self, player, opponent):
        super().__init__(player, opponent)
        self.help_text = self.help_text + help_text

    def run_initial_action(self):
        """
        As initial actions, print player and opponent 
        summons.
        """
        print("Attack phase. [f: finish]")
        print(self.player.name + " monsters:")
        print(self.player.monster_list.stringify())
        print(self.opponent.name + " monsters:")
        print(self.opponent.monster_list.stringify())

    def parse_command(self, command):
        """
        Parse the command obtained from prompt. Return True 
        if command is valid.
        """
        # finish attack phase command
        if command.equals("f"):
            self.finish =  True

        # attack command
        elif command.len == 2 and command.are_params_int():
            self.run_attack_command(command)
        
        # ML attack command
        elif command.len == 1 and command.are_params_int():
            self.run_attack_ml_command(command)

        # generic commands
        else:
            return super().parse_command(command)
        
        # valid command
        return True

    def run_attack_command(self, command):
        """
        Run command that makes a player monster to attack an
        opponent monster.
        """
        # get command indeces
        i0 = command.list[0]
        i1 = command.list[1]

        # first get player monster
        result = self.player.monster_list.get(i0)
        if not result["success"]:
            print(result["message"])
            return
        attacker = result["item"]

        # if monster has already attacked, deny attack
        if attacker.in_cooldown:
            print(attacker.name + " has already attacked.")
            return

        # then get opponent monster
        result = self.opponent.monster_list.get(i1)
        if not result["success"]:
            print(result["message"])
            return
        attacked = result["item"]
        
        # inform the battle situation
        print(attacker.stringify_prebattle(attacked))

        # then get defense flag
        defense_state = DefenseState(self.player, 
            self.opponent)
        defense_state.start()
        defend = defense_state.defend

        # do the attack
        message = attacker.attack_monster(attacked, defend)
        print(message)

        # check if any of the monsters is dead
        message = self.player.check_for_casualities()
        print(message)
        message = self.opponent.check_for_casualities()
        print(message)

    def run_attack_ml_command(self, command):
        """
        Run command that makes a player monster to attack the
        opponent monster lord.
        """
        # get command index
        i = command.list[0]

        # first get player monster
        result = self.player.monster_list.get(i)
        if not result["success"]:
            print(result["message"])
            return
        attacker = result["item"]

        # if monster has already attacked, deny attack
        if attacker.in_cooldown:
            print(attacker.name + " has already attacked.")
            return

        # then check that opponent has no monster left
        if not self.opponent.monster_list.is_empty():
            print("Cannot attack ML. Opponent still has " +
                "monsters left.")
            return

        # do the attack
        message = attacker.attack_ml(self.opponent)
        print(message)
        
        # check opponent dm is dead
        if self.opponent.monster_lord.is_dead():
            self.finished = True
            print(player.name + " is the winner!")

help_text = "\n\n\
Attack commands: \n\
    #1 #2: player's monster #1 attacks opponent \n\
           monster's #2 \n\
    #    : player's monster # attacks opponent \n\
           dungeon master \n\
    f    : finish phase."
