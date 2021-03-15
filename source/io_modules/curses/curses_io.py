import curses
from pool_win import PoolWin
from player_crest_win import PlayerCrestWin
from opponent_crest_win import OpponentCrestWin
from dungeon_win import DungeonWin
from prompt_win import PromptWin

class CursesIO():
    """
    Input/output method based in curses library.
    """
    def __init__(self, name):
        self.name = name

        # do all the curses preamble
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak() # necessary in this mode?
        self.stdscr.keypad(True)
        #curses.curs_set(False)
        curses.start_color()

        # initial refresh with title
        self.stdscr.addstr(0, 56, "YDDM-re")
        self.stdscr.refresh()

        # define initial windows
        self.poolwin = PoolWin(self.stdscr, 1, 0)
        self.pcrestwin = PlayerCrestWin(self.stdscr, 18, 0)
        self.ocrestwin = OpponentCrestWin(self.stdscr, 21, 0)
        self.dungeonwin = DungeonWin(self.stdscr, 1, 65)
        self.promptwin = PromptWin(self.stdscr, 18, 32)

        # group all windows
        self.winlist = [self.poolwin, self.pcrestwin,
            self.ocrestwin, self.dungeonwin, self.promptwin]

    def get_command(self):
        """
        Get commmand from prompt.
        """
        return self.promptwin.get_command()

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
        self.stdscr.getkey()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        #curses.curs_set(True)
        curses.endwin()
