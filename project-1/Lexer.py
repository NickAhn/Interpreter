import re

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
        input_list = input.split()

        errorFound = False
        for input in input_list:  
            x = input
            while len(x) > 0:
                temp = self.getTokenType(x)
                if temp[0] == None:
                    print("ERROR PRINTING ", temp[1])
                    return []
                x = temp[1]

    
    #returns a tuple containing Token Object and input string without it
    #if it returns None, it found and Error
    def getTokenType(self, input):
        for key, val in self.t_types.items():
            match = re.match(val,input)
            if match:
                print(match.group(0), ": ", key)
                temp = input[match.end():]
                return Token(key, match.group(0)), temp

        #ERROR
        return None, input[0]

        
# input = "34 + 89 - x * y23"
# lexer_test = Lexer()
# lexer_test.scan(input)
# test = lexer_test.getTokenType(input)
# print(test[0], test[1])

# input2 = test[1]
# test2 = lexer_test.getTokenType(input2)
# print(test2[0], test2[1])
# print(len(test2[1]))




# input = "10ad"
# lexer_test.scan(input)             

        


        # x = input
        # moreString = True
        # while moreString:
        #     for key, val in self.t_types.items():
        #         match = re.match(val, x)
        #         if match:
        #             x = input[match.end():]
        #             print(key, ": ", x) # just printing; put in list in the future
        #         else:
        #             #error is found.
        #             print("Error printing ", x[0])
        #             moreString = False
        #             break

        #     if match.end() == len(input)-1:
        #         moreString = False

'''
for each input in input list:
    given input:
        - look for what type of token it matches.
        - if match found, keep looking for other tokens starting from input[match.end:]
        - if match.end() == input.length-1:
            - stop
    - 


'''



##################
t_types = {
            "IDENTIFIER" : "([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*",
            "NUMBER" : "[0-9]+",
            "SYMBOL" : "\+|\-|\*|/|\(|\)",    
        }

# ''' TEST CODE '''
# input = "ad"
# match = re.match(t_types["IDENTIFIER"], input)
# print(match)
# print(match.group(0,1))

# match = re.match(t_types["NUMBER"], input)
# print(match)
# match = re.match(t_types["SYMBOL"], input)
# print(match)








