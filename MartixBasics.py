from numpy import *
import scipy.linalg


arr1 = array([
    [1, 2, 3, 6],
    [4, 5, 6, 7]
])

print(arr1)

m = matrix('1 1 1; 1 1 1; 1 1 1')
print(m)

m1 = matrix('1 2 3; 6 4 5; 1 6 7')

print(m1)

m2 = m * m1

print(m2)