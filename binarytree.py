#lesson no : 22 binary tree
#binary tree using linked list

import queue

class Treenode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

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
#search for a node in bt
def searchbt(rootnode,nodevalue):
    if not rootnode:
        return
    else:
        customqueue = queue.queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value.data==nodevalue:
                return root.value.data
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)
            else:
                return 'not found'

#insert a node in bt (little issue)
def insertnodebt(rootnode,newnode):
    if not rootnode:
        return
    else:
        customqueue = queue.queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild=newnode
                return 'node successfully inserted'
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newnode
                return 'node successfully inserted'

#delete a node from bt (little issue)
def getdeepestnode(rootnode):
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
            deepestnode=root.value
            return deepestnode
def deletedeepestnode(rootnode,dnode):
    if not rootnode:
        return
    else:
        customqueue=queue.queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root=customqueue.dequeue()
            if root.value is dnode:
                root.value=None
                return
            if root.value.rightchild:
                if root.value.rightchild==dnode:
                    root.value.rightchild=None
                    return
            else:
                if root.value.leftchild:
                    if root.value.leftchild == dnode:
                        root.value.leftchild = None
                        return
def deletenodebt(rootnode,node):
    if not rootnode:
        return
    else:
        customqueue = queue.queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value.data==node:
                dnode=getdeepestnode(rootnode)
                root.value.data=dnode.data
                deletedeepestnode(rootnode,dnode)
                return 'sucessfully deleted'
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)
            return 'faild to delete'

#delete bt
def deletebt(rootnode):
    rootnode.data=None
    rootnode.leftchild.data = None
    rootnode.rightchild.data=None
    return "successfully deleted bt"

newbt = Treenode('Drinks')
hot = Treenode('hot')
cold = Treenode('cold')
newbt.leftchild = hot
newbt.rightchild = cold
cofee = Treenode('cofee')
tea = Treenode('tea')
hot.leftchild = cofee
hot.rightchild = tea
alcholic = Treenode('alcholic')
nonalcholic = Treenode('non-alcholic')
cold.leftchild = alcholic
cold.rightchild = nonalcholic

deletebt(newbt)
#insertnodebt(newbt,"hot cofee")
levelordertraversal(newbt)
