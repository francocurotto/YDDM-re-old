class Summon():
    """
    Generic summon class parent of monsters and items.
    """
    def __init__(self, params):
        self.name = params["name"]
        self.level = params["level"]

        self.name_crop = 15
        self.chars_ascii   = {}
        self.chars_unicode = {}
        self.chars_emoji   = {}
        self.print_type = 1 # 1: print as ascii
                            # 2: print as unicode
                            # 3: print as emoji

        self.chars = self.select_chars()

    def select_chars(self):
        """
        Select the type of characters that will be used when
        printing summon information.
        """
        if self.print_type == 1:
            return self.chars_ascii
        elif self.print_type == 2:
            return self.chars_unicode
        elif self.print_type == 3:
            return self.chars_emoji
