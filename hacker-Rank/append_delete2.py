#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    end=0
    for i in range(min(len(t), len(s))):
        if s[i]==t[i]:
            end+=1
        else:
            break

    maxIter=len(s) + len(t)
    minIter=maxIter - (2 * end)
    if (k >= minIter) & ((k - minIter) % 2==0):
        return "Yes"
    elif k >= maxIter:
        return "Yes"
    else:
        return "No"


if __name__=='__main__':
    fptr=open(os.environ['OUTPUT_PATH'], 'w')

    s=input()

    t=input()

    k=int(input())

    result=appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
