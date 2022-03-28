'''
Nicolas Ahn
Emily Yeh
Phase 2.1 Parser for expressions
'''
import sys 
import re #regex library
import Lexer
import Parser

'''
This is the Test Driver.
Set testParser to True if you want the Parser to run. False Otherwise
'''
testParser = True

# Run program as: "python3 main.py <input-file> <output-file>"
try:
    input_list = open(sys.argv[1]).read().splitlines()
    output_file = open(sys.argv[2], "a")
    output_file.truncate(0)
    # sys.stdout = open(sys.argv[2], "w")

except:
    print("Failed to open file(s).")
    sys.exit(1)

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

if(testParser):
        output_file.write("AST:\n")
        parser = Parser.Parser(tokens_list)
        # treeNode = parser.parseExpression()
        treeNode = parser.parseStatement()
        output_file.write(treeNode.inorderString(treeNode, 0)+"\n")


print("Scanning and Parsing Complete!\nCheck", sys.argv[2], "to see output")