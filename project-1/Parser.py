'''
Nicolas Ahn
Emily Yeh
Phase 2.1 Parser for expressions
'''

import copy
import Lexer


class Tree:
    def __init__(self) -> None:
        self.token = None
        self.leftChild = self.rightChild = None
    
    def print(self, node):
        print(node.token.value, ":", node.token.type)

    def printInorder(self, node, spaces):
        if node == None:
            return
        str = "\t"*spaces
        # self.print(node)
        print(str, node.token)
        self.printInOrder(node.leftChild, spaces+1)
        self.printInOrder(node.rightChild, spaces+1)

    def inorderString(self, node, spaces):
        # finalWord = word
        if node == None:
            return ""
        tabs = "\t"*spaces
        # word += tabs + str(node.token)
        ast = tabs + str(node.token) + "\n"
        ast += self.inorderString(node.leftChild, spaces+1)
        ast += self.inorderString(node.rightChild, spaces+1)
        return ast




class Parser:
    ''' - EBNF:
        statement ::= basestatement { ; basestatement }
        basestatement ::= assignment | ifstatement | whilestatement | skip
        assignmet ::= IDENTIFIER := <expression>
        ifstatement ::= if <expression> then <statement> else <statement> endif
        whilestatement ::= while <expression> do <statement> endwhile

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
        if len(self.tokens) != 0 and self.tokens[0].value == "(":
            self.tokens.pop(0)
            treeNode = self.parseExpression()
            if len(self.tokens) != 0 and self.tokens[0].value == ")":
                self.tokens.pop(0)
                return treeNode
            else:
                raise Exception("Not an expression\n")
        
        #check for NUMBER
        elif len(self.tokens) != 0 and self.tokens[0].type == "NUMBER":
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0).value
            return treeNode

        # check for IDENTIFIER
        elif len(self.tokens) != 0 and self.tokens[0].type == "IDENTIFIER":
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
            
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode 
            treeNode.rightChild = self.parseFactor()
        return treeNode
    

    # expression ::= term { + term }
    def parseExpression(self):
        treeNode = self.parseTerm()
        while len(self.tokens) != 0 and self.tokens[0].value == '+':
            tempNode = copy.copy(treeNode)
            
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode 
            treeNode.rightChild = self.parseTerm()            
        return treeNode
    

# # testing
# input = "3 * (5 + 2 / x - 1)"
# lexer = Lexer.Lexer()
# tokens = lexer.scan(input)
# print("Tokens:\n")
# for token in tokens:
#     print(token)

# print("\nAST:\n")
# parser = Parser(tokens)
# treeNode = parser.parseExpression()
# # treeNode.inorder(treeNode, 0)
# print("------------stirng")
# print(treeNode.inorderString(treeNode, 0))




