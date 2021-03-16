from window import Window

class BoxedWin(Window):
    """
    A window that has a box border and a title.
    """
    def __init__(self, parwin, title, dy, dx, y, x):
        super().__init__(parwin, dy, dx, y, x)
        
        # decorate window
        self.win.border()
        self.win.addstr(0, 2, title)
        self.win.noutrefresh()

        # create content window
        self.contwin = self.win.derwin(dy-2, dx-2, 1, 1)

    def refresh(self, game_state):
        """
        refresh the content of the window.
        """
        content = self.get_content(game_state)
        self.add_contwin(content)
        self.contwin.noutrefresh()

    def add_contwin(self, content):
        """
        Add content to content window.
        """
        self.addstr(self.contwin, content)
