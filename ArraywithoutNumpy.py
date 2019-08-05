from array import *

arr = array('i', [1,2,3])

print(arr)
print(arr.index(1))
arr.append(4)
print(arr)
print(arr.typecode)
print(arr.buffer_info())
arr1 = array.reverse(arr)
arr2 = arr
print(arr2)

arr3 = arr + arr2

print(arr3)