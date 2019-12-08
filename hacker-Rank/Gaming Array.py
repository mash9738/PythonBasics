arr = [1, 3, 5, 7, 9]
def gamingArray(arr):
    players = ['BOB', 'ANDY']
    i = 0; max_e = 0
    for j in arr:
        if j > max_e:
            max_e = j
            i+=1
    return players[not bool(i%2)]



a  = gamingArray(arr)
print(a)
