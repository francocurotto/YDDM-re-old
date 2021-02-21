class Logger():
    """
    Log informations of the game, so that later it can be 
    printed.
    """
    def __init__(self):
        self.log = ""

    def add(self, string):
        """
        Add string to log.
        """
        self.log += string

    def flush(self):
        """
        Return log and clear. 
        """
        logtemp = self.log
        self.log = ""
        return logtemp
