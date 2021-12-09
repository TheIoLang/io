# The tokens (lists all the tokens, everything with tokens)

import backend.lexer as lexer


class IoToken:
    def __init__(self, e):
        # global dict_num

        dict_num = 0
        ltoken_word = []
        ltokens = {}
        file = lexer.IoLexer("main.ioo")
        line = file.return_value()
        tokens = (
                "STRING",
                "INTEGER",
                "FLOAT",
                "BOOL",
                "LPAREN",
                "RPAREN",
                "PLUS",
                "MINUS",
                "DIVIDE",
                "MULTI",
                "SQUARE",
                "EQUAL",
                "VARIABLE",
                "PRINT",
                "INPUT",
                "COMMENT",
        )

        t_string = str
        t_integer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
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

        # print(line.split())

        """
        a = line.split()
        if not a:
          print("e")
        else:
          print("a")
        """
        # import time;time.sleep(1)

        if " " in line:
            findspace = line.find(" ")
            if findspace != -1:
                line.split("\n")
        # print(line)
        # print(list(group(line.split(), " ")))
        # print(line.split())
        # print(line)

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
                raise UnfoundVariable("no such variable exists!")

            if char == " ":
                # word = "".join(ltoken_word)
                # print(word)
                dict_num += 1
                word = line + "\uFE61" + str(dict_num)
                ltokens[word] = token
                # ltokens.update({word:token})
                # print(ltokens)

                    # print(token, end=" ")
                    # ltoken_word.append(char)
                    # print(ltoken_word)

        self.ltokens = ltokens

    def returnTokens(self):
        return self.ltokens