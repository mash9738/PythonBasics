
def person(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)


person('mahesh', age=28, city='managalore', mob=9756789, office='MF')