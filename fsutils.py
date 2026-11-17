# mfos-next-py fsutils sysmodule

import os
from pathlib import Path

homedir = os.getcwd()

def cd():
    cd = input("Directory to enter: ")
    if Path(cd).exists():
        os.chdir(cd)
    else:
        print(f"Directory {cd} invalid!")

def list():
    print("Current working directory:", os.getcwd())
    print("")
    print(os.listdir(os.getcwd()))

def rm():
    rm = input("File to delete: ")
    if Path(rm).exists():
        os.remove(rm)
        if os.path.exists(rm):
            print(f"\nFailed to delete file {rm}!")
        else:
            print(f"\nDeleted file {rm}")
    else:
        print(f"\nFile {rm} not found!")

def rmdir():
    rmdir = input("Directory to delete: ")
    if Path(rmdir).exists():
        os.rmdir(rmdir)
        if os.path.exists(rmdir):
            print(f"\nFailed to delete file {rmdir}!")
        else:
            print(f"\nDeleted directory {rmdir}")
    else:
        print(f"\nDirectory {rmdir} not found!")

def mkdir():
    print("Create a path by seperating folders with forward slashes.")
    mkdirs = input("Folder(s) to create: ")
    if Path(mkdirs).exists():
        print(f"\nDirectory {mkdir} already exists!")
    else:
        os.makedirs(mkdirs)
        if Path(mkdirs).exists():
            print(f"\nCreated path {mkdirs}")
        else:
            print(f"\nFailed to create path {mkdirs}!")

def home():
    os.chdir(homedir)
    print("Back to home directory:\n")
    print(os.getcwd())

def back():
    print("Going up one level.")
    os.chdir('../')

def rename():
    oldname = input("File/folder to rename: ")
    newname = input("\nNew name: ")
    if Path(oldname).exists():
        os.rename(oldname, newname)
        if Path(oldname).exists():
            print(f"\nFailed to rename {oldname}!")
        else:
            print(f"\nRenamed {oldname} to {newname}")
