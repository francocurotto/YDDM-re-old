import sys
sys.path.append("..")
sys.path.append("../ddm_list")
sys.path.append("../ddm_dice")
sys.path.append("../summons")
sys.path.append("../player")
sys.path.append("../command")
import settings
from player import Player
from dice_list import DiceList
from roll_state import RollState
from attack_state import AttackState

class Duel():
    """
    A YDDM duel.
    """
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.first_turn = True

    def start(self):
        """
        Start duel loop.
        """
        i = False # current player index

        # duel loop
        while True:
            # sort out current and opponent player
            player   = self.players[i]
            opponent = self.players[not i]
            print(player.name + " turn.")

            # run roll state
            RollState(player, opponent).start()

            # check finish condition
            if self.duel_finished(player, opponent):
                break

            # run roll state (skip in first turn)
            if not self.first_turn:
                AttackState(player, opponent).start()

            # check finish condition
            if self.duel_finished(player, opponent):
                break

            # after first iteration, no longer in first turn
            self.first_turn = False

            # decooldown player monsters
            player.decooldown_monsters()

            # update player index
            i = not i

    def duel_finished(self, player, opponent):
        """
        Check finish condition for duel. This can be a win
        condition from a player or a forfit condition.
        """
        # Forfeit condition
        if player.forfeited:
            return True

        # normal win condition (monster lord beaten)
        if opponent.monster_lord.is_dead():
            return True

        return False
        
def set_print_type():
    """
    Set the print type for the game from command line input.
    If not given or invalid, use default
    """
    print_types = ["ascii", "unicode", "emoji"]
    if len(sys.argv) >= 2 and sys.argv[1] in print_types:
        settings.print_type = sys.argv[1]

if __name__ == "__main__":
    # set print type if given as cmdline input
    set_print_type()
    
    # generate dice library
    lib_filename = "../databases/my_database.txt"
    library = DiceList()
    library.fill_from_file(lib_filename)

    # generate players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # fill dice pool of players with random dice
    player1.dice_pool.fill_random(library)
    player2.dice_pool.fill_random(library)
        
    # generate duel
    duel = Duel(player1, player2)

    # start duel
    duel.start()
