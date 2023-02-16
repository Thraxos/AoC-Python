import os
import sys
from itertools import combinations

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

containers = []
for line in lines:
    line = line.rstrip()
    containers.append(int(line))

count = 0
flag = 0
min_list = []
for r in range(1, len(containers)):
    for combo in combinations(containers,r):
        if sum(combo) == 150:
            count += 1
            if flag == 0:
                min_list.append(list(combo))
    if count > 0 and flag == 0:
        min_count = count
        min_choice = r
        flag = 1

print(f"The number of different combinations of containers that fit exactly 150 liters are: {count}")
print(f"The minimal number of containers that fit exactly 150 liters are: {min_choice}. There are {min_count} ways to use that many containers: {min_list}")