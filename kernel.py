'''
very ugly port of mfos-next from batch to python

by knbnoob1

original mfos-next: https://github.com/knbn1/mfos-next
'''

import os
import socket
import importlib
import pickle

# set a whole bunch of variables

mfosVer = "2026.11.19-py"
mfos_modules = ["core", "fsutils", "devtools"]
hostname = socket.gethostname()
user = os.getlogin()

print("[bootloader] INFO: logging system initialized")
print(f"[kernel] INFO: hello world, my version is {mfosVer}")

# load modules

for mod in mfos_modules:
    try:
        globals()[mod] = importlib.import_module(mod)
    except Exception as error:
        print(f"[kmodsinit] ERROR: failed to load sysmodule {mod}: {error}")
        exit()
    else:
        print("[kmodsinit] INFO: loaded sysmodule", mod)

''''
get command list from file commands.txt with pickle
todo: replace with json encoding for human readable data
for now you can generate a commands.txt with the included cmdgen.py
'''
with open("commands.txt", "rb") as file:
    commands = pickle.load(file)

print("[kernel] INFO: boot process completed")

# an motd would go well here

print("\nWelcome to MicroflashOS Next!\n")
print("Available commands:", len(commands))
print("Modules loaded:", len(mfos_modules))

# command parser

while True:
    user_input = input(f"\n{user}@{hostname}: ")
    if user_input == "":
        print("\nInvalid command.")
    else:
        cmdline = user_input.split(' ')
        command = cmdline[0]
        args = cmdline[1:]
        print("") # empty line
        if command in commands:
            try:
                commands[command](*args)
            except TypeError as error:
                print("A TypeError exception has occured.\nMaybe you haven't specified an argument?\n")
                print(error)
            except Exception as error:
                print("An unhandled exception has occurred:\n")
                print(error)
        else:
            print("Invalid command.")







