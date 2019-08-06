from functools import reduce
nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda n: n % 2 ==0, nums))
print(evens)

double = list(map(lambda n: n * 2, evens))

print(double)

sums = reduce(lambda a, b: a + b, double)

print(sums)