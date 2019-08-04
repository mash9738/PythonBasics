num = [5, 3, 8, 6, 7, 2, 1, 0]

n = len(num)


def numsort(num):
    for j in range(n):
        for i in range(n-1):
            if num[i] > num[i+1]:
                a = num[i]
                b = num[i+1]
                num[i] = b
                num[i+1] = a

    print(num)

numsort(num)
