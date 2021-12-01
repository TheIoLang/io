# The tokens (lists all the tokens, everything with tokens)

from backend.lexer import *


class IoTokens:
  def __init__(self):
    file = lexer.IoLexer("main.ioo")
    contents = file.returnTokens()

    