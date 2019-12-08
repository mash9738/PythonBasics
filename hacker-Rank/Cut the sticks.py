import math
import os
import random
import re
import sys
arr = [5, 4, 4, 2, 2, 8]

def cutTheSticks(arr):
    result = list()
    l = len(arr)
    for k,v in sorted(Counter(arr).items()):
        result.append(l)
        l-=v
    return result
