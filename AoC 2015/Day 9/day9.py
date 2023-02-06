import os
import sys
from itertools import permutations
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

places = set()
distances = dict()

for line in lines:
    line = line.rstrip()
    locations, distance = line.split(" = ")
    loc1, loc2 = locations.split(" to ")
    places.add(loc1)
    places.add(loc2)
    distances.setdefault(loc1, dict())[loc2] = int(distance)
    distances.setdefault(loc2, dict())[loc1] = int(distance)

shortest = sys.maxsize
longest = 0

for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    if dist < shortest:
        current_shortest_path = items
    if dist > longest:
        current_longest_path = items
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print(f"The shortest path has length: {shortest}, and the path is: {current_shortest_path}")
print(f"The longest path has length: {longest}, and the path is: {current_longest_path}")