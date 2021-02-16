from command import Command

class CommandPrompt():
    """
    Input Output method based in command prompt.
    """

    def get_command(self):
        """
        Get command by waiting for used test input.
        """
        # get user input
        string = input(">")
            
        # convert input into command
        command = Command(string)
        return command

    def display(self, message):
        """
        Display the message of the game.
        """
        print(message)