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
        # sys.stdout = open(sys.argv[2], "w")

    except:
        print("Failed to open file(s).")
        sys.exit(1)

    lexer = Lexer.Lexer()

    for input in input_list:
        tokens = lexer.scan(input)
        for token in tokens:
            token.print()

    #TODO: create funciton to write file with token list


scanner = Scanner()