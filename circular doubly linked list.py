#implemening circular doubly linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class CDlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node == self.tail.next:
                break
    def createCDll(self,nodevalue):
        node=Node(nodevalue)
        node.prev=node
        node.next=node
        self.head=node
        self.tail=node
        return 'dll is created'
    def insertinCDll(self,nodevalue,location):
        if self.head is None:
            print("list does not exist")
        else:
            newnode=Node(nodevalue)
            if location==0:
                newnode.prev=self.tail
                newnode.next=self.head
                self.head.prev=newnode
                self.head=newnode
                self.tail.next=newnode
            elif location==1:
                newnode.next=self.head
                newnode.prev=self.tail
                self.head.prev=newnode
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                newnode.next=tempnode.next
                newnode.prev=tempnode
                newnode.next.prev=newnode
                tempnode.next=newnode

    # traverse doubly linked list
    def traversel(self):
        if self.head is None:
            print('list does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                if node==self.tail:
                    break
                node = node.next
    # reverse traverse doubly linked list
    def reversetraversel(self):
        if self.head is None:
            print('list does not exist')
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                if node==self.head:
                    break
                node = node.prev
# search value in cicular doubly linked list
    def search(self, nodevalue):
        if self.head is None:
            print('list does not exists')
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    print(node.value)
                if node==self.tail:
                    return print('value does not exist')
                node = node.next
    # delete an node in single linked list
    def deletenode(self,location):
        if self.head is None:
            print('list does not exists')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
            elif location==1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            else:
                tempnode=self.head
                index=0
                while index < location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next
                tempnode.next.prev=tempnode
    # delete entire single linked list
    def DeleteentireCDLL(self):
        if self.head is None:
            print('nonlist exist')
        else:
            self.tail.next=None
            tempnode=self.head
            while tempnode:
                tempnode.prev=None
                tempnode=tempnode.next
            self.head=None
            self.tail=None

circularDLL=CDlinkedlist()
circularDLL.createCDll(0)
circularDLL.insertinCDll(1,1)
circularDLL.insertinCDll(2,3)
circularDLL.insertinCDll(4,4)
print([node.value for node in circularDLL])
#circularDLL.reversetraversel()
#circularDLL.search(7)
#circularDLL.deletenode(2)
circularDLL.DeleteentireCDLL()
print([node.value for node in circularDLL])