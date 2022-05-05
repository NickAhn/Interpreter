'''
Nicolas Ahn
Emily Yeh
Phase 3.1: Parser for full language
'''
import sys 
import re #regex library
import Lexer
import Parser
import Evaluator
'''
This is the Test Driver.
Set testParser to True if you want the Parser to run. False Otherwise
'''

# Run program as: "python3 main.py <input-file> <output-file>"
try:
    input_list = open(sys.argv[1]).read().splitlines()
    output_file = open(sys.argv[2], "a")
    output_file.truncate(0)
    # sys.stdout = open(sys.argv[2], "w")

except:
    print("Failed to open file(s).")
    sys.exit(1)

# - Scan - #
lexer = Lexer.Lexer()
tokens_list = []
for input in input_list:
    tokens = lexer.scan(input)
    output_file.write("Line: " + input + "\n")
    for token in tokens:
        # print(token)
        output_file.write(str(token)+"\n") 
        tokens_list.append(token)
    output_file.write("\n")

# - Parse - #
output_file.write("AST:\n")
parser = Parser.Parser(tokens_list)
# treeNode = parser.parseExpression() # parse Expressions only
treeNode = parser.parseStatement() # parse Statements and expressions
output_file.write(treeNode.inorderString(treeNode, 0)+"\n")

# - Evaluate - #
ev = Evaluator.Evaluator(treeNode)
output = ev.evaluateStatement(treeNode)
# output = ev.evaluate(treeNode)
# output_file.write("Output " + str(output))


print("Scanning and Parsing Complete!\nCheck", sys.argv[2], "to see output")