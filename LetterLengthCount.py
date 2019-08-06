N = int(input("Enter the number of users \n"))
Names = []
for i in range(N):
    Name = input("Enter user names: \n")
    Names.append(Name)


print(Names)

a = []
for j in Names:
    b = 0
    b = len(j)
    if b > 5:
        print('{} is more then 5 letter and length of {} is equal to {}'.format(j, j, b))

