s = 'fnaaxtyyzzz'


def lowercaseAlphabets():
    d = []
    # lowercase
    for c in range(97, 123):
        d.append(chr(c))
        print(chr(c), end=" ");

    print("");
    print(d)

lowercaseAlphabets()


def uppercaseAlphabets():
    # uppercase
    for c in range(65, 91):
        print(c , end='')
        print(chr(c), end=" ");

    print("");

uppercaseAlphabets()


print(ord("a",))
print(ord('A'))