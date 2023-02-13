import os
import sys
import math
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

race_time = 2503

raindeer_stats = []

for line in lines:
    line = line.rstrip()
    line = line.split()
    stat = [line[0], int(line[3]), int(line[6]), int(line[-2]), 0, 0]
    raindeer_stats.append(stat)

total_time = 0

for second in range(1,race_time+1):
    total_time = second
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
        raindeer[4] = distance
    max_distance = 0
    index = 0
    for raindeer in raindeer_stats:
        if raindeer[4] > max_distance:
            max_distance = raindeer[4]
            max_index = index
        index += 1
    raindeer_stats[max_index][5] += 1

max_distance = 0
max_points = 0

for raindeer in raindeer_stats:
    if raindeer[4] > max_distance:
        max_distance = raindeer[4]
        winner1_index = raindeer_stats.index(raindeer)
    if raindeer[5] > max_points:
        max_points = raindeer[5]
        winner2_index = raindeer_stats.index(raindeer)

print(f"The winner with the old scoring system after {race_time} seconds is: {raindeer_stats[winner1_index][0]}, with a distance travelled of: {max_distance} km")
print(f"The winner with the new scoring system after {race_time} seconds is: {raindeer_stats[winner2_index][0]}, with a point total of: {max_points}")