import copy

class DdmList():
    """
    A generic list of item in the game with handy methods
    that communicate results to the classes that use it.
    The result are usually used to indicate if an action was
    successfull or not, by returning a result dictionary.
    """
    def __init__(self, name, itemname, limit=float("inf")):
        self.list = []
        self.name = name
        self.itemname = itemname
        self.limit = limit

    def get(self, i):
        """
        Get item at index i. If index out of range, ignore
        operation and return message.
        """
        result = {}

        # check if index is valid
        if 0 <= i < len(self.list):
            result["item"] = self.list[i]
            result["success"] = True

        # if invalid, operation unsuccessfull
        else:
            result["message"] = "Invalid index."
            result["success"] = False

        return result

    def get_copy(self, i):
        """
        Get a (deep) copy of the item at index i.
        """
        result = self.get(i)
        if not result["success"]:
            return result

        result["item"] = copy.deepcopy(result["item"])

        return result

    def add(self, item):
        """
        Add item to list. If list if full, ignore operation
        and return message.
        """
        result = {}

        # check if list is full
        if not self.is_full():
            self.list.append(item)
            result["success"] = True

        # if full, operation unsuccessfull
        else:
            result["message"] = self.name + " full."
            result["success"] = False

        return result

    def remove(self, item):
        """
        Remove item from list. If item not present, 
        ignore operation and return message.
        """
        # check if item is in list
        if item in self.list:
            i = self.list.index(item)
            return self.remove_idx(i)

        # if not, operation unsuccessfull
        else:
            result = {}
            result["message"] = self.itemname + \
                " not in " + self.name + "."
            result["success"] = False
            return result

    def remove_idx(self, i):
        """
        Remove item at index i. If index out of range, ignore
        operation and return message.
        """
        result = {}

        # check if index is valid
        if 0 <= i < len(self.list):
            dice = self.list[i]
            del(self.list[i])
            result["item"] = dice
            result["success"] = True
        
        # if invalid, operation unsuccessfull
        else:
            result["message"] = "Invalid index."
            result["success"] = False

        return result

    def is_full(self):
        """
        Check if list is full.
        """
        return len(self.list) >= self.limit

    def is_empty(self):
        """
        Check if list is empty.
        """
        return len(self.list) == 0

    def stringify(self):
        """
        Returns a string version of object.
        """
        indeces = range(len(self.list))
        strlist = [self.stringify_short(i) for i in indeces]
        string = "\n".join(strlist)

        return string

    def stringify_short(self, i):
        """
        Return the short string version of item at position i 
        from the DdmList.
        """
        # add summon number
        string = str(i).rjust(3) + ". "
        # add dice short string
        string += self.list[i].stringify_short()

        return string

    def stringify_item(self, i):
        """
        Return the string version of item at position i from 
        the dice library.
        """
        return self.list[i].stringify()

# quick child class too short to have their own file
class MonsterList(DdmList):
    def __init__(self):
        super().__init__("monster list", "monster")
class ItemList(DdmList):
    def __init__(self):
        super().__init__("item list", "item")
class Graveyard(DdmList):
    def __init__(self):
        super().__init__("graveyard", "summon")
