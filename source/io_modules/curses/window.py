import curses
from ansi_translator import ANSITranslator

class Window():
    """
    Generic windown for curses interface.
    """
    def __init__(self, parwin, dy, dx, y, x):
        try:
            self.win = parwin.derwin(dy, dx, y, x)
        except curses.error:
            curses.echo()
            curses.endwin()
            print("Curses error. Probably because the " + \
                "window was too small to play the game.")
            exit()
        self.translator = ANSITranslator()

    def addstr(self, win, string):
        """
        Add string to window win line by line to avoid 
        vertical misalignment. It also uses a try/except to 
        avoid stupid curses error when adding char at lower 
        right corner of window.
        """
        str_list = string.split("\n")
        for i, line in enumerate(str_list):
            # move cursor to the start of the line
            win.move(i,0)
            
            # get curses color from ANSI escape characters
            ctuple_list = self.translator.get_ctuples(line)
            for ctuple in ctuple_list:
                # try/except to bypass stupid curses error
                try:
                    win.addstr(ctuple[0], ctuple[1])
                except curses.error:
                    pass

    def add_win(self, string):
        """
        Add string to main window.
        """
        self.win.clear()
        self.addstr(self.win, string)

    def refresh(self):
        """
        Refresh window.
        """
        self.win.noutrefresh()
