from window import Window

class OutputWin(Window):
    """
    Class that contains the output part of the prompt window.
    """
    def __init__(self, parwin, dy, dx, y, x):
        super().__init__(parwin, dy, dx, y, x)
        # create output buffer
        self.outbuffer = ["" for _ in range(dy)]
        self.width_lim = dx

    def refresh(self, game_state):
        """
        Refresh output by flushing log from game state.
        """
        string = game_state.log.flush()
        self.update_buffer(string)
        self.add_win("\n".join(self.outbuffer))
        super().refresh()

    def update_buffer(self, string):
        """
        Fill output buffer with string displacing prevous
        text in a queue like manner.
        """
        lines = string.split("\n")
        for line in lines:
            if line != "":
                # remove las line
                self.outbuffer.pop(0)
                # add new line
                self.outbuffer.append(line)


