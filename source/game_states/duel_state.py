import settings
from player import Player
from dice_list import DiceList
from roll_state import RollState
#from attack_state import AttackState

class DuelState():
    """
    A YDDM duel state.
    """
    def __init__(self):
        self.player1, self.player2 = random_init()
        self.players = [self.player1, self.player2]
        self.state = RollState(self.player1, self.player2)
        self.initial_message()
        self.finished = False

    def initial_message(self):
        """
        As initial message: duel started message.
        """
        self.state.set_initial_message()
        self.message  = "GAME ON!\n"
        self.message += self.state.message

    def update(self, command):
        """
        Update state given command.
        """
        # update state
        self.state.update(command)
        self.message = self.state.message

        # check if winning condition is met
        # if duel finished, early return
        self.check_finished()
        if self.finished:
            return

        # change states and get message from new state
        self.state = self.state.next_state
        self.message += self.state.message

    def check_finished(self):
        """
        Check finish condition for duel. This can be a win
        condition from a player or a forfeit condition.
        """
        for player in self.players:
            # Forfeit condition
            if player.forfeited:
                self.finished = True
                self.message += player.name + " forfeited.\n"

            # normal win condition (monster lord beaten)
            if player.monster_lord.is_dead():
                opponent = self.get_opponent(player)
                self.finished = True
                self.message += opponent.name + \
                    " is the winner!\n" + \
                    "Broke all opponent's hearts.\n"

    def get_opponent(self, player):
        """
        Get opponent of player.
        """
        return (set(self.players) - set(player)).pop()
        
def random_init():
    """
    Helper function to initialize a duel with two players 
    with random dice pools.
    """
    # generate dice library
    lib_filename = "databases/my_database.txt"
    library = DiceList()
    library.fill_from_file(lib_filename)

    # generate players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # fill dice pool of players with random dice
    player1.dice_pool.fill_random(library)
    player2.dice_pool.fill_random(library)
        
    return player1, player2
