from numpy import *

arr1 = array([
                [1,2,3,6,2,9],
                [4,5,6,7,5,3]
            ])

arr2 = arr1.flatten()
print(arr1, arr1.dtype, arr1.ndim, arr1.shape, arr1.size)
print(arr2)

arr3 = arr2.reshape(3, 4)
print(arr3)
arr4 = arr2.reshape(2, 2, 3)
print(arr4)