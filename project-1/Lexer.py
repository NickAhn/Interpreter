import re

output_file = open("out.txt", "a")

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

class Lexer:
    def __init__(self) -> None:
        self.t_types = {
            "IDENTIFIER" : "([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*",
            "NUMBER" : "[0-9]+",
            "SYMBOL" : "\+|\-|\*|/|\(|\)",
        }

    # Output: list of tokens
    def scan(self, input):
        self.output("\nLine: " + input, output_file)  #
        input_list = input.split()

        errorFound = False
        for input in input_list:  
            x = input
            while len(x) > 0:
                temp = self.getTokenType(x)
                if temp[0] == None:
                    print("ERROR PRINTING ", temp[1])
                    self.output("ERROR PRINTING " + temp[1], output_file)  #
                    return []
                x = temp[1]


    def output(self, input, output_file):
        output_file.write(input + "\n")

    
    #returns a tuple containing Token Object and input string without it
    #if it returns None, it found and Error
    def getTokenType(self, input):
        for key, val in self.t_types.items():
            match = re.match(val,input)
            if match:
                print(match.group(0), ": ", key)
                self.output(str(match.group(0)) + ": " + str(key), output_file)
                temp = input[match.end():]
                return Token(key, match.group(0)), temp

        #ERROR
        return None, input[0]








