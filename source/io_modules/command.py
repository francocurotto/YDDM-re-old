class Command():
    """
    A command input from a player, parsed for better usage.
    """
    def __init__(self, string):
        # split command by spaces
        self.list = string.split()
        self.len = len(self.list)

        # if input represents an int, convert into int
        for i, item in enumerate(self.list):
            try:
                self.list[i] = int(item)
            except ValueError:
                pass

    def get_param(self, i):
        """
        Get parameter from command at position i. Return None 
        if index is out of range.
        """
        try:
            return self.list[i]
        except IndexError:
            return None

    def equals_param(self, i, value):
        """
        Check if command parameter at position i is equal to 
        input value.
        """
        return self.get_param(i) == value

    def equals(self, *argv):
        """
        Check if inputs are all equals and in the same order
        than command parameters.
        """
        return self.list == list(argv)

    def is_int(self, i):
        """
        Check if command item at position i is int.
        """
        return isinstance(self.get_param(i), int)

    def are_params_int(self):    
        """
        Check if all the parameters in the command are ints.
        Empty command is considered invalid.
        """
        # check empty list
        if self.is_empty():
            return False

        for param in self.list:
            if not isinstance(param, int):
                return False

        return True

    def is_empty(self):
        """
        Return True if command list is empty.
        """
        return len(self.list) == 0

    def subcommand(self, start, end=None):
        """
        Creates a new command that is a subset of command,
        with parameters starting at start and ending at end
        (default till last param) of the param list.
        """
        # if end is not defined, command list end
        if end is None:
            end = self.len

        # get new parameter list
        new_params = self.list[start:end]
        return Command(" ".join(map(str, new_params)))
