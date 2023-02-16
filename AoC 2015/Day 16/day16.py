import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

with open(os.path.join(sys.path[0], "ticker_tape.txt"), "r") as f:
    gifts = f.readlines()
f.close()

gift_list = {}
for line in gifts:
    line = line.rstrip()
    line = line.split()
    gift_list[line[0][:-1]] = int(line[1])

sue_count = 1

for line in lines:
    sue = {}

    line = line.rstrip()
    line = line.split()

    item1 = line[2][:-1]
    amount1 = int(line[3][:-1])
    sue[item1] = amount1

    item2 = line[4][:-1]
    amount2 = int(line[5][:-1])
    sue[item2] = amount2

    item3 = line[6][:-1]
    amount3 = int(line[7])
    sue[item3] = amount3

    count1 = 0
    count2 = 0
    for item in sue:
        if item in gift_list:
            if sue[item] == gift_list[item]:
                count1 += 1
            elif (item == 'cats' or item == 'trees') and sue[item] > gift_list[item]:
                count2 += 1
            elif (item == 'pomeranians' or item == 'goldfish') and sue[item] < gift_list[item]:
                count2 += 1

    if count1 == 3:
        sue_count1 = sue_count
    if count1 + count2 == 3:
        sue_count2 = sue_count
    
    sue_count += 1

print(f"The fake number of the Sue that got me the gift is: {sue_count1}")
print(f"The real number of the Sue that got me the gift is: {sue_count2}")
