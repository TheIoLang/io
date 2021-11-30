# The lexer (the lexer identifies everything)
from frontend.styles import *


class InvalidFileExtension(Exception):
  pass
class InvalidFile(Exception):
  pass


class IoLexer:
  def __init__(self, __file__):
    try:
      if ".io" in __file__:
        f = open(__file__)
      else:
        raise InvalidFileExtension("that is not a correct file extension!")
    except:
      raise InvalidFile("no such file exists!")

    file = f.read()
    for i in file:
      print(i)
