'''
Nicolas Ahn
Emily Yeh
Phase 1.1: Scanner for Lexp
'''

import re

output_file = open("out.txt", "a")

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

    # returns string representing token as "<value> <type>" to be used in AST output (more readable to user)
    def toString(self) -> str:
        return self.type + " " + self.value
    
    def __str__(self) -> str:
        return self.value + " : " + self.type


class Lexer:
    def __init__(self) -> None:
        self.t_types = {
            "KEYWORD" : r"\bif\b|\bthen\b|\belse\b|\bendif\b|\bwhile\b|\bdo\b|\bendwhile\b|\bskip\b", #\b refers to word boundaries; r needs to be added to work
            "IDENTIFIER" : "([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*",
            "NUMBER" : "[0-9]+",
            "SYMBOL" : "\+|\-|\*|/|\(|\)|:=|;"
        }


    def scan(self, input):
        # print("Line: ", input)
        input_list = input.split()
        token_list = []

        for input in input_list:  
            x = input
            while len(x) > 0:
                temp = self.getTokenType(x)
                if temp[0] == None:
                    print("ERROR READING ", temp[1], "\n")
                    token_list.append("ERROR READING \"" + temp[1] + "\"\n")
                    return token_list
                x = temp[1]

                # Creating Token Instance
                token = temp[0]
                token_list.append(token)
        
        return token_list
    

    '''
    Returns a tuple containing Token and a substring of the input string without the token found
    If it returns None, it found and Error
    '''
    def getTokenType(self, input):
        # key = tokenType; val = regex
        for key, val in self.t_types.items():
            match = re.match(val,input)
            if match:
                # print(match.group(0), ": ", key)
                temp = input[match.end():]
                return Token(key, match.group(0)), temp

        #ERROR
        return None, input[0]








