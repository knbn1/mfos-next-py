'''
mfos-next-py command generator
add your commands into the dictionary below and run the script
format: "[command]": [module].[command]
'''

# load modules to process commands

from importlib import import_module
from pickle import dump
from compact import unhandledException
from sys import argv

mfos_modules = ["core", "fsutils", "devtools"]
for mod in mfos_modules:
    globals()[mod] = import_module(mod)
    print("[cmdgen] INFO: loaded sysmodule", mod)

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

# generate and save to output

def gencmd(output):
    print(f"Generating commands list as {output}\n")
    try:
        with open(output, "wb") as file:
            dump(commands, file)
    except Exception as error:
        unhandledException(f"Could not generate {output}!", error)
    else:
        print("Generated new commands list as", output)

try:
    arg = argv[1]
    print("\nRunning in standalone mode.\n")
except IndexError:
    print("\nPlease specify a file to save to.")
    exit()
except Exception as error:
    unhandledException(f"Unknown error:", error)
else:
    gencmd(arg)
