# mfos-next-py core sysmodule

import sys
import os
import socket
import datetime

mfosVer = "2026.11.01-py"
user = os.getlogin()
hostOS = os.name
hostname = socket.gethostname()

cmd_help = {
    "help": "Show this help screen",
    "about": "Show some system information",
    "clock": "Get current date and time",
    "clear": "Clear console output",
    "shutdown": "Power off",
    "list": "List available files and folders",
    "cd": "Change directory",
    "mkdir": "Create a directory",
    "rm": "Delete a file",
    "rmdir": "Delete a directory",
    "rename": "Rename a file/folder",
    "home": "Revert to home/starting directory",
    "back": "Go up one level"
}

def help():
    for key, value in cmd_help.items():
        print(f"{key}: {value}")

def about():
    print("MicroflashOS version:", mfosVer)
    print("Hostname:", hostname)
    print("Environment:", hostOS)
    print("\nLogged in as", user)

def clock():
    print(datetime.datetime.now())

def clear():
    # thank you stack overflow
    os.system('cls' if os.name == 'nt' else 'clear')

def shutdown():
    print("Shutting down...")
    exit()
