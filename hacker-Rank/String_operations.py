s = "hackerrankhappy"

k = 'h'

for i in s:
    print(i, end='')
print("\n**************************************************")
j = 0
while j < len(s):
    print(s[j], end='')
    j += 1
print("\n**************************************************")

for i in s:
    print(i, end='')

print("\n**************************************************")

for l in range(len(s)-1):
    if s[l] == k:
        pos = l
        print("Found at ", pos)


print("\n**************************************************")
for p in range(len(s)-1):
    if p == k:
        pos1 = s.index(p)
        print("Found at ", pos1)


s = "hackerhappy"
s1 = list(s)
print("S1=:", s1)
t = "hackerrank"
t1 = list(t)
print("t1=:", t1)
k = '9'
i = 0
for a, b in zip(s1, t1):
    if a != b:
        s1[i] = t1[i]
    i += 1
print(s1)

if len(s1) > len(t1):
    l = len(s1) - len(t1)
    for e in range(len(t1), len(s1)):
        print(e)
        s1.remove(s1[e])


if len(s1) == len(t1) and s1 == t1:
    new=""
    for x in s1:
        new+=x
    print(new)












# Complete the appendAndDelete function below.


