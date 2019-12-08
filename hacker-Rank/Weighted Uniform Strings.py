def weightedUniformStrings(s, queries):
    t=s[0]
    acc=-(ord(t) - 96)
    tot={}
    for i in s:
        if i ==t:
            acc+=ord(i) - 96
            tot[ord(i) - 96+acc if i != 0 else ord(i) - 96]=0
        else:
            acc=0
            tot[ord(i) - 96+acc]=0
        t=i
    return ['Yes' if i in tot else 'No' for i in queries]


weightedUniformStrings('abccddde', 1)