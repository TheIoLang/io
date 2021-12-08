# The lexer (the lexer identifies everything)

from frontend.styles import *


def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        g.append(el)
    yield g


class IoLexer:
    def __init__(self, __file__):
        global cline
        global ltokens
        cline = 0
        try:
            if ".ioo" in __file__:
                f = open(__file__)
            else:
                raise InvalidFileExtension("that is not a correct file extension!")
        except:
            raise InvalidFile("no such file exists!")

        file = f.read()
        content = file.split("\n")
        content2 = file.split()
        # print(content)

        for i in content:
            cline += 1
            if i.startswith("#"):
                i = ""
                pass
            elif "#" in i:
                findcom = i.find("#")
                if findcom == -1:
                    pass
                else:
                    i = i[:findcom]  # This discards comments
                    # print(i)

            line = i
        
        self.line = line

    def return_value(self):
      return self.line