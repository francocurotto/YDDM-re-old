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
        self.print_type = params["print_type"]

        self.chars = self.select_chars()

    def select_chars(self):
        """
        Select the type of characters that will be used when
        printing summon information.
        """
        if self.print_type == "ascii":
            return self.chars_ascii
        elif self.print_type == "unicode":
            return self.chars_unicode
        elif self.print_type == "emoji":
            return self.chars_emoji
