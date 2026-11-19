'''
mfos-next-py command generator
add your commands into the dictionary below and run the script
format: "[command]": [module].[command]
'''

# load modules to process commands

import pickle
import importlib

mfos_modules = ["core", "fsutils", "devtools"]
for mod in mfos_modules:
    globals()[mod] = importlib.import_module(mod)
    print("[kmodsinit] INFO: loaded sysmodule", mod)

# add commands here

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
    "extract": fsutils.extract,
    # devtools
    "tryauth": devtools.tryauth,
    "gencmd": devtools.gencmd
}

# list generator, default commands.txt

print(f"\nGenerating commands list as commands.txt\n")
try:
    with open("commands.txt", "wb") as file:
        pickle.dump(commands, file)
except Exception as error:
    print("Unhandled exception:", error)
else:
    print("Generated new commands list as commands.txt")
