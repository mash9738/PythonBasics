from collections import *

original_str = deque('abcdefghijklmnopqrstuvwxyz')

k = 87
original_lst = list(original_str)
print(original_lst)
original_str.rotate(-1)
print(original_str)
encr_str = ''
for y in original_str:
    encr_str+=y
print(encr_str)











