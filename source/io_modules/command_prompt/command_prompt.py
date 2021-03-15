from command import Command

class CommandPrompt():
    """
    Input/output method based in command prompt.
    """
    def __init__(self, name):
        self.name = name

    def get_command(self):
        """
        Get command by waiting for used test input.
        """
        # get user input
        try:
            string = input(">")
        except:
            print("\nbye!")
            exit()
            
        # convert input into command
        command = Command(string)
        return command

    def display(self, game_state):
        """
        Display the message of the game log.
        """
        print(game_state.log.flush(), end="")

    def terminate(self):
        """
        Terminate the IO.
        """
        pass
