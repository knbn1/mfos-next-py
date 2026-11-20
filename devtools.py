# mfos-next-py debug tools

import devtools
import os
from proctector import auth

def tryauth():
    print("Triggering authentication process...")
    try:
        if os.path.exists("auth.yes"):
            os.remove("auth.yes")
        auth()
        if os.path.exists("auth.yes"):
            print("Authentication successful.")
            os.remove("auth.yes")
        else:
            print("Failed to authenticate.")
    except FileNotFoundError:
        print("Proctector module not found!")

def gencmd():
    out = input("Output file (default: commands.txt): ")
    print("")
    try:
        import cmdgen
        if os.path.exists("auth.yes"):
            os.remove("auth.yes")
        auth()
        if os.path.exists("auth.yes"):
            cmdgen.gencmd(out)
            os.remove("auth.yes")
        else:
            print("Could not generate command list.")
    except FileNotFoundError:
        print("cmdgen.py not found!")
