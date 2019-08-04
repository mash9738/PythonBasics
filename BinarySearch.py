pos = -1


def binary_search(list1, n):
    l = 0
    u = len(list1) - 1

    while l <= u:
        mid = (l + u) // 2

        if list1[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list1[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False





list1 = [4, 7, 8, 12, 45, 99]
n = 45

if binary_search(list1, n):
    print(n, "is found at", pos)
else:
    print("Not Found")