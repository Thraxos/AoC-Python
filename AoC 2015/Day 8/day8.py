import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

code_total = 0
memory_total = 0
new_strings_length = 0

for line in lines:
    line = line.rstrip()
    code_number = len(line)
    memory_number = code_number - 2
    trim_line = line[1:-1]
    indx = 0
    new_strings_length += 6
    while indx < len(trim_line):
        char = trim_line[indx]
        if char == "\\":
            if trim_line[indx+1]=="\\":
                memory_number -= 1
                new_strings_length += 4
                indx += 2
            elif trim_line[indx+1]=="\"":
                memory_number -= 1
                new_strings_length += 4
                indx += 2
            elif trim_line[indx+1]=="x":
                memory_number -= 3
                new_strings_length += 5
                indx += 4
        else:
            indx += 1
            new_strings_length += 1
    code_total += code_number
    memory_total += memory_number

print(f"The number of characers of code minus the number of characters in memory for all the strings are: {code_total-memory_total}")
print(f"The total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal is: {new_strings_length-code_total}")
