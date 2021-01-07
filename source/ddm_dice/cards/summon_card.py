class SummonCard():
    """
    Generic summon card class parent of monster and item 
    cards.
    """
    name_crop = 15 # name length limit for short print
    
    def __init__(self, params):
        self.name = params["name"]
        self.level = params["level"]

        self.chars_ascii   = {}
        self.chars_unicode = {}
        self.chars_emoji   = {}
        self.print_type = params["print_type"]

        self.chars = self.select_chars()

    def select_chars(self):
        """
        Select the type of characters that will be used when
        printing card information.
        """
        if self.print_type == "ascii":
            return self.chars_ascii
        elif self.print_type == "unicode":
            return self.chars_unicode
        elif self.print_type == "emoji":
            return self.chars_emoji
