from numpy import *

print("***********************************")
print("Array copy used same address memory")
arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1
print(arr1, id(arr1))
print(arr2, id(arr2))
print("************************************")
print("shallow copy used different address but modification apply to other  ")
arr3 = arr1.view()

print(arr1, id(arr1))
print(arr3, id(arr3))

arr1[1] = 7

print(arr1, id(arr1))
print(arr3, id(arr3))

print("**********************************************8")

