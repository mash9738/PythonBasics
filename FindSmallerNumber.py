M = [9, 6, 231, 8, 2, 98, 0]

N = len(M)


temp = M[0]
for i in M:
    if i < temp:
        temp = i
    else:
        temp = temp

print("Smaller number is ", temp)