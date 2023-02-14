import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
f.close()

ingredients = []
for line in lines:
    line = line.rstrip()
    line = line.split()
    name = line[0][:-1]
    capacity = int(line[2][:-1])
    durability = int(line[4][:-1])
    flavor = int(line[6][:-1])
    texture = int(line[8][:-1])
    calories = int(line[-1])
    ingredients.append([name, capacity, durability, flavor, texture, calories])

max_score = 0
max_score2 = 0
for i in range(0,101):
    for j in range(0,101-i):
        for k in range(0,101-i-j):
            l = 100-i-j-k
            capacity_score = ingredients[0][1]*i + ingredients[1][1]*j + ingredients[2][1]*k + ingredients[3][1]*l
            durability_score = ingredients[0][2]*i + ingredients[1][2]*j + ingredients[2][2]*k + ingredients[3][2]*l
            flavor_score = ingredients[0][3]*i + ingredients[1][3]*j + ingredients[2][3]*k + ingredients[3][3]*l
            texture_score = ingredients[0][4]*i + ingredients[1][4]*j + ingredients[2][4]*k + ingredients[3][4]*l
            calories_score = ingredients[0][5]*i + ingredients[1][5]*j + ingredients[2][5]*k + ingredients[3][5]*l

            if capacity_score <= 0 or durability_score <= 0 or flavor_score <= 0 or texture_score <= 0:
                total_score = 0
            else:
                total_score = capacity_score*durability_score*flavor_score*texture_score
            if total_score > max_score2 and calories_score == 500:
                    max_score2 = total_score
                    ingredient_amount2 = [i, j, k, l]
            if total_score > max_score:
                max_score = total_score
                ingredient_amount = [i, j, k, l]

print(f"The total score of the highest scoring cookie is: {max_score}, with the ingredient amount: {ingredient_amount}")
print(f"The total score of the highest scoring cookie with exactly 500 calories is: {max_score2}, with the ingredient amount: {ingredient_amount2}")