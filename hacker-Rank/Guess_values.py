x = ('a', 'b', 'c', 'd', 'e')
y = (1, 2, 3, 4, 5)
A0 = dict(zip(x, y))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i, i*i] for i in A1]
print("A0=:", A0)
print("A1=:", A1)
print("A2=:", A2)
print("A3=:", A3)
print("A4=:", A4)
print("A5=:", A5)
print("A6=:", A6)