from array import *


val = array('i', [5, 9, 7, -6, 2])
val1 = array('b', [5, 9, -7, 6, 2])
val2 = array('u', ['a', 'b', 'y', 'r'])

print(val)
print(val1)
print(val.buffer_info())
print(val1.typecode)
print(val2)

val.reverse()
print(val)

newArr = array(val.typecode, (a for a in val1))

for e in newArr:
    print(e)