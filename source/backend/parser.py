# The parser (it literally parses the code)

from backend.token import *

def InvalidFileExtension(exception):
    error = "error: <invalid file extension>".center(40)
    print(f"{bold}{Red}{error}{reset}{Red}\n\t-> line {cline}: {underline}{exception}{reset}")
    exit()


def InvalidFile(exception):
    error = "error: <invalid file>".center(40)
    print(f"{bold}{Red}{error}{reset}{Red}\n\t-> line {cline}: {underline}{exception}{reset}")
    exit()


def UnfoundVariable(exception):
    error = "error: <unfound variable>".center(40)
    print(f"{bold}{Red}{error}{reset}{Red}\n\t-> line {cline}: {underline}{exception}{reset}")
    exit()

class IoParser:
    def __init__(self, __file__):
        try:
            if ".ioo" in __file__:
                f = open(__file__)
            else:
                raise InvalidFileExtension("that is not a correct file extension!")
        except:
            raise InvalidFile("no such file exists!")