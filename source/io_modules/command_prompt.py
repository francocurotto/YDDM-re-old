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
        try:
            string = input(">")
        except:
            print("\nbye!")
            exit()
            
        # convert input into command
        command = Command(string)
        return command

    def display(self, log):
        """
        Display the message of the game log.
        """
        print(log.flush(), end="")
