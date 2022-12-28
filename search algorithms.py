# SORTING ALGORITHMS
# LESSON NO: 29
import math
# 1: linear search
def linearsearch(list,value):
    for i in range(len(list)):
        if list[i]==value:
            return value
    return -1
# 2: Binary search
def binarysearch(list,value):
    start=0
    end=len(list)-1
    middle=math.floor((start+end)/2)
    while not(list[middle]==value):
        if value<list[middle]:
            end=middle-1
        else:
            start=middle+1
        middle = math.floor((start + end) / 2)
    if list[middle]==value:
        return middle
    else:
        return 'not fond'
sortedlist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(binarysearch(sortedlist,5))

