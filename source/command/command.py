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
        return self.list == argv

    def is_int(self, i):
        """
        Check if command item at position i is int.
        """
        return isinstance(self.get_param(i), int)

    def is_empty(self):
        """
        Return True if command list is empty.
        """
        return len(self.list) == 0

    def subcommand(self, i):
        """
        Creates a new command that is a subset of command,
        with parameters starting at i from old command.
        """
        new_params = self.list[i:]
        return Command(" ".join(map(str, new_params)))

def run_prompt():
    """
    Run a command prompt were a player can input a command 
    as string and it is converted into a Command object.
    """
    # get user input
    string = input(">")
        
    # convert input into command
    command = Command(string)
    return command
