numbers = [5, 5, 1, 2, 3, 3, 4]    #amazing question
num = []  #empty list
for number in numbers:
    if number not in num:
        num.append(number)
num.sort()
print(num)


