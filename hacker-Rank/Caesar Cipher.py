import math
import os
import random
import re
import sys
from collections import deque



def caesarCipher(s, k):
    rotated_str = ''
    encr_str = ''
    encr_lst = []
    junk = []
    n = len(s)
    print(n)
    original = deque('abcdefghijklmnopqrstuvwxyz')
    original_str = 'abcdefghijklmnopqrstuvwxyz'
    original.rotate(-k)
    for y in original:
        rotated_str += y
    for i in s:
        for j in original_str:
            if i.isalpha():
                if i == j:
                    a = original_str.index(j)
                    b = rotated_str[a]
                    encr_lst.append(b)
                elif i == j.capitalize():
                    d = original_str.index(j)
                    e = rotated_str[d]
                    f = e.capitalize()
                    encr_lst.append(f)
            else:
                encr_lst.append(i)
                break

    for y in encr_lst:
        encr_str += y
    print(encr_str)




caesarCipher('deepikamahesh', 26)
