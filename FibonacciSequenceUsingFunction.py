

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)


def number_check():
    m = int(input("enter the number \n"))
    while m < 0:
        print("Number should greater then 0 \n")
        m = int(input("enter the number \n"))
    else:
        fib(m)

number_check()