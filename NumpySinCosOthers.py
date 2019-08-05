from numpy import *

arr = array([1, 2, 3, 4, 5])
arr1 = array([1, 30, 60, 90, 120, 180, 270, 360])

print(sin(arr))
print(cos(arr))
print(tan(arr))
print(sinh(arr))
print(cosh(arr))
print(tanh(arr))
print(log(arr))
print(sum(arr))
print(min(arr), max(arr))
print(concatenate([arr, arr1]))
print("--------------------------------------------")
print(sin(arr1))
print(cos(arr1))
print(tan(arr1))