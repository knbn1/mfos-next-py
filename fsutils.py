# mfos-next-py fsutils sysmodule

import os
import shutil

homedir = os.getcwd()

def cd(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(f"Directory {directory} invalid!")
    else:
        print("Current working directory:", os.getcwd())

def list():
    print("Current working directory:", os.getcwd())
    print("")
    print(os.listdir(os.getcwd()))

def rm(rm):
    try:
        os.remove(rm)
    except FileNotFoundError:
        print(f"File {rm} not found!")
    except PermissionError:
        print("You do not have read-write privileges!")
    except IsADirectoryError:
        try:
            shutil.rmtree(rm)
        except FileNotFoundError:
            print(f"Directory {rm} not found!")
        except PermissionError:
            print("You do not have read-write privileges!")
        except Exception as error:
            print(f"Failed to delete path {rm}!")
            print("An unhandled exception has occurred:\n")
            print(error)
        else:
            print(f"Deleted directory {rm}")
    except Exception as error:
        print(f"Failed to delete file {rm}!")
        print("An unhandled exception has occurred:\n")
        print(error)
    else:
        print(f"Deleted file {rm}")

def mkdir(mkdirs):
    if os.path.exists(mkdirs):
        print(f"Directory {mkdirs} already exists!")
    else:
        try:
            os.makedirs(mkdirs)
        except PermissionError:
            print("You do not have read-write privileges!")
        except Exception as error:
            print(f"Failed to create path {mkdirs}!")
            print("An unhandled exception has occurred:\n")
            print(error)
        else:
            print(f"Created path {mkdirs}")

def home():
    try:
        os.chdir(homedir)
    except FileNotFoundError:
        print("Home directory does not exist!")
        print("Seriously though, what have you done?!")
    else:
        print("Back to home directory:\n")
        print(os.getcwd())

def back():
    print("Going up one level.")
    os.chdir('../')

def rename(oldname, newname):
    try:
        os.rename(oldname, newname)
    except FileNotFoundError:
        print("Target not found!")
    except PermissionError:
        print("You do not have read-write privileges!")
    except Exception as error:
        print(f"Failed to rename {oldname}!")
        print("An unhandled exception has occurred:\n")
        print(error)
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
        print("Please specify a type to copy: file or folder")

def extract(file, destination):
    try:
        shutil.unpack_archive(file, destination)
    except PermissionError:
        print("You do not have read-write privileges!")
    except FileNotFoundError:
        print("Target zip file not found!")
    except shutil.ReadError:
        print("Could not read archive! Is it in the correct .zip format?")
    except Exception as error:
        print(f"Failed to extract {file} to {destination}!")
        print("An unhandled exception has occurred:\n")
        print(error)
    else:
        print(f"Extracted contents of {file} to {destination}")
