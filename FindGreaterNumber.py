M = [9, 6, 231, 8, 2, 98]

N = len(M)


temp = 0
for i in M:
    if i > temp:
        temp = i
    else:
        temp = temp

print("Greater number is ", temp)