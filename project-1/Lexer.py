import re

class Lexer:
    def __init__(self) -> None:
        self.t_types = {
            "IDENTIFIER" : "([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])",
            "NUMBER" : "[0-9]+",
            "SYMBOL" : "\+ | \- | \* | / | \( | \)",    
        }


    def scan(self, input):
        input_list = input.split() # separate inputs by delimiters (whitespaces)
        for input in input_list:
            currTokenPos = 0 #keep track of beginning of the token being analyzed #WE MIGHT NOT NEED THIS!
            currToken = "" # currToken = input[:1]

            for i in range(len(input)):
                currToken += input[i]
                if i == 0:
                    continue
                

                # if i == 0:
                #     # prevTokenType = getTokenType of input[i] #WE MIGHT NOT NEED THIS!
                #     continue
                
                if self.getTokenType(currToken):
                    print("-NOT MATCH")
                    print(self.getTokenType(currToken[:-1]), ": ", currToken[:-1])
                    currTokenPos = i


    def getTokenType(self, buffer):
        token_type = ""
        for key, val in self.t_types.items():
            print(key, ": ", val, " -> ", buffer)
            match = re.match(regex, buffer)
            if match:
                return key

        return None
