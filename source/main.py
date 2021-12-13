import backend.lexer as lexer
import backend.parser as parser
import backend.token as token

file = lexer.IoLexer(True, "e")
print(token.IoToken("e").returnTokens())