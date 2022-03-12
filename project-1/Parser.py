'''
IDENIFIER =([a-z] | [A-Z])([a-z] | [A-Z] | [0-9])*
NUMBER =[0-9]+
SYMBOL =\+ | \- | \* | / | \( | \) | := | ;
KEYWORD =if | then | else | endif | while | do | endwhile | skip

expression ::= term { + term }
term ::= factor { - factor }
factor ::= piece { / piece }
piece ::= element { * element }
element ::= ( expression ) | NUMBER | IDENTIFIER
'''

class Tree:
    def __init__(self, token) -> None:
        self.token = token
        self.leftChild = self.rightChild = None
    
    def print(self):
        print(self.token.value, ":", self.token.type)

class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens

    def parseElement(self):

