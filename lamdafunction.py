terms = int(input("Enter the terms: \n"))

result = list(map(lambda x: 2 ** x, range(terms)))
print("the total terms is : ", terms)
for i in range(terms):
    print(" 2 raised to power ", i, "is", result[i])


my_list = [12, 65, 54, 39, 102, 339, 221]
result1 = list(filter(lambda x: (x % 13 == 0), my_list))
print(result1)