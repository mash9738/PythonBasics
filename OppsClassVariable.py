class Car:

    wheels = 4
    print("wheels is Class variable")

    def __init__(self):
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 23

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)