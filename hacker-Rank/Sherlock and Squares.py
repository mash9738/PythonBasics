import math
a = 465868129
b = 988379794
count = 0

for _ in range(a, b):
    count = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
print(count)

