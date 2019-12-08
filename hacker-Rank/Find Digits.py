
def findDigits(n):
    l = str(n)
    count = 0
    for i in l:
        j = int(i)
        if j <= 0:
            continue
        elif n % j == 0:
            count += 1
    print(count)









findDigits(1012)