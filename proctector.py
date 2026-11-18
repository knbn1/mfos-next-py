# mfos-next-py proctector sysmodule

import random

def auth():
    a = random.randrange(1, 10, 1)
    b = random.randrange(1, 10, 1)
    try:
        ans = int(input(f"Solve the equation to authenticate: {a} + {b} = "))
    except ValueError:
        print("\nInvalid input.")
    else:
        if ans == a + b:
            print("\nCorrect!")
            auth = True
        else:
            print("\nIncorrect!")
            auth = False
