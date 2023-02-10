import os
import sys
import json
from itertools import repeat

with open(os.path.join(sys.path[0], "input.json"), "r") as f:
    data = json.load(f)
f.close()

def find_ints(data, part):
    if isinstance(data, dict):
        if "red" in data.values() and part==2:
            return 0
        return sum(map(find_ints, data.values(), repeat(part)))
    if isinstance(data, list):
        return sum(map(find_ints, data, repeat(part)))
    if isinstance(data, int):
        return data
    return 0

print(f"The sum of all numbers in the document is: {find_ints(data,1)}")
print(f"The sum of all numbers in the document, ignoring any object with the value \"red\" is: {find_ints(data,2)}")

