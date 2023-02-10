import os
import sys
from itertools import permutations
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

happiness = {}
invited = []

for line in lines:
    line = line.rstrip()
    line = line.split()

    if line[2] == "lose":
        if line[0] not in happiness:
            happiness[line[0]] = {line[-1][:-1] : -int(line[3])}
            invited.append(line[0])
        else:
            happiness[line[0]][line[-1][:-1]] = -int(line[3])
    if line[2] == "gain":
        if line[0] not in happiness:
            happiness[line[0]] = {line[-1][:-1] : int(line[3])}
            invited.append(line[0])
        else:
            happiness[line[0]][line[-1][:-1]] = int(line[3])

happiest = -sys.maxsize

def find_happiest_order(happiness, invited, happiest, part):
    if part == 2:
        invited.append("Marcus")
        happiness["Marcus"] = {}
        for guest in happiness:
            happiness[guest]["Marcus"] = 0
            happiness["Marcus"][guest] = 0

    for guest_order in permutations(invited):
        score = sum(map(lambda x, y: happiness[x][y], guest_order[:-1], guest_order[1:]))
        score += sum(map(lambda x, y: happiness[y][x], guest_order[:-1], guest_order[1:]))
        score += happiness[guest_order[-1]][guest_order[0]]
        score += happiness[guest_order[0]][guest_order[-1]]
        if score > happiest:
            current_order = guest_order
        happiest = max(happiest, score)
    return happiest, current_order

happiest1, current_order1 = find_happiest_order(happiness, invited, happiest, 1)
happiest2, current_order2 = find_happiest_order(happiness, invited, happiest, 2)

print(f"The total change in happiness that doesn't include me is: {happiest1}, and the seating order is {current_order1}")
print(f"The total change in happiness that includes me is: {happiest2}, and the seating order is {current_order2}")

