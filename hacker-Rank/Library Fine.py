d1 = 6
m1 = 6
y1 = 2015

d2 = 9
m2 = 6
y2 = 2016


if y1 == y2 and m1 == m2 and d1 <= d2:
    print(0)
elif y1 == y2 and m1 == m2 and d1 > d2:
    f = 15 * (d1 - d2)
    print(f)
elif y1 == y2 and m1 < m2:
    print(0)
elif y1 == y2 and m1 > m2:
    f = 500 * (m1 - m2)
    print(f)
elif y1 < y2:
    print(0)
elif y1 > y2:
    f = 10000
    print(f)







