from boxed_win import BoxedWin

class OpponentCrestWin(BoxedWin):
    """
    A window that displays opponent's crest pool information.
    """
    def __init__(self, parwin, y, x):
        title = "Opponent's Crest Pool"
        super().__init__(parwin, title, 3, 31, y, x)

    def get_content(self, game_state):
        """
        Get the content to display from the game state.
        """
        crest_pool = game_state.duel.opponent.crest_pool
        return crest_pool.stringify_short()
