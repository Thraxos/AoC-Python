import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    line = f.readline()
f.close()

line = line.rstrip()

dict1 = {}
pos = [0,0]
dict1[tuple(pos)] = 1
for char in line:
    if char == ">":
        pos[0] += 1
    elif char == "<":
        pos[0] -= 1
    elif char == "^":
        pos[1] += 1
    elif char == "v":
        pos[1] -= 1
    
    if tuple(pos) in dict1:
        dict1[tuple(pos)] += 1
    else:
        dict1[tuple(pos)] = 1

dict2 = {}
pos1 = [0,0]
pos2 = [0,0]
dict2[tuple(pos1)] = 2
for char1 in line[::2]:
    if char1 == ">":
        pos1[0] += 1
    elif char1 == "<":
        pos1[0] -= 1
    elif char1 == "^":
        pos1[1] += 1
    elif char1 == "v":
        pos1[1] -= 1
    
    if tuple(pos1) in dict2:
        dict2[tuple(pos1)] += 1
    else:
        dict2[tuple(pos1)] = 1

for char2 in line[1::2]:
    if char2 == ">":
        pos2[0] += 1
    elif char2 == "<":
        pos2[0] -= 1
    elif char2 == "^":
        pos2[1] += 1
    elif char2 == "v":
        pos2[1] -= 1
    
    if tuple(pos2) in dict2:
        dict2[tuple(pos2)] += 1
    else:
        dict2[tuple(pos2)] = 1


print(f"The number of houses that received at least one present from Santa is: {len(dict1)}")
print(f"The number of houses that received at least one present from Santa and Robo-Santa is: {len(dict2)}")
