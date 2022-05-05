'''
Nicolas Ahn
Emily Yeh
Phase 3.1: Evaluator for expressions
'''

import Parser
class Evaluator:
    def __init__(self, ast:Parser.Tree) -> None:
        self.ast = ast
        self.memory = {}


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
            for key,value in self.memory.items():
                print(key, value, sep=" : ")
            return
        
        #TOOD: WHILE-LOOP
        if node.token.type == "WHILE-LOOP":
            #call while-loop function
            pass

        if node.token.type == "IF-STATEMENT":
            print("IF-STATEMENT")

            # evaluate "Then" statement
            if self.evaluate(node.leftChild) > 0:
                return self.evaluateStatement(node.middleChild)
            
            # evaluate "Else" statement
            return self.evaluateStatement(node.rightChild)

        if node.token.value == "Skip":
            pass

        
        print("end")

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
      