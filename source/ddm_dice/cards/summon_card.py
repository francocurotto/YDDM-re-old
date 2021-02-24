import sys
sys.path.append("..")

class SummonCard():
    """
    Generic summon card class parent of monster and item 
    cards.
    """
    name_crop = 15 # name length limit for short print
    
    def __init__(self, params):
        self.name = params["name"]
        self.level = params["level"]

        self.chars = self.select_chars()

    def select_chars(self):
        """
        Select the type of characters that will be used when
        printing card information.
        """
        # weird import here so that the print_type parameter
        # can be changed at runtime
        from settings import print_type
        
        if print_type == "ascii":
            return self.chars_ascii
        elif print_type == "unicode":
            return self.chars_unicode
        elif print_type == "emoji":
            return self.chars_emoji
