import re
b = '01010010'
def rep(b):
    return len(re.findall('010',b))

a = rep(b)
print(a)