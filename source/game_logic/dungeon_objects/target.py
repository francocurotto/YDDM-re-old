from dungeon_object import DungeonObject

class Target(DungeonObject):
    """
    A dungeon object that can be target of an attack (i.e. a
    monster or a monster lord).
    """
    def is_target(self):
        return True   
