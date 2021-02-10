from functions import color
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
        print("<ATTACK PHASE> [f: finish]")
        print(self.stringify_state())

    def parse_command(self, command):
        """
        Parse the command obtained from prompt. Return True 
        if command is valid.
        """
        # finish attack phase command
        if command.equals("f"):
            self.finish =  True
            return True

        # attack command
        elif is_attack_command(command):
            self.run_attack_command(command)
            return True
        
        # generic commands
        else:
            return super().parse_command(command)
        
    def run_attack_command(self, command):
        """
        Run command that makes a player monster attack.
        """
        # get monster index
        i0 = command.list[0]

        # get player monster
        result = self.player.prepare_attack(i0)
        if not result["success"]:
            print(result["message"])
            return
        attacker = result["attacker"]
            
        # distinguish between monster attack and ML attack
        if command.len == 2: # monster attack
            # get opponent monster
            i1 = command.list[1]
            result = self.opponent.monster_list.get(i1)
            if not result["success"]:
                print(result["message"])
                return
            attacked = result["item"]
            
            # perform the attack
            self.attack_monster(attacker, attacked)

        else: # command.len == 1 (ML attack)            
            # perform the attack
            self.attack_monster_lord(attacker)

            # check if opponent dm is dead
            if self.opponent.monster_lord.is_dead():
                self.finish = True
                print("")
                print(self.player.name + " is the winner!")
                return

        # print state info
        print("")
        print(self.stringify_state())

    def attack_monster(self, attacker, attacked):
        """
        Make attacker monster attack attacked monster.
        """
        # if everything went okay at this point the attack is
        # confirmed, so decrease the attack crest from player
        self.player.crest_pool.attack -= 1

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
        message = self.player.check_for_casualties()
        if message:
            print(message)
        message = self.opponent.check_for_casualties()
        if message:
            print(message)

    def attack_monster_lord(self, attacker):
        """
        Make attacker monster attack the opponent monster 
        lord.
        """
        # check that opponent has no monster left
        if not self.opponent.monster_list.is_empty():
            print("Cannot attack ML. Opponent still has " +
                "monsters left.")
            return

        # if everything went okay at this point the attack is
        # confirmed, so decrease the attack crest from player
        self.player.crest_pool.attack -= 1

        # do the attack
        message = attacker.attack_ml(self.opponent)
        print(message)

    def stringify_state(self):
        """
        Create a string with relevant information in for the
        state.
        """
        string  = self.player.name + " crests:\n"
        string += self.player.crest_pool.stringify_short()
        string += "\n"
        string += self.player.name + " monsters:\n"
        string += self.player.monster_list.stringify()
        string += "\n\n"
        string += self.opponent.name + " crests:\n"
        string += self.opponent.crest_pool.stringify_short()
        string += "\n"
        string += self.opponent.name + " monsters:\n"
        string += self.opponent.monster_list.stringify()
        return string 

def is_attack_command(command):
    """
    Check if a command is an attack command, either and 
    attack to an opponent monster or to the dungeon master.
    """
    correct_len = 1 <= command.len <= 2
    return correct_len and command.are_params_int()

help_text = "\n\n\
Attack commands: \n\
    #1 #2: player's monster #1 attacks opponent \n\
           monster's #2 \n\
    #    : player's monster # attacks opponent \n\
           dungeon master \n\
    f    : finish phase."
