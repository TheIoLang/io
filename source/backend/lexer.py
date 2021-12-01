# The lexer (the lexer identifies everything)

from frontend.styles import *


def InvalidFileExtension(exception):
  print(f"{RED}error - line {cline}: {exception}{reset}")
  exit()
def InvalidFile(exception):
  print(f"{Red}error - line {cline}: {exception}{reset}")
  exit()



class IoLexer:
  def __init__(self, __file__):
    global cline
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

    ltoken_word = []
    ltokens = {}
    dict_num = 0

    for i in content:
      cline+=1
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

      print(line.split())

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
          if char != " " or char != "" or char != "  ":
            token = tokens[0]
          else:
          # print("\n")
          # print("efsda")

            word = "".join(ltoken_word)
            # print(word)
            dict_num+=1
            ltokens[line+u"\uFE61"+str(dict_num)] = token
            # ltokens.update({word:token})
            print(ltokens)
          
        # print(token, end=" ")
        ltoken_word.append(char)
        # print(ltoken_word)