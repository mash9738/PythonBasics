from array import *

a = array('i', [1, 2, 332, 4, 1, 3, 1, 1, 3])
print(a, type(a))
a.append(5)
print(a, type(a))
a.remove(1)
print(a, type(a))
a.insert(1, 33)
print(a, type(a))
print(a.index(33))
print(a.count(1))
d = a.reverse()
print(d, type(d))
print(a.buffer_info())