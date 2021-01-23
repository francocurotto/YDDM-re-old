from command import run_prompt

class PromptState():
    """
    Generic game state that initializes a command prompt.
    """
    def start(self):
        """
        Start prompt state.
        """
        while True:
            command = run_prompt()
            finish = self.parse_command(command)
            if finish:
                break
        
    def parse_command(self, command):
        """
        Parse the command obtained from prompt.
        """
        if command.equals("q"):
            print("bye!")
            exit()

        elif command.equals("h"):
            print(self.help_text)
