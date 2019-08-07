class Computer:

    def __init__(self):
        self.name = 'Mahesh'
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

obj1 = Computer()
obj1.age = 30
obj2 = Computer()

obj1.name = "Deepika"
obj1.age = 24

obj1.update()


print(obj1.name, obj1.age)
print(obj2.name, obj2.age)

if obj1.compare(obj2):
    print("they are same")
else:
    print("they are not same")