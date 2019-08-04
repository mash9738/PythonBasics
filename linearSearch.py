list1 = [5, 8, 4, 5, 3, 6, 9, 2]
m = 3
pos = -1


def linear_search(list1, m):
    for i in list1:
        if i == m:
            a = list1.index(i)
            globals()['pos'] = a
            return True
    return False


if linear_search(list1, m):
    print(m, "is Found at", pos, "position on the given list")
else:
    print("Not Found")