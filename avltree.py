# lesson no : 24 avl tree
# avl tree using queue + linked list
import queue

class avltree:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

# traversal functions in avl
def preordertraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)

def inordertraversal(rootnode):
    if not rootnode:
        return
    preordertraversal(rootnode.leftchild)
    print(rootnode.data)
    preordertraversal(rootnode.rightchild)


def postordertraversal(rootnode):
    if not rootnode:
        return
    preordertraversal(rootnode.leftchild)
    preordertraversal(rootnode.rightchild)
    print(rootnode.data)


def levelordertraversal(rootnode):
    if not rootnode:
        return
    else:
        customqueue = queue.queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)


def searchode(rootnode, nodevalue):
    if rootnode.data == nodevalue:
        return nodevalue
    elif nodevalue < rootnode.data:
        if rootnode.leftchild.data == nodevalue:
            return nodevalue
        else:
            searchode(rootnode.leftchild, nodevalue)
    else:
        if rootnode.rightchild.data == nodevalue:
            return nodevalue
        else:
            searchode(rootnode.rightchild, nodevalue)


def getHeight(rootnode):
    if not rootnode:
        return 0
    else:
        return rootnode.height


def rightrotate(disbalancednode):
    newroot = disbalancednode.leftchild
    disbalancednode.leftchild = disbalancednode.leftchild.rightchild
    newroot.rightchild = disbalancednode
    disbalancednode.height = 1 + max(getHeight(disbalancednode.leftchild), getHeight(disbalancednode.rightchild))
    newroot.height = 1 + max(getHeight(newroot.leftchild), getHeight(newroot.rightchild))
    return newroot


def leftrotate(disbalancednode):
    newroot = disbalancednode.rightchild
    disbalancednode.rightchild = disbalancednode.rightchild.leftchild
    newroot.leftchild = disbalancednode
    disbalancednode.height = 1 + max(getHeight(disbalancednode.leftchild), getHeight(disbalancednode.rightchild))
    newroot.height = 1 + max(getHeight(newroot.leftchild), getHeight(newroot.rightchild))
    return newroot


def getbalance(rootnode):
    if not rootnode:
        return
    else:
        return (getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild))


def insertnode(rootnode, nodevalue):
    if not rootnode:
        return avltree(nodevalue)
    elif nodevalue < rootnode.data:
        rootnode.leftchild = insertnode(rootnode.leftchild, nodevalue)
    else:
        rootnode.rightchild = insertnode(rootnode.rightchild, nodevalue)
    rootnode.height = 1 + max(getHeight(rootnode.leftchild), getHeight(rootnode.rightchild))
    balance = getbalance(rootnode)
    if balance > 1 and nodevalue < rootnode.leftchild.data:
        return rightrotate(rootnode)
    if balance > 1 and nodevalue > rootnode.leftchild.data:
        rootnode.leftchild = leftrotate(rootnode.leftchild)
        return rightrotate(rootnode)
    if balance < -1 and nodevalue > rootnode.rightchild.data:
        return leftrotate(rootnode)
    if balance < -1 and nodevalue < rootnode.rightchild.data:
        rootnode.rightchild = rightrotate(rootnode.rightchild)
        leftrotate(rootnode)
    return rootnode


def getminvalue(rootnode):
    if rootnode is None or rootnode.leftchild is None:
        return rootnode
    return getminvalue(rootnode.leftchild)


def deletenode(rootnode, nodevalue):
    if not rootnode:
        return rootnode
    elif nodevalue < rootnode.data:
        rootnode.leftchild = deletenode(rootnode.leftchild, nodevalue)
    elif nodevalue > rootnode.data:
        rootnode.rightchild = deletenode(rootnode.rightchild, nodevalue)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        elif rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp

        temp = getminvalue(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = deletenode(rootnode.rightchild, temp.data)
    balance = getbalance(rootnode)
    if balance > 1 and getbalance(rootnode.leftchild) >= 0:
        return rightrotate(rootnode)
    if balance < -1 and getbalance(rootnode.rightchild) <= 0:
        return leftrotate(rootnode)
    if balance > 1 and getbalance(rootnode.leftchild) < 0:
        rootnode.leftchild = leftrotate(rootnode.leftchild)
        return rightrotate(rootnode)
    if balance < -1 and getbalance(rootnode.rightchild) > 0:
        rootnode.rightchild = rightrotate(rootnode.rightchild)
        return leftrotate(rootnode)
    return rootnode


def deleteentireavl(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None


newavl = avltree(10)
newavl = insertnode(newavl, 20)
newavl = insertnode(newavl, 30)
newavl = insertnode(newavl, 40)
newavl = insertnode(newavl, 50)
newavl = insertnode(newavl, 60)
newavl = deleteentireavl(newavl)
newavl = levelordertraversal(newavl)
