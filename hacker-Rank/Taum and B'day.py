b = 5
w = 9

bc = 2
wc = 3
z = 4

R = 0

if bc <= z and wc <= z:
    R = (b * bc) + (w * wc)
    print(R)

if bc > wc and bc > z and z <= wc:
    R = (z * b) + ((b + w) * wc)
    print(R)





