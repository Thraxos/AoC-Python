input = "hepxcrrq"

numlist = [ord(char)-96 for char in input]

forbidden = [ord("i") - 96, ord("o") - 96, ord("l") - 96]

flag = False

while True:
    valid_check_1 = False
    valid_check_2 = False
    valid_check_3 = False

    check = [numlist[0]]
    for i in range(1,len(numlist)):
        if numlist[i-1]+1 == numlist[i]:
            check.append(numlist[i])
        else:
            check = [numlist[i]]
        if len(check) == 3:
            valid_check_1 = True
            break
    
    if not any(x in numlist for x in forbidden):
        valid_check_2 = True

    doubles = []
    prev = numlist[0]
    for i in numlist[1:]:
        if i == prev:
            doubles.append(i)
        if len(doubles) >= 2 and len(set(doubles)) != 1:
            valid_check_3 = True
            break
        prev = i

    if valid_check_1 and valid_check_2 and valid_check_3:
        if flag==False:
            numlist1 = numlist.copy()
            flag = True
        elif flag == True:
            numlist2 = numlist.copy()
            break
    numlist[-1] += 1
    for i in range(len(numlist)-1,0,-1):
        if numlist[i] == 27:
            numlist[i] = 1
            numlist[i-1] += 1

password1 = ""
for i in numlist1:
    char = chr(i+96)
    password1 = password1 + char
password2 = ""
for i in numlist2:
    char = chr(i+96)
    password2 = password2 + char

print(f"The first password is: {password1}")
print(f"The second password is: {password2}")