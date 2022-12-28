from array import *
def count(lst):
    n = int(input('enter the length of an array'))
    for i in range(n):
        list = array('i', [])
        x = int(input('enter list'))
        list.append(x)
        print(list)
    even = 0
    odd = 0
    for i in list:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print('even:{},odd:{}'.format(even, odd))  # or    return even,odd
count(list)  # or even,odd=count(list)
