n=0


def age_calc(a):
    age = 2019 - int(a)
    print(age)


while n <= 5:
    birth_year = input('Enter Birth year in YYYY format:\n ')
    age_calc(birth_year)
    n += 1