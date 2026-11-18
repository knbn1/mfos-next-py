'''
very ugly port of mfos-next from batch to python

by knbnoob1

original mfos-next: https://github.com/knbn1/mfos-next
'''

import os
import socket
import importlib

# set a whole bunch of variables

mfosVer = "2026.11.18-py"
mfos_modules = ["core", "fsutils"]
hostname = socket.gethostname()
user = os.getlogin()

print("[bootloader] INFO: logging system initialized")
print(f"[kernel] INFO: hello world, my version is {mfosVer}")

# load modules

for mod in mfos_modules:
    try:
        globals()[mod] = importlib.import_module(mod)
    except Exception as error:
        print("[kmodsinit] ERROR: failed to load", mod)
        print("[kmodsinit] ERROR:", error)
        exit()
    else:
        print("[kmodsinit] INFO: loaded", mod)

# command list

commands = {
    # core sysmodule
    "about": core.about,
    "clock": core.clock,
    "shutdown": core.shutdown,
    "help": core.help,
    "clear": core.clear,
    # fsutils sysmodule
    "list": fsutils.list,
    "rm": fsutils.rm,
    "mkdir": fsutils.mkdir,
    "home": fsutils.home,
    "back": fsutils.back,
    "cd": fsutils.cd,
    "rename": fsutils.rename,
    "copy": fsutils.copy,
    "extract": fsutils.extract
}

print("[kernel] INFO: boot process completed")

# an motd would go well here

print("\nWelcome to MicroflashOS Next!\n")
print("Available commands:", len(commands))
print("Modules loaded:", len(mfos_modules))

# set a variable for the while loop

status = "running"

# very simple parser

while status == "running":
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
            except TypeError:
                print("A TypeError exception has occured.\nMaybe you haven't specified an argument?")
            except Exception as error:
                print("An unhandled exception has occurred:\n")
                print(error)
        else:
            print("Invalid command.")







