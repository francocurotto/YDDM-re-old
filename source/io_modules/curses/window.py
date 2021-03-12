import curses

class Window():
    """
    Generic windown for curses interface.
    """
    def __init__(self, parwin, dy, dx, y, x):
        self.win = parwin.derwin(dy, dx, y, x)

    def addstr(self, win, string):
        """
        Add string to window win removeing newlines for nice
        printing in curses windows and avoiding stupid curses
        error when adding char at lower right corner of 
        window.
        """
        string = string.replace("\n", "")
        try:
            win.addstr(string)
        except curses.error:
            pass

    def add_win(self, string):
        """
        Add string to main window.
        """
        self.addstr(self.win, string)
