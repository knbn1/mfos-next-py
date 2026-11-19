# mfos-next-py core sysmodule

import sys
import os
import socket
import datetime

mfosVer = "2026.11.19-py"

sections = ["core", "fsutils", "devtools"]
helpdir = f"{os.getcwd()}/docs"

user = os.getlogin()
hostOS = os.name
hostname = socket.gethostname()

def help():
    count_section = 0
    if not os.path.exists(helpdir):
        print("Help section directory does not exist!\nRedownload MicroflashOS Next and try again.")
    else:
        for section in sections:
            try:
                with open(f"{helpdir}/{section}.mhs", "r") as file:
                    print(file.read())
                    count_section = count_section + 1
            except FileNotFoundError:
                print(f"Could not find help section {section}.mhs")
            except Exception as error:
                print(f"Failed to delete path {rm}!")
                print("An unhandled exception has occurred:\n")
                print(error)
        print(f"Loaded {count_section} help sections")

def about():
    print("MicroflashOS version:", mfosVer)
    print("Hostname:", hostname)
    print("Environment:", hostOS)
    print("Processors:", os.cpu_count())
    print("\nLogged in as", user)

def clock():
    print(datetime.datetime.now())

def clear():
    # thank you stack overflow
    os.system('cls' if os.name == 'nt' else 'clear')

def shutdown():
    print("Shutting down...")
    exit()

