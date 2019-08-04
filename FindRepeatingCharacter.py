def rec_char(my_list):
    for j in my_list:
        print(j)
        a = my_list.index(j)
        print(a)
        for k in my_list:
            print(k)
            b = my_list.index(k)
            print(b)
            if j == k:
                globals()['new_list'].append(k)
    print("result", new_list)


my_list = ['u', 's', 'q', 'a', 'b', 'u', 'h', 'q']
copy_my_list = my_list
new_list = []
k = 0
for i in my_list:
    print(i)
    if i == my_list[k]:
        print(i,k, my_list[k])
        new_list.append(i)
        k += 1
    k += 1
    print(new_list)