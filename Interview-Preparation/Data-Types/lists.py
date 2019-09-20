lst = [1, 2.5, 'mahesh']
lst2 = [6, 2.7, 'naveesh', lst]
print(type(lst[0]))
print(type(lst[1]))
print(type(lst[2]))
print(type(lst2[3]))

print(lst, type(lst), id(lst))
print(lst2, type(lst2), id(lst2))
print(lst.count(1))
print(lst.index(1))
lst.insert(1, 34)
print(lst)
lst.reverse()
print(lst)
lst.pop(1)
print(lst)
lst.remove('mahesh')
print(lst)