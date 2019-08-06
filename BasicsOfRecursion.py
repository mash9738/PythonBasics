import sys

print("below section is to under the recursion ")
print("recursion limit modification ")
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0


def greet():
    global i
    i += 1
    print("Hello", i)
    if i <= 50:
        greet()

greet()

print("----------------------------------------------------------")