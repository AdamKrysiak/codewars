def validBraces(string):
    while string.__len__() != 0:
        x = string.__len__()
        string = string.replace("{}", "")
        string = string.replace("[]", "")
        string = string.replace("()", "")
        if x == string.__len__(): return False
    return True


if __name__ == '__main__':
    print validBraces("{{()}[{())}[}")
    print validBraces("{()}")
