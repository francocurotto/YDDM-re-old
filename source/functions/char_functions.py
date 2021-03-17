import curses
from color_functions import color_fg, grayout

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
    stdscr.move(0,0)
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
        if print_type == "ascii":
             char = char_dict["ascii"]
        elif print_type == "unicode":
            char = char_dict["unicode"]
        elif print_type == "emoji":
            char = char_dict["emoji"]

        print_length = get_print_length(char)
        
        line = char + "\t"
        line += char_dict["info"].ljust(13)
        line += str(print_length)
        print(line)

char_list = [
    # crests
    {"emoji"   : "⭐",
     "unicode" : "★",
     "ascii"   : "S",
     "info"    : "summon"},
    {"emoji"   : "⬆️ ",
     "unicode" : "⬆",
     "ascii"   : "M",
     "info"    : "movement"},
    {"emoji"   : "⚔️ ",
     "unicode" : "⚔",
     "ascii"   : "A",
     "info"    : "attack"},
    {"emoji"   : "🛡️ ",
     "unicode" : "⊝",
     "ascii"   : "D",
     "info"    : "defense"},
    {"emoji"   : "✡️ ",
     "unicode" : "✡",
     "ascii"   : "G",
     "info"    : "magic"},
    {"emoji"   : "⚡",
     "unicode" : "⊗",
     "ascii"   : "T",
     "info"    : "trap"},
     # summon
    {"emoji"   : "❤️ ",
     "unicode" : "♥",
     "ascii"   : "L",
     "info"    : "life"},
    {"emoji"   : "🧙",
     "unicode" : "S",
     "ascii"   : "S",
     "info"    : "spellcaster"},
    {"emoji"   : "🧟",
     "unicode" : "U",
     "ascii"   : "U",
     "info"    : "undead"},
    {"emoji"   : "🐺",
     "unicode" : "B",
     "ascii"   : "B",
     "info"    : "beast"},
    {"emoji"   : "🥋",
     "unicode" : "W",
     "ascii"   : "W",
     "info"    : "warrior"},
    {"emoji"   : "🐲",
     "unicode" : "D",
     "ascii"   : "D",
     "info"    : "dragon"},
     # monster lord
    {"emoji"   : "👑",
     "unicode" : "♛",
     "ascii"   : "ML",
     "info"    : "monster lord"},
    {"emoji"   : "💙",
     "unicode" : "♥",
     "ascii"   : "<3",
     "info"    : "heart"},
    {"emoji"   : "🖤",
     "unicode" : "♡",
     "ascii"   : grayout("<3"),
     "info"    : "no heart"},
     # dungeon
    {"emoji"   : "🔲",
     "unicode" : "[]",
     "ascii"   : "[]",
     "info"    : "block"},
    {"emoji"   : "⬛",
     "unicode" : grayout("[]"),
     "ascii"   : grayout("[]"),
     "info"    : "empty tile"},
    {"emoji"   : "🟦",
     "unicode" : color_fg("[]", "blue"),
     "ascii"   : color_fg("[]", "blue"),
     "info"    : "blue tile"},
    {"emoji"   : "🟥",
     "unicode" : color_fg("[]", "red"),
     "ascii"   : color_fg("[]", "red"),
     "info"    : "red tile"}]

if __name__ == "__main__":
    test_chars("emoji")
