pos = -1


def binary_search_for(list2, m):
    l = 0
    u = len(list2) - 1
    mid = (l + u) // 2

    for i in range(mid):
        for j in range(mid):
            if list2[mid] == m:
                globals()['pos'] = mid
                return True
            else:
                if list2[mid] < m:
                    l = mid + 1
                else:
                    u = mid - 1
            mid = (l + u) // 2
    return False



list2 = [4, 7, 8, 12, 45, 99]
m = 4

if binary_search_for(list2, m):
    print("Found at", pos)
else:
    print("Not Found")