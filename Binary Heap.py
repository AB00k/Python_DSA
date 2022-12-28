# lesson no : 25 Binary Heap

class BinaryHeap:
    def __init__(self, size):
        self.customlist = (size + 1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1


def peekofheap(rootnode):
    if not rootnode:
        return
    return rootnode.customlist[1]


def heapsize(rootnode):
    if not rootnode:
        return
    return rootnode.heapsize


# traveersal functions are same as in binary tree using python
def levelordertraversal(rootnode):
    if not rootnode:
        return
    for i in range(1, rootnode.heapsize + 1):
        print(rootnode.customlist[i])


def heapyifytreeinsert(rootnode, index, heaptype):
    parentindex = int(index / 2)
    if index <= 1:
        return
    if heaptype == 'min':
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
        heapyifytreeinsert(rootnode, parentindex, heaptype)
    elif heaptype == 'max':
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[parentindex] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
        heapyifytreeinsert(rootnode, parentindex, heaptype)


def insertnode(rootnode, nodevalue, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return 'BH is full'
    rootnode.customlist[rootnode.heapsize + 1] = nodevalue
    rootnode.heapsize += 1
    heapyifytreeinsert(rootnode, rootnode.heapsize, heaptype)
    return 'successfully inserted'


# extract a node from binary heap
# note : we can only extract rootnode
def heapifytreeextract(rootnode, index, heaptype):
    leftindex = index * 2
    rightindex = index * 2 + 1
    swapchild = 0
    if rootnode.heapsize < leftindex:
        return
    elif rootnode.heapsize == leftindex:
        if heaptype == 'min':
            if rootnode.customlist[index] > rootnode.customlist[leftindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return
        else:
            if heaptype == 'max':
                if rootnode.customlist[index] < rootnode.customlist[leftindex]:
                    temp = rootnode.customlist[index]
                    rootnode.customlist[index] = rootnode.customlist[leftindex]
                    rootnode.customlist[leftindex] = temp
                return
    else:
        if heaptype == 'min':
            if rootnode.customlist[leftindex] < rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if rootnode.customlist[leftindex] > rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
        else:
            if rootnode.customlist[leftindex] > rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if rootnode.customlist[leftindex] < rootnode.customlist[swapchild]:
                temp = rootnode.customlist[leftindex]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
        heapyifytreeinsert(rootnode, swapchild, heaptype)


def extractnode(rootnode, heaptype):
    if rootnode.heapsize == 0:
        return
    else:
        extractnode = rootnode.customlist[1]
        rootnode.customlist[1] = rootnode.customlist[rootnode.heapsize]
        rootnode.customlist[rootnode.heapsize] = None
        rootnode.heapsize -= 1
        heapifytreeextract(rootnode, 1, heaptype)

    return extractnode


def deletebh(rootnode):
    rootnode.customlist = None


heapnode = BinaryHeap(10)
insertnode(heapnode, 1, 'max')
insertnode(heapnode, 2, 'max')
insertnode(heapnode, 3, 'max')
insertnode(heapnode, 4, 'max')
insertnode(heapnode, 5, 'max')
insertnode(heapnode, 6, 'max')
# extractnode(heapnode,'max')
deletebh(heapnode)
levelordertraversal(heapnode)
