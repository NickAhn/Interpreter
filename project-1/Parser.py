'''
Nicolas Ahn
Emily Yeh
Phase 2.1 Parser for expressions
'''

import copy
from logging import raiseExceptions
import Lexer


class Tree:
    def __init__(self) -> None:
        self.token = None
        self.leftChild = self.middleChild = self.rightChild = None

    
    def print(self, node):
        print(node.token.value, ":", node.token.type)

    def inorderString(self, node, spaces:int):
        # finalWord = word
        if node == None:
            return ""
        tabs = "\t"*spaces
        # word += tabs + str(node.token)
        ast = tabs + str(node.token) + "\n"
        ast += self.inorderString(node.leftChild, spaces+1)
        ast += self.inorderString(node.middleChild, spaces+1)
        ast += self.inorderString(node.rightChild, spaces+1)
        return ast




class Parser:
    ''' - EBNF:
        statement ::= basestatement { ; basestatement }
        basestatement ::= assignment | ifstatement | whilestatement | skip
        assignment ::= IDENTIFIER := <expression>
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

    # TODO: create raise Exception function and refactor code?

    # statement ::= basestatement { ; basestatement }
    def parseStatement(self):
        treeNode = self.parseBaseStatement()
        while len(self.tokens) != 0 and self.tokens[0].value == ';':
            tempNode = copy.copy(treeNode)

            treeNode.token = self.tokens[0]
            self.tokens.pop(0)
            treeNode.leftChild = tempNode
            treeNode.rightChild = self.parseBaseStatement()
        return treeNode


    #basestatement ::= assignment | ifstatement | whilestatement | skip
    def parseBaseStatement(self):
        # check for assignment
        if len(self.tokens) != 0 and self.tokens[0].type == "IDENTIFIER":
            return self.parseAssignment()

        # check for ifStatement
        elif len(self.tokens) != 0 and self.tokens[0].value == "if":
            return self.parseIfStatement()

        # check for whileStatement
        elif len(self.tokens) != 0 and self.tokens[0].value == "while":
            return self.parseWhileStatement()

        # check for skip //TODO: skip
        elif len(self.tokens) != 0 and self.tokens[0].value == "skip":
            return self.parseSkip()

        # ERROR
        raise Exception("Not a base statement\n")

    # assignment ::= IDENTIFIER := <expression>
    def parseAssignment(self):
        treeNode = Tree()
        if len(self.tokens) != 0 and self.tokens[0].type == "IDENTIFIER":
            treeNode.leftChild = Tree()
            treeNode.leftChild.token = self.tokens[0]
            self.tokens.pop(0)

            if len(self.tokens) != 0 and self.tokens[0].value == ":=":
                treeNode.token = self.tokens[0]
                self.tokens.pop(0)

                treeNode.rightChild = self.parseExpression()
            else:
                raise Exception("Not an Assignment: missing \":=\"")

            return treeNode
        
        raise Exception("Not an Assignment")
        

    #ifstatement ::= if <expression> then <statement> else <statement> endif
    def parseIfStatement(self):
        if len(self.tokens) != 0 and self.tokens[0].value == "if":
            # if <expression>
            treeNode = Tree() 
            treeNode.token = self.tokens[0] # root node = "if"
            self.tokens.pop(0)

            treeNode.leftChild = self.parseExpression()

            # then <statement>
            if len(self.tokens) != 0 and self.tokens[0].value == "then":
                self.tokens.pop(0)
                treeNode.middleChild = self.parseExpression()

                # else <expression>
                if len(self.tokens) != 0 and self.tokens[0].value == "else":
                    self.tokens.pop(0)
                    treeNode.rightChild = self.parseStatement()

                    # check for endif
                    if len(self.tokens) != 0 and self.tokens[0].value == "endif":
                        self.tokens.pop(0)
                        return treeNode
                    else:
                        raise Exception("Not an if-statement: missing an \"endif\" token")
                else:
                    raise Exception("Not an if-statement: missing an \"else\" token")
            else:
                raise Exception("Not an if-statement: missing a \"then\" token")

            
        raise Exception("Not an if-statement")


            # endif
        

    # whilestatement ::= while <expression> do <statement> endwhile
    def parseWhileStatement(self):
        if len(self.tokens) != 0 and self.tokens[0].value == "while":
            # while <expression>
            treeNode = Tree()
            treeNode.token = self.tokens[0]
            self.tokens.pop(0)

            treeNode.leftChild = self.parseExpression()

            #do <statement>
            if len(self.tokens) != 0 and self.tokens[0].value == "do":
                self.tokens.pop(0)
                treeNode.rightChild = self.parseStatement()
                if len(self.tokens) != 0 and self.tokens[0].value == "endwhile":
                    return treeNode
                raise Exception("Not a while-loop: missing an \"endwhile\" token")
            else:
                raise Exception("Not a while-loop: missing a \"do\" token")

            

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




