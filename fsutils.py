# mfos-next-py fsutils sysmodule

import os
from pathlib import Path

homedir = os.getcwd()

def cd(directory):
    if Path(directory).exists():
        os.chdir(directory)
        print("Current working directory:", os.getcwd())
    else:
        print(f"Directory {directory} invalid!")

def list():
    print("Current working directory:", os.getcwd())
    print("")
    print(os.listdir(os.getcwd()))

def rm(rm):
    if Path(rm).exists():
        os.remove(rm)
        if os.path.exists(rm):
            print(f"Failed to delete file {rm}!")
        else:
            print(f"Deleted file {rm}")
    else:
        print(f"File {rm} not found!")

def rmdir(rmdir):
    if Path(rmdir).exists():
        os.rmdir(rmdir)
        if os.path.exists(rmdir):
            print(f"Failed to delete file {rmdir}!")
        else:
            print(f"Deleted directory {rmdir}")
    else:
        print(f"Directory {rmdir} not found!")

def mkdir(mkdirs):
    if Path(mkdirs).exists():
        print(f"Directory {mkdir} already exists!")
    else:
        os.makedirs(mkdirs)
        if Path(mkdirs).exists():
            print(f"Created path {mkdirs}")
        else:
            print(f"Failed to create path {mkdirs}!")

def home():
    os.chdir(homedir)
    print("Back to home directory:\n")
    print(os.getcwd())

def back():
    print("Going up one level.")
    os.chdir('../')

def rename(oldname, newname):
    if Path(oldname).exists():
        os.rename(oldname, newname)
        if Path(oldname).exists():
            print(f"Failed to rename {oldname}!")
        else:
            print(f"Renamed {oldname} to {newname}")
