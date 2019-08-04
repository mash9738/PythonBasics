M = [9, 6, 231, 8, 2, 98, 0, 43]

N = len(M)
M1 = []
j = N - 1
for i in range(N):
    M1.append(M[j])
    j -= 1
print("Input Number   :", M)
print("Revered Number :", M1)