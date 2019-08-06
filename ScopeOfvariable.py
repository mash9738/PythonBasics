

# global variable 'a'
a = 10


def something():
    a = 15
    print('inside the function a =', a)


something()

print('outside a =', a)


def something1():
    global a
    a = 15
    print('inside the function a =', a)


something1()
print('outside a =', a)

print('outside a id', id(a))


def something2():
    a = 9
    x = globals()['a']
    print(id(x))
    print('inside the function a =', a)
    globals()['a'] = 20


something2()
print('outside a =', a)
