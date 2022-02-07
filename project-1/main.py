import sys 
import re #regex library
import Lexer

# Run program as: "python3 main.py <input-file> <output-file>"
try:
    input_list = open(sys.argv[1]).read().splitlines()
    output_file = open(sys.argv[2], "a")
except:
    print("Failed to open file(s).")
    sys.exit(1)

lexer = Lexer.Lexer()

for input in input_list:
    # print("Line: ", input)
    lexer.scan(input)
    # print("")