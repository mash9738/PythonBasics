#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    n=len(s)
    m=len(t)
    ES=0
    ET=0

    if n > m:
        ES=n - m
    else:
        ET=m - n

    l=0
    for i, j in zip(s, t):
        if i!=j:
            break
        l+=1
    if n==l and s==t:
        UST=0
    elif n > m:
        UST=m - l
    else:
        UST=n - l

    D=ES + UST
    A=ET + UST
    if n==m and s==t:
        return "Yes"
    elif (D + A) <= k:
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
