from curses.textpad import Textbox
from boxed_win import BoxedWin
from output_win import OutputWin
from command import Command

class PromptWin(BoxedWin):
    """
    Window that contains that input/output prompt.
    """
    def __init__(self, parwin, y, x):
        title = "Prompt"
        super().__init__(parwin, title, 17, 79, y, x)

        # decorate with prompt indicator
        (y, x) = self.contwin.getmaxyx()
        self.contwin.addstr(y-1, 0, ">")
        self.contwin.refresh()

        # create input window/textbox
        self.inputwin = self.contwin.derwin(1, x-1, y-1, 1)
        self.inputbox = Textbox(self.inputwin)

        # create output window
        self.outwin = OutputWin(self.contwin, y-1, x, 0, 0)

    def get_command(self):
        """
        Get input string from input box, and then turn it
        into a command.
        """
        self.inputbox.edit()
        string = self.inputbox.gather()
        self.inputwin.clear()
        return Command(string)

    def refresh(self, game_state):
        """
        Refresh prompt by showing game state log in output
        window.
        """
        self.outwin.refresh(game_state)
