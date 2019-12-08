a = -5
print(a)
print(abs(a))

iterable1 = 'Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:'


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


print(all(iterable1))


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


print(any(iterable1))

print(repr('asdd'))
print(ascii('asdf'))

print(bin(10))
print(format(10, '#b'), format(10, 'b'))
print(bool(0))