# The lexer (the lexer identifies everything)

from frontend.styles import *


class InvalidFileExtension(Exception):
  pass
class InvalidFile(Exception):
  pass



class IoLexer:
  def __init__(self, __file__):
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

      tokens = (
        "STRING", "INTEGER", "FLOAT", "BOOL",
        "LPAREN", "RPAREN",
        "PLUS", "MINUS", "DIVIDE", "MULTI", "SQUARE", 
        "EQUAL"
      )

      t_string = str
      t_integer = ["1","2","3","4","5","6","7","8","9","0"]
      t_float = float
      t_bool = bool
      t_lparen = "("
      t_rparen = ")"
      t_plus = "+"
      t_minus = "-"
      t_divide = "/"
      t_multi = "*"
      t_square = "**"
      t_equal = "="

      for char in line:
        if char in t_integer:
          token = tokens[1]
        elif type(char) == t_float:
          token = tokens[2]
        elif type(char) == t_bool:
          token = tokens[3]
        elif char == t_lparen:
          token = tokens[4]
        elif char == t_rparen:
          token = tokens[5]
        elif char == t_plus:
          token = tokens[6]
        elif char == t_minus:
          token = tokens[7]
        elif char == t_divide:
          token = tokens[8]
        elif char == t_multi:
          token = tokens[9]
        elif char == t_square:
          token = tokens[10]
        elif char == t_equal:
          token = tokens[11]
        elif type(char) == t_string:
          token = tokens[0]
        print(token)