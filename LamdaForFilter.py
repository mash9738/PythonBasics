nums = [3, 2, 6, 8, 4, 2, 9]

evens = list(filter(lambda n: n , nums))
print(evens)



functions = []
for i in range(10):
    functions.append(lambda i : i + 1)

for f in functions:
    print(f())

print(functions)