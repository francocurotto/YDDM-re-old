# simple test for command prompt

from command import run_prompt

while True:
    c = run_prompt()

    if c.is_equal("q"):
        print("bye!")
        exit()

    if c.is_equal("a", 2) and c.is_int(1) and c.len == 3:
        print("MAGIC COMMAND!\n")

    else:
        print(str(c.list)+"\n")
