number = int(input("Enter Number: \n"))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Number not Prime")
            break
    else:
        print("Number is Prime")

else:
    print("Number is not prime")


lower = 900
upper = 1000
prime_number =[]
print("Prime number between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            j = 0
            if (num % i) == 0:
                print("{} is Prime".format(num))
                prime_number.append(num)
                j += 1
                break
        else:
            print("{} is Not Prime".format(num))
print(prime_number)