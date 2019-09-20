def cost(B):
    maxi, max1 = 0, 0
    for i in range(1,len(B)):
        curr, prev = B[i], B[i-1]
        newmaxi = max(maxi + abs(curr - prev), max1 + (curr - 1))
        newmax1 = max(maxi + abs(1 - prev), max1)
        maxi, max1 = newmaxi, newmax1
    return(max(maxi, max1))


