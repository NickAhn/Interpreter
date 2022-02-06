class Lexer:
    def __init__(self) -> None:
        self.t_types = {
            "IDENTIFIER" : "([a-z]|[A-Z]|)([a-z]|[A-Z]|[0-9])",
            "NUMBER" : "[0-9]+",
            "SYMBOL" : "\+ | \- | \* | / | \( | \)",    
        }


    def scan(list: input):
        input_list = input.split() # separate inputs by delimiters (whitespaces)
        for input in input_list:
            currTokenPos = 0 #keep track of beginning of the token being analyzed #WE MIGHT NOT NEED THIS!
            currToken = ""
            for i in range(len(input)):
                currToken += input[i]
                if i == 0:
                    # prevTokenType = getTokenType of input[i] #WE MIGHT NOT NEED THIS!
                    continue
                
                '''if getTokenType(currToken, self.t_tpes):
                        
                    else:
                        print(getTokenType(currToken[:-1]), ": ", currToken[:-1])
                        currToken = ""
                '''
