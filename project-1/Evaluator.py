'''
• Values evaluate as expected, e.g., 56 evaluates to number 56, and 26 evaluates to number 26.
• Operators are applied to the values, returned by their subtrees.
• Operators evaluate as expected2, i.e.,
    • + denotes numerical addition.
    • * denotes numerical multiplication.-
    • - denotes numerical subtraction. There are no negative numbers in this language. Refer to
lexical structure for clarification.
    • / denotes division on nonnegative integers, e.g., 3/2 evaluates to 1. In the case of division by
zero, the evaluator must stop and raise an exception.

'''
import Parser
class Evaluator:
    def __init__(self, ast:Parser.Tree) -> None:
        self.ast = ast

    def evaluate(self, node):
        if node.token.value == "+":
            return self.evaluate(node.leftChild) + self.evaluate(node.rightChild)
        if node.token.value == "*":
            return self.evaluate(node.leftChild) * self.evaluate(node.rightChild)
        if node.token.value == "-":
            #TODO: if result is negative, return 0
            result = self.evaluate(node.leftChild) - self.evaluate(node.rightChild)
            if result < 0:
                return 0
            return result
        if node.token.value == "/":
            divisor = self.evaluate(node.rightChild)
            if divisor == 0:
                raise Exception("Division by 0!")
            return self.evaluate(node.leftChild) // self.evaluate(node.rightChild)

        return int(node.token.value)
        