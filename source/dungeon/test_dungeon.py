import sys
sys.path.append("..")

import settings
settings.print_type = "ascii"
#settings.print_type = "unicode"

from dungeon import Dungeon

dungeon = Dungeon()
print(dungeon.stringify())
