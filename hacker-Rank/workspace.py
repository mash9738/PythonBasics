A = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#print(A.index('Z'))
s = 'abccddde'
S = s.upper()
S1 = []

for i in range(len(S) - 1):
    b = S[i]
    c = A.index(b)
    S1.append(c)
    print("b:{} c:{} S1{}".format(b, c, S1))
    #print(b, c, S1)
    d = S[i + 1]

    if b == d:
        S1.append(S1[i] + S1 [i])

#print(S1)



