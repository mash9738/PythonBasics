
numbers = [1,2,1,3,4,4,5,67,34,45,32,1,2,4,5,98, 23, 0, 7, 6, 0]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
    else:
        pass
uniques.sort()
print(uniques)