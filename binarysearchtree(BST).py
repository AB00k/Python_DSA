#lesson no : 23 binary search tree
#binary search tree using queue + linked list
import queue
class BST:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
#insert a node in BST
def insertnode(rootnode,nodevalue):
    if rootnode.data==None:
        rootnode.data=nodevalue
    elif nodevalue<=rootnode.data:
        if rootnode.leftchild==None:
            rootnode.leftchild=BST(nodevalue)
        else:
            insertnode(rootnode.leftchild,nodevalue)
    else:
        if rootnode.rightchild==None:
            rootnode.rightchild=BST(nodevalue)
        else:
            insertnode(rootnode.rightchild,nodevalue)
    return 'node successfully inderted'

#traversal functions in bt
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
        customqueue=queue.queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root=customqueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)

def searchode(rootnode,nodevalue):
    if rootnode.data==nodevalue:
        return nodevalue
    elif nodevalue<rootnode.data:
        if rootnode.leftchild.data==nodevalue:
            return  nodevalue
        else:
            searchode(rootnode.leftchild,nodevalue)
    else:
        if rootnode.rightchild.data==nodevalue:
            return  nodevalue
        else:
            searchode(rootnode.rightchild,nodevalue)

#delete a node from BST
def minvalue(bstnode):
    currentnode=bstnode
    while currentnode.leftchild is not None:
        currentnode=currentnode.leftchild
    return currentnode
def deletenode(rootnode,nodevalue):
    if rootnode is None:
        return rootnode
    if nodevalue<rootnode.data:
        rootnode.leftchild=deletenode(rootnode.leftchild,nodevalue)
    elif nodevalue>rootnode.data:
        rootnode.rightchild=deletenode(rootnode.rightchild,nodevalue)
    else:
        if rootnode.leftchild is None:
            temp=rootnode.rightchild
            rootnode=None
            return temp
        if rootnode.rightchild is None:
            temp=rootnode.leftchild
            rootnode=None
            return temp
        temp = minvalue(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = deletenode(rootnode.rightchild, temp.data)
    return rootnode

#delete entre binary search tree
def deleteBT(rootnode):
    rootnode.data=None
    rootnode.leftchild=None
    rootnode.rightchild=None
    return 'BT successfully deleted'
newbst=BST(10)
insertnode(newbst,20)
insertnode(newbst,30)
insertnode(newbst,40)
insertnode(newbst,50)
insertnode(newbst,60)
insertnode(newbst,5)
insertnode(newbst,6)
insertnode(newbst,8)
#deletenode(newbst,20)
deleteBT(newbst)
levelordertraversal(newbst)
