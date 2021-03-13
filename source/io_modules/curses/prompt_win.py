from curses.textpad import Textbox
from boxed_win import BoxedWin
from window import Window
from command import Command

class PromptWin(BoxedWin):
    """
    Window that contains that input/output prompt.
    """
    def __init__(self, parwin, y, x):
        title = "Prompt"
        super().__init__(parwin, title, 16, 79, y, x)

        # decorate with prompt indicator
        self.add_contwin(">")
        self.contwin.refresh()

        # create input window/textbox
        (y, x) = self.contwin.getmaxyx()
        self.inputwin = self.contwin.derwin(1, x-1, 0, 1)
        self.inputbox = Textbox(self.inputwin)

        # create output window
        self.outputwin = Window(self.contwin, y-1, x, 1, 0)

    def get_command(self):
        """
        Get input string from input box, and then turn it
        into a command.
        """
        self.inputbox.edit()
        string = self.inputbox.gather()
        return Command(string)

    def refresh(self, game_state):
        """
        Refresh prompt by showing game state log in output
        window.
        """
        self.outputwin.win.clear()
        self.outputwin.add_win(game_state.log.flush())
        self.outputwin.win.refresh()
