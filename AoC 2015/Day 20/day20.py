import math

input = 33100000

for house1 in range(2, input):
    sum = 10
    for i in range(2,int(math.sqrt(house1))+1):
        if house1 % i == 0:
            if house1 / i != i:
                sum += (i*10) + (house1/i)*10
            else:
                sum += (i*10)
    sum += (house1*10)
    if int(sum) >= input:
        break

print(f"The lowest house number to get at least as many presents as the input is: {house1}")


for house1 in range(2, input):
    sum = 11
    for i in range(2,50):
        if house1 % i == 0:
            if house1 / i != i:
                sum += (i*11) + (house1/i)*11
            else:
                sum += (i*11)
    sum += (house1*11)
    if int(sum) >= input:
        break

print(f"The new lowest house number to get at least as many presents as the input is: {house1}")