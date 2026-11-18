# mfos-next-py fsutils sysmodule

import os
import shutil

homedir = os.getcwd()

def cd(directory):
    if os.path.exists(directory):
        os.chdir(directory)
        print("Current working directory:", os.getcwd())
    else:
        print(f"Directory {directory} invalid!")

def list():
    print("Current working directory:", os.getcwd())
    print("")
    print(os.listdir(os.getcwd()))

def rm(rm):
    if os.path.exists(rm):
        os.remove(rm)
        if os.path.exists(rm):
            print(f"Failed to delete file {rm}!")
        else:
            print(f"Deleted file {rm}")
    else:
        print(f"File {rm} not found!")

def rmdir(rmdir):
    if os.path.exists(rmdir):
        shutil.rmtree(rmdir)
        if os.path.exists(rmdir):
            print(f"Failed to delete file {rmdir}!")
        else:
            print(f"Deleted directory {rmdir}")
    else:
        print(f"Directory {rmdir} not found!")

def mkdir(mkdirs):
    if os.path.exists(mkdirs):
        print(f"Directory {mkdir} already exists!")
    else:
        os.makedirs(mkdirs)
        if os.path.exists(mkdirs):
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
    if os.path.exists(oldname):
        os.rename(oldname, newname)
        if os.path.exists(oldname):
            print(f"Failed to rename {oldname}!")
        else:
            print(f"Renamed {oldname} to {newname}")

def copy(type, source, destination):
    if type == "directory":
        if os.path.exists(source) and not os.path.exists(destination):
            shutil.copytree(source, destination, symlinks=False)
            print(f"Copied directory {source} to {destination}")
        else:
            print(f"Directory {destination} already exists!")
    elif type == "file":
        if os.path.exists(source) and not os.path.exists(destination):
            shutil.copy(source, destination, follow_symlinks=False)
            print(f"Copied file {source} to {destination}")
        else:
            print(f"File {destination} already exists!")
    else:
        print("Please specify a type.")
