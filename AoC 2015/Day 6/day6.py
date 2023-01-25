import os
import sys
import numpy as np
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

grid1 = np.zeros((1000,1000))
grid2 = np.zeros((1000,1000))

for line in lines:
    line = line.rstrip()
    line = line.split()
    index = line.index("through")
    pair1 = line[index-1]
    pair2 = line[index+1]   
    x1 = int(pair1.split(",")[0])
    y1 = int(pair1.split(",")[1])
    x2 = int(pair2.split(",")[0])
    y2 = int(pair2.split(",")[1])

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if "toggle" in line:
                if grid1[i,j] == 0.0:
                    grid1[i,j] = 1.0
                else:
                    grid1[i,j] = 0.0
                grid2[i,j] += 2.0
            elif "on" in line:
                grid1[i,j] = 1.0
                grid2[i,j] += 1.0
            elif  "off" in line:
                grid1[i,j] = 0.0
                if grid2[i,j] > 0.0:
                    grid2[i,j] -= 1.0

print(f"The number of lights that are lit after following the first instructions are: {int(sum(sum(grid1)))}")
print(f"The number of lights that are lit after following the second instructions are: {int(sum(sum(grid2)))}")