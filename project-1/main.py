'''
Nicolas Ahn
Emily Yeh
Phase 1.1: Scanner for Lexp
'''

import sys 
import re #regex library
import Lexer


def Scanner():
    # Run program as: "python3 main.py <input-file> <output-file>"
    try:
        input_list = open(sys.argv[1]).read().splitlines()
        sys.stdout = open(sys.argv[2], "w")

    except:
        print("Failed to open file(s).")
        sys.exit(1)

    lexer = Lexer.Lexer()

    for input in input_list:
        lexer.scan(input)


scanner = Scanner()
# "\bif\b|\bthen\b|\belse\b|\bendif\b|\bwhile\b|\bdo\b|\bendwhile\b|\bskip\b"
# match = re.match(r"\bif\b|\bthen\b","then");
# print(match)