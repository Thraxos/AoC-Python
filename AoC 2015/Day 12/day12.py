import os
import sys
import json

with open(os.path.join(sys.path[0], "input.json"), "r") as f:
    data = json.load(f)
f.close()

def find_ints(list_type, total=0):
    for element in list_type:
        if isinstance(element, int):
            total += element
        elif isinstance(element, dict):
            total += sum(x for x in element.values() if isinstance(x,int))
        else:
            total += find_ints(element, total)
    return total

print(find_ints(data))