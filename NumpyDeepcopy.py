from numpy import *

print("***********************************")
print("Array copy used same address memory")
arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1
print(arr1, id(arr1))
print(arr2, id(arr2))
print("************************************")

print("Deep copy used different memory address and change of one array will not affect other")

arr3 = arr1.copy()
arr1[2] = 9
print(arr1, id(arr1))
print(arr3, id(arr3))
print("************************************")