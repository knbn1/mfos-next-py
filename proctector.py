# mfos-next-py proctector sysmodule

from random import randrange
import datetime

def auth():
    a, b = randrange(1, 10, 1), randrange(1, 10, 1)
    try:
        ans = int(input(f"\nSolve the equation to authenticate: {a} + {b} = "))
    except ValueError:
        print("\nInvalid input.")
        print("\nCould not authenticate, operation was cancelled.")
    else:
        if ans == a + b:
            print("\nCorrect!\n")
            with open ("auth.yes", "w") as key:
                print(f"Authenticated: {datetime.datetime.now()}", file=key)
        else:
            print("\nIncorrect answer!\nCould not authenticate, operation cancelled.\n")
