'''
very ugly port of mfos-next from batch to python

by knbnoob1

original mfos-next: https://github.com/knbn1/mfos-next
'''

import os
from socket import gethostname
from importlib import import_module
from pickle import load

# set a whole bunch of variables

mfosVer = "2026.11.20-py"
mfos_modules = ["core", "fsutils", "devtools", "compact"]

print("[bootloader] INFO: logging system initialized")
print(f"[kernel] INFO: hello world, my version is {mfosVer}")

# load modules

for mod in mfos_modules:
    try:
        globals()[mod] = import_module(mod)
        print("[kmodsinit] INFO: loading sysmodule", mod)
    except FileNotFoundError:
        print(f"[kmodsinit] ERROR: could not find sysmodule {mod}")
        exit()
    except Exception as error:
        print(f"[kmodsinit] ERROR: failed to load sysmodule {mod}: {error}")
        exit()

''''
get command list from file commands.txt with pickle
todo: replace with json encoding for human readable data
for now you can generate a commands.txt with the included cmdgen.py
'''
print("[kcmdinit] INFO: loading commands.txt")
try:
    with open("commands.txt", "rb") as file:
        commands = load(file)
except FileNotFoundError:
    print(f"[kcmdinit] ERROR: could not find commands.txt")
    exit()
except Exception as error:
    print(f"[kcmdinit] ERROR: failed to load commands.txt: {error}")
    exit()

print("[kernel] INFO: boot process completed")

# an motd would go well here

print("\nWelcome to MicroflashOS Next!\n")
print("Available commands:", len(commands))
print("Modules loaded:", len(mfos_modules))

# command parser

while True:
    user_input = input(f"\n{os.getlogin()}@{gethostname()}: ")
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
                compact.unhandledException(f"Could not execute command {command}!", error)
        else:
            print("Invalid command.")







