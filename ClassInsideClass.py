class Student:
    def __init__(self, name, roleno):
        self.name = name
        self.roleno = roleno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roleno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "I5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Mahesh', 2)
s2 = Student('deepi', 3)


s1.show()
s2.show()

lap1 = s1.lap
lap2 = s2.lap
