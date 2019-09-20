import math
import os
import random
import re
import sys
m = 25

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    a = 1
    for i in range(1, n+1):
        a = a * i
    print(a)
    print(type(a))

extraLongFactorials(m)