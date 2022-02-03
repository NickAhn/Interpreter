import sys

# Run program as: "python3 main.py <input-file> <output-file>"
try:
    input_list = open(sys.argv[1]).read().splitlines()
    output_file = open(sys.argv[2], "w")
except:
    print("Failed to open file(s).")
    sys.exit(1)


# output
for x in input_list:
    output_file.write("Line: " + x + "\n")