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

    def get_item(self, i):
        """
        Get item from command at position i. Return None if
        index is out of range.
        """
        try:
            return self.list[i]
        except IndexError:
            return None

    def is_equal(self, value, i=0):
        """
        Check if command item at position i is equal to input
        value. By default check first item.
        """
        return self.get_item(i) == value

    def is_int(self, i):
        """
        Check if command item at position i is int.
        """
        return isinstance(self.get_item(i), int)

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
