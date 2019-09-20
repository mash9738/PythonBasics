g = 2
s = 'hereiamstackerrank'
s1 = list(s)
m = 'hackerrank'
m1 = list(m)
r = ''
r1 = []
k = 0
for i in m:
    for j in m1:
        if i == j:
            r1.append(j)
            m1.remove(k)


