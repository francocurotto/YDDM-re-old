from window import Window

class DungeonWin(Window):
    """
    A window that displays the dungeon.
    """
    # dungeon dimensions
    dy = 17
    dx = 46
    def __init__(self, parwin, y, x):
        super().__init__(parwin, self.dy, self.dx, y, x)

    def refresh(self, game_state):
        """
        Refresh the window with the dungeon information.
        """
        content = game_state.duel.dungeon.stringify()
        self.add_win(content)
        self.win.refresh()
