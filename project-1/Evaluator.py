'''
Nicolas Ahn
Emily Yeh
Phase 3.2: Evaluator for full language
'''
import Lexer
import Parser
class Evaluator:
    def __init__(self, ast:Parser.Tree) -> None:
        self.ast = ast
        self.memory = {}

    def printMemory(self):
        for identifier, value in self.memory.items():
            print(identifier, " := ", value)
    
    def toStringMemory(self):
        msg = ""
        for identifier, value in self.memory.items():
            msg += identifier + " := " + str(value) + "\n"
        return msg

    def evaluateStatement(self, node):
         # Sequencing ;
        #   - Evaluate statement in LHS of sequencing
        #   - Next, replace whole tree with the subtree in RHS
        if node.token.value == ";":
            self.evaluateStatement(node.leftChild)
            return self.evaluateStatement(node.rightChild)

        # Evaluate RHS expression (using stack) and store result in memory entry for the LHS identifier. 
        # Then, remove subtree that corresponds to the assignment
        if node.token.value == ":=":
            self.memory[node.leftChild.token.value] = self.evaluate(node.rightChild)
            return self.memory[node.leftChild.token.value]

        # While <expression> do <statement> endwhile
        # - if expression evaluates to a positive number, then substitute the whole subtree with a sequencing tree
        #   where leftChild is the statement of the body of the While-loop
        #   and the rightChild is the original While-loop
        # - if expression = 0, remove whole subtree
        if node.token.type == "WHILE-LOOP":
            #call while-loop function
            expression = self.evaluate(node.leftChild)
            if expression > 0:
                semicolon_token = Lexer.Token("SYMBOL", ";")
                self.ast = Parser.Tree(semicolon_token, node.rightChild, None, node)
                return self.evaluateStatement(Parser.Tree(semicolon_token, node.rightChild, None, node))

            return None
    
        # if <expression> then <statement> else <statement> endif
        # if expression evaluates to a positive number, evaluate "then" statement
        # Otherwise, evaluate "else" statement
        if node.token.type == "IF-STATEMENT":
            # evaluate "Then" statement
            if self.evaluate(node.leftChild) > 0:
                return self.evaluateStatement(node.middleChild)
            # evaluate "Else" statement
            return self.evaluateStatement(node.rightChild)

        if node.token.value == "Skip":
            return

        
        print("end\n")

    # Post-order traversal of the tree
    def evaluate(self, node):
        if node.token.value == "+":
            return self.evaluate(node.leftChild) + self.evaluate(node.rightChild)
        if node.token.value == "*":
            return self.evaluate(node.leftChild) * self.evaluate(node.rightChild)
        if node.token.value == "-":
            result = self.evaluate(node.leftChild) - self.evaluate(node.rightChild)
            if result < 0:
                return 0
            return result
        if node.token.value == "/":
            divisor = self.evaluate(node.rightChild)
            if divisor == 0:
                raise Exception("Division by 0!")
            return self.evaluate(node.leftChild) // self.evaluate(node.rightChild)

        # if node value is an identifier, return value from memory
        if node.token.value.isalpha():
            try:
                return self.memory[node.token.value]
            except:
                raise Exception(node.token.value, " has not been assigned in memory.")

        # node is a digit
        return int(node.token.value)
      