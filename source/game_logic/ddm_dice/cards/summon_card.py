from char_functions import select_chars

class SummonCard():
    """
    Generic summon card class parent of monster and item 
    cards.
    """
    name_crop = 15 # name length limit for short print
    
    def __init__(self, params):
        self.name = params["name"]
        self.level = params["level"]

        self.chars = select_chars(self.chars_ascii, 
            self.chars_unicode, self.chars_emoji)
