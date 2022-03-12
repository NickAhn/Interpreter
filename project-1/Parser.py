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

import copy
import Lexer


class Tree:
    def __init__(self) -> None:
        self.token = None
        self.leftChild = self.rightChild = None
    
    def print(self, node):
        print(node.token.value, ":", node.token.type)

    def inorder(self, node):
        res = []
        if node == None:
            return
        
        self.print(node)
        self.inorder(node.leftChild)
        self.inorder(node.rightChild)


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.treeNode = Tree()
        print("---- token list --")
        for token in tokens:
            print(token.value)
        print("----\n")

    def parseElement(self):
        if self.tokens[0].value == "(":
            self.tokens.pop(0)
            treeNode = self.parseExpression()
            if self.tokens[0].value == ")":
                self.tokens.pop(0)
                return treeNode
            else:
                raise Exception("Not an expression\n")
        elif self.tokens[0].type == "NUMBER":
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0).value
            return treeNode
        elif self.tokens[0].type == "IDENTIFIER":
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            return treeNode
        
        
        raise Exception("Not an identifier or token\n")

    # piece ::= element { * element }
    def parsePiece(self):
        treeNode = self.parseElement()
        while len(self.tokens) != 0 and self.tokens[0].value == "*":
            tempNode = copy.copy(treeNode) # create temp copy of treeNode
            # current node
            TreeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode 
            treeNode.rightChild = self.parseElement()

            #consume token (putting consume token last to see if this works)
            # self.tokens.pop(0)
        return treeNode


    # factor ::= piece { / piece }
    def parseFactor(self):
        treeNode = self.parsePiece()
        while len(self.tokens) != 0 and self.tokens[0].value == '/':
            tempNode = copy.copy(treeNode) # create temp copy of treeNode
            # current node
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode
            # print("root: ", treeNode.token.value)
            # print(" left: ", treeNode.leftChild.token.value)
            treeNode.rightChild = self.parsePiece()
            # print(" right: ", treeNode.rightChild.token.value)

            #consume token (putting consume token last to see if this works)
            # self.tokens.pop(0)
        return treeNode


    # term ::= factor { - factor }
    def parseTerm(self):
        treeNode = self.parseFactor()
        while len(self.tokens) != 0 and self.tokens[0].value == '-':
            tempNode = copy.copy(treeNode) # create temp copy of treeNode
            # current node
            TreeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode 
            treeNode.rightChild = self.parseFactor()

            #consume token (putting consume token last to see if this works)
        return treeNode
    

    # expression ::= term { + term }
    def parseExpression(self):
        treeNode = self.parseFactor()
        while len(self.tokens) != 0 and self.tokens[0].value == '+':
            tempNode = copy.copy(treeNode) # create temp copy of treeNode
            # current node
            TreeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode 
            treeNode.rightChild = self.parseTerm()

            #consume token (putting consume token last to see if this works)
            # self.tokens.pop(0)
            
        return treeNode
    

# testing
input = "3 * (5 + 2 / x - 1)"
lexer = Lexer.Lexer()
tokens = lexer.scan(input)
for token in tokens:
    token.print()

parser = Parser(tokens)
treeNode = parser.parseExpression()
treeNode.inorder(treeNode)
# treeNode.leftChild.token.print()
# treeNode.rightChild.token.print()



