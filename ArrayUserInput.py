from array import *

arr = array('i', [])

n = int(input("Enter the length of array\n"))

for i in range(n):
    x = int(input("Enter the next value \n"))
    arr.append(x)


print(arr)
val = int(input("Enter value for search \n"))
for j in arr:
    if j == val:
        print(val, "present at", arr.index(j))