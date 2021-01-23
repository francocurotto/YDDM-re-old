# simple test for command prompt

from command import run_prompt

while True:
    c = run_prompt()

    if c.equals("q"):
        print("bye!")
        exit()

    if c.equals_param(2, "a") and c.is_int(1) and c.len == 3:
        print("MAGIC COMMAND!\n")

    else:
        print(str(c.list)+"\n")
