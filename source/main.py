import backend.lexer as lexer
import backend.parser as parser
import backend.token as token

# import os


file = lexer.IoLexer(True)
print(token.IoToken("e").returnTokens())