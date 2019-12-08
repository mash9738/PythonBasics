
t = int(input())
max_count = 0
max_index = 0
max_char = ''
max_char_ascii = 0
for p in range(t):
    s=input()
    s1=sorted(s)
    s2=s1
    max_count = 0
    max_index = 0
    max_char = ''
    max_char_ascii = 0
    for i in s1:
        freq = s1.count(i)
        ind_i = s1.index(i)
        if freq > max_count and i != max_char:
            max_count = freq
            max_char = i
            max_index = s1.index(i)
            max_char_ascii = ord(i)
            for j in range(max_count):
                s2.remove(i)
        elif freq == max_count and i != max_char:
            a = ord(i)
            b = ord(max_char)
            if a < b:
                max_count = freq
                max_char = i
                max_index = s1.index(i)
                max_char_ascii = a
                for k in range(max_count):
                    s2.remove(i)
            else:
                max_count = max_count
                max_char = max_char
                max_index = max_index
                max_char_ascii = max_char_ascii
                for l in range(max_count):
                    s2.remove(i)
        elif freq == max_count and i == max_char:
            continue
        else:
            for o in range(freq):
                s2.remove(i)



    print(max_char)



