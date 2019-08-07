class Computer:
    def config(self):
        print("i7, 16GB RAM, 500GB HDD")


com1 = Computer()
com2 = Computer()
print(type(com1))

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()
a = 5
print(a.bit_length())