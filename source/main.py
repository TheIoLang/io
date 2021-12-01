import backend.lexer as lexer
import backend.parser as parser
import backend.token as token
import backend.interpreter as interpreter

file = lexer.IoLexer("main.ioo")
print(file.returnTokens())