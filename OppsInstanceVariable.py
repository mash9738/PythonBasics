class Car:

    def __init__(self):
        print("mil and com is instance variable")
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

print(c1.com, c1.mil)
print(c2.com, c2.mil)