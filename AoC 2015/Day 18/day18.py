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

old_grid = grid
new_grid = [[0]*100]*100
for step in range(0,100):
    i = 0
    j = 0
    for line in old_grid:
        for light in line:
            if light == 1 and not count_neighbors_on(old_grid, i, j) in [2, 3]:
                light = 0
            elif light == 0 and count_neighbors_on(old_grid, i, j) == 3:
                light = 1
            new_grid[i][j] = light
            j += 1
        j = 0
        i += 1
    old_grid = new_grid
    new_grid = [[0]*100]*100

sum = 0
for row in old_grid:
    for element in row:
        sum += element
print(sum)