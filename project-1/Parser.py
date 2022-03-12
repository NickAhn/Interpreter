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
    def __init__(self) -> None:
        self.token = None
        self.leftChild = self.rightChild = None
    
    def print(self):
        print(self.token.value, ":", self.token.type)


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.treeNode = Tree()

    def parseElement(self):
        if self.tokens[0] == "(":
            self.tokens.remove(0)
            treeNode = parseExpression()
            if self.tokens[0] == ")":
                self.tokens.remove(0)
                return treeNode
            else
                raise Exception("Not an expression\n")
        elif self.tokens[0].type == "NUMBER":
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            return treeNode
        elif self.tokens[0].type == "IDENTIFIER":
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            return treeNode
        raise Exception("Not an identifier or token\n")

    # piece ::= element { * element }
    def parcePiece(self):
        treeNode = self.parseElement()
        while self.tokens[0] == "*":
            # current node
            treeNode = Tree()
            treeNode.token = self.tokens[0]

            treeNode.leftChild = treeNode
            treeNode.rightChild = self.parseElement()
        return treeNode

    
