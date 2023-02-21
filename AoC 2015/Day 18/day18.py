import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

def count_neighbors_on(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    lights_on_count = 0

    for i in range((0 if x-1 < 0 else x-1), (rows if x+2 > rows else x+2), 1):
        for j in range((0 if y-1 < 0 else y-1), (cols if y+2 > cols else y+2), 1):
            if x == i and y==j:
                continue
            else:
                lights_on_count += grid[i][j]
    return lights_on_count

grid = []
i = 0
for line in lines:
    line = line.rstrip()
    grid.append([])
    for char in line:
        if char == "#":
            grid[i].append(1)
        elif char == ".":
            grid[i].append(0)
    i += 1

old_grid1 = grid
old_grid2 = grid
new_grid1 = [[0]*100 for _ in range(100)]
new_grid2 = [[0]*100 for _ in range(100)]

for step in range(0,100):
    i = 0
    j = 0
    for line in old_grid1:
        for light in line:
            if (light == 1) and not (count_neighbors_on(old_grid1, i, j) in [2, 3]):
                new_grid1[i][j] = 0
            elif (light == 0) and (count_neighbors_on(old_grid1, i, j) == 3):
                new_grid1[i][j] = 1
            else:
                new_grid1[i][j] = light
            j += 1
        j = 0
        i += 1
    old_grid1 = new_grid1
    new_grid1 = [[0]*100 for _ in range(100)]

    i = 0
    j = 0
    for line in old_grid2:
        for light in line:
            if (light == 1) and not (count_neighbors_on(old_grid2, i, j) in [2, 3]):
                new_grid2[i][j] = 0
            elif (light == 0) and (count_neighbors_on(old_grid2, i, j) == 3):
                new_grid2[i][j] = 1
            else:
                new_grid2[i][j] = light
            j += 1
        j = 0
        i += 1
    old_grid2 = new_grid2
    old_grid2[0][0] = 1
    old_grid2[0][99] = 1
    old_grid2[99][0] = 1
    old_grid2[99][99] = 1
    new_grid2 = [[0]*100 for _ in range(100)]

sum1 = 0
for row in old_grid1:
    for element in row:
        sum1 += element

sum2 = 0
for row in old_grid2:
    for element in row:
        sum2 += element

print(f"The number of lights that are on for part 1 is: {sum1}")
print(f"The number of lights that are on for part 2 is: {sum2}")
