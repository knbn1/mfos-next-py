def unhandledException(message, error):
    print(message)
    print("An unhandled exception has occurred:")
    print(error)
    print("Please open an issue at https://github.com/knbn1/mfos-next-py")

def noPermission():
    print("You do not have read-write privileges!")
