import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

with open(os.path.join(sys.path[0], "molecule.txt"), "r") as f:
    molecule = f.readlines()
f.close()

molecule = molecule[0]
replacements = set()

for line in lines:
    line = line.rstrip()
    line = line.split(" => ")
    replace_this, with_this = line
    positions = [i for i in range(len(molecule)) if molecule.startswith(replace_this, i)]
    for index in positions:
        new_molecule = molecule[0:index] + with_this + molecule[index+len(replace_this):]
        replacements.add(new_molecule)

print(f"The number of distincts molecules that can be created is: {len(replacements)}")

current_molecule = molecule
steps = 0
while current_molecule != "e":
    for line in lines:
        line = line.rstrip()
        line = line.split(" => ")
        replace_this, with_this = line
        positions = [i for i in range(len(current_molecule)) if current_molecule.startswith(with_this, i)]
        while len(positions) > 0:
            current_molecule = current_molecule[0:positions[0]] + replace_this + current_molecule[positions[0]+len(with_this):]
            steps += 1
            positions = [i for i in range(len(current_molecule)) if current_molecule.startswith(with_this, i)]

print(f"The fewest number of steps to go from e to the medicine molecule is: {steps}")