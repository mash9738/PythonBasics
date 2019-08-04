num = [5, 3, 8, 6, 7, 2]
n = len(num)


def selsort(num):
    for i in range(n-1):
        minpos = i
        for j in range(i, n):
            if num[j] < num[minpos]:
                minpos = j

        temp = num[i]
        num[i] = num[minpos]
        num[minpos] = temp

    return num


print(selsort(num))