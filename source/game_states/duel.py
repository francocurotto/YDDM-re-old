import sys
sys.path.append("../dice_collections")
sys.path.append("../ddm_dice")
sys.path.append("../summons")
sys.path.append("../player")
sys.path.append("../command")
from player import Player
from dice_library import DiceLibrary
from roll_state import RollState

class Duel():
    """
    A YDDM duel.
    """
    def __init__(self, player1, player2, library):
        self.players = [player1, player2]
        self.library = library
        self.print_type = print_type

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

            # check win condition
            if self.duel_finished(player):
                break

            # update player index
            i = not i

    def duel_finished(self, player):
        """
        Check finish condition for duel. This can be a win
        condition from a player or a forfit condition.
        """
        if len(player.summons) >= player.summon_limit:
            print(player.name + " is the winner!\n" + \
                "He/She summoned " + \
                str(player.summon_limit) + " monsters/items")
            return True

        return False
        
def get_print_type():
    """
    Get the print type for the game from command line input
    """
    print_types = ["ascii", "unicode", "emoji"]
    if len(sys.argv) >= 2 and sys.argv[1] in print_types:
        return sys.argv[1]
    return "emoji"

if __name__ == "__main__":
    # get print type
    print_type = get_print_type()
    
    # generate dice library
    lib_filename = "../databases/my_database.txt"
    library = DiceLibrary(lib_filename, print_type)

    # generate players
    player1 = Player("Player 1", print_type)
    player2 = Player("Player 2", print_type)

    # fill dice pool of players with random dice
    player1.dice_pool.fill_random(library)
    player2.dice_pool.fill_random(library)
        
    # generate duel
    duel = Duel(player1, player2, library)

    # start duel
    duel.start()
