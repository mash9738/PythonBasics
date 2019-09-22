g = 2
s = 'hereiamstackerrank'

s1 = list(s)
m = 'hackerrank'
m1 = list(m)
m2 = m
r = ''
r1 = []
k = 0

def hackerrankInString(s):
    # Complete this function
    p = 0
    for e in 'hackerrank':
        if e in s[p:]:
            p = s.index(e,p) + 1
        else:
            return 'NO'
    return 'YES'

q = 'hereiamstackerrank'
hackerrankInString(q)


