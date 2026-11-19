# mfos-next-py debug tools

def tryauth():
    import proctector
    proctector.auth()

def gencmd():
    out = input("output file (default: commands.txt): ")
    import cmdgen
    cmdgen.gencmd(out)
