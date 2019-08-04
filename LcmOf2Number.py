def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm1 = greater
            break
        greater += 1
    return lcm1


num1 = int(input("numb1: \n"))
num2 = int(input("numb2: \n"))
print(" the lcm of ", num1, "and ", num2, "is ", lcm(num1, num2))

