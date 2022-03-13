'''
IDENIFIER =([a-z] | [A-Z])([a-z] | [A-Z] | [0-9])*
NUMBER =[0-9]+
SYMBOL =\+ | \- | \* | / | \( | \) | := | ;
KEYWORD =if | then | else | endif | while | do | endwhile | skip
'''

import copy
import Lexer


class Tree:
    def __init__(self) -> None:
        self.token = None
        self.leftChild = self.rightChild = None
    
    def print(self, node):
        print(node.token.value, ":", node.token.type)

    def inorder(self, node, spaces):
        res = []
        if node == None:
            return
        str = "\t"*spaces
        # self.print(node)
        print(str, node.token.value, ":", node.token.type)
        self.inorder(node.leftChild, spaces+1)
        self.inorder(node.rightChild, spaces+1)


class Parser:
    ''' - EBNF:
        expression ::= term { + term }
        term ::= factor { - factor }
        factor ::= piece { / piece }
        piece ::= element { * element }
        element ::= ( expression ) | NUMBER | IDENTIFIER'''
    

    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.treeNode = Tree()


    # element ::= ( expression ) | NUMBER | IDENTIFIER
    def parseElement(self):
        # check for (expression)
        if self.tokens[0].value == "(":
            self.tokens.pop(0)
            treeNode = self.parseExpression()
            if self.tokens[0].value == ")":
                self.tokens.pop(0)
                return treeNode
            else:
                raise Exception("Not an expression\n")
        
        #check for NUMBER
        elif self.tokens[0].type == "NUMBER":
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0).value
            return treeNode

        # check for IDENTIFIER
        elif self.tokens[0].type == "IDENTIFIER":
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            return treeNode
        # ERROR
        raise Exception("Not an identifier or token\n")


    # piece ::= element { * element }
    def parsePiece(self):
        # create element
        treeNode = self.parseElement()
        # create { * element }
        while len(self.tokens) != 0 and self.tokens[0].value == "*":
            '''
            while creates following tree:
                        *
                       / \
                treeNode  element
            '''
            tempNode = copy.copy(treeNode) # create copy of treeNode to be used as left child of current node
            TreeNode = Tree() # current node
            treeNode.token = self.tokens[0] 
            self.tokens.pop(0)
            treeNode.leftChild = tempNode
            treeNode.rightChild = self.parseElement()
        return treeNode


    # factor ::= piece { / piece }
    def parseFactor(self):
        # create piece
        treeNode = self.parsePiece()
        # create {/ piece }
        while len(self.tokens) != 0 and self.tokens[0].value == '/':
            tempNode = copy.copy(treeNode) # create temp copy of treeNode to be used as left child of current node
            treeNode = Tree() # current node
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode
            treeNode.rightChild = self.parsePiece()
        return treeNode


    # term ::= factor { - factor }
    def parseTerm(self):
        treeNode = self.parseFactor()
        while len(self.tokens) != 0 and self.tokens[0].value == '-':
            tempNode = copy.copy(treeNode) # create temp copy of treeNode to be used as left child of current node
            TreeNode = Tree() # current node
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode 
            treeNode.rightChild = self.parseFactor()
        return treeNode
    

    # expression ::= term { + term }
    def parseExpression(self):
        treeNode = self.parseFactor()
        while len(self.tokens) != 0 and self.tokens[0].value == '+':
            tempNode = copy.copy(treeNode)
            TreeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode 
            treeNode.rightChild = self.parseTerm()            
        return treeNode
    

# testing
input = "3 * (5 + 2 / x - 1)"
lexer = Lexer.Lexer()
tokens = lexer.scan(input)
print("-- input: --")
print(input)
for token in tokens:
    token.print()

print("\n-- Starting Parser: --")
parser = Parser(tokens)
treeNode = parser.parseExpression()
treeNode.inorder(treeNode, 0)




