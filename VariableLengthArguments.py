# -----formal arguments--------------
def add(a, *b):
    print('add(a, b): *b are variable length arguments')
    c = a
    for i in b:
        c = c + i
    print(c)

add(5, 6, 34, 78)


print('*************************************************')

def sum(*a):
    c = 0
    for i in a:
        c = c + i
    print(c)

    
sum(5, 6, 34, 78)