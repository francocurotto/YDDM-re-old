import settings
from player import Player
from dice_list import DiceList
from roll_state import RollState
from attack_state import AttackState

class Duel_State():
    """
    A YDDM duel state.
    """
    def __init__(self):
        self.player1, self.player2 = random_init()
        self.players = [self.player1, self.player2]
        self.state = RollState(self.player1, self.player2)

    def initial_message(self):
        """
        As initial message: duel started message.
        """
        message  = "Duel Started!\n" + \
             self.state.initial_message()
        return message

    def update(self, command):
        """
        Update state given command. Return result dictionary
        with the necessary information for parent state.
        """
        # update state
        result = self.state.update(command)

        # check if winning condition is met
        result = self.check_finished(result)

        # if duel finished, early return
        if result["finished"]:
            return result

        # get state transition message and change state
        result["message"] += result["message2"]
        self.state = result["nextstate"]

        return result

    def check_finished(self, result):
        """
        Check finish condition for duel. This can be a win
        condition from a player or a forfit condition.
        Fill result dictionary with the results of the check.
        """
        for player in self.players:
            # Forfeit condition
            if player.forfeited:
                result["finished"] = True
                result["message"] += player.name + \
                    " forfeited."
                return result

            # normal win condition (monster lord beaten)
            if player.monster_lord.is_dead():
                opponent = self.get_opponent(player)
                result["finished"] = True
                result["message"] = +"\n" + opponent.name + \
                    " is the winner!\n" + \
                    "Broke all opponent's hearts."
                return result

        # default duel hasn't finished
        result["finished"] = False
        return result

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
    lib_filename = "../databases/my_database.txt"
    library = DiceList()
    library.fill_from_file(lib_filename)

    # generate players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # fill dice pool of players with random dice
    player1.dice_pool.fill_random(library)
    player2.dice_pool.fill_random(library)
        
    return player1, player2
