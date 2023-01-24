import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    line = f.readline()
f.close()

line = line.rstrip()

floor = 0
pos = 0
flag = 0

for char in line:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    pos += 1
    if floor == -1 and flag == 0:
        basement_pos = pos
        flag = 1

print(f"The instructions take Santa to floor: {floor}")
print(f"The position of the character that causes Santa to first enter the basement is: {basement_pos}")