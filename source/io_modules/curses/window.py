import curses

class Window():
    """
    Generic windown for curses interface.
    """
    def __init__(self, parwin, dy, dx, y, x):
        self.win = parwin.derwin(dy, dx, y, x)

    def addstr(self, win, string):
        """
        Add string to window win line by line to avoid 
        vertical misalignment. It also uses a try/except to 
        avoid stupid curses error when adding char at lower 
        right corner of window.
        """
        str_list = string.split("\n")
        for i, line in enumerate(str_list):
            try:
                win.addstr(i, 0, line)
            except curses.error:
                pass

    def add_win(self, string):
        """
        Add string to main window.
        """
        self.addstr(self.win, string)
