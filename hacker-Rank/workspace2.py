def shift_left(n):
    original_str = 'abcdefghijklmnopqrstuvwxyz'
    lst = list(original_str)

    assert (n > 0), "n should be non-negative integer"

    def shift(ntimes):
        if ntimes == 0:
            return
        else:
            temp = lst[0]
            for index in range(len(lst) - 1):
                lst[index] = lst[index + 1]
            lst[index + 1] = temp
            return shift(ntimes-1)

    return shift(n)


a = shift_left(2)
print(a)