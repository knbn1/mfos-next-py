'''
very ugly port of mfos-next from batch to python

by knbnoob1

original mfos-next: https://github.com/knbn1/mfos-next
'''

import os
import importlib

# set a whole bunch of variables

mfosVer = "2026.11.18-py"

modules = ["core", "fsutils"]

user = os.getlogin()

print("[bootloader] INFO: logging system initialized")
print(f"[kernel] INFO: hello world, my version is {mfosVer}")

# load modules

for mod in modules:
    if os.path.exists(f"{mod}.py"):
        globals()[mod] = importlib.import_module(mod)
        print("[kmodsinit] INFO: loaded", mod)
    else:
        print("[kmodsinit] ERROR: failed to load", mod)
        exit()

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
    "rmdir": fsutils.rmdir,
    "mkdir": fsutils.mkdir,
    "home": fsutils.home,
    "back": fsutils.back,
    "cd": fsutils.cd,
    "rename": fsutils.rename,
    "copy": fsutils.copy
}

print("[kernel] INFO: boot process completed")

# an motd would go well here

print("\nWelcome to MicroflashOS Next (Python)!")
print("Available commands:", len(commands))
print("\nLogged in as", user)

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
            commands[command](*args)
        else:
            print("Invalid command.")







