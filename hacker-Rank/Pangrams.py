def pangrams(s):
    C=s
    C1=''
    A=['A', 'B', 'C', 'D', 'E', 'F', 'G',
       'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in C:
        if i==' ':
            pass
        else:
            C1+=i

    C2=C1.upper()
    D=sorted(C2)
    E=[]
    for i in range(len(D) - 1):
        if D[i]!=D[i + 1]:
            E.append(D[i])

    E.append(D[len(D) - 1])

    if A==E:
        return 'pangram'
    else:
        return 'not pangram'


if __name__=='__main__':
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    s=input()

    result=pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
