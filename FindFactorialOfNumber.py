num = 0
fact = 1


if num == 0:
    fact = 1
    print('factorial of {}'.format(num), 'is', fact)
else:
    for i in range(0, (num + 1)):
        if i == 0:
            pass
        else:
            fact = fact * i
    print('factorial of {}'.format(num), 'is', fact)