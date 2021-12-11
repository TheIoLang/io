import backend.lexer as lexer
import backend.parser as parser
import backend.token as token

# import os
print("errrr")

file = lexer.IoLexer(True)
print("Running...")
print(token.IoToken("e").returnTokens())