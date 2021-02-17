import copy

class DdmList():
    """
    A generic list of item in the game with handy methods
    that communicate results to the classes that use it.
    The result are usually used to indicate if an action was
    successfull or not, by returning a boolean or item in 
    list.
    """
    def __init__(self, name, itemname, limit=float("inf")):
        self.list = []
        self.name = name
        self.itemname = itemname
        self.limit = limit
        self.message = ""

    def get(self, i):
        """
        Get item at index i. If index out of range, ignore
        operation and return None and update message.
        """
        # check if index is valid
        if 0 <= i < len(self.list):
            self.message = ""
            return self.list[i]

        # if invalid return none
        self.message = "Invalid index."
        return None

    def get_copy(self, i):
        """
        Get a (deep) copy of the item at index i.
        """
        return copy.deepcopy(self.get(i))

    def add(self, item):
        """
        Add item to list. If list if full, return false and 
        update message.
        """
        # check if list is full
        if not self.is_full():
            self.message = ""
            self.list.append(item)
            return True

        # if full, operation unsuccessfull
        self.message = self.name + " full."
        return False

    def remove(self, item):
        """
        Remove item from list. If item not present, return 
        none and update message.
        """
        # check if item is in list
        if item in self.list:
            self.message = ""
            i = self.list.index(item)
            return self.remove_idx(i)

        # if not, operation unsuccessfull
        self.message = self.itemname + " not in " + \
            self.name + "."
        return None

    def remove_idx(self, i):
        """
        Remove item at index i. If index out of range, return 
        none and update message.
        """
        # get item to remove
        item = self.get(i)

        # if item found, remove item
        if item:
            del(self.list[i])

        # return item
        return item

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
class ItemList(DdmList):
    def __init__(self):
        super().__init__("item list", "item")
class Graveyard(DdmList):
    def __init__(self):
        super().__init__("graveyard", "summon")
