s ='AABABAABABB'
S = list(s)
S1 = S
j = 0
for i in range(len(S)+1):
    if S[i] == S[i+1]:
        S.remove(S[i])
        print(S)

print(S)
