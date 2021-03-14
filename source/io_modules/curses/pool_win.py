from boxed_win import BoxedWin

class PoolWin(BoxedWin):
    """
    A window that displays player's dice pool information.
    """
    def __init__(self, parwin, y, x):
        title = "Dice Pool"
        super().__init__(parwin, title, 17, 64, y, x)

    def get_content(self, game_state):
        """
        Get the content to display from the game state.
        """
        return game_state.duel.player.stringify_pool()
