"""
This script is to translate Magirus database into my own
format (which is actually quite similar). Is alto to detect
possible errors in Magirus database.
"""

def main():
    in_db = "magirus_database.txt"
    out_db = "my_database.txt"

    with open(in_db, "r") as fi, open(out_db, "w") as fo:
        while True:
            # get current line
            try:
                line = next(fi)
            except StopIteration:
                break
        
            # if line is name get the data
            if line.startswith("Name:"):
                # extract the data from magirus database
                data = extract_data(line, fi)
                
                # write the data to my database
                write_data(data, fo)

def extract_data(nameline, fi):
    """
    Extract data from file assuming the name line was read.
    """
    # name
    data = {}
    data["name"] = nameline[6:]
    
    # type
    line = next(fi)
    assert(line.startswith("Type:"))
    data["type"] = line[6:].strip() + "\n"

    # level
    line = next(fi)
    assert(line.startswith("Level:"))
    data["level"] = line[7:]

    # life
    line = next(fi)
    assert(line.startswith("Hearts:"))
    data["life"] = line[8:-1].strip() + "0\n"

    # attack
    line = next(fi)
    assert(line.startswith("Attack:"))
    data["attack"] = line[8:]

    # defense
    line = next(fi)
    assert(line.startswith("Defense:"))
    data["defense"] = line[9:]

    # dice
    line = next(fi)
    assert(line.startswith("Crests:"))
    data["dice"] = translate_dice(line[8:]).strip() + "\n"

    # ability
    line = next(fi)
    assert(line.startswith("Special ability (ies):"))
    data["ability"] = line[23:]
    # get next line if necesary
    line = next(fi)
    if not line.startswith("_ _"):
        data["ability"] = data["ability"][:-1]
        data["ability"] += " " + line

    return data

def translate_dice(string):
    string = string.replace(", ", "")
    string = string.replace("P", "G")
    return string

def write_data(data, fo):
    """
    Write the data extracted from magirus database and write
    it in my own format.
    """
    fo.write("NAME:" + data["name"])
    fo.write("TYPE:" + data["type"])
    fo.write("LEVL:" + data["level"])
    if data["type"] != "Item\n":
        fo.write("ATTK:" + data["attack"])
        fo.write("DEFS:" + data["defense"])
        fo.write("LIFE:" + data["life"])
    fo.write("ABTY:" + data["ability"])
    fo.write("DICE:" + data["dice"])
    fo.write("\n")



if __name__ == "__main__":
    main()

