# mfos-next-py debug tools

import devtools
import os

def tryauth():
    print("Triggering authentication process...")
    try:
        import proctector
        proctector.auth()
        if os.path.exists("auth.yes"):
            print("Authentication successful.")
        else:
            print("Failed to authenticate.")
    except FileNotFoundError:
        print("Proctector module not found!")

def gencmd():
    out = input("Output file (default: commands.txt): ")
    print("")
    try:
        import cmdgen
        import proctector
        if os.path.exists("auth.yes"):
            os.remove("auth.yes")
        proctector.auth()
        if os.path.exists("auth.yes"):
            cmdgen.gencmd(out)
            os.remove("auth.yes")
    except FileNotFoundError:
        print("cmdgen.py not found!")
