import curses
from pool_win import PoolWin
from player_crest_win import PlayerCrestWin
from opponent_crest_win import OpponentCrestWin
from dungeon_win import DungeonWin

class CursesIO():
    """
    Input/output method based in curses library.
    """
    def __init__(self):
        # do all the curses preamble
        self.stdscr = curses.initscr()
        #curses.start_color() # necessary for colors?
        curses.noecho()
        curses.cbreak() # necessary in this mode?
        self.stdscr.keypad(True)
        curses.curs_set(0)

        # initial refresh with title
        self.stdscr.addstr(0, 56, "YDDM-re")
        self.stdscr.refresh()

        # define initial windows
        self.poolwin = PoolWin(self.stdscr, 1, 0)
        self.pcrestwin = PlayerCrestWin(self.stdscr, 18, 0)
        self.ocrestwin = OpponentCrestWin(self.stdscr, 21, 0)
        self.dungeonwin = DungeonWin(self.stdscr, 1, 65)

        # group all windows
        self.winlist = [self.poolwin, self.pcrestwin,
            self.ocrestwin, self.dungeonwin]

    def display(self, game_state):
        """
        Display game given current game status.
        """
        # refresh all the windows in the game
        for win in self.winlist:
            win.refresh(game_state)

    def terminate(self):
        """
        Terminate the IO.
        """
        input("")
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.curs_set(1)
