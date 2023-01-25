import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

code_total = 0
memory_total = 0

for line in lines:
    line = line.rstrip()
    code_number = len(line)
    memory_number = code_number - 2
    trim_line = line[1:-1]
    indx = 0
    for char in trim_line:
        if char == "\\":
            if trim_line[indx+1]=="\\":
                memory_number -= 1
            elif trim_line[indx+1]=="\"":
                memory_number -= 1
            elif trim_line[indx+1]=="\\x":
                memory_number -= 3
        indx += 1
    code_total += code_number
    memory_total += memory_number
    