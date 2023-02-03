import os
import sys
from itertools import permutations
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

graph = {}
graph["Dummy"] = []

for line in lines:
    line = line.rstrip()
    locations, distance = line.split(" = ")
    loc1, loc2 = locations.split(" to ")
    if loc1 not in graph:
        graph[loc1] = [[loc2, int(distance)]]
        graph[loc1].append(["Dummy", 0])
        graph["Dummy"].append([loc1,0])
    else:
        graph[loc1].append([loc2, int(distance)])
    if loc2 not in graph:
        graph[loc2] = [[loc1, int(distance)]]
        graph[loc2].append(["Dummy", 0])
        graph["Dummy"].append([loc2,0])
    else:
        graph[loc2].append([loc1, int(distance)])

