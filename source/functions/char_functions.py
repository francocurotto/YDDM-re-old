import curses

def select_chars(chars_ascii, chars_unicode, chars_emoji):
    """
    Select the correct type of chars from the 3 supported 
    ones given the "print _type" set at the settings module.
    User must take care of pasing the the parameters in the
    correct order.
    """
    # weird import here so that the print_type parameter can
    # be changed at runtime
    from settings import print_type

    if print_type == "ascii":
        return chars_ascii
    elif print_type == "unicode":
        return chars_unicode
    elif print_type == "emoji":
        return chars_emoji

def get_print_length(char):
    """
    Get the print length of a char using curses and cursor
    postion to have a more accurate measurement.
    """
    stdscr = curses.initscr()
    pos1 = stdscr.getyx()
    stdscr.addstr(char)
    pos2 = stdscr.getyx()
    curses.endwin()
    return pos2[1] - pos1[1]

def test_chars(print_type):
    """
    Test character display.
    """
    for char_dict in char_list:
        # get char
        if print_type == "unicode":
            char = char_dict["unicode"]
        elif print_type == "emoji":
            char = char_dict["emoji"]

        print_length = get_print_length(char)
        
        line  = char + " "
        line += char_dict["info"].ljust(13)
        line += str(print_length)
        print(line)

char_list = [
    # crests
    {"emoji"   : "⭐",
     "unicode" : "★",
     "info"    : "summon"},
    {"emoji"   : "⬆️ ",
     "unicode" : "⬆",
     "info"    : "movement"},
    {"emoji"   : "⚔️ ",
     "unicode" : "⚔",
     "info"    : "attack"},
    {"emoji"   : "🛡️ ",
     "unicode" : "⊝",
     "info"    : "defense"},
    {"emoji"   : "✡️ ",
     "unicode" : "✡",
     "info"    : "magic"},
    {"emoji"   : "⚡",
     "unicode" : "⊗",
     "info"    : "trap"},
     # summon
    {"emoji"   : "❤️ ",
     "unicode" : "♥",
     "info"    : "life"},
    {"emoji"   : "🧙",
     "unicode" : "S",
     "info"    : "spellcaster"},
    {"emoji"   : "🧟",
     "unicode" : "U",
     "info"    : "undead"},
    {"emoji"   : "🐺",
     "unicode" : "B",
     "info"    : "beast"},
    {"emoji"   : "🥋",
     "unicode" : "W",
     "info"    : "warrior"},
    {"emoji"   : "🐲",
     "unicode" : "D",
     "info"    : "dragon"},
     # monster lord
    {"emoji"   : "👑",
     "unicode" : "♛",
     "info"    : "monster lord"},
    {"emoji"   : "💙",
     "unicode" : "♥",
     "info"    : "heart"},
    {"emoji"   : "🖤",
     "unicode" : "♡",
     "info"    : "no heart"},
     # dungeon
    {"emoji"   : "🔲",
     "unicode" : "[]",
     "info"    : "block"},
    {"emoji"   : "⬛",
     "unicode" : "[]",
     "info"    : "empty tile"},
    {"emoji"   : "🟦",
     "unicode" : "[]",
     "info"    : "blue tile"},
    {"emoji"   : "🟥",
     "unicode" : "[]",
     "info"    : "red tile"}]

if __name__ == "__main__":
    test_chars("emoji")
