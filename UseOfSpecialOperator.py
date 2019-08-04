import math
x = 2.8976
y = 2.46666
print(round(x))
print(round(y))

n = 0


def rounding_number():
    a = input('enter rounding number: \n')
    b = float(a)
    print(round(b),'\n')


def abs_number():
    a = input('enter rounding number: \n')
    b = float(a)
    print(abs(b), '\n')


def ceil_number():
    a = input('enter rounding number: \n')
    b = float(a)
    print(math.ceil(b), '\n')


def floor_number():
    a = input('enter rounding number: \n')
    b = float(a)
    print(math.floor(b), '\n')


while n <= 5:
    floor_number()
    n += 1