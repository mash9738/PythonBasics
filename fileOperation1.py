f = open("mydata.txt", 'r')
#print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline(1000))
print(f.readlines())

f1 = open("mydata1.txt", 'w')

f1.write('New Name')


f2 = open('mydata1.txt', 'a')

f2.write('\nOld Name')
