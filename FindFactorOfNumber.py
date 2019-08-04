def factor(x):
    print("The factor of x are : \n")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


a = int(input("Enter a number to find factors = \n"))

factor(a)