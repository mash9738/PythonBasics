import re
r, p = 4, 2
s = [1, 1, 0, 0]
s1 = []

d = r//2
series_win = d + 1
e = series_win - p
if series_win == p:
    start = p
elif series_win < p:
    start = p + e

for i in range(p, r):
    s1.append(0)

print(s1)

for i in s1:
