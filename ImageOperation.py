f = open('Tiger.jpeg', 'rb')

f1 = open('Newtiger.png', 'wb')

for imag in f:
    f1.write(imag)