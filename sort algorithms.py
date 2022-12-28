# SORTING ALGORITHMS
# LESSON NO:
import math

# 1: Bubble Sort
def bubblesort(customlist):
    for i in range(len(customlist) - 1):
        for j in range(len(customlist) - i - 1):
            if customlist[j] > customlist[j + 1]:
                customlist[j], customlist[j + 1] = customlist[j + 1], customlist[j]
    print(customlist)

# 2: selectionsort
def selectionsort(customslist):
    for i in range(len(customslist)):
        minindex = i
        for j in range(i + 1, len(customslist)):
            if customslist[minindex] > customslist[j]:
                minindex = j
        customslist[i], customslist[minindex] = customslist[minindex], customslist[i]
    print(customslist)

# 3: insertion sort
def insertionsort(customlist):
    for i in range(1, len(customlist)):
        key = customlist[i]
        j = i - 1
        while j >= 0 and key < customlist[j]:
            customlist[j + 1] = customlist[j]
            j -= 1
        customlist[j + 1] = key
    return customlist

# 4: Bucket sort
def bucketsort(customlist):
    noofbuckets = round(math.sqrt(len(customlist)))
    maxvalue = max(customlist)
    arr = []
    for i in range(noofbuckets):
        arr.append([])
    for j in customlist:
        index = math.ceil(j * noofbuckets / maxvalue)
        arr[index - 1].append(j)
    for i in range(noofbuckets):
        arr[i] = insertionsort(arr[i])
    k = 0
    for i in range(noofbuckets):
        for j in range(len(arr[i])):
            customlist[k] = arr[i][j]
            k += 1
    return customlist

# 5: Merge sort
def merge(customlist, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = customlist[l + i]
    for j in range(0, n2):
        R[j] = customlist[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customlist[k] = L[i]
            i += 1
        else:
            customlist[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customlist[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customlist[k] = R[j]
        j += 1
        k += 1


def mergesort(customlist, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergesort(customlist, l, m)
        mergesort(customlist, m + 1, r)
        merge(customlist, l, m, r)
    return customlist

# 6: Quick sort
def partition(customlist, low, high):
    i = low - 1
    pivot = customlist[high]
    for j in range(low, high):
        if customlist[j] <= pivot:
            i += 1
            customlist[i], customlist[j] = customlist[j], customlist[i]
    customlist[i + 1], customlist[high] = customlist[high], customlist[i + 1]
    return (i + 1)


def quicksort(customlist, low, high):
    if low < high:
        pi = partition(customlist, low, high)
        quicksort(customlist, low, pi - 1)
        quicksort(customlist, pi + 1, high)
    return customlist

# 7: Heap sort
def heapify(customlist,n,i):
    smallest=i
    L=2*i+1
    R=2*i+2
    if L < n and customlist[L]<customlist[smallest]:
        smallest=L
    if R<n and customlist[R]<customlist[smallest]:
        smallest=R
    if smallest !=i:
        customlist[i],customlist[smallest]=customlist[smallest],customlist[i]
        heapify(customlist,n,smallest)
def heapsort(customlist):
    n=len(customlist)
    for i in range(int(n/2)-1,-1,-1):
        heapify(customlist,n,i)
    for i in range(n-1,0,-1):
        customlist[i],customlist[0]=customlist[0],customlist[i]
        heapify(customlist,i,0)
    customlist.reverse()
    return customlist
list = [2, 3, 6, 8, 4, 7, 5, 9, 10, 12, 14, 11, 1 , 13]
print(heapsort(list))

