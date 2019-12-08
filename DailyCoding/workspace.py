alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


def main():
    t = int(input())
    while t < 0:
        t = int(input())
    while t > 10:
        t = int(input())
    for j in range(1, t+1):
        st = input().lower()
        s=''.join(filter(str.isalpha, st))
        s1 = sorted(s)
        max_count = 0
        max_char = ''
        for i in s1:
            freq = s1.count(i)
            if max_char != i:
                if freq < max_count:
                    max_count = max_count
                    max_char = max_char
                elif freq > max_count:
                    max_count = freq
                    max_char = i
                elif freq == max_count:
                    a = ord(i)
                    b = ord(max_char)
                    if a < b:
                        max_count = freq
                        max_char = i
                    elif b < a:
                        max_count = max_count
                        max_char = max_char
            else:
                continue

        print(max_char)



main()




