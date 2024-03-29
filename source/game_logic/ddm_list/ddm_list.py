import copy

class DdmList():
    """
    A generic list of item in the game with handy methods
    that communicate results to the classes that use it.
    The result are usually used to indicate if an action was
    successfull or not, by returning a boolean or item in 
    list.
    """
    def __init__(self, name, itemname, log,   
        limit=float("inf")):

        self.list = []
        self.name = name
        self.itemname = itemname
        self.log = log
        self.limit = limit
        
    def get(self, i):
        """
        Get item at index i. If index out of range, ignore
        operation and return None.
        """
        # distinguish between int and user command
        i = sanitize_int(i)

        # check if index is valid
        if 0 <= i < len(self.list):
            return self.list[i]

        # if invalid return none
        self.log.add("Invalid index.\n")
        return None

    def get_copy(self, i):
        """
        Get a (deep) copy of the item at index i.
        """
        return copy.deepcopy(self.get(i))

    def add(self, item):
        """
        Add item to list. If list if full, return false.
        """
        # check if list is full
        if not self.is_full():
            self.message = ""
            self.list.append(item)
            return True

        # if full, operation unsuccessfull
        self.log.add(self.name + " full.\n")
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
        self.log.add(self.itemname + " not in " + self.name + 
            ".")
        return None

    def remove_idx(self, i):
        """
        Remove item at index i. If index out of range, return 
        none and update message.
        """
        # distinguish between int and user command
        i = sanitize_int(i)

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
        # get the digit lendth of list
        jlength = len(str(len(self.list)))
        # add summon number, convert to 1-indexing
        string = str(i+1).rjust(jlength) + ". "
        # add dice short string
        string += self.list[i].stringify_short()

        return string

    def stringify_item(self, i):
        """
        Return the string version of item at position i from 
        the dice library.
        """
        return self.list[i].stringify()

def sanitize_int(i):
    """
    Distinguish between int object and string representing an
    int. If string, it is assumed that it comes from an user
    input, therefore it must be corrected for 0-indexing.
    """
    # case int
    if isinstance(i, int):
        return i

    # case string
    return int(i) - 1

# quick child class too short to have their own file
class ItemList(DdmList):
    def __init__(self, log):
        super().__init__("item list", "item", log)
class Graveyard(DdmList):
    def __init__(self, log):
        super().__init__("graveyard", "summon", log)
