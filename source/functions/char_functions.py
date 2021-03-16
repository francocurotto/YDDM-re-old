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

def test_print_length():
    """
    Test the get_print_length function for various emoji 
    characters.
    """
    dice_chars    = ["⭐", "⬆️", "⚔️", "🛡️", "✡️", "⚡"]
    summon_chars  = ["❤️", "🧙", "🧟", "🐺", "🥋", "🐲"]
    ml_chars      = ["👑", "💙", "🖤"]
    dungeon_chars = ["🔲", "⬛", "🟦", "🟥"]
    chars = dice_chars + summon_chars + ml_chars + \
        dungeon_chars
    for char in chars:
        print(char + ":" + str(get_print_length(char)))

if __name__ == "__main__":
    test_print_length()
