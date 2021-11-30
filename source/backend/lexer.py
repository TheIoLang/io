# The lexer (the lexer identifies everything)

from frontend.styles import *


class InvalidFileExtension(Exception):
  pass
class InvalidFile(Exception):
  pass



class IoLexer:
  def __init__(self, __file__):
    try:
      if ".i" in __file__:
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
      if i.startswith("#"):
        i = ""
        pass
      elif "#" in i:
        findcom = i.find("#")
        if findcom == -1:
          pass
        else:
          i = i[:findcom] # This discards comments
          # print(i)
    
      line = i