import hashlib

input = "ckczppom"

num = 1
flag = 0

while True:
    key = input + str(num)
    result = hashlib.md5(key.encode())
    hex = result.hexdigest()
    if str(hex).startswith("00000") and flag == 0:
        num1 = num
        flag = 1
    elif str(hex).startswith("000000"):
        num2 = num
        break
    num += 1

print(f"The lowest number the key combines with to make an MD5 hash starting with five zeroes is: {num1}")
print(f"The lowest number the key combines with to make an MD5 hash starting with six zeroes is: {num2}")