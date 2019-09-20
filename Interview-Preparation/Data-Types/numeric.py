num1 = 2
num2 = 2.5
num3 = 4 + 9j
num4 = True
num41 = num2 < num1

a = int(num2)
c = complex(a, a)


print(num1, type(num1), id(num1))
print(num2, type(num2), id(num2))
print(num3, type(num3), id(num3))
print(a, type(a), id(a))
print(c, type(c), id(c))
print(num4, type(num4), id(num4))
print(num41, type(num41), id(num41))