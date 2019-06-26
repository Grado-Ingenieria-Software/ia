import os



def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def imprimeMenu(opciones, info):
    clear()
    print("#"*60)
    print("# ____   ___  __  __ ____  ____            ___    _")
    print("#|  _ \ / _ \|  \/  |  _ \|  _ \          |_ _|  / \\")
    print("#| |_) | | | | |\/| | | | | |_) |  _____   | |  / _ \\")
    print("#|  __/| |_| | |  | | |_| |  __/  |_____|  | | / ___ \\")
    print("#|_|    \___/|_|  |_|____/|_|             |___/_/   \_\\")
    print("#")
    print("#"*60)
    if info != None:
        print(info)
        print("#"*60)
    i = 1
    for opcion in opciones:
        print("#  " + str(i) + ") " + opcion)
        i += 1
    print("#"*60)