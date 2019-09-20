s = 'SOSSOT'
n = len(s)
print(n)
k = 3
m = n // k
print(m)
com = 'SOS'
orginal = m * com
print(orginal)
dif = 0
for i, j in zip(s, orginal):
    if i != j:
        dif += 1

print(dif)
