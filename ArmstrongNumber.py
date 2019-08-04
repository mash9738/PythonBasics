# abcd... = an + bn + cn + dn + ...
# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


def armstrong_number(ar):
    for i in ar:
        globals()['a'] = int(i)
        globals()['j'] = j + (a * a * a)
    if j == n:
        print(n, "is Armstrong number")
    else:
        print(n, "is not Armstrong number")


for i in range(5):
    n = int(input("Enter the number to Armstrong \n"))
    ar = str(n)
    a=0
    b=0
    j=0
    armstrong_number(ar)
