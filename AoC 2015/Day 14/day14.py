import os
import sys
import math
from itertools import permutations
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

total_time = 2503

raindeer_stats = []

for line in lines:
    line = line.rstrip()
    line = line.split()
    stat = (line[0], int(line[3]), int(line[6]), int(line[-2]))
    raindeer_stats.append(stat)

distances = []

print(raindeer_stats)

for raindeer in raindeer_stats:
    speed = raindeer[1]
    fly_time = raindeer[2]
    rest_time = raindeer[3]

    chunk_time = fly_time + rest_time
    chunk_amount = math.floor(total_time/chunk_time)
    extra_time = total_time%chunk_time
    if extra_time <= fly_time:
        extra_dist = speed*extra_time
    else:
        extra_dist = speed*fly_time

    distance = speed*fly_time*chunk_amount + extra_dist
    distances.append(distance)

print(f"The raindeer who won was {raindeer_stats[distances.index(max(distances))][0]}, with distance: {max(distances)} km")