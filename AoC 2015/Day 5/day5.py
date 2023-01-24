import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

nice_count1 = 0
forbidden = ["ab", "cd", "pq", "xy"]

for line in lines:
    line = line.rstrip()
    check1 = {x : line.count(x) for x in set("aeiou")}
    check2 = {x : line.count(x) for x in forbidden}
    if sum(check1.values()) >= 3 and sum(check2.values()) == 0:
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                nice_count1 += 1
                break

nice_count2 = 0
for line in lines:
    line = line.rstrip()
    check_count = 0
    flag1 = 0
    flag2 = 0
    for i in range(len(line)):
        sub = line[:i] + line[i+2:]
        if line[i:i+2:] in sub and flag1 == 0:
            check_count += 1
            flag1 = 1
        if i < len(line)-2:
            if line[i] == line[i+2] and flag2 == 0:
                check_count += 1
                flag2 = 1
        if check_count == 2:
            nice_count2 += 1
            break

print(f"The number of strings that are nice in the first model is: {nice_count1}")
print(f"The number of strings that are nice in the second model is: {nice_count2}")