import copy
from player import Player
from dice_list import DiceList

class Duel():
    """
    A duel were player are playing YDDM.
    """
    def __init__(self):
        # For now, creates players with random pools
        self.player1, self.player2 = random_init()
        self.players = [self.player1, self.player2]

        # define current player and opponent
        self.player = self.players[0]
        self.opponent = self.players[1]
        self.turn = 1
        
        self.message = ""

    def next_turn_copy(self):
        """
        Returns a copy of the duel but at one turn in 
        advance.
        """
        next_turn_duel = copy.deepcopy(self)
        next_turn_duel.advance_turn()
        return next_turn_duel

    def advance_turn(self):
        """
        Update the duel as if a turn has finished.
        """
        self.turn += 1
        
        # lame temp variable for swap
        temp = self.opponent
        self.opponent = self.player
        self.player = temp

    def finished(self):
        """
        Check finish condition for duel. This can be a win
        condition from a player or a forfeit condition.
        """
        for player in self.players:
            # Forfeit condition
            if player.forfeited:
                self.message += player.name + " forfeited.\n"
                return True

            # normal win condition (monster lord beaten)
            if player.monster_lord.is_dead():
                opponent = self.get_opponent(player)
                self.message += opponent.name + \
                    " is the winner!\n" + \
                    "Broke all opponent's hearts.\n"
                return True

        return False

    def check_for_casualties(self):
        """
        Check if any of the players has a monster that has
        died.
        """
        self.duel.player.check_for_casualties(self)
        self.duel.message = self.player.message
        self.duel.opponent.check_for_casualties(self)
        self.duel.message = self.opponent.message

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
